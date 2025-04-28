# Purpose: Summary of Variables, Data Types, and Data Structures for Robotics Programming in Python

# -----------------------------
# 1. VARIABLES
# -----------------------------

# Variables store information the robot needs (position, speed, sensor data, etc.)
robot_name = "ExplorerBot"       # String
battery_level = 87.5              # Float
is_moving = True                  # Boolean
wheel_count = 4                   # Integer

# -----------------------------
# 2. BASIC DATA TYPES
# -----------------------------

# Integers: whole numbers (used for counting, discrete steps)
steps_moved = 120

# Floats: numbers with decimals (used for precise measurements)
motor_speed = 2.5   # meters per second

# Strings: text (used for IDs, labels)
sensor_type = "Infrared"

# Booleans: True/False (used for checking robot states)
obstacle_detected = False

# -----------------------------
# 3. COLLECTION DATA TYPES (important for grouping robot data)
# -----------------------------

# Lists: Ordered collections (good for multiple sensors, motor speeds)
sensor_readings = [23.4, 22.9, 24.1]  # readings from temperature sensors

# Access elements
first_reading = sensor_readings[0]  # 23.4

# Modify elements
sensor_readings[1] = 23.0

# Append new readings
sensor_readings.append(24.5)

# Iterate through a list
for reading in sensor_readings:
    print("Sensor reading:", reading)

# -----------------------------
# Tuples: Immutable collections (good for fixed coordinates)
# -----------------------------

position = (10, 5)  # (x, y) position of robot

# Access tuple elements
x_coord = position[0]
y_coord = position[1]

# Tuples can't be changed, which is good for constant positions

# -----------------------------
# Dictionaries: Key-value pairs (good for labeling sensor data)
# -----------------------------

sensor_data = {
    "front_sensor": 1.5,  # meters
    "rear_sensor": 2.0,
    "left_sensor": 0.8
}

# Access dictionary values
front_distance = sensor_data["front_sensor"]

# Add new data
sensor_data["right_sensor"] = 1.2

# Iterate through dictionary
for sensor, distance in sensor_data.items():
    print(sensor, "distance:", distance)

# -----------------------------
# Sets: Unordered, unique items (less common, but useful for tracking unique events)
# -----------------------------

visited_zones = {"A", "B", "C"}

# Add a new zone
visited_zones.add("D")

# Check if a zone has been visited
if "B" in visited_zones:
    print("Zone B has been visited.")

# -----------------------------
# 4. TYPE CONVERSION (important for sensor data)
# -----------------------------

# Example: sensor gives string output, but we need a float
sensor_output = "23.7"
sensor_value = float(sensor_output)

# Example: motor ID integer to string
motor_id = 5
motor_label = "Motor_" + str(motor_id)

# -----------------------------
# 5. CONSTANTS (optional best practice)
# -----------------------------

# Constants: variables you shouldn't change (Python doesn't enforce this, but ALL_CAPS by convention)
MAX_SPEED = 5.0  # meters per second

# Example usage
if motor_speed > MAX_SPEED:
    print("Warning: Exceeding maximum speed!")

# -----------------------------
# End of script
# -----------------------------

# This covers all fundamental variable/data concepts you'll use when programming a robot!
# Practice Tip: Try to simulate a small robot control system using these types!
