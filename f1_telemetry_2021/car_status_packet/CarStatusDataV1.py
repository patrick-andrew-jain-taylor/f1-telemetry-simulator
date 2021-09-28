import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure


class CarStatusDataV1(PackedLittleEndianStructure):
    """This type is used for the 22-element 'carStatusData' array of the PacketCarStatusData_V1 type, defined below.

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
        ('tractionControl', ctypes.c_uint8),  # Traction control - 0 = off, 1 = medium, 2 = full
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
        ('drsAllowed', ctypes.c_uint8),  # 0 = not allowed, 1 = allowed
        ('drsActivationDistance', ctypes.c_uint16),  # 0 = DRS not available, non-zero - DRS will be available in [X]
        # metres
        ('actualTyreCompound', ctypes.c_uint8),  # F1 Modern - 16 = C5, 17 = C4, 18 = C3, 19 = C2, 20 = C1,
        # 7 = inter, 8 = wet, F1 Classic - 9 = dry, 10 = wet, F2 – 11 = super soft, 12 = soft, 13 = medium,
        # 14 = hard, 15 = wet
        ('visualTyreCompound', ctypes.c_uint8),  # F1 visual (can be different from actual compound) 16 = soft,
        # 17 = medium, 18 = hard, 7 = inter, 8 = wet F1 Classic – same as above, F2 ‘19, 15 = wet, 19 – super soft,
        # 20 = soft, 21 = medium , 22 = hard
        ('tyresAgeLaps', ctypes.c_uint8),  # Age in laps of the current set of tyres
        ('vehicleFiaFlags', ctypes.c_int8),  # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        ('ersStoreEnergy', ctypes.c_float),  # ERS energy store in Joules
        ('ersDeployMode', ctypes.c_uint8),  # ERS deployment mode, 0 = none, 1 = medium, 2 = hotlap, 3 = overtake
        ('ersHarvestedThisLapMGUK', ctypes.c_float),  # ERS energy harvested this lap by MGU-K
        ('ersHarvestedThisLapMGUH', ctypes.c_float),  # ERS energy harvested this lap by MGU-H
        ('ersDeployedThisLap', ctypes.c_float),  # ERS energy deployed this lap
        ('networkPaused', ctypes.c_uint8)  # Whether the car is paused in a network game
    ]
