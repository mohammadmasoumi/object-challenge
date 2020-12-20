FROM openresty/openresty:1.19.3.1-2-focal

# install mongo-c
RUN wget https://github.com/mongodb/libbson/releases/download/1.3.5/libbson-1.3.5.tar.gz \
    && tar -xzf libbson-1.3.5.tar.gz \
    && cd libbson-1.3.5 \
    && make \
    && sudo make install

# install dependencies
RUN ["luarocks", "install", "lua-resty-session"]
RUN ["luarocks", "install", "lua-resty-http"]
RUN ["luarocks", "install", "lua-resty-jwt"]
RUN ["luarocks", "install", "mongorover"]
RUN ["luarocks", "install", "cbson"]

#ADD lib/resty/openidc.lua /usr/local/openresty/lualib/resty/openidc.lua

EXPOSE 80 443 8080