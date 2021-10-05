NAMESPACE="oceancd"
JOB_NAME="spot-oceancd-controller-installer"
wait_for_pod() {
    set +e
    desired_status=${2:-'Running'}
    is_pod_in_desired_status=false
    i=1
    timeout=10
    pod_status="$(kubectl get pod -n $NAMESPACE "$1" | awk '{print $3}')"
    if [ "$pod_status" = "Pending" ]; then
        echo "The pod is in Pending status"
        while true; do
          read -p "Do you want to continue with installation? y|n" yn
          case $yn in
            [Yy]* ) timeout=200; break;;
            [Nn]* ) kubectl delete -f ./spot-oceancd-controller-installer.yaml; kubectl delete ns $NAMESPACE; exit;;
            * ) echo "Please answer yes or no.";;
          esac
        done
        total_timeout=$(($timeout*3))
        for s in / - \\ \|
        do
          if [ "$i" -ge "$timeout" ]; then
             break
          fi
          pod_status="$(kubectl get pod -n $NAMESPACE "$1" -o jsonpath='{.status.phase}')"
          if [ "$pod_status" = "$desired_status" ]; then
            is_pod_in_desired_status=true
            printf "pod %s is %s\n" "$1" "$desired_status"
            break
          fi
          printf "\r$s"
          sleep 3
          i=$((i + 1))
        done
        if [ $is_pod_in_desired_status = "false" ]; then
          printf "pod %s does not transition to %s within %s seconds\n" "$1" "$desired_status" "$total_timeout"
          kubectl get event -n $NAMESPACE --field-selector involvedObject.name="$1" -o=jsonpath="{range .items[*]}{.message}{'\n'}{end}" | grep 'Failed\| Error'
          kubectl delete -f ./spot-oceancd-controller-installer.yaml;
          kubectl delete ns $NAMESPACE
          exit 1
        fi
    fi
    set -e
}




TOKEN=$1
if [ "$TOKEN" = '' ]; then
  echo "Error: token not provided"
  exit 1
fi
token=$(echo -n $TOKEN | base64)
sed -i spot-oceancd-controller-installer.bak "1,/value:.*/s/value:.*/value: $token/" spot-oceancd-controller-installer.yaml
kubectl create ns $NAMESPACE
kubectl apply -f spot-oceancd-controller-installer.yaml
pod_name=$(kubectl get pods -n $NAMESPACE --selector=job-name=$JOB_NAME | grep -v NAME | head -1 | awk '{print $1}')
wait_for_pod "$pod_name" "Succeded"
kubectl logs -f $pod_name -n $NAMESPACE
desired_status=${2:-'Completed'}
pod_status="$(kubectl get pod -n $NAMESPACE "$pod_name" | grep -v NAME | awk '{print $3}')"
if [ "$pod_status" != "$desired_status" ]; then
  printf "pod %s status is %s\n" "$pod_name" "$pod_status"
  kubectl delete -f ./spot-oceancd-controller-installer.yaml;
  kubectl delete ns $NAMESPACE
  exit 1
fi
