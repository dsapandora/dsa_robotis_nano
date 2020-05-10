# ROS ROBOTIS MINI CONTROLLER

[![Watch the video](https://img.youtube.com/vi/JsVMXDAF_R4/maxresdefault.jpg)](https://www.youtube.com/watch?v=JsVMXDAF_R4)


To make it work
we need to bridge de bluetooth connection as a serial device using
```bash
rfcomm bind 0 <ROBOTIS MINI BLUETTOH MAC ADDRESS WITH :>
```

To disconnect
```bash
rfcomm relese 0 <ROBOTIS MINI BLUETTOH MAC ADDRESS WITH :>
```

This will create a connection to port */dev/rfcomm0*



A Controller for deep learning robotis mini

 - [X] Control robotis mini BASIC MOVEMENT USING ROS
 - [ ] Add Camera to robotis MINI
 - [ ] Define movement politics
 - [ ] Train based in Conscale approuch
 
