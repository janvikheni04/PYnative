#Access the value of key2 from the following JSON
import json

j = """{"key1": "value1", "key2": "value2"}"""

data = json.loads(j)
print(data['key2'])