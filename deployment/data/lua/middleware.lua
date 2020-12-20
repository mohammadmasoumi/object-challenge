local mongo = require "mongo"
local client = mongo.Clinet("mongodb://root:1234@mongo:27017/")
userCollection = client:getCollection("challenge", "users")

local function createBucket()
  local result = userCollection:find_one({})
  ngx.say('Hello this is mohammad')
end

return createBucket