import matplotlib.pyplot as plt

data = {
    "status": "success",
    "data": {
        "resultType": "vector",
        "result": [
            {
                "metric": {
                    "__name__": "kube_pod_info",
                    "container": "kube-state-metrics",
                    "created_by_kind": "ReplicaSet",
                    "created_by_name": "teastore-auth-6588c4cd9b",
                    "endpoint": "http",
                    "host_ip": "172.16.192.8",
                    "host_network": "false",
                    "instance": "10.176.0.6:8080",
                    "job": "kube-state-metrics",
                    "namespace": "default",
                    "node": "econome-8.nantes.grid5000.fr",
                    "pod": "teastore-auth-6588c4cd9b-pd2xp",
                    "pod_ip": "10.176.3.4",
                    "service": "kube-prometheus-stack-kube-state-metrics",
                    "uid": "b0e8ccd0-51d4-4e1c-a8dd-8e7454394edf"
                },
                "value": [
                    1714666456.118,
                    "1"
                ]
            },
            {
                "metric": {
                    "__name__": "kube_pod_info",
                    "container": "kube-state-metrics",
                    "created_by_kind": "ReplicaSet",
                    "created_by_name": "teastore-db-7685d7b587",
                    "endpoint": "http",
                    "host_ip": "172.16.192.8",
                    "host_network": "false",
                    "instance": "10.176.0.6:8080",
                    "job": "kube-state-metrics",
                    "namespace": "default",
                    "node": "econome-8.nantes.grid5000.fr",
                    "pod": "teastore-db-7685d7b587-cf85s",
                    "pod_ip": "10.176.3.1",
                    "service": "kube-prometheus-stack-kube-state-metrics",
                    "uid": "e0c4c51d-8ec4-4cdb-83e0-a4e5ad12bc0d"
                },
                "value": [
                    1714666456.118,
                    "1"
                ]
            },
            {
                "metric": {
                    "__name__": "kube_pod_info",
                    "container": "kube-state-metrics",
                    "created_by_kind": "ReplicaSet",
                    "created_by_name": "teastore-image-866749dd95",
                    "endpoint": "http",
                    "host_ip": "172.16.192.8",
                    "host_network": "false",
                    "instance": "10.176.0.6:8080",
                    "job": "kube-state-metrics",
                    "namespace": "default",
                    "node": "econome-8.nantes.grid5000.fr",
                    "pod": "teastore-image-866749dd95-dhk62",
                    "pod_ip": "10.176.3.5",
                    "service": "kube-prometheus-stack-kube-state-metrics",
                    "uid": "06623779-52f5-4232-ac10-686940da59f4"
                },
                "value": [
                    1714666456.118,
                    "1"
                ]
            },
            {
                "metric": {
                    "__name__": "kube_pod_info",
                    "container": "kube-state-metrics",
                    "created_by_kind": "ReplicaSet",
                    "created_by_name": "teastore-persistence-545cf59c9b",
                    "endpoint": "http",
                    "host_ip": "172.16.192.8",
                    "host_network": "false",
                    "instance": "10.176.0.6:8080",
                    "job": "kube-state-metrics",
                    "namespace": "default",
                    "node": "econome-8.nantes.grid5000.fr",
                    "pod": "teastore-persistence-545cf59c9b-wknqw",
                    "pod_ip": "10.176.3.3",
                    "service": "kube-prometheus-stack-kube-state-metrics",
                    "uid": "dba34d53-4c0a-4c50-9ca5-11fff90d9acb"
                },
                "value": [
                    1714666456.118,
                    "1"
                ]
            },
            {
                "metric": {
                    "__name__": "kube_pod_info",
                    "container": "kube-state-metrics",
                    "created_by_kind": "ReplicaSet",
                    "created_by_name": "teastore-recommender-56747d546c",
                    "endpoint": "http",
                    "host_ip": "172.16.192.8",
                    "host_network": "false",
                    "instance": "10.176.0.6:8080",
                    "job": "kube-state-metrics",
                    "namespace": "default",
                    "node": "econome-8.nantes.grid5000.fr",
                    "pod": "teastore-recommender-56747d546c-xnr7l",
                    "pod_ip": "10.176.3.6",
                    "service": "kube-prometheus-stack-kube-state-metrics",
                    "uid": "87caef27-0fad-4916-8b78-fd8e1313bc66"
                },
                "value": [
                    1714666456.118,
                    "1"
                ]
            },
            {
                "metric": {
                    "__name__": "kube_pod_info",
                    "container": "kube-state-metrics",
                    "created_by_kind": "ReplicaSet",
                    "created_by_name": "teastore-registry-84b85bd645",
                    "endpoint": "http",
                    "host_ip": "172.16.192.8",
                    "host_network": "false",
                    "instance": "10.176.0.6:8080",
                    "job": "kube-state-metrics",
                    "namespace": "default",
                    "node": "econome-8.nantes.grid5000.fr",
                    "pod": "teastore-registry-84b85bd645-gv5z9",
                    "pod_ip": "10.176.3.2",
                    "service": "kube-prometheus-stack-kube-state-metrics",
                    "uid": "d1070d16-ed90-4905-ab42-e8cb15fddc71"
                },
                "value": [
                    1714666456.118,
                    "1"
                ]
            },
            {
                "metric": {
                    "__name__": "kube_pod_info",
                    "container": "kube-state-metrics",
                    "created_by_kind": "ReplicaSet",
                    "created_by_name": "teastore-webui-859f4f58dd",
                    "endpoint": "http",
                    "host_ip": "172.16.192.8",
                    "host_network": "false",
                    "instance": "10.176.0.6:8080",
                    "job": "kube-state-metrics",
                    "namespace": "default",
                    "node": "econome-8.nantes.grid5000.fr",
                    "pod": "teastore-webui-859f4f58dd-tmrx8",
                    "pod_ip": "10.176.3.7",
                    "service": "kube-prometheus-stack-kube-state-metrics",
                    "uid": "5e43c096-f1aa-43fd-b1d0-0f3f02b16c0c"
                },
                "value": [
                    1714666456.118,
                    "1"
                ]
            }
        ]
    }
}

timestamps = []
values = []
labels = []

for item in data["data"]["result"]:
    timestamp = item["value"][0]
    value = float(item["value"][1])
    pod = item["metric"]["pod"]

    timestamps.append(timestamp)
    values.append(value)
    labels.append(pod)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(timestamps, values, marker='o', linestyle='-', linewidth=2)



plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Timestamp vs Value')

plt.grid(True)
plt.show()
