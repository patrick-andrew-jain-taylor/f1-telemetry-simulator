import ctypes

from f1_telemetry_2019 import PackedLittleEndianStructure


class CarTelemetryDataV1(PackedLittleEndianStructure):
    """This type is used for the 20-element 'carTelemetryData' array of the PacketCarTelemetryData_V1 type,
    defined below. """
    _fields_ = [
        ('speed', ctypes.c_uint16),  # Speed of car in kilometres per hour
        ('throttle', ctypes.c_float),  # Amount of throttle applied (0.0 to 1.0)
        ('steer', ctypes.c_float),  # Steering (-1.0 (full lock left) to 1.0 (full lock right))
        ('brake', ctypes.c_float),  # Amount of brake applied (0 to 1.0)
        ('clutch', ctypes.c_uint8),  # Amount of clutch applied (0 to 100)
        ('gear', ctypes.c_int8),  # Gear selected (1-8, N=0, R=-1)
        ('engineRPM', ctypes.c_uint16),  # Engine RPM
        ('drs', ctypes.c_uint8),  # 0 = off, 1 = on
        ('revLightsPercent', ctypes.c_uint8),  # Rev lights indicator (percentage)
        ('brakesTemperature', ctypes.c_uint16 * 4),  # Brakes temperature (celsius)
        ('tyresSurfaceTemperature', ctypes.c_uint16 * 4),  # Tyres surface temperature (celsius)
        ('tyresInnerTemperature', ctypes.c_uint16 * 4),  # Tyres inner temperature (celsius)
        ('engineTemperature', ctypes.c_uint16),  # Engine temperature (celsius)
        ('tyresPressure', ctypes.c_float * 4),  # Tyres pressure (PSI)
        ('surfaceType', ctypes.c_uint8 * 4)  # Driving surface, see appendices
    ]


