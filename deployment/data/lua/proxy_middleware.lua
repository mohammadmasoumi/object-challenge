local http = require "resty.http"
local httpc = http.new()

local challenge_url = "http://challenge:5000" .. ngx.var.uri

ngx.say(challenge_url)
ngx.say(ngx.req.get_method())
ngx.say(ngx.req.get_body_data())

--ngx.req.get_body_data()

--body = ngx.req.get_body_data(),

local res, err = https:request_uri(challenge_url, {
    method = ngx.req.get_method(),
--    header = ngx.req.get_headers()
})
ngx.say("response is:" .. res)