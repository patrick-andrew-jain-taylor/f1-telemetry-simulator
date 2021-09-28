import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure


class FinalClassificationDataV1(PackedLittleEndianStructure):
    _fields_ = [
        ('position', ctypes.c_uint8),  # Finishing position
        ('numLaps', ctypes.c_uint8),  # Number of laps completed
        ('gridPosition', ctypes.c_uint8),  # Grid position of the car
        ('points', ctypes.c_uint8),  # Number of points scored
        ('numPitStops', ctypes.c_uint8),  # Number of pit stops made
        ('resultStatus', ctypes.c_uint8),  # Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished,
        # 4 = didnotfinish, 5 = disqualified, 6 = not classified, 7 = retired
        ('bestLapTimeInMS', ctypes.c_uint32),  # Best lap time of the session in milliseconds
        ('totalRaceTime', ctypes.c_double),  # Total race time in seconds without penalties
        ('penaltiesTime', ctypes.c_uint8),  # Total penalties accumulated in seconds
        ('numPenalties', ctypes.c_uint8),  # Number of penalties applied to this driver
        ('numTyreStints', ctypes.c_uint8),  # Number of tyres stints up to maximum
        ('tyreStintsActual', ctypes.c_uint8 * 8),  # Actual tyres used by this driver
        ('tyreStintsVisual', ctypes.c_uint8 * 8)  # Visual tyres used by this driver
    ]
