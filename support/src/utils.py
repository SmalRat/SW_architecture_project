from support.src.models import Dialog, Message
from support.src.common import connect_to_hz

mq_name = "mq"

client_maps = connect_to_hz("dev", "MAPS_HZ_NETWORK_ADDRESS")
client_mq = connect_to_hz(mq_name, "MQ_HZ_NETWORK_ADDRESS")


class SupportRepository:
    def __init__(self):
        hazel_mapname = "hz_mapname"
        self.distributed_map = client_maps.get_map(hazel_mapname).blocking()

    def create_session(self):
        new_id = self.distributed_map.size()
        self.distributed_map.set(new_id, Dialog(session_id=new_id, messages=[]))
        return new_id

    def put_message(self, session_id, role, message):
        temp = self.distributed_map.get(session_id)
        temp.messages.append(Message(sender=role, message=message))
        self.distributed_map.set(session_id, temp)
        return "Success"

    def get_session(self, session_id):
        return self.distributed_map.get(session_id)
