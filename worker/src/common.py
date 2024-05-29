import hazelcast
import logging
import os


def connect_to_hz():
    hazelcast_cluster_member = os.getenv("HZ_NETWORK_PUBLICADDRESS", "hazel-node-1:5701")
    hazel_cluster = "dev"
    logging.info("Test")
    print(f"Connecting to: {hazelcast_cluster_member}")
    client = hazelcast.HazelcastClient(
        cluster_members=[hazelcast_cluster_member], cluster_name=hazel_cluster
    )
    return client
