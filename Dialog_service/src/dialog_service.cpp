#include "../include/dialog_service.hpp"

svc_response DialogService::create_session(int session_id) {
    return svc_response();
}

svc_response DialogService::put_message_user(int session_id, std::string message) {
    return svc_response();
}

svc_response DialogService::put_message_admin(int session_id, std::string message) {
    return svc_response();
}

svc_response DialogService::get_session(int session_id) {
    return svc_response();
}

DialogService::DialogService(DialogRepository &repository): repository(repository) {

}
