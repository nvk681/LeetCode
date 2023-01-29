import json
import requests


URL = "https://api.weather.gov/alerts/active/count"#/alerts/active?area=?
response = requests.get(URL)
string = response.content.decode('utf-8')
json_obj = json.loads(string)

print(json.dumps(json_obj, indent=4))
# print(json_obj)


json_string = """{"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}"""