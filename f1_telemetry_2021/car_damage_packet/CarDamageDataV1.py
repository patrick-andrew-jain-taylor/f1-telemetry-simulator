import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure


class CarDamageDataV1(PackedLittleEndianStructure):
    _fields_ = [
        ('tyresWear', ctypes.c_float * 4),  # Tyre wear (percentage)
        ('tyresDamage', ctypes.c_uint8 * 4),  # Tyre damage (percentage)
        ('brakesDamage', ctypes.c_uint8 * 4),  # Brakes damage (percentage)
        ('frontLeftWingDamage', ctypes.c_uint8),  # Front left wing damage (percentage)
        ('frontRightWingDamage', ctypes.c_uint8),  # Front right wing damage (percentage)
        ('rearWingDamage', ctypes.c_uint8),  # Rear wing damage (percentage)
        ('floorDamage', ctypes.c_uint8),  # Floor damage (percentage)
        ('diffuserDamage', ctypes.c_uint8),  # Diffuser damage (percentage)
        ('sidepodDamage', ctypes.c_uint8),  # Sidepod damage (percentage)
        ('drsFault', ctypes.c_uint8),  # Indicator for DRS fault, 0 = OK, 1 = fault
        ('gearBoxDamage', ctypes.c_uint8),  # Gear box damage (percentage)
        ('engineDamage', ctypes.c_uint8),  # Engine damage (percentage)
        ('engineMGUHWear', ctypes.c_uint8),  # Engine wear MGU-H (percentage)
        ('engineESWear', ctypes.c_uint8),  # Engine wear ES (percentage)
        ('engineCEWear', ctypes.c_uint8),  # Engine wear CE (percentage)
        ('engineICEWear', ctypes.c_uint8),  # Engine wear ICE (percentage)
        ('engineMGUKWear', ctypes.c_uint8),  # Engine wear MGU-K (percentage)
        ('engineTCWear', ctypes.c_uint8)  # Engine wear TC (percentage)
    ]
