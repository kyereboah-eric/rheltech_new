# Please edit the object below. Lines beginning with a '#' will be ignored,
# and an empty file will abort the edit. If an error occurs while saving this file will be
# reopened with the relevant failures.
#
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"apps/v1","kind":"ReplicaSet","metadata":{"annotations":{},"labels":{"env":"demo"},"name":"nginx-rs","namespace":"default"},"spec":{"replicas":3,"selector":{"matchLabels":{"env":"demo"}},"template":{"metadata":{"labels":{"env":"demo"},"name":"nginx"},"spec":{"containers":[{"image":"nginx","name":"nginx"}]}}}}
  creationTimestamp: "2025-06-07T22:17:24Z"
  generation: 1
  labels:
    env: demo
  name: nginx-rs
  namespace: default
  resourceVersion: "101520"
  uid: 9be536a4-980c-424d-8d69-dc21ab09bb66
spec:
  replicas: 5
  selector:
    matchLabels:
      env: demo
  template:
    metadata:
      creationTimestamp: null
      labels:
        env: demo
      name: nginx
    spec:
      containers:
      - image: nginx
        imagePullPolicy: Always
        name: nginx
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30
status:
  availableReplicas: 3
  fullyLabeledReplicas: 3
  observedGeneration: 1
  readyReplicas: 3
  replicas: 3
