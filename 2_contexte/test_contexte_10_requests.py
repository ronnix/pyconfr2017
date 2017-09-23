"""
Remplacer une réponse HTTP
"""
import requests

import pytest
import responses


class OpenWeather:
    base_url = "http://api.openweathermap.org/data/2.5"

    def __init__(self, api_key):
        self.api_key = api_key

    def temperature(self, ville):
        response = requests.get(
            self.base_url + '/find',
            params={
                'q': ville,
                'units': 'im',
                'api_key': self.api_key,
            },
        )
        data = response.json()
        return data['list'][0]['main']['temp']


@pytest.fixture
def api():
    return OpenWeather(api_key='123456789')


@responses.activate
def test_temperature(api):
    responses.add(
        responses.GET,
        'http://api.openweathermap.org/data/2.5/find',
        status=200,
        json={
            "message": "accurate",
            "cod": "200",
            "count": 2,
            "list": [
                {
                    "id": 2972315,
                    "name": "Toulouse",
                    "coord": {
                        "lat": 43.6043,
                        "lon": 1.4437
                    },
                    "main": {
                        "temp": 22,
                        "pressure": 1020,
                        "humidity": 49,
                        "temp_min": 22,
                        "temp_max": 22
                    },
                    "dt": 1506162600,
                    "wind": {
                        "speed": 3.1,
                        "deg": 110
                    },
                    "sys": {
                        "country": "FR"
                    },
                    "rain": None,
                    "snow": None,
                    "clouds": {
                        "all": 20
                    },
                    "weather": [
                        {
                            "id": 801,
                            "main": "Clouds",
                            "description": "few clouds",
                            "icon": "02d"
                        }
                    ]
                },
                {
                    "id": 6453974,
                    "name": "Toulouse",
                    "coord": {
                        "lat": 43.6043,
                        "lon": 1.4437
                    },
                    "main": {
                        "temp": 22,
                        "pressure": 1020,
                        "humidity": 49,
                        "temp_min": 22,
                        "temp_max": 22
                    },
                    "dt": 1506162600,
                    "wind": {
                        "speed": 3.1,
                        "deg": 110
                    },
                    "sys": {
                        "country": "FR"
                    },
                    "rain": None,
                    "snow": None,
                    "clouds": {
                        "all": 20
                    },
                    "weather": [
                        {
                            "id": 801,
                            "main": "Clouds",
                            "description": "few clouds",
                            "icon": "02d"
                        }
                    ]
                }
            ]
        }
    )

    assert api.temperature('Toulouse,fr') == 22
