local mongorover = require "mongorover"
local client = mongorover.MongoClient.new("mongodb://root:1234@mongo:27017/")
local challengeDatabase = client:getDatabase("challenge")
userCollection = challengeDatabase:getCollection("users")

local function createBucket()
  local result = userCollection:find_one({})
  ngx.say('Hello this is mohammad')
end

return createBucket