import serial
import matplotlib.pyplot as plt
import numpy as np
import time

# Set up the serial connection (adjust 'COM3' to your Arduino's port)
ser = serial.Serial('COM3', 9600, timeout=1)  # Replace 'COM3' with your port
time.sleep(2)  # Wait for the connection to establish

# Lists to hold the data
accel_data = []
gyro_data = []
mag_data = []

# Set up the plot
plt.ion()  # Enable interactive mode
fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Labels and titles for the plots
axs[0].set_title('Accelerometer Data')
axs[0].set_ylabel('Acceleration (g)')
axs[1].set_title('Gyroscope Data')
axs[1].set_ylabel('Gyro Rate (°/s)')
axs[2].set_title('Magnetometer Data')
axs[2].set_ylabel('Magnetic Field (gauss)')
axs[2].set_xlabel('Time (seconds)')

# Start time for x-axis
start_time = time.time()

try:
    while True:
        line = ser.readline().decode('utf-8').strip()  # Read a line from the serial port

        if line:
            # Split the received line into data points
            data = line.split(',')
            if len(data) == 9:  # Make sure we have all 9 values
                # Append data to lists
                accel_data.append([float(data[0]), float(data[1]), float(data[2])])  # Ax, Ay, Az
                gyro_data.append([float(data[3]), float(data[4]), float(data[5])])   # Gx, Gy, Gz
                mag_data.append([float(data[6]), float(data[7]), float(data[8])])     # Mx, My, Mz

                # Plotting the data
                current_time = time.time() - start_time

                # Update accelerometer plot
                axs[0].cla()  # Clear the previous plot
                axs[0].plot(accel_data, label=['Ax', 'Ay', 'Az'])
                axs[0].legend(loc='upper right')
                axs[0].set_title('Accelerometer Data')
                axs[0].set_ylabel('Acceleration (g)')
                axs[0].set_ylim([-60000, 60000])  # Adjust y-axis limit as needed

                # Update gyroscope plot
                axs[1].cla()  # Clear the previous plot
                axs[1].plot(gyro_data, label=['Gx', 'Gy', 'Gz'])
                axs[1].legend(loc='upper right')
                axs[1].set_title('Gyroscope Data')
                axs[1].set_ylabel('Gyro Rate (°/s)')
                axs[1].set_ylim([-2000, 2000])  # Adjust y-axis limit as needed

                # Update magnetometer plot
                axs[2].cla()  # Clear the previous plot
                axs[2].plot(mag_data, label=['Mx', 'My', 'Mz'])
                axs[2].legend(loc='upper right')
                axs[2].set_title('Magnetometer Data')
                axs[2].set_ylabel('Magnetic Field (gauss)')
                axs[2].set_ylim([-20000, 20000])  # Adjust y-axis limit as needed
                axs[2].set_xlabel('Time (seconds)')

                plt.pause(0.1)  # Pause to allow the plot to update

except KeyboardInterrupt:
    print("Data collection stopped by user.")
finally:
    ser.close()
    print("Serial connection closed.")
