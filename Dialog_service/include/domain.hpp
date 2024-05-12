#ifndef DIALOG_SERVICE_DOMAIN_HPP
#define DIALOG_SERVICE_DOMAIN_HPP

#include "common.hpp"


// Todo: probably better to create class with encapsulated enum and conversion logic to keep everything in one place
enum class Role {
    USER,
    ADMIN
};

const std::map<Role, std::string> ROLE_TO_STRING = {
        {Role::USER, "USER"},
        {Role::ADMIN, "ADMIN"}
};

class Message {
    public:
        Role sender; // todo: potentially can be a separate class referring to user_id or admin_id
        std::string message;
        Message(Role sender, std::string message);
        ~Message() = default;
        [[nodiscard]] std::string to_string() const;
};

class Dialog {
    public:
        int session_id{};
        std::vector<Message> messages;

        explicit Dialog(int session_id);
        Dialog(int session_id, std::vector<Message> &&messages);
        Dialog(const Dialog &other) = default;
        ~Dialog() = default;

        [[nodiscard]] std::vector<Message> get_messages() const;
};



#endif //DIALOG_SERVICE_DOMAIN_HPP
