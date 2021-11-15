#!/usr/bin/env python3
import argparse
import json
import logging
from urllib import request
from urllib.error import URLError, HTTPError


class ParseKwargs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, dict())
        for value in values:
            key, value = value.split('=')
            getattr(namespace, self.dest)["key"] = key
            getattr(namespace, self.dest)["value"] = value


class CreateEntities:

    def __init__(self, token):
        self.header = {"Authorization": "Bearer {}".format(token)}

    def create_entity(self, url, body):
        req = request.Request(url=url, data=body, headers=self.header)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata = json.dumps(body)
        jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
        try:
            response = request.urlopen(req, jsondataasbytes, timeout=30)
        except HTTPError as e:
            # do something
            raise SystemExit(e.read().decode('utf8'))
        except URLError as e:
            # do something (set req to blank)
            raise SystemExit(e)

    def create_environment(self, env_name, cluster_id):
        logger.info("create environment entity")
        data = {
            "environment": {
                "name": env_name,
                "clusterId": cluster_id
            }
        }
        self.create_entity(url="https://api.spotinst.io/ocean/cd/environment", body=data)

    def create_microservice(self, microservice_name, labels):
        logger.info("create microservice entity")
        data = {
            "microservice": {
                "name": microservice_name,
                "k8sResources": {
                    "workload": {
                        "type": "deployment",
                        "labels": [
                            labels
                        ]
                    }
                }
            }
        }
        self.create_entity(url="https://api.spotinst.io/ocean/cd/microservice", body=data)

    def create_notification_provider(self, notification_provider, webhook_url):
        logger.info("create notification entity")
        data = {
            "notificationProvider": {
                "name": notification_provider,
                "webhook": {
                    "url": webhook_url
                }
            }
        }
        self.create_entity(url="https://api.spotinst.io/ocean/cd/notificationProvider", body=data)

    def create_rollout_spec(self, env_name, microservice_name, notification_provider=None):
        logger.info("create rollout spec entity")
        data = {
            "rolloutSpec": {
                "name": env_name + "-" + microservice_name + "-spec",
                "microservice": microservice_name,
                "environment": env_name,
                "strategy": {
                    "rolling": {
                    }
                },
                "failurePolicy": {
                    "rollback": {
                        "mode": "newRollout"
                    }
                }
            }
        }
        if notification_provider is not None:
            data['rolloutSpec'].update({'notification': {'providers': [notification_provider]}})
        self.create_entity(url="https://api.spotinst.io/ocean/cd/rolloutSpec", body=data)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',)
    logger = logging.getLogger(__name__)
    example_text = ''' example:
    ./oceancd_baker.py -t 1234 -e test-environment -c test-cluster -m test-microservice -l app=test -n test-notification -w https://webhook.site
    '''
    parser = argparse.ArgumentParser(prog='oceancd_baker',
                                     description='oceancd_baker',
                                     epilog=example_text,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-t", "--token", type=str,
                        help="Api token to spot api", required=True)
    parser.add_argument("-e", "--environment_name", type=str,
                        help="Environment name", required=True)
    parser.add_argument("-c", "--cluster_id", type=str,
                        help="Cluster id for environment", required=True)
    parser.add_argument("-m", "--microservice_name", type=str,
                        help="Microservice name", required=True)
    parser.add_argument("-l", "--labels", help="Set of k8s labels that are exisitng on the wanted workload ",
                        required=True, nargs='*', action=ParseKwargs)
    parser.add_argument("-n", "--notification_provider", type=str,
                        help="The name identifier of the Ocean CD notification provider")
    parser.add_argument("-w", "--webhook", type=str,
                        help="Webhook url")
    args = parser.parse_args()
    entity = CreateEntities(args.token)
    entity.create_environment(env_name=args.environment_name, cluster_id=args.cluster_id)
    entity.create_microservice(microservice_name=args.microservice_name, labels=args.labels)
    if all(items is not None for items in [args.notification_provider, args.webhook]):
        entity.create_notification_provider(notification_provider=args.notification_provider, webhook_url=args.webhook)
    entity.create_rollout_spec(env_name=args.environment_name, microservice_name=args.microservice_name,
                               notification_provider=args.notification_provider)
