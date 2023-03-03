import requests
import json

# post_codes_req = requests.get("https://api.postcodes.io/postcodes/CR78BW")
#
# print(post_codes_req)
#
# # print(post_codes_req.headers)
# # print(post_codes_req.content)
#
# print(post_codes_req.json())
# print(type(post_codes_req.json()))

json_body = json.dumps({"postcodes": ["CR7 8BT", "SW16 4QL", "SW15 2DA"]})
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_multi_req.json())