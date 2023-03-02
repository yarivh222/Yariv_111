import pytest
import requests

def test_invalid_IP():

    url = "https://ipinfo.io/999.999.999.999/geo"
    response = requests.get(url)
    assert response.status_code == 404
    # Assert that the response contains an error message
    response_data = response.json()
    assert 'error' in response_data


# Scenario 4: Test for a specific language
def test_language():
    response = requests.get("https://ipinfo.io/161.185.160.93/geo?lang=en")
    assert response.status_code == 200
    assert response.json()["country"] == "United States"


def test_language():
    response = requests.get("https://ipinfo.io/161.185.160.93/geo?lang=en")
    assert response.status_code == 200
    assert response.json()["country"] == "US"