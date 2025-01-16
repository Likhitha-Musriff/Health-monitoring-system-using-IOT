# health_monitoring_system.py
import requests
import time
import random
import matplotlib.pyplot as plt

# Simulate sensor data collection (for demo purposes)
def get_sensor_data():
    heart_rate = random.randint(60, 100)  # Simulating heart rate data
    temperature = random.uniform(36.5, 38.0)  # Simulating body temperature in Celsius
    oxygen = random.uniform(95, 100)  # Simulating oxygen saturation level
    blood_pressure = (random.randint(110, 140), random.randint(70, 90))  # Simulating blood pressure
    return {
        "heart_rate": heart_rate,
        "temperature": temperature,
        "oxygen": oxygen,
        "blood_pressure": blood_pressure
    }

# Cloud API URL to send the data
cloud_api_url = "http://yourcloudapi.com/upload_data"

# Function to send data to cloud
def send_to_cloud(sensor_data):
    response = requests.post(cloud_api_url, json=sensor_data)
    if response.status_code == 200:
        print("Data successfully sent to cloud.")
    else:
        print("Failed to send data to cloud.")

# Real-time monitoring and visualization
def real_time_monitoring():
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()
    heart_rate_data = []
    temp_data = []

    while True:
        sensor_data = get_sensor_data()
        print(f"Heart Rate: {sensor_data['heart_rate']} BPM")
        print(f"Temperature: {sensor_data['temperature']} C")
        print(f"Oxygen: {sensor_data['oxygen']} %")
        print(f"Blood Pressure: {sensor_data['blood_pressure'][0]}/{sensor_data['blood_pressure'][1]} mmHg")
        
        # Send data to the cloud
        send_to_cloud(sensor_data)

        # Update the graph with heart rate and temperature data
        heart_rate_data.append(sensor_data["heart_rate"])
        temp_data.append(sensor_data["temperature"])
        ax.clear()
        ax.plot(heart_rate_data, label="Heart Rate (BPM)", color='blue')
        ax.plot(temp_data, label="Temperature (C)", color='red')
        ax.legend(loc="upper left")
        plt.pause(1)  # Update every second

if __name__ == "__main__":
    real_time_monitoring()
