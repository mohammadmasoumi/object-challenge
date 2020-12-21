local function createBucketMiddleware()
  ngx.say('Start logging response')
  ngx.say('Finish logging response')
end

return createBucketMiddleware