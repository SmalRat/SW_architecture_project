from psycopg import sql
from support.src.models import Dialog
import os
import hazelcast


class SupportRepository:
    def __init__(self):
        hazelcast_cluster_member = os.getenv("HAZELCAST_CLUSTER_MEMBER", "localhost:5701")
        hazel_cluster = "dev"
        hazel_mapname = "hz_mapname"
        client = hazelcast.HazelcastClient(
            cluster_members=[hazelcast_cluster_member], cluster_name=hazel_cluster
        )

        self.distributed_map = client.get_map(hazel_mapname).blocking()

    def create_session(self):
        new_id = self.distributed_map.size()
        self.distributed_map[new_id] = Dialog()
        return new_id

    def put_message(self, session_id, role, message):
        self.distributed_map[session_id].messages.append(Message(role, message))
        return True

    def get_session(self, session_id):
        return Dialog(session_id)