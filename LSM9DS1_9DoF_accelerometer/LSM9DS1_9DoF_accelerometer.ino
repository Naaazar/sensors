#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_LSM9DS1.h>

// Create LSM9DS1 object
Adafruit_LSM9DS1 lsm = Adafruit_LSM9DS1();

void setup() {
  Serial.begin(9600);

  // Initialize LSM9DS1
  if (!lsm.begin()) {
    Serial.println("Failed to initialize LSM9DS1 sensor!");
    while (1);
  }

  // Set sensor ranges
  lsm.setupAccel(lsm.LSM9DS1_ACCELRANGE_2G);    // 2, 4, 8, 16 g
  lsm.setupMag(lsm.LSM9DS1_MAGGAIN_4GAUSS);     // 4, 8, 12, 16 gauss
  lsm.setupGyro(lsm.LSM9DS1_GYROSCALE_2000DPS);  // 245, 500, 2000 dps
}

void loop() {
  // Read LSM9DS1 sensor data
  lsm.read();
  float accelX = lsm.accelData.x;
  float accelY = lsm.accelData.y;
  float accelZ = lsm.accelData.z;

  float gyroX = lsm.gyroData.x;
  float gyroY = lsm.gyroData.y;
  float gyroZ = lsm.gyroData.z;

  float magX = lsm.magData.x;
  float magY = lsm.magData.y;
  float magZ = lsm.magData.z;

  // Send sensor data over serial in CSV format
  Serial.print(accelX); Serial.print(",");
  Serial.print(accelY); Serial.print(",");
  Serial.print(accelZ); Serial.print(",");
  Serial.print(gyroX); Serial.print(",");
  Serial.print(gyroY); Serial.print(",");
  Serial.print(gyroZ); Serial.print(",");
  Serial.print(magX); Serial.print(",");
  Serial.print(magY); Serial.print(",");
  Serial.println(magZ);  // Complete the line

  delay(500);  // Adjust delay if needed
}
