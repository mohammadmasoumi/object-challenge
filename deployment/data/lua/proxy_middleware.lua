local http = require "resty.http"
local cjson = require "cjson"

local httpc = http.new()

local challenge_url = "http://" .. ngx.var.flask_webservice .. ngx.var.uri
local request_header = ngx.req.get_headers()
local request_method = ngx.req.get_method()
local request_body = ngx.req.get_body_data()

if request_body == nil then
    request_body = {}
end

if request_header == nil then
    request_header = {}
end

ngx.log(ngx.DEBUG, challenge_url)
ngx.log(ngx.DEBUG, "request_header: " .. cjson.encode(request_header))
ngx.log(ngx.DEBUG, "request_method: " .. request_method)
ngx.log(ngx.DEBUG, "request_body: " .. cjson.encode(request_body))

local res, err = httpc:request_uri(challenge_url, {
    method = request_method,
    headers = request_header,
    body = request_body
})

ngx.log(ngx.DEBUG, "response is:" .. cjson.encode(res))
ngx.log(ngx.DEBUG, "error is:" .. cjson.encode(err))
