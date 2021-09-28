import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure


class LobbyInfoDataV1(PackedLittleEndianStructure):
    _fields_ = [
        ('aiControlled', ctypes.c_uint8),  # Whether the vehicle is AI (1) or Human (0) controlled
        ('teamId', ctypes.c_uint8),  # Team id - see appendix (255 if no team currently selected)
        ('nationality', ctypes.c_uint8),  # Nationality of the driver
        ('name', ctypes.c_char * 48),  # Name of participant in UTF-8 format – null terminated, will be truncated
        # with ... (U+2026) if too long
        ('carNumber', ctypes.c_uint8),  # Car number of the player
        ('readyStatus', ctypes.c_uint8)  # 0 = not ready, 1 = ready, 2 = spectating
    ]
