# Enter you module contents here
"""Modulet beregner arealet af en trekant og dets hypotenuse"""

import math

__version__ = "1.0"
__author__ = "JJDED"

def hypothenuse(a, b):
    """Returnere en trekants hypotenuse"""
    return (math.sqrt(a**2 + b**2))

def area(h, g):
    """Returnere en trekants areal"""
    return (0.5 * h * g)