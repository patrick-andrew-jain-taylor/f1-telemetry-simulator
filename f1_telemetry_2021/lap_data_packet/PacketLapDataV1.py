from f1_telemetry_2021 import PackedLittleEndianStructure, PacketHeader
from f1_telemetry_2021.lap_data_packet.LapDataV1 import LapDataV1


class PacketLapDataV1(PackedLittleEndianStructure):
    """The lap data packet gives details of all the cars in the session.

    Frequency: Rate as specified in menus
    Size: 970 bytes
    Version: 1
    """
    _fields_ = [
        ('header', PacketHeader),  # Header
        ('lapData', LapDataV1 * 22)  # Lap data for all cars on track
    ]
