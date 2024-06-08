"""
Display the data received from API
"""

def display_weather(data):
    """Display the weather information."""
    city = data['name']
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']

    print(f"Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Condition: {description}")
    print(f"Humidity: {humidity}%")
