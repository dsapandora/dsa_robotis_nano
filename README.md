# ROS ROBOTIS MINI CONTROLLER

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
 
