import ctypes

from f1_telemetry_2019 import PackedLittleEndianStructure, PacketHeader


class PacketEventDataV1(PackedLittleEndianStructure):
    """This packet gives details of events that happen during the course of a session.

    Frequency: When the event occurs
    Size: 32 bytes
    Version: 1
    """
    _fields_ = [
        ('header', PacketHeader),  # Header
        ('eventStringCode', ctypes.c_char * 4),  # Event string code, see below
        # Event details - should be interpreted differently for each type
        ('vehicleIdx', ctypes.c_uint8),  # Vehicle index of car (valid for events: FTLP, RTMT, TMPT, RCWN)
        ('lapTime', ctypes.c_float)  # Lap time is in seconds (valid for events: FTLP)
    ]


