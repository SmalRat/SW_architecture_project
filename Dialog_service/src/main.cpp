#include "../include/dialog_controller.hpp"
#include "../include/dialog_service.hpp"
#include "../include/dialog_repository_in_mem.hpp"

int main(){
    DialogRepositoryInMem dialog_repository;
    DialogService dialog_service(dialog_repository);
    DialogController dialog_controller(dialog_service);

    dialog_controller.start();

    return 0;
}