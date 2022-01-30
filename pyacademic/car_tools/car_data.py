""" Misc car data for calculations """

from car_tools import *

# ---------------------------------------------------------------------------- #
# Renault Twingo I 1.2 16V (C06) - D4F engine, R14 65x155
# ---------------------------------------------------------------------------- #
tire = Tire(14*inch, 155*mm, 65)
TwingoI_C06 = CarModel(tire=tire)