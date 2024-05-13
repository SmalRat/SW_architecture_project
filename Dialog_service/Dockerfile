# Use an official C++ runtime as a parent image
FROM ubuntu:20.04

# Set the working directory
WORKDIR /usr/src/app

# Avoid user interaction with tzdata
ENV DEBIAN_FRONTEND=noninteractive

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y \
    g++ \
    cmake \
    git

# Clone and build Hazelcast C++ Client
RUN git clone https://github.com/hazelcast/hazelcast-cpp-client.git \
    && cd hazelcast-cpp-client \
    && cmake . -DHAZELCAST_INSTALL=ON -DBUILD_SHARED_LIBS=ON \
    && cmake --build . --target install

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Set the Jsoncpp and Boost include and lib paths
#ENV JSONCPP_INCLUDE_DIRS=/usr/include/jsoncpp
#ENV JSONCPP_LIB_PATH=/usr/lib/x86_64-linux-gnu/libjsoncpp.so

# Run CMake and make
RUN cmake . \
    && make

# Reset the frontend var to avoid any side effects
ENV DEBIAN_FRONTEND=dialog

# Run the application
CMD ["./dialog-service"]
