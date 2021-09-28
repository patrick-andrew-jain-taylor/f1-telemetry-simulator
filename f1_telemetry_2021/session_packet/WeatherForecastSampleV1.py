import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure


class WeatherForecastSampleV1(PackedLittleEndianStructure):
    """This type is used for the 56-element 'weatherForecastSamples' array of the PacketSessionData_V1 type,
    defined below. """
    _fields_ = [
        ('sessionType', ctypes.c_uint8),  # 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P, 5 = Q1, 6 = Q2, 7 = Q3,
        # 8 = Short Q, 9 = OSQ, 10 = R, 11 = R2, 12 = Time Trial
        ('timeOffset', ctypes.c_uint8),  # Time in minutes the forecast is for
        ('weather', ctypes.c_uint8),  # Weather - 0 = clear, 1 = light cloud, 2 = overcast, 3 = light rain, 4 = heavy
        # rain, 5 = storm
        ('trackTemperature', ctypes.c_int8),  # Track temp. in degrees Celsius
        ('trackTemperatureChange', ctypes.c_int8),  # Track temp. change – 0 = up, 1 = down, 2 = no change
        ('airTemperature', ctypes.c_int8),  # Air temp. in degrees celsius
        ('airTemperatureChange', ctypes.c_int8),  # Air temp. change – 0 = up, 1 = down, 2 = no change
        ('rainPercentage', ctypes.c_uint8)  # Rain percentage (0-100)
    ]
