#access the nested key ‘salary’ from the following JSON
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

a = json.loads(sampleJson)
print(a['company']['employee']['payble']['salary'])