FROM openresty/openresty:1.19.3.1-2-focal

# installing mongo drivers
RUN apt-get -y update \
    && apt-get -y upgrade

RUN apt-get install -y \
    openssh-server \
    g++ \
    cmake \
    git

#installing the mongoc dependencies and driver
RUN apt-get install -y \
    pkg-config \
    libssl-dev \
    libsasl2-dev

RUN cd ~ \
    && wget https://github.com/mongodb/mongo-c-driver/archive/debian/1.17.3-1.tar.gz \
    && tar xzf mongo-c-driver-1.6.2.tar.gz \
    && cd mongo-c-driver-1.6.2 \
    && ./configure --disable-automatic-init-and-cleanup \
    && make \
    && make install \
    && cd ~ \
    && rm mongo-c-driver-1.6.2.tar.gz \
    && rm -rf mongo-c-driver-1.6.2

#installing mongocxx driver - connects c++ to mongo
RUN cd ~ \
    && wget https://github.com/mongodb/mongo-cxx-driver/archive/debian/3.6.2-1.tar.gz \
    && tar -xzf r3.1.1.tar.gz \
    && cd mongo-cxx-driver-r3.1.1/build \
    && cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local .. \
    && make EP_mnmlstc_core \
    && make \
    && make install \
    && cd ~ \
    && rm r3.1.1.tar.gz \
    && rm -rf mongo-cxx-driver-r3.1.1



# install dependencies
RUN ["luarocks", "install", "lua-resty-session"]
RUN ["luarocks", "install", "lua-resty-http"]
RUN ["luarocks", "install", "lua-resty-jwt"]
RUN ["luarocks", "install", "lua-mongo"]
RUN ["luarocks", "install", "cbson"]

#ADD lib/resty/openidc.lua /usr/local/openresty/lualib/resty/openidc.lua

EXPOSE 80 443 8080