#ifndef DIALOG_SERVICE_DIALOG_SERVICE_HPP
#define DIALOG_SERVICE_DIALOG_SERVICE_HPP

#include "./common.hpp"
#include "./domain.hpp"
#include "./dialog_repository.hpp"

using svc_post_response = std::pair<int, std::string>;

class DialogService {
private:
    DialogRepository &repository;
public:
    explicit DialogService(DialogRepository &repository);
    ~DialogService() = default;

    std::tuple<int, std::string, int> create_session(); // TODO: change all of that to size_t?
    svc_post_response put_message_user(int session_id, std::string message);
    svc_post_response put_message_admin(int session_id, std::string message);
    std::tuple<int, std::string, Dialog> get_session(int session_id);
};

#endif //DIALOG_SERVICE_DIALOG_SERVICE_HPP
