import requests

def get_weather_data(lat, lon, api_key):
    # Define the endpoint for OpenWeather API (current weather data)
    url = f"http://api.openweathermap.org/data/2.5/weather"
    
    # Set up the parameters for the API request
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,  # Your API key
        'units': 'metric'  # To get temperature in Celsius. Use 'imperial' for Fahrenheit.
    }
    
    try:
        # Make a GET request to the OpenWeather API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an exception for 4XX/5XX responses
        weather_data = response.json()
        
        # Return the weather data
        return weather_data
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Example usage
if __name__ == "__main__":
    # Your OpenWeather API Key
    api_key = "307b371c5cbf4a6137af7eedaadd0c3a"
    
    # Coordinates for the location (latitude and longitude)
    lat = -0.16678600224  # Example: Latitude for San Francisco
    lon = 34.122756999572  # Example: Longitude for San Francisco
    
    # Get the weather data
    weather_data = get_weather_data(lat, lon, api_key)
    
    if weather_data:
        print("Weather Data:", weather_data)
