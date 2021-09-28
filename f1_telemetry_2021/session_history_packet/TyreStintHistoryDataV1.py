import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure


class TyreStintHistoryDataV1(PackedLittleEndianStructure):
    _fields_ = [
        ('endLap', ctypes.c_uint8),  # Lap the tyre usage ends on (255 of current tyre)
        ('tyreActualCompound', ctypes.c_uint8),  # Actual tyres used by this driver
        ('tyreVisualCompound', ctypes.c_uint8),  # Visual tyres used by this driver
    ]
