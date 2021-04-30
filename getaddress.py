import requests
import json


class GetAddress:

    def __init__(self, postcode: str):
        postcode = postcode.replace(" ","")
        info = requests.get("https://api.postcodes.io/postcodes/" + postcode)
        json_variable = info.json()
        result = json_variable["result"]
        self.country = result["country"]
        self.region = result["region"]
        print("retrieved info for "+postcode)

