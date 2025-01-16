// Arduino code for reading heart rate, temperature, oxygen, and blood pressure sensors

int heartRatePin = A0;  // Sensor pin for heart rate
int temperaturePin = A1;  // Sensor pin for body temperature
int oxygenPin = A2;  // Sensor pin for oxygen saturation
int bpPin = A3;  // Sensor pin for blood pressure

void setup() {
  Serial.begin(9600);
  pinMode(heartRatePin, INPUT);
  pinMode(temperaturePin, INPUT);
  pinMode(oxygenPin, INPUT);
  pinMode(bpPin, INPUT);
}

void loop() {
  int heartRate = analogRead(heartRatePin);  // Read heart rate sensor
  int temperature = analogRead(temperaturePin);  // Read temperature sensor
  int oxygen = analogRead(oxygenPin);  // Read oxygen saturation sensor
  int bloodPressure = analogRead(bpPin);  // Read blood pressure sensor

  // Send the data to Serial Monitor
  Serial.print("Heart Rate: ");
  Serial.println(heartRate);
  Serial.print("Temperature: ");
  Serial.println(temperature);
  Serial.print("Oxygen: ");
  Serial.println(oxygen);
  Serial.print("Blood Pressure: ");
  Serial.println(bloodPressure);

  delay(1000);  // Wait for 1 second before the next reading
}
