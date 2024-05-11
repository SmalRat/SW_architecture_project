#ifndef DIALOG_SERVICE_DIALOG_CONTROLLER_HPP
#define DIALOG_SERVICE_DIALOG_CONTROLLER_HPP

#include "./common.hpp"
#include "./dialog_service.hpp"

constexpr int dialog_service_port = 9000;

const std::string DIALOG_SERVICE_CREATE_SESSION_ENDPOINT = "/create_session";
const std::string DIALOG_SERVICE_PUT_MESSAGE_USER_ENDPOINT = "/put_message_user";
const std::string DIALOG_SERVICE_PUT_MESSAGE_ADMIN_ENDPOINT = "/put_message_admin";
const std::string DIALOG_SERVICE_GET_SESSION_ENDPOINT = "/get_session";

const std::string DIALOG_SERVICE_HOSTNAME = "localhost";

const std::string DIALOG_SERVICE_SUCCESSFULLY_CREATED_SESSION_JSON_RESPONSE = R"({"status": 0, "comment": "Session successfully created"})";

class DialogController {
private:
    httplib::Server server;
    int m_port = dialog_service_port;

    DialogService &service;
public:
    explicit DialogController(DialogService &service);
    ~DialogController();

    void setup_endpoints();
    void start();

    void create_session(const httplib::Request& req, httplib::Response& res);
    void put_message_user(const httplib::Request& req, httplib::Response& res);
    void put_message_admin(const httplib::Request& req, httplib::Response& res);
    void get_session(const httplib::Request& req, httplib::Response& res);
};

#endif //DIALOG_SERVICE_DIALOG_CONTROLLER_HPP
