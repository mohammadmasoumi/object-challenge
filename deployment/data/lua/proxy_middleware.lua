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

ngx.log(ngx.DEBUG, challenge_url)
ngx.log(ngx.DEBUG, "request_header: " .. cjson.encode(request_header))
ngx.log(ngx.DEBUG, "request_method: " .. request_method)
ngx.log(ngx.DEBUG, "request_body: " .. cjson.encode(request_body))

local res, err = httpc:request_uri(challenge_url, {
    method = request_method,
    headers = request_header,
    body = request_body
})

local response_body = res.body
local response_headers = res.headers
local response_status = res.status

ngx.log(ngx.DEBUG, "response_body: " .. cjson.encode(response_body))
ngx.log(ngx.DEBUG, "response_headers: " .. cjson.encode(response_headers))
ngx.log(ngx.DEBUG, "response_status: " .. cjson.encode(response_status))
ngx.log(ngx.DEBUG, "error: " .. cjson.encode(err))

ngx.log(ngx.DEBUG, "logger: " .. response_status == 200)
ngx.log(ngx.DEBUG, "status type: " .. type(response_status))

if response_status == 200 then
    ngx.log(ngx.DEBUG, "Redirecting ...")
    local redirected_res = ngx.location.capture("/redirect_to", {
        method = ngx.HTTP_POST,
        always_forward_body = true
    })
    ngx.log(ngx.DEBUG, "redirect res body: " .. cjson.encode(redirected_res.body))
    ngx.log(ngx.DEBUG, "redirect res status: " .. cjson.encode(redirected_res.status))

    ngx.status = redirected_res.status
    ngx.say(redirected_res.body)
    ngx.exit(ngx.HTTP_OK)

else
    ngx.status = response_status
    ngx.say(response_body)
    ngx.exit(ngx.HTTP_OK)
end