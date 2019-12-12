# ENGI301 project II
# Project N.A.P.A.L.M.
# (Working name was Gauntlet V2)
# This project and the PCB being designed for it is to create a second Gauntlet for my right arm.

Board Functionality
The PCB for Gauntlet Mk II. will mainly function as a breakout board for an Arduino Nano. A buck converter will also sit on the same board to power all systems.
5 Analog Pins will be used as specified:
1. Flex Sensor - Index proximal interphalangeal
2. Flex Sensor - Middle proximal interphalangeal
3. Flex Sensor - Ring proximal interphalangeal
4. Flex Sensor - Pinky proximal interphalangeal
5. Flex Sensor - Wrist

7 Digital Pins will be used as specified:
1. MOSFET for Solenoid Cowl Retract
2. MOSFET for water gun motor control 
3. [Undisclosed]
4. [Undisclosed]
5. Neopixel Ring 1 Output
6. Neopixel Ring 2 Output
7. Data out to R.E.G.A.L.I.A.

In addition, 5V and GND will be connected to the buck converter’s output pins

Overview
This Gauntlet would be a multifunctional apparatus to serve as turn and brake Indicators for biking and rollerblading, Quad knuckle-mounted LEDs, and a palm-mounted water gun

This is achieved with Adafruit's Neopixel Rings mounted on the palm and backhand on brackets riveted to a glove. These will glow red and orange depending on if I am signaling a turn
or a stop.

Additionally, the Neopixels will fade in / out in green when the water gun is firing, and pulse random RGB colors in a 'party mode'

4 5mm 'Super Bright' Green LEDs will sit in cowls above the knuckles, wired in parallel.
These will activate when a certain combination of fingers is held for 1.5 seconds, and when all 4 fingers are flexed in a fist.
Supposed to simulate a 'powered punch' or something along those lines.

In the center of the palm-mounted Neopixel Ring is a nozzle to blast water.
A full-auto water gun will be used as a high pressure pump to send bursts of water through a water line to this nozzle.
This water gun uses a sector gear (basically a gear with some missing teeth) to pull back a spring-loaded piston.
When the gears run out and disengage, the spring forces the piston back forward and water through the tube.
This will allow for harmless water 'projectiles', and can easily be modified for something more exciting...

A suite of 5 flex sensors is the user input for this project.
4 are mounted on the fingers of a glove (centered along proximal interphalangeal joint), and 1 additional one is mounted on cuff on outer surface of wrist

Hand Commands: Most activate with a single gesture, but other take a 2-step safety sequence

A) Mode Selection
	1. Projectile Mode (middle, ring, and pinky flexed for 1.5 seconds - basically making a finger gun)
	2. Knuckle Mode (middle and ring fingers flexed for 2 seconds - spiderman web gesture)
	3. Turn Signal (ring and pinky fingers flexed triggers, 0 sec time delay)
	4. Stop Signal (default) (wrist flexion to activate)
	5. Reset (only index finger flexed)
	6. Party Mode (shakas)


B) Excecute Commands
	1. Knuckle Mode selected + All fingers flexed ==> Knuckles activate
	2. Projectile Mode selected + wrist flexion ==> water shoots out
	3. Projectile Mode deselected + wrist flexion ==> stop signal




