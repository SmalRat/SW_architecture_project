#include "../include/dialog_controller.hpp"
#include "../include/dialog_service.hpp"
#include "../include/dialog_repository.hpp"

int main(){
    DialogRepository dialog_repository;
    DialogService dialog_service(dialog_repository);
    DialogController dialog_controller(dialog_service);

    dialog_controller.start();

    return 0;
}