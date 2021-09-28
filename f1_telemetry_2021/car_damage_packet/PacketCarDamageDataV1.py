from f1_telemetry_2021 import PackedLittleEndianStructure, PacketHeader
from CarDamageDataV1 import CarDamageDataV1


class PacketCarDamageDataV1(PackedLittleEndianStructure):
    """
    This packet details car damage parameters for all the cars in the race.

    Frequency: 2 per second
    Size: 882 bytes
    Version: 1
    """
    _fields_ = [
        ('header', PacketHeader),  # Header
        ('carDamageData', CarDamageDataV1 * 22)  # Header
    ]
