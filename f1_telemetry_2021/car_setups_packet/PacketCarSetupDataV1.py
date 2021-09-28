from f1_telemetry_2019 import PackedLittleEndianStructure, PacketHeader, CarSetupDataV1


class PacketCarSetupDataV1(PackedLittleEndianStructure):
    """This packet details the car setups for each vehicle in the session.

    Note that in multiplayer games, other player cars will appear as blank, you will only be able to see your car
    setup and AI cars.

    Frequency: 2 per second
    Size: 843 bytes
    Version: 1
    """
    _fields_ = [
        ('header', PacketHeader),  # Header
        ('carSetups', CarSetupDataV1 * 20)
    ]


