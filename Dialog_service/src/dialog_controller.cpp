#include "../include/dialog_controller.hpp"
#include "../include/dialog_service.hpp"

std::string dialog_serializations::to_string(const Dialog& dialog){
    Json::Value root;
    root["session_id"] = dialog.session_id;
    Json::Value messages;
    for (const auto &message : dialog.messages){
        Json::Value message_json;
        message_json["sender"] = ROLE_TO_STRING.at(message.sender);
        message_json["message"] = message.message;
        messages.append(message_json);
    }
    root["messages"] = messages;
    Json::StreamWriterBuilder writer;
    return Json::writeString(writer, root);
}

std::string dialog_serializations::to_string (int value){
    return std::to_string(value);
}

DialogController::DialogController(DialogService &service): service(service) {
    setup_endpoints();
}

DialogController::~DialogController() = default;

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

template <typename Func>
void respond_get(const httplib::Request& req, httplib::Response& res, Func given_func, const std::string &data_field, const std::string &alternative) {
    Json::Value response_json;
    std::string response_str;
    try {
        const auto result = given_func();
        const auto &status = std::get<0>(result);
        const auto &comment = std::get<1>(result);
        auto data = std::get<2>(result);

        response_json["status"] = STATUS_MAP.at(status);
        response_json["comment"] = comment;
        response_json[data_field] = dialog_serializations::to_string(data);

        response_str = Json::writeString(Json::StreamWriterBuilder(), response_json);
    }
    catch (std::exception &e) {
        std::cerr << "Error: " << e.what() << std::endl;

        response_json["status"] = int(WEB_STATUS::INTERNAL_SERVER_ERROR);
        response_json["comment"] = e.what();
        response_json[data_field] = alternative;

        response_str = Json::writeString(Json::StreamWriterBuilder(), response_json);
    }
    res.set_content(response_str, "text/plain");
}

template <typename Func>
void respond_post(const httplib::Request& req, httplib::Response& res, Func given_func) {
    Json::Value response_json;
    std::string response_str;
    try {
        const auto result = given_func();
        const auto &status = std::get<0>(result);
        const auto &comment = std::get<1>(result);

        response_json["status"] = STATUS_MAP.at(status);
        response_json["comment"] = comment;

        response_str = Json::writeString(Json::StreamWriterBuilder(), response_json);
    }
    catch (std::exception &e) {
        std::cerr << "Error: " << e.what() << std::endl;

        response_json["status"] = int(WEB_STATUS::INTERNAL_SERVER_ERROR);
        response_json["comment"] = e.what();

        response_str = Json::writeString(Json::StreamWriterBuilder(), response_json);
    }
    res.set_content(response_str, "text/plain");
}

void DialogController::create_session(const httplib::Request& req, httplib::Response& res) {
    respond_get(req, res, [this]() {
        return service.create_session();
    }, "session_id", std::to_string(BAD_SESSION_ID));
}

void DialogController::put_message_user(const httplib::Request& req, httplib::Response& res) {
    const auto &req_str = req.body;

    const auto json_data = read_json(req_str);
    auto parsed_data = read_put_message(json_data);
    auto session_id = parsed_data.first;
    auto &message = parsed_data.second;

    respond_post(req, res, [this, session_id, message]() {
        return service.put_message_user(session_id, message); // todo: Can optimize this
    });
}

void DialogController::put_message_admin(const httplib::Request& req, httplib::Response& res) {
    const auto &req_str = req.body;

    const auto json_data = read_json(req_str);
    auto parsed_data = read_put_message(json_data);
    auto session_id = parsed_data.first;
    auto &message = parsed_data.second;

    respond_post(req, res, [this, session_id, message]() {
        return service.put_message_admin(session_id, std::move(message)); // todo: Can optimize this
    });
}

void DialogController::get_session(const httplib::Request& req, httplib::Response& res) {
    const auto &session_id_str = req.body;
    const auto &session_id = std::stoi(session_id_str);

    respond_get(req, res, [this, session_id]() {
        return service.get_session(session_id);
    }, "session", dialog_serializations::to_string(Dialog(BAD_SESSION_ID)));
}

void DialogController::setup_endpoints() {
    server.Get(DIALOG_SERVICE_CREATE_SESSION_ENDPOINT, [this](const httplib::Request& req, httplib::Response& res) {
        create_session(req, res);
    });

    server.Post(DIALOG_SERVICE_PUT_MESSAGE_USER_ENDPOINT, [this](const httplib::Request& req, httplib::Response& res) {
        put_message_user(req, res);
    });

    server.Post(DIALOG_SERVICE_PUT_MESSAGE_ADMIN_ENDPOINT, [this](const httplib::Request& req, httplib::Response& res) {
        put_message_admin(req, res);
    });

    server.Post(DIALOG_SERVICE_GET_SESSION_ENDPOINT, [this](const httplib::Request& req, httplib::Response& res) {
        get_session(req, res);
    });
}

void DialogController::start() {
    std::cout << "Starting dialog service on port " << m_port << std::endl;
    if (server.listen(DIALOG_SERVICE_HOSTNAME, m_port)){
        std::cout << "Server stopped on port " << m_port << std::endl;
    }
    else {
        std::cerr << "Failed to start dialog service on port " << m_port << std::endl;
        throw std::runtime_error("Failed to start dialog service on port " + std::to_string(m_port)); // Todo: optimize
    }
}
