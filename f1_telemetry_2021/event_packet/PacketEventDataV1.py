import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure, PacketHeader
from EventDataDetailsV1 import EventDataDetailsV1


class PacketEventDataV1(PackedLittleEndianStructure):
    """This packet gives details of events that happen during the course of a session.

    Frequency: When the event occurs
    Size: 36 bytes
    Version: 1
    """
    _fields_ = [
        ('header', PacketHeader),  # Header
        ('eventStringCode', ctypes.c_uint8 * 4),  # Event string code, see below
        # Event details - should be interpreted differently for each type
        ('eventDetails', EventDataDetailsV1)  # Event details - should be interpreted differently for each type
    ]
