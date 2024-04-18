#Convert the following dictionary into JSON format
import json
data = {"key1" : "value1", "key2" : "value2"}
j = json.dumps(data)
print(j)
