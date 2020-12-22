# JSON Tutorial

### What is JSON?
JSON is an acronym for ```JavaScript Object Notation```
-    A JavaScript "Object" is very similar to what we know in Python as "dictionaries"
--        **Note :** JavaScript Objects are also very similar to JavaScript maps, which would be considered the "true Python Dictionary equvialent"
 --       **Warning :** In JavaScript, an Object is a type of object, so a Javascript Object is essentially an "Object object" which can be confusing to many people. You don't have to understand the distinction for the purposes of this this course.
-    Much like Python dictionaries, there are "keys", which each have "values"
-   The JSON file format provides an efficient way of transmiting data from once place to another.
    Ex. sending data from backend to frontend

### What is a Python dictionary?
A Python dictionary is essentially a list of "keys" and "values"
-    Every key is matched with a value.
--        **Note :** Keys cannot be mutable--only values can be. (ex a key cannot be a list, but a value can be a list.)
-    Think of the keys as the words in a real dictionary, and the values the definition of the words.
    
### Example JSON File
Example of a JSON file :
```
{"menu": {
    "id": "file",
    "value": "File",
    "popup": {
        "menuitem": [
        {"value": "New", "onclick": "CreateNewDoc()"},
        {"value": "Open", "onclick": "OpenDoc()"},
        {"value": "Close", "onclick": "CloseDoc()"}
        ]
    }
}}
```
-    Here, the string, `"menu"`, is the key to the Object value.
-    `"id"` is the key to the `"file"` value.
-    `"value"` is the key to the `"File"` value.
-    `"menuitem"` is the key to a list (aka array) value.
-    and so on...

### Combining Python and JSON
Important Python libaries and modules for JSON :
-    *requests* 
--        a library that allows you to request files from a server using HTTP (HyperText Transfer Protocol)
-    *json* 
--        a library that allows you to decode and interact with JSON files within a Python program.

### Example Python code using JSON
```python3
# import the necessary libraries
import requests
import json

# request a file from the server
raw_file = requests.get(url='https://example.com/test.json')

# decode the string into equivalent Python data types
decoded_file = json.loads(raw_json_file.content)

# now, you can use regular Python syntax such as index operators to get the data you want
print(decoded_file['menu']['id'])
>>> file

print(decoded_file['menu']['menuitem'][0])
>>> {"value": "New", "onclick" : "CreateNewDoc()"}

print(decoded_file['menu']['menuitem'][2]['onclick'])
>>> CloseDoc()
```

### Final Remarks
JSON is extremely important in the world of programming.
-    JSON is an extremely convenient way to transfer data, and most modern day programming languages support JSON decoding and interaction.
-   JSON will be very important for the purposes of this course, because the API we will be using returns relevant data in the JSON file format.