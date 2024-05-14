from support.src.utils import SupportRepository, client

QUEUE_NAME = "mq"


class SupportService:
    def __init__(self):
        self.messaging_queue = client.get_queue(QUEUE_NAME).blocking()
        self.repository = SupportRepository()

    def create_session(self):
        return self.repository.create_session()

    def put_message_user(self, session_id, message):
        self.messaging_queue.put(session_id)
        return self.repository.put_message(session_id, "User", message)

    def put_message_admin(self, session_id, message):
        return self.repository.put_message(session_id, "Admin", message)

    def get_session(self, session_id):
        return self.repository.get_session(session_id)
