#include "domain.hpp"

Message::Message(Role sender, std::string message): sender(sender), message(std::move(message)) {

}

std::string Message::to_string() const {
    return message;
}

Dialog::Dialog(int session_id): session_id(session_id) {

}

Dialog::Dialog(int session_id, std::vector<Message> &&messages): session_id(session_id), messages(std::move(messages)) {

}

std::vector<Message> Dialog::get_messages() const {
    return messages;
}
