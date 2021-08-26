KUBE_VERSION='v1.22.1'
docker pull kubeimage/kube-apiserver-amd64:$KUBE_VERSION
docker pull kubeimage/kube-controller-manager-amd64:
docker pull kubeimage/kube-scheduler-amd64:
docker pull kubeimage/kube-proxy-amd64:
docker pull kubeimage/pause-amd64:3.1

