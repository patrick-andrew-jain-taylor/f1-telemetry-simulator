import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure, PacketHeader
from f1_telemetry_2021.final_classification_packet.FinalClassificationDataV1 import FinalClassificationDataV1


class PacketFinalClassificationDataV1(PackedLittleEndianStructure):
    """
    This packet details the final classification at the end of the race, and the data will match with the post race
    results screen. This is especially useful for multiplayer games where it is not always possible to send lap times
    on the final frame because of network delay.

    Frequency: Once at the end of a race
    Size: 839 bytes
    Version: 1

    """
    _fields_ = [
        ('header', PacketHeader),  # Header
        ('numCars', ctypes.c_uint8),  # Number of cars in the final classification
        ('classificationData', FinalClassificationDataV1 * 22)  # Number of cars in the final classification
    ]
