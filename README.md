# ROS Robotis Mini Controller

This repository contains a library for connecting to and controlling a Robotis Nano robot using Python and ROS (Robot Operating System). The library facilitates communication with the Robotis Mini via Bluetooth, enabling basic movements and further development for more advanced functionalities.

[![Watch the video](https://img.youtube.com/vi/JsVMXDAF_R4/maxresdefault.jpg)](https://www.youtube.com/watch?v=JsVMXDAF_R4)

## Getting Started

### Prerequisites

To use this library, ensure you have the following:
- Python
- ROS (Robot Operating System)
- Bluetooth capability on your machine
- Robotis Mini robot

### Connecting to the Robotis Mini

To establish a connection, bridge the Bluetooth connection as a serial device using the following command:

```bash
rfcomm bind 0 <ROBOTIS MINI BLUETOOTH MAC ADDRESS WITH :>
