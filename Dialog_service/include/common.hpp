#ifndef DIALOG_SERVICE_COMMON_HPP
#define DIALOG_SERVICE_COMMON_HPP

#include <string>
#include <httplib.h>
#include "json/json.h"

constexpr int BAD_SESSION_ID = -1;

const std::string SUCCESS_COMMENT = "Success!";

enum INTERNAL_CODES{
    SUCCESS = 0,
    BAD_REQUEST = 1,
    INTERNAL_SERVER_ERROR = 2
};

#endif //DIALOG_SERVICE_COMMON_HPP
