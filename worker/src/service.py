from worker.src.common import connect_to_hz

client = connect_to_hz()


class SupportWorkerService:
    def __init__(self):
        mq_name = "mq"
        self.messaging_queue = client.get_queue(mq_name).blocking()

    def deque_session(self):
        return self.messaging_queue.take()
