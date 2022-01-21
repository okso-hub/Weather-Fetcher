import requests

API_KEY = "5232ce150cdf1e63a6dcd6ca1fffd31a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)


def main():
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"] - 273.15, 2)

        print(f"Weather: {weather}")
        print(f"Temperature: {temperature}°C")
    else:
        print("An error occured.")


if __name__ == "__main__":
    main()
