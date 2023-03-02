import pytest
import requests

def test001_language():
    url = "https://ipinfo.io/161.185.160.93/geo?lang=en"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["country"] == "US"
def test002_missing_ip():
    url = "https://ipinfo.io/geo"
    response = requests.get(url)
    assert response.status_code == 200
    assert "readme" in response.json()

def test003_invalid_IP():
    url = "https://ipinfo.io/999.999.999.999/geo"
    response = requests.get(url)
    assert response.status_code == 404
    response_data = response.json()
    assert 'error' in response_data

def test000_Validation():
    url = "https://ipinfo.io/161.185.160.93/geo"
    response = requests.get(url)
    print(response.json())