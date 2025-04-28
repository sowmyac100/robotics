# Purpose: Summary of Control Flow for Robotics Programming (with examples)

# -----------------------------
# 1. IF / ELIF / ELSE (decision making)
# -----------------------------

# Robots constantly make decisions based on sensor inputs
obstacle_detected = True
battery_level = 25

if obstacle_detected:
    print("Obstacle detected! Stopping robot.")
elif battery_level < 30:
    print("Battery low! Returning to charging station.")
else:
    print("Path is clear. Moving forward.")

# -----------------------------
# 2. FOR LOOPS (repeat actions a fixed number of times)
# -----------------------------

# Example: Check multiple sensor readings
sensor_readings = [1.2, 1.5, 0.9, 2.0]

for reading in sensor_readings:
    if reading < 1.0:
        print("Warning: Object very close!")
    else:
        print("Distance OK:", reading, "meters")

# -----------------------------
# 3. WHILE LOOPS (repeat actions until a condition is false)
# -----------------------------

# Example: Keep moving until destination is reached
destination_reached = False
steps_taken = 0

while not destination_reached:
    print("Taking a step forward.")
    steps_taken += 1
    
    if steps_taken >= 5:
        destination_reached = True
        print("Destination reached!")

# -----------------------------
# 4. BREAK and CONTINUE (special control keywords)
# -----------------------------

# BREAK: exit a loop early
sensor_readings = [1.2, 0.5, 1.1, 2.0]

for reading in sensor_readings:
    if reading < 0.7:
        print("Critical alert! Stopping check.")
        break
    print("Sensor OK:", reading)

# CONTINUE: skip the current loop iteration
for reading in sensor_readings:
    if reading < 1.0:
        print("Skipping faulty sensor reading:", reading)
        continue
    print("Valid reading:", reading)

# -----------------------------
# 5. NESTED CONTROL FLOWS
# -----------------------------

# Example: Complex decision logic
battery_level = 80
obstacle_detected = False
speed = 3.0  # m/s

if battery_level > 50:
    if not obstacle_detected:
        if speed <= 5.0:
            print("Move at current speed.")
        else:
            print("Speed too high! Slowing down.")
    else:
        print("Obstacle ahead! Stopping.")
else:
    print("Battery too low. Shutting down.")

# -----------------------------
# 6. MATCH-CASE (Python 3.10+ alternative to long if-elif chains)
# -----------------------------

# Example: Robot modes (idle, moving, charging)

robot_mode = "moving"

match robot_mode:
    case "idle":
        print("Robot is idle.")
    case "moving":
        print("Robot is moving.")
    case "charging":
        print("Robot is charging.")
    case _:
        print("Unknown mode!")

# -----------------------------
# End of script
# -----------------------------

# This script shows all major control flow techniques you need for robotics!
# Practice Tip: Try simulating a robot's daily cycle (moving, sensing, charging) using only control flow!
