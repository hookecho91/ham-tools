import numpy as np
from metpy.units import units


def antenna_leg_length(freq: float, freq_units: str='MHz') -> units:
    """
    Calculates the length for one leg of a dipole antenna

    Parameters:
    freq: float
        frequency you for which the antenna will be tuned
    freq_units: str
        frequency unit corresponding to freq input, default is MHz
    
    Returns:
    l: float
        length of one leg of the dipole antenna, in ft
    """

    freq = freq*units(freq_units)
    L = 468/freq.to('MHz').m
    l = (L/2)*units('ft')

    return l
