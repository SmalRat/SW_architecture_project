from psycopg import sql
from support.src.models import Dialog, Message
import hazelcast
import logging

from support.src.common import connect_to_hz

client = connect_to_hz()

class SupportRepository:
    def __init__(self):
        hazel_mapname = "hz_mapname"
        self.distributed_map = client.get_map(hazel_mapname).blocking()

    def create_session(self):
        new_id = self.distributed_map.size()
        self.distributed_map.set(new_id, Dialog(session_id = new_id, messages = [Message(sender = "2", message = "mess")]))
        return new_id

    def put_message(self, session_id, role, message):
        temp = self.distributed_map.get(session_id)
        temp.messages.append(Message(sender=role, message = message))
        self.distributed_map.set(session_id, temp)
        return "Success"

    def get_session(self, session_id):
        return self.distributed_map.get(session_id)