import ctypes

from f1_telemetry_2019.PackedLittleEndianStructure import PackedLittleEndianStructure


class PacketHeader(PackedLittleEndianStructure):
    """The header for each of the UDP telemetry packets."""
    _fields_ = [
        ('packetFormat', ctypes.c_uint16),  # 2019
        ('gameMajorVersion', ctypes.c_uint8),  # Game major version - "X.00"
        ('gameMinorVersion', ctypes.c_uint8),  # Game minor version - "1.XX"
        ('packetVersion', ctypes.c_uint8),  # Version of this packet type, all start from 1
        ('packetId', ctypes.c_uint8),  # Identifier for the packet type, see below
        ('sessionUID', ctypes.c_uint64),  # Unique identifier for the session
        ('sessionTime', ctypes.c_float),  # Session timestamp
        ('frameIdentifier', ctypes.c_uint32),  # Identifier for the frame the data was retrieved on
        ('playerCarIndex', ctypes.c_uint8)  # Index of player's car in the array
    ]
