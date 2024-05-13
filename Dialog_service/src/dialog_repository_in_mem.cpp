#include "../include/dialog_repository_in_mem.hpp"

DialogRepositoryInMem::DialogRepositoryInMem() {

}

DialogRepositoryInMem::~DialogRepositoryInMem() {

}

std::tuple<int, std::string, int> DialogRepositoryInMem::create_session() {
    m_mutex.lock();
    int session_id = m_sessions.size();
    m_sessions.emplace(session_id, Dialog(session_id));
    m_mutex.unlock();
    return {INTERNAL_CODES::SUCCESS, SUCCESS_COMMENT, session_id};
}

repo_post_response DialogRepositoryInMem::put_message(int session_id, Role role, std::string message) {
    try{
        m_mutex.lock();
        m_sessions.at(session_id).messages.emplace_back(role, std::move(message));
        m_mutex.unlock();
        return {INTERNAL_CODES::SUCCESS, SUCCESS_COMMENT};
    }
    catch (std::exception &e){
        return {INTERNAL_CODES::INTERNAL_SERVER_ERROR, "Failed to put message into session."};
    }

}

std::tuple<int, std::string, Dialog> DialogRepositoryInMem::get_session(int session_id) {
    try{
        return {INTERNAL_CODES::SUCCESS, SUCCESS_COMMENT, m_sessions.at(session_id)};
    }
    catch (std::exception &e){
        return {INTERNAL_CODES::INTERNAL_SERVER_ERROR, "Failed to get session.", Dialog(BAD_SESSION_ID)};

    }
}

void DialogRepositoryInMem::lock_repository() {
    m_mutex.lock();
}

void DialogRepositoryInMem::unlock_repository() {
    m_mutex.unlock();
}
