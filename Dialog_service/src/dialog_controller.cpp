#include "../include/dialog_controller.hpp"
#include "../include/dialog_service.hpp"

DialogController::DialogController(DialogService &service): service(service) {

}

DialogController::~DialogController() {

}

std::pair<int, std::string> read_put_message(Json::Value json_data) {
    return std::make_pair(json_data["session_id"].asInt(), json_data["msg"].asString());
}

Json::Value read_json(const std::string &json_str) {
    Json::CharReaderBuilder builder;
    Json::CharReader *reader = builder.newCharReader();
    Json::Value json_data;
    std::string errors;

    bool parsingSuccessful = reader->parse(json_str.c_str(), json_str.c_str() + json_str.length(), &json_data, &errors);
    delete reader;

    if (!parsingSuccessful) {
        std::stringstream error_msg;
        error_msg << "Error parsing JSON: " << errors << std::endl;
        throw std::runtime_error(error_msg.str());
    }

    return json_data;
}

void DialogController::create_session(const httplib::Request& req, httplib::Response& res) {
    const auto &session_id_str = req.body;
    const auto &session_id = std::stoi(session_id_str);
    const auto result = service.create_session(session_id);
    const auto &status = result.first;
    const auto &comment = result.second;

    // TODO: create appropriate jsons
    if (status == 0) {
        res.set_content(DIALOG_SERVICE_SUCCESSFULLY_CREATED_SESSION_JSON_RESPONSE, "text/plain");
    } else {
        res.set_content(comment, "text/plain");
    }
    res.set_content(DIALOG_SERVICE_SUCCESSFULLY_CREATED_SESSION_JSON_RESPONSE, "text/plain");
}

void DialogController::put_message_user(const httplib::Request& req, httplib::Response& res) {
    const auto &req_str = req.body;

    const auto json_data = read_json(req_str);
    auto parsed_data = read_put_message(json_data);
    auto session_id = parsed_data.first;
    auto &message = parsed_data.second;

    service.put_message_user(session_id, std::move(message));
}

void DialogController::put_message_admin(const httplib::Request& req, httplib::Response& res) {
    const auto &req_str = req.body;

    const auto json_data = read_json(req_str);
    auto parsed_data = read_put_message(json_data);
    auto session_id = parsed_data.first;
    auto &message = parsed_data.second;

    service.put_message_admin(session_id, std::move(message));
}

void DialogController::get_session(const httplib::Request& req, httplib::Response& res) {
    const auto &session_id_str = req.body;
    const auto &session_id = std::stoi(session_id_str);

    service.get_session(session_id);
}
