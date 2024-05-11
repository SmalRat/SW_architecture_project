#include "../include/dialog_controller.hpp"
#include "../include/dialog_service.hpp"
#include "../include/dialog_repository.hpp"

int main(){
    DialogRepository repository;
    DialogService service(repository);
    DialogController dialog_controller(service);

    return 0;
}