import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure


class MarshalZoneV1(PackedLittleEndianStructure):
    """This type is used for the 21-element 'marshalZones' array of the PacketSessionData_V1 type, defined below."""
    _fields_ = [
        ('zoneStart', ctypes.c_float),  # Fraction (0..1) of way through the lap the marshal zone starts
        ('zoneFlag', ctypes.c_int8)  # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
    ]
