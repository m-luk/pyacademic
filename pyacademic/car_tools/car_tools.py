""" car-tools package main script with self-call operation and utilities """

import math
from dataclasses import dataclass

import pint
import pytest
from pint import Quantity

# ---------------------------------------------------------------------------- #
# Pint unit registry constants
# ---------------------------------------------------------------------------- #
ureg = pint.UnitRegistry()
km = ureg.kilometer
sec = ureg.second
minute = ureg.minute
hour = ureg.hour
meter = ureg.meter
inch = ureg.inch
mm = ureg.mm

kph = km / hour
ms = meter / sec

# ---------------------------------------------------------------------------- #
# Classes
# ---------------------------------------------------------------------------- #

# TODO: implement car model


class TorqueCurve:
    pass


@dataclass
class Tire:
    """ Data class for Tire data """
    radius: Quantity
    width: Quantity
    profile: Quantity

    @property
    def r(self):
        """ get tire outer radius """
        return (self.width * self.profile / 100 + self.radius.to(mm) / 2).to(mm)

    @property
    def rd(self):
        """ get tire dynamic radius """
        return (0.97 * self.r).to(mm)


@dataclass
class CarModel:
    """ class storing car parameters """
    tire: Tire

    # TODO: add attributes


# ---------------------------------------------------------------------------- #
# functions
# ---------------------------------------------------------------------------- #
def rpm_from_v(v: Quantity, ig: float, i_trans: float, tire: Tire) -> Quantity:
    """ Get engine RPM from wheel-speed """
    return (ig * i_trans * (v/(2 * tire.rd * math.pi))).to(1 / minute)


# ---------------------------------------------------------------------------- #
# tests
# ---------------------------------------------------------------------------- #

def test_rpm_from_v():
    """ simple value test based on twingo tyre """
    # tire data
    tw_tire = Tire(14 * inch, 155 * mm, 65)

    # car state
    v = 115 * kph
    i_trans = 0.76
    ig = 4.06

    rpm = round(rpm_from_v(v, ig, i_trans, tw_tire).magnitude, 3)

    assert 3483.625 == rpm, "RPM value incorrect"

# TODO: test for Tire class, maybe move tests to separate file
