from f1_telemetry_2019 import PackedLittleEndianStructure, PacketHeader, LapDataV1


class PacketLapDataV1(PackedLittleEndianStructure):
    """The lap data packet gives details of all the cars in the session.

    Frequency: Rate as specified in menus
    Size: 843 bytes
    Version: 1
    """
    _fields_ = [
        ('header', PacketHeader),  # Header
        ('lapData', LapDataV1 * 20)  # Lap data for all cars on track
    ]
