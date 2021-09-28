import ctypes

from f1_telemetry_2019 import PackedLittleEndianStructure


class ParticipantDataV1(PackedLittleEndianStructure):
    """This type is used for the 20-element 'participants' array of the PacketParticipantsData_V1 type,
    defined below. """
    _fields_ = [
        ('aiControlled', ctypes.c_uint8),  # Whether the vehicle is AI (1) or Human (0) controlled
        ('driverId', ctypes.c_uint8),  # Driver id - see appendix
        ('teamId', ctypes.c_uint8),  # Team id - see appendix
        ('raceNumber', ctypes.c_uint8),  # Race number of the car
        ('nationality', ctypes.c_uint8),  # Nationality of the driver
        ('name', ctypes.c_char * 48),  # Name of participant in UTF-8 format – null terminated
        # Will be truncated with … (U+2026) if too long
        ('yourTelemetry', ctypes.c_uint8)  # The player's UDP setting, 0 = restricted, 1 = public
    ]
