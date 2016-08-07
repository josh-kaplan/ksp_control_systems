#!/usr/bin/env python
'''

File:           01_booster_separation.py

Author:         Josh Kaplan
Date:           July 31, 2016

Description:    This file automate booster separation for a spacecraft in
                Kerbal Space Program using kRPC. The craft file can be found at
                jkpl.io/assets/files/01_Booster_Separation.craft


'''
import krpc
import time

# Connect to Kerbal and our vessel
conn = krpc.connect(name='Sub-orbital flight script')
vessel = conn.space_center.active_vessel

# Initiate Autopilot
vessel.auto_pilot.target_pitch_and_heading(90,90)
vessel.auto_pilot.engage()
vessel.control.throttle = 0.4
time.sleep(1)

# Launch
print('3 ... '); time.sleep(1)
print('2 ... '); time.sleep(1)
print('1 ... '); time.sleep(1)
print('Launch!')
vessel.control.activate_next_stage()


# Sleep 1 second while we still have solid fuel
while vessel.resources.amount('SolidFuel') > 0.1:
    time.sleep(1)

# Once we're out of fuel, separate the boosters.
print('Booster separation')
vessel.control.activate_next_stage()

# Disengage autopilot
vessel.auto_pilot.disengage()