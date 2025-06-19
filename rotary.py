#!/usr/bin/env python
#
# This class uses a standard rotary encoder with push switch
#

import sys
import time
from rotary_class import RotaryEncoder

# Define GPIO inputs
dial_up = 26 	# Pin 8 
dial_down = 19	# Pin 10
Data = 21	# Pin 7
knob_up = 27 #GPIO 27
knob_down = 22 #GPIO 22
Items = 20 #GPIO 20

# This is the event callback routine to handle events
def dial_event(event):
	if event == RotaryEncoder.CLOCKWISE:
		print ("Dial Clockwise")
		exec ("dial_up")
	elif event == RotaryEncoder.ANTICLOCKWISE:
		print ("Dial Anticlockwise")
		exec ("dial_down")
	elif event == RotaryEncoder.BUTTONDOWN:
		print ("Data DialButton down")
		exec ("module_data")
	elif event == RotaryEncoder.BUTTONUP:
		print ("Data DialButton up")
	return
	
def knob_event(event):
	if event == RotaryEncoder.CLOCKWISE:
		print ("Knob Clockwise")
		exec ("knob_up")
	elif event == RotaryEncoder.ANTICLOCKWISE:
		print ("Knob Anticlockwise")
		exec ("knob_down")
	elif event == RotaryEncoder.BUTTONDOWN:
		print ("Item Button down")
		exec ("module_items")
	elif event == RotaryEncoder.BUTTONUP:
		print ("Item Button up")
	return

# Define the switch
dial = RotaryEncoder(dial_up,dial_down,Data,dial_event)
knob = RotaryEncoder(knob_up,knob_down,Items,knob_event)

#print("Pin A "+ str(dial_up))
#print("Pin B "+ str(dial_down))
#print("BUTTON "+ str(Data))

#print("Pin A "+ str(knob_up))
#print("Pin B "+ str(knob_down))
#print("BUTTON "+ str(Items))

# Listen
while True:
	time.sleep(0.5)


