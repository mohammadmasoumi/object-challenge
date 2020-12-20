FROM openresty/openresty:1.19.3.1-2-focal

# install dependencies
RUN ["luarocks", "install", "lua-resty-session"]
RUN ["luarocks", "install", "lua-resty-http"]
RUN ["luarocks", "install", "lua-resty-jwt"]
RUN ["luarocks", "install", "mongorover.MongoClient"]
RUN ["luarocks", "install", "cbson"]

#ADD lib/resty/openidc.lua /usr/local/openresty/lualib/resty/openidc.lua

EXPOSE 80 443 8080