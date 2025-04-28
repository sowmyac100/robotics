// Summary of Variables and Data Structures in C++ (for Robotics Programming)

#include <iostream>
#include <vector> // Dynamic array
#include <array>  // Fixed-size array
#include <string> // Text data
using namespace std;

int main() {
    // --- VARIABLES ---

    // Integer (robot ID, counter, etc.)
    int robotID = 1;

    // Float (position coordinates, speeds)
    float robotSpeed = 3.5f; // "f" suffix for float literals

    // Double (more precision for calculations)
    double distanceToGoal = 15.6789;

    // Boolean (status flags)
    bool isOperational = true;

    // Character (single character)
    char direction = 'N'; // N for North

    // String (useful for names, messages)
    string robotName = "Atlas";

    // Print variables
    cout << "Robot " << robotName << " [ID: " << robotID << "] is heading "
         << direction << " at speed " << robotSpeed << " m/s." << endl;

    // --- DATA STRUCTURES ---

    // 1. Arrays (fixed-size collection of elements)
    int sensorValues[5] = {100, 95, 90, 85, 80};
    cout << "First sensor reading: " << sensorValues[0] << endl;

    // 2. std::array (safer fixed-size array)
    array<int, 3> wheelSpeeds = {10, 20, 30};
    cout << "Second wheel speed: " << wheelSpeeds[1] << endl;

    // 3. std::vector (dynamic array)
    vector<float> lidarReadings;
    lidarReadings.push_back(1.2);
    lidarReadings.push_back(2.5);
    lidarReadings.push_back(0.9);

    cout << "LIDAR reading 1: " << lidarReadings[0] << endl;

    // 4. Structs (group related variables together)
    struct Position {
        double x;
        double y;
        double theta; // orientation in radians
    };

    Position robotPosition = {0.0, 0.0, 0.0};
    robotPosition.x = 5.2;
    robotPosition.y = 3.8;
    robotPosition.theta = 1.57; // ~90 degrees

    cout << "Robot Position -> x: " << robotPosition.x
         << ", y: " << robotPosition.y
         << ", theta: " << robotPosition.theta << " radians" << endl;

    // --- BONUS: CONSTANTS ---
    // Useful for things that shouldn't change (e.g., robot parameters)
    const double WHEEL_RADIUS = 0.15; // meters
    // WHEEL_RADIUS = 0.2; // Error! Cannot modify const variables

    return 0;
}
