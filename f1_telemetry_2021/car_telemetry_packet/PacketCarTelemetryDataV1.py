import ctypes

from f1_telemetry_2019 import PackedLittleEndianStructure, PacketHeader, CarTelemetryDataV1


class PacketCarTelemetryDataV1(PackedLittleEndianStructure):
    """This packet details telemetry for all the cars in the race.

    It details various values that would be recorded on the car such as speed, throttle application, DRS etc.

    Frequency: Rate as specified in menus
    Size: 1347 bytes
    Version: 1
    """
    _fields_ = [
        ('header', PacketHeader),  # Header
        ('carTelemetryData', CarTelemetryDataV1 * 20),
        ('buttonStatus', ctypes.c_uint32)  # Bit flags specifying which buttons are being
        # pressed currently - see appendices
    ]
