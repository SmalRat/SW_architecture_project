from worker.src.common import connect_to_hz

timeout_seconds = 5

client = connect_to_hz()


class SupportWorkerService:
    def __init__(self):
        mq_name = "mq"
        self.messaging_queue = client.get_queue(mq_name).blocking()

    def deque_session(self):
        try:
            print("Received dequeue request!")
            return self.messaging_queue.take()
        except TimeoutError:
            print(f"No messages received in {timeout_seconds} seconds")
            return None
