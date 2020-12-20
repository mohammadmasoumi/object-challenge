json = require "json"

local function createBucketMiddleware()
  ngx.say('Start logging response')

  local data = {request={}, response={}}
  local req = data["request"]
  local resp = data["response"]

  req["host"] = ngx.var.host
  req["uri"] = ngx.var.uri
  req["headers"] = ngx.req.get_headers()
  req["time"] = ngx.req.start_time()
  req["method"] = ngx.req.get_method()
  req["get_args"] = ngx.req.get_uri_args()

  resp["headers"] = ngx.resp.get_headers()
  resp["status"] = ngx.status
  resp["duration"] = ngx.var.upstream_response_time
  resp["time"] = ngx.now()
  resp["body"] = ngx.var.response_body
  ngx.log(ngx.CRIT, json.encode(data));

  ngx.say('Finish logging response')

end

return createBucketMiddleware