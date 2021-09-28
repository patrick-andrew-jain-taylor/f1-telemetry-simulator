from f1_telemetry_2021 import PackedLittleEndianStructure, PacketHeader
from f1_telemetry_2021.car_status_packet.CarStatusDataV1 import CarStatusDataV1


class PacketCarStatusDataV1(PackedLittleEndianStructure):
    """This packet details car statuses for all the cars in the race.

    It includes values such as the damage readings on the car.

    Frequency: Rate as specified in menus
    Size: 1058 bytes
    Version: 1
    """
    _fields_ = [
        ('header', PacketHeader),  # Header
        ('carStatusData', CarStatusDataV1 * 22)
    ]
