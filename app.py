from kubernetes import client
from kubernetes import config
from kubernetes.client.rest import ApiException

def main():

  config.load_kube_config()

  api_instance = client.CoreV1Api()
  cmap = client.V1ConfigMap()
  cmap.metadata = client.V1ObjectMeta(name="special-config1")
  print("test1")
  cmap.data = {}
  cmap.data["special.how"] = "very"
  cmap.data["special.type"] = "charm"
  cmap.data["special.creationTimestamp"]= "2016-02-18T18:52:05Z"
  cmap.data["special.namespace"] = "default"
  print("test2")
  #api_instance.create_namespaced_config_map(namespace="default", body=cmap)
  # print(cmap.data)
  print(cmap)

if __name__ == '__main__':
    main()
