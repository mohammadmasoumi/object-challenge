local http = require "resty.http"
local cjson = require "cjson"

local httpc = http.new()

local challenge_url = "http://challenge:5000" .. ngx.var.uri
local request_header = ngx.req.get_headers()
local request_method = ngx.req.get_method()
local request_body = ngx.req.get_body_data()

if request_body == nil then
    request_body = {}
end

if request_header == nil then
    request_header = {}
end

ngx.say(challenge_url)
ngx.say("request_header: " .. cjson.encode(request_header))
ngx.say("request_method: " .. request_method)
ngx.say("request_body: " .. cjson.encode(request_body))

local res, err = https:request_uri(challenge_url, {
    method = request_method,
    headers = request_header,
    body = request_body
})

ngx.say("response is:" .. cjson.encode(res))
ngx.say("error is:" .. cjson.encode(err))
