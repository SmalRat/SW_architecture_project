cmake_minimum_required(VERSION 3.15)

set(PROJECT_NAME dialog_service)
project(${PROJECT_NAME} C CXX) # project(${PROJECT_NAME} C CXX ASM)

set(CMAKE_CXX_STANDARD 17)

#! By default - build release version if not specified otherwise.
if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif ()

##########################################################
# Project files, packages, libraries and so on
##########################################################
set(JSONCPP_INCLUDE_DIRS ${PROJECT_SOURCE_DIR}/libs/jsoncpp/include)
set(JSONCPP_LIB_PATH ${PROJECT_SOURCE_DIR}/libs/jsoncpp/build/lib/libjsoncpp.so)

IF(CMAKE_BUILD_TYPE MATCHES Debug)
    add_compile_definitions(ENABLE_DEBUG_INFO)
ENDIF(CMAKE_BUILD_TYPE MATCHES Debug)

find_package(Boost REQUIRED COMPONENTS system)
if(Boost_FOUND)
    include_directories(${Boost_INCLUDE_DIRS})
endif()

find_package(hazelcast-cpp-client CONFIG REQUIRED)

add_executable(dialog-service ./src/dialog_controller.cpp ./src/dialog_service.cpp src/dialog_repository_in_mem.cpp ./src/domain.cpp ./src/main.cpp src/dialog_repository_hz.cpp)
target_include_directories(dialog-service PRIVATE ./include ${JSONCPP_INCLUDE_DIRS})
target_link_libraries(dialog-service ${JSONCPP_LIB_PATH} -pthread ${Boost_LIBRARIES} hazelcast-cpp-client::hazelcast-cpp-client)
