import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure


class CarStatusDataV1(PackedLittleEndianStructure):
    """This type is used for the 20-element 'carStatusData' array of the PacketCarStatusData_V1 type, defined below.

    There is some data in the Car Status packets that you may not want other players seeing if you are in a
    multiplayer game. This is controlled by the "Your Telemetry" setting in the Telemetry options. The options are:

        Restricted (Default) – other players viewing the UDP data will not see values for your car;
        Public – all other players can see all the data for your car.

    Note: You can always see the data for the car you are driving regardless of the setting.

    The following data items are set to zero if the player driving the car in question has their "Your Telemetry" set
    to "Restricted":

        fuelInTank
        fuelCapacity
        fuelMix
        fuelRemainingLaps
        frontBrakeBias
        frontLeftWingDamage
        frontRightWingDamage
        rearWingDamage
        engineDamage
        gearBoxDamage
        tyresWear (All four wheels)
        tyresDamage (All four wheels)
        ersDeployMode
        ersStoreEnergy
        ersDeployedThisLap
        ersHarvestedThisLapMGUK
        ersHarvestedThisLapMGUH
    """
    _fields_ = [
        ('tractionControl', ctypes.c_uint8),  # 0 (off) - 2 (high)
        ('antiLockBrakes', ctypes.c_uint8),  # 0 (off) - 1 (on)
        ('fuelMix', ctypes.c_uint8),  # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
        ('frontBrakeBias', ctypes.c_uint8),  # Front brake bias (percentage)
        ('pitLimiterStatus', ctypes.c_uint8),  # Pit limiter status - 0 = off, 1 = on
        ('fuelInTank', ctypes.c_float),  # Current fuel mass
        ('fuelCapacity', ctypes.c_float),  # Fuel capacity
        ('fuelRemainingLaps', ctypes.c_float),  # Fuel remaining in terms of laps (value on MFD)
        ('maxRPM', ctypes.c_uint16),  # Cars max RPM, point of rev limiter
        ('idleRPM', ctypes.c_uint16),  # Cars idle RPM
        ('maxGears', ctypes.c_uint8),  # Maximum number of gears
        ('drsAllowed', ctypes.c_uint8),  # 0 = not allowed, 1 = allowed, -1 = unknown
        ('tyresWear', ctypes.c_uint8 * 4),  # Tyre wear percentage
        ('actualTyreCompound', ctypes.c_uint8),  # F1 Modern - 16 = C5, 17 = C4, 18 = C3, 19 = C2, 20 = C1
        # 7 = inter, 8 = wet
        # F1 Classic - 9 = dry, 10 = wet
        # F2 – 11 = super soft, 12 = soft, 13 = medium, 14 = hard
        # 15 = wet
        ('tyreVisualCompound', ctypes.c_uint8),  # F1 visual (can be different from actual compound)
        # 16 = soft, 17 = medium, 18 = hard, 7 = inter, 8 = wet
        # F1 Classic – same as above
        # F2 – same as above
        ('tyresDamage', ctypes.c_uint8 * 4),  # Tyre damage (percentage)
        ('frontLeftWingDamage', ctypes.c_uint8),  # Front left wing damage (percentage)
        ('frontRightWingDamage', ctypes.c_uint8),  # Front right wing damage (percentage)
        ('rearWingDamage', ctypes.c_uint8),  # Rear wing damage (percentage)
        ('engineDamage', ctypes.c_uint8),  # Engine damage (percentage)
        ('gearBoxDamage', ctypes.c_uint8),  # Gear box damage (percentage)
        ('vehicleFiaFlags', ctypes.c_int8),  # -1 = invalid/unknown, 0 = none, 1 = green
        # 2 = blue, 3 = yellow, 4 = red
        ('ersStoreEnergy', ctypes.c_float),  # ERS energy store in Joules
        ('ersDeployMode', ctypes.c_uint8),  # ERS deployment mode, 0 = none, 1 = low, 2 = medium
        # 3 = high, 4 = overtake, 5 = hotlap
        ('ersHarvestedThisLapMGUK', ctypes.c_float),  # ERS energy harvested this lap by MGU-K
        ('ersHarvestedThisLapMGUH', ctypes.c_float),  # ERS energy harvested this lap by MGU-H
        ('ersDeployedThisLap', ctypes.c_float)  # ERS energy deployed this lap
    ]
