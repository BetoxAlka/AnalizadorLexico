import random
import datetime

WEATHER_TYPES = ['Sunny', 'Rainy', 'Cloudy', 'Windy', 'Stormy', 'Snowy']

class WeatherDay:
    def __init__(self, date, weather, high_temp, low_temp):
        self.date = date
        self.weather = weather
        self.high_temp = high_temp
        self.low_temp = low_temp

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')}: {self.weather} with highs of {self.high_temp}°C and lows of {self.low_temp}°C"

class WeatherSimulator:
    def __init__(self, days=7):
        self.days = days
        self.forecast = []

    def generate_forecast(self):
        current_date = datetime.date.today()
        for i in range(self.days):
            date = current_date + datetime.timedelta(days=i)
            weather = random.choice(WEATHER_TYPES)
            high = random.randint(15, 35)
            low = high - random.randint(5, 15)
            self.forecast.append(WeatherDay(date, weather, high, low))

    def display_forecast(self):
        print("Weather Forecast:")
        for day in self.forecast:
            print(day)

    def get_weather_by_date(self, target_date):
        for day in self.forecast:
            if day.date == target_date:
                return day
        return None

def test_simulator():
    print("Running Weather Simulation Test...")
    sim = WeatherSimulator(5)
    sim.generate_forecast()
    sim.display_forecast()

    today = datetime.date.today()
    print("\nTesting specific date lookup:")
    result = sim.get_weather_by_date(today)
    if result:
        print("Found:", result)
    else:
        print("No weather data found for today.")

def main():
    simulator = WeatherSimulator(10)
    simulator.generate_forecast()
    simulator.display_forecast()

if __name__ == "__main__":
    test_mode = input("Run in test mode? (y/n): ").lower()
    if test_mode == "y":
        test_simulator()
    else:
        main()
