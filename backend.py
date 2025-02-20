import requests

API_KEY = 'a418075cf5c492ca2918eb53a1c94ec0'

def get_data(place, days=1):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    number_of_days = days * 8
    filtered_data = data["list"][:number_of_days]
    return filtered_data

if __name__ == '__main__':
    print(get_data(place='Lagos', days=2))