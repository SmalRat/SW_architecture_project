import hazelcast
import logging
import os


def connect_to_hz(cluster, address):
    hazelcast_cluster_member = os.getenv(address, "hazel-node-1:5701")
    hazel_cluster = cluster
    logging.info("Test")
    print(f"Connecting to: {hazelcast_cluster_member}")
    client = hazelcast.HazelcastClient(
        cluster_members=[hazelcast_cluster_member], cluster_name=hazel_cluster
    )
    return client
