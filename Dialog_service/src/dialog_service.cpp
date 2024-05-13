#include <utility>

#include "../include/dialog_service.hpp"

std::tuple<int, std::string, int> DialogService::create_session() {
    return repository.create_session();
}

svc_post_response DialogService::put_message_user(int session_id, std::string message) {
    return repository.put_message(session_id, Role::USER, std::move(message));
}

svc_post_response DialogService::put_message_admin(int session_id, std::string message) {
    return repository.put_message(session_id, Role::ADMIN, std::move(message));
}

std::tuple<int, std::string, Dialog> DialogService::get_session(int session_id) {
    return repository.get_session(session_id);
}

DialogService::DialogService(DialogRepositoryInMem &repository): repository(repository) {

}
