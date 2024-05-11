#ifndef DIALOG_SERVICE_DIALOG_SERVICE_HPP
#define DIALOG_SERVICE_DIALOG_SERVICE_HPP

#include "./common.hpp"
#include "./dialog_repository.hpp"

using svc_response = std::pair<int, std::string>;

class DialogService {
private:
    DialogRepository &repository;
public:
    explicit DialogService(DialogRepository &repository);
    ~DialogService() = default;

    svc_response create_session(int session_id); // TODO: change all of that to size_t?
    svc_response put_message_user(int session_id, std::string message);
    svc_response put_message_admin(int session_id, std::string message);
    svc_response get_session(int session_id);
};

#endif //DIALOG_SERVICE_DIALOG_SERVICE_HPP
