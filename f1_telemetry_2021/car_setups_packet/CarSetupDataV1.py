import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure


class CarSetupDataV1(PackedLittleEndianStructure):
    """This type is used for the 20-element 'carSetups' array of the PacketCarSetupData_V1 type, defined below."""
    _fields_ = [
        ('frontWing', ctypes.c_uint8),  # Front wing aero
        ('rearWing', ctypes.c_uint8),  # Rear wing aero
        ('onThrottle', ctypes.c_uint8),  # Differential adjustment on throttle (percentage)
        ('offThrottle', ctypes.c_uint8),  # Differential adjustment off throttle (percentage)
        ('frontCamber', ctypes.c_float),  # Front camber angle (suspension geometry)
        ('rearCamber', ctypes.c_float),  # Rear camber angle (suspension geometry)
        ('frontToe', ctypes.c_float),  # Front toe angle (suspension geometry)
        ('rearToe', ctypes.c_float),  # Rear toe angle (suspension geometry)
        ('frontSuspension', ctypes.c_uint8),  # Front suspension
        ('rearSuspension', ctypes.c_uint8),  # Rear suspension
        ('frontAntiRollBar', ctypes.c_uint8),  # Front anti-roll bar
        ('rearAntiRollBar', ctypes.c_uint8),  # Rear anti-roll bar
        ('frontSuspensionHeight', ctypes.c_uint8),  # Front ride height
        ('rearSuspensionHeight', ctypes.c_uint8),  # Rear ride height
        ('brakePressure', ctypes.c_uint8),  # Brake pressure (percentage)
        ('brakeBias', ctypes.c_uint8),  # Brake bias (percentage)
        ('frontTyrePressure', ctypes.c_float),  # Front tyre pressure (PSI)
        ('rearTyrePressure', ctypes.c_float),  # Rear tyre pressure (PSI)
        ('ballast', ctypes.c_uint8),  # Ballast
        ('fuelLoad', ctypes.c_float)  # Fuel load
    ]
