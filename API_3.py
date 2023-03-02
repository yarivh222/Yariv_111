"""
url = "https://ipinfo.io/161.185.160.93/geo"
response = requests.get(url)
print(response.json())
"""

#*************Example1-Validate resposne and comapre output *************
# Send a get request and the response prints in JSON format "

import requests

url = "https://ipinfo.io/161.185.160.93/geo"
response = requests.get(url)
print(response.json())

"""
****Output**** 
{
  "ip": "161.185.160.93",
  "city": "New York City",
  "region": "New York",
  "country": "US",
  "loc": "40.7143,-74.0060",
  "org": "AS22252 The City of New York",
  "postal": "10004",
  "timezone": "America/New_York",
  "readme": "https://ipinfo.io/missingauth"
}
"""
#*************Example2-Invalid IP  *************
url = "https://ipinfo.io/999.999.999.999/geo"
response = requests.get(url)

# Assert 404 response
assert response.status_code == 404
# Assert that the response contains an error message
response_data = response.json()
assert 'error' in response_data
assert response_data['error'] == 'wrong ip'

"""
#*************Example3-valid IP  *************
url = "https://ipinfo.io/161.185.160.93/geo"
response = requests.get(url)
assert response.status_code == 200
assert "city" in response.json()

#*************Example4-language *************
url = "https://ipinfo.io/161.185.160.93/geo?lang=en"
response = requests.get(url)
assert response.status_code == 200
assert response.json()["country"] == "United States"


#*************Example5-specific field *************
url = "https://ipinfo.io/161.185.160.93/geo?fields=city"
response = requests.get(url)
assert "city" in response.json()
assert "country" not in response.json()
"""