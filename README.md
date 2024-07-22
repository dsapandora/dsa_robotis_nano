
# ROS Robotis Mini Controller

This repository contains a library for connecting to and controlling a Robotis Nano robot using Python and ROS (Robot Operating System). The library facilitates communication with the Robotis Mini via Bluetooth, enabling basic movements and further development for more advanced functionalities.

![Robotis Mini Drawing](https://user-images.githubusercontent.com/12345678/robotis-mini-drawing.png)

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
```

### Disconnecting from the Robotis Mini

To disconnect, use the following command:

```bash
rfcomm release 0 <ROBOTIS MINI BLUETOOTH MAC ADDRESS WITH :>
```

This will create a connection to port `/dev/rfcomm0`.

## Features

- **Basic Movements**: Control the Robotis Mini's basic movements using ROS.
- **Future Enhancements**:
  - Add a camera to the Robotis Mini.
  - Define movement policies.
  - Train the robot based on the Conscale approach.

## Usage

### Basic Movement Control

To control the Robotis Mini, follow the instructions in the library's documentation. Ensure your ROS setup is correctly configured and that you have a Bluetooth connection established as described above.

### Adding Camera

Future updates will include instructions for adding and utilizing a camera with the Robotis Mini.

### Movement Policies

We plan to define movement policies to improve the robot's interaction and responses.

### Training with Conscale Approach

Training the Robotis Mini based on the Conscale approach will be implemented in future versions of this library.

## Contributions

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any questions or support, please open an issue in this repository.

---

Follow the progress and watch our demo video:
[![Watch the video](https://img.youtube.com/vi/JsVMXDAF_R4/maxresdefault.jpg)](https://www.youtube.com/watch?v=JsVMXDAF_R4)
