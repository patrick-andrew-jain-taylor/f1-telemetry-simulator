import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure


class LapHistoryDataV1(PackedLittleEndianStructure):
    _fields_ = [
        ('lapTimeInMS', ctypes.c_uint32),  # Lap time in milliseconds
        ('sector1TimeInMS', ctypes.c_uint16),  # Sector 1 time in milliseconds
        ('sector2TimeInMS', ctypes.c_uint16),  # Sector 2 time in milliseconds
        ('sector3TimeInMS', ctypes.c_uint16),  # Sector 3 time in milliseconds
        ('lapValidBitFlags', ctypes.c_uint8)  # 0x01 bit set-lap valid, 0x02 bit set-sector 1 valid, 0x04 bit
        # set-sector 2 valid, 0x08 bit set-sector 3 valid
    ]
