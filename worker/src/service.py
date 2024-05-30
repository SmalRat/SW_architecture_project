from worker.src.common import connect_to_hz

timeout_seconds = 5
mq_name = "mq"

client_maps = connect_to_hz("dev", "MAPS_HZ_NETWORK_ADDRESS")
client_mq = connect_to_hz(mq_name, "MQ_HZ_NETWORK_ADDRESS")


class SupportWorkerService:
    def __init__(self):
        self.messaging_queue = client_mq.get_queue(mq_name).blocking()

    def deque_session(self):
        try:
            print("Received dequeue request!")
            return self.messaging_queue.take()
        except TimeoutError:
            print(f"No messages received in {timeout_seconds} seconds")
            return None
