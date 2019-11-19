import http.client
import json
# https://rapidapi.com/community/api/open-weather-map/endpoints
conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "1aece3393emsh73ca8dfe0f5722dp1dc8fbjsn6ad8250ba066"
    }


city = "Hundested"
link = "/weather?callback=test&id=2172797&units=%22metric%22%20or%20%22imperial%22&mode=xml%2C%20html&q="+city+"%2Cdk"

conn.request("GET", link, headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
weather = data.decode("utf-8")
weather = json.loads(weather)
