#baki the grappler

Build Instructions
1. Visit https://www.hackster.io/projects/d21824/ and https://github.com/bcrb26/ENGI301/tree/master/project_01_Brian for code, Fritzing diagrams, and Solidworks parts
2. 3D Print and Laser cut all appropriate parts
3. Modify Servo hat by desoldering screw junction, barrel connector, and all header pins. Solder on 2+ 90 degree male headers to the underside
4. Connect appropriate 5V, 12V, GND, SDA, and SCL leads between components, as specified in Fritzing diagram
5. Assemble lower box out of laser-cut parts
6. Install wiring loom inside box
7. Use zipties and epoxy where appropriate to keep cavity clean and free from loose wires that could entangle with the servo gear train
8. Paint if desired
9. Join all JST connectors.
10. Install dependencies on Raspberry pi, load baki.py


Operation Instructions:
1. Toggle main (bottom) switch to power on Raspberry Pi (baki.py will execute on boot)
2. Duck and Cover

2.1 Alternatively, stay out of the camera's range
2.1.2 Use the IP Address listed on the LCD display to log into the Raspberry Pi via VNC Viewer
2.1.3 Recalibrate target color using trackbar_test.py (run from command line or from Thonny IDE)
2.1.4 Reboot to run baki.py on boot with new colors to target.