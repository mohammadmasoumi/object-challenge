local http = require "resty.http"
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
ngx.log("request_header: " .. request_header)
ngx.log("request_method: " .. request_method)
ngx.log("request_body: " .. request_body)

local res, err = https:request_uri(challenge_url, {
    method = request_method,
    headers = request_header,
    body = request_body
})

ngx.log("response is:" .. res)
ngx.log("response is:" .. err)
ngx.say("response is:" .. res)