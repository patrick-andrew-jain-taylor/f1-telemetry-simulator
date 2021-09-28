import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure, PacketHeader
from ParticipantDataV1 import ParticipantDataV1


class PacketParticipantsDataV1(PackedLittleEndianStructure):
    """This is a list of participants in the race.

    If the vehicle is controlled by AI, then the name will be the driver name.
    If this is a multiplayer game, the names will be the Steam Id on PC, or the LAN name if appropriate.
    On Xbox One, the names will always be the driver name, on PS4 the name will be the LAN name if playing a LAN game,
    otherwise it will be the driver name.

    Frequency: Every 5 seconds
    Size: 1104 bytes
    Version: 1
    """
    _fields_ = [
        ('header', PacketHeader),  # Header
        ('numActiveCars', ctypes.c_uint8),  # Number of active cars in the data – should match number of
        # cars on HUD
        ('participants', ParticipantDataV1 * 20)
    ]


