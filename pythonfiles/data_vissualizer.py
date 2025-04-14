import random
import matplotlib.pyplot as plt
import statistics

class WeatherDataGenerator:
    def __init__(self, days=30):
        self.days = days
        self.temperatures = []

    def generate_data(self):
        for _ in range(self.days):
            daily_temp = random.uniform(10.0, 35.0)
            self.temperatures.append(round(daily_temp, 1))
        return self.temperatures

class WeatherAnalyzer:
    def __init__(self, data):
        self.data = data

    def calculate_average(self):
        return round(statistics.mean(self.data), 2)

    def calculate_max(self):
        return max(self.data)

    def calculate_min(self):
        return min(self.data)

    def generate_report(self):
        avg = self.calculate_average()
        max_temp = self.calculate_max()
        min_temp = self.calculate_min()

        print("Weather Report")
        print("==============")
        print(f"Average Temperature: {avg} °C")
        print(f"Maximum Temperature: {max_temp} °C")
        print(f"Minimum Temperature: {min_temp} °C")

class WeatherVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_data(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.data, marker='o', linestyle='-', color='skyblue')
        plt.title("Daily Temperature over 30 Days")
        plt.xlabel("Day")
        plt.ylabel("Temperature (°C)")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def histogram(self):
        plt.figure(figsize=(8, 4))
        plt.hist(self.data, bins=10, color='salmon', edgecolor='black')
        plt.title("Temperature Distribution")
        plt.xlabel("Temperature (°C)")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()

def main():
    generator = WeatherDataGenerator(days=30)
    temperatures = generator.generate_data()

    analyzer = WeatherAnalyzer(temperatures)
    analyzer.generate_report()

    visualizer = WeatherVisualizer(temperatures)
    visualizer.plot_data()
    visualizer.histogram()

if __name__ == "__main__":
    main()
