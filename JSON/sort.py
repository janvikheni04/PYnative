#Sort JSON keys in and write them into a file
import json
j = {"id" : 1, "name" : "value2", "age" : 29}

print("writing in json file")
with open("j.json", "w") as write_file:
    json.dump(j, write_file, indent=4, sort_keys=True)

print("Done writing")