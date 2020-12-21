
local http = require "resty.http"
--local httpc = http.new()

--request section
local request_method = ngx.req.get_method()
local request_body = ngx.req.get_body_data()

--response section
local response_status = ngx.status
local response_body = ngx.var.response_body

ngx.say("I have got a request!")
ngx.say(request_method)
ngx.say(request_body)
ngx.say("response!")
ngx.say(response_status)
ngx.say(response_body)

