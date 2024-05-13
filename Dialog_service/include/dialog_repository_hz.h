#ifndef DIALOG_SERVICE_DIALOG_REPOSITORY_HZ_HPP
#define DIALOG_SERVICE_DIALOG_REPOSITORY_HZ_HPP

#include "./common.hpp"
#include "domain.hpp"

using repo_post_response = std::pair<int, std::string>;

class DialogRepositoryHz {
private:
    std::map<int, Dialog> m_sessions;
    std::mutex m_mutex;
public:
    DialogRepositoryHz();
    ~DialogRepositoryHz();

    std::tuple<int, std::string, int> create_session();
    repo_post_response put_message(int session_id, Role role, std::string message);
    std::tuple<int, std::string, Dialog> get_session(int session_id);

    void lock_repository();
    void unlock_repository();
};

#endif //DIALOG_SERVICE_DIALOG_REPOSITORY_HZ_HPP
