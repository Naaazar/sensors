import serial
import csv
import time
import os

# Set up the serial connection (adjust 'COM3' to your Arduino's port)
ser = serial.Serial('COM3', 115200, timeout=1)  # Use the same baud rate as in the Arduino code
time.sleep(2)  # Allow time for the serial connection to initialize

# Specify the CSV file name (it will be created in the same directory)
file_name = 'sensor_data.csv'

# Check if the file already exists
file_exists = os.path.isfile(file_name)

# Open the CSV file for writing (in append mode)
with open(file_name, mode='a', newline='') as file:
    csv_writer = csv.writer(file)

    # If the file doesn't exist, write the header row
    if not file_exists:
        csv_writer.writerow(['Accel1_X', 'Accel1_Y', 'Accel1_Z', 
                             'Gyro1_X', 'Gyro1_Y', 'Gyro1_Z', 
                             'Mag1_X', 'Mag1_Y', 'Mag1_Z',
                             'Accel2_X', 'Accel2_Y', 'Accel2_Z', 
                             'Gyro2_X', 'Gyro2_Y', 'Gyro2_Z', 
                             'Mag2_X', 'Mag2_Y', 'Mag2_Z'])

    try:
        while True:
            # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip()  # Read and decode a line from the Arduino

            if line:
                # Split the data by commas
                data = line.split(',')

                # Check if the data has 18 elements (9 for each sensor)
                if len(data) == 18:
                    # Write the data to the CSV file
                    csv_writer.writerow(data)
                    print(f"Data written: {data}")
                else:
                    print(f"Unexpected data format: {data}")

    except KeyboardInterrupt:
        # Exit the loop when Ctrl+C is pressed
        print("Data collection stopped.")

    finally:
        # Close the serial connection
        ser.close()
        print("Serial connection closed.")
