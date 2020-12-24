FROM openresty/openresty:1.19.3.1-2-focal

## installing mongo drivers
#RUN apt-get -y update \
#    && apt-get -y upgrade
#
#RUN apt-get install -y \
#    openssh-server \
#    g++ \
#    cmake \
#    git
#
##installing the mongoc dependencies and driver
#RUN apt-get install -y \
#    pkg-config \
#    libssl-dev \
#    libsasl2-dev
#
###installing mongoc driver - connects c to mongo
#RUN cd ~ \
#    && wget https://github.com/mongodb/mongo-c-driver/releases/download/1.17.3/mongo-c-driver-1.17.3.tar.gz \
#    && tar xzf mongo-c-driver-1.17.3.tar.gz \
#    && cd mongo-c-driver-1.17.3 \
##    && ./configure --disable-automatic-init-and-cleanup \
#    && cmake . \
#    && make install \
#    && cd ~ \
#    && rm mongo-c-driver-1.17.3.tar.gz \
#    && rm -rf mongo-c-driver-1.17.3
#
###installing mongocxx driver - connects c++ to mongo
#RUN cd ~ \
#    && wget https://github.com/mongodb/mongo-cxx-driver/releases/download/r3.6.2/mongo-cxx-driver-r3.6.2.tar.gz \
#    && tar -xzf mongo-cxx-driver-r3.6.2.tar.gz \
#    && cd mongo-cxx-driver-r3.6.2/build \
#    && cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local .. \
#    && make EP_mnmlstc_core \
#    && cmake . \
#    && make install \
#    && cd ~ \
#    && rm mongo-cxx-driver-r3.6.2.tar.gz \
#    && rm -rf mongo-cxx-driver-r3.6.2

# install dependencies
RUN ["luarocks", "install", "lua-resty-http"]
RUN ["luarocks", "install", "luajson"]
RUN ["luarocks", "install", "lua-cjson"]

EXPOSE 80 443