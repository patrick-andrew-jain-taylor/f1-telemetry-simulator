"""

F1 2021 UDP Telemetry support package

This package is based on the CodeMasters Forum post documenting the F1 2019 packet format:

    https://forums.codemasters.com/topic/80231-f1-2021-udp-specification/

"""

import ctypes
import enum

from PackedLittleEndianStructure import PackedLittleEndianStructure
from PacketHeader import PacketHeader
from car_setups_packet.PacketCarSetupDataV1 import PacketCarSetupDataV1
from car_status_packet.PacketCarStatusDataV1 import PacketCarStatusDataV1
from car_telemetry_packet.PacketCarTelemetryDataV1 import PacketCarTelemetryDataV1
from event_packet.PacketEventDataV1 import PacketEventDataV1
from final_classification_packet.PacketFinalClassificationDataV1 import PacketFinalClassificationDataV1
from lobby_info_packet.PacketLobbyInfoDataV1 import PacketLobbyInfoDataV1
from lap_data_packet.PacketLapDataV1 import PacketLapDataV1
from motion_packet.PacketMotionDataV1 import PacketMotionDataV1
from participants_packet.PacketParticipantsDataV1 import PacketParticipantsDataV1
from session_packet.PacketSessionDataV1 import PacketSessionDataV1

###################################################################
#                                                                 #
#  Appendices: various value enumerations used in the UDP output  #
#                                                                 #
###################################################################

TeamIDs = {
    0: 'Mercedes',
    1: 'Ferrari',
    2: 'Red Bull Racing',
    3: 'Williams',
    4: 'Racing Point',
    5: 'Renault',
    6: 'Toro Rosso',
    7: 'Haas',
    8: 'McLaren',
    9: 'Alfa Romeo',
    10: 'McLaren 1988',
    11: 'McLaren 1991',
    12: 'Williams 1992',
    13: 'Ferrari 1995',
    14: 'Williams 1996',
    15: 'McLaren 1998',
    16: 'Ferrari 2002',
    17: 'Ferrari 2004',
    18: 'Renault 2006',
    19: 'Ferrari 2007',
    21: 'Red Bull 2010',
    22: 'Ferrari 1976',
    23: 'ART Grand Prix',
    24: 'Campos Vexatec Racing',
    25: 'Carlin',
    26: 'Charouz Racing System',
    27: 'DAMS',
    28: 'Russian Time',
    29: 'MP Motorsport',
    30: 'Pertamina',
    31: 'McLaren 1990',
    32: 'Trident',
    33: 'BWT Arden',
    34: 'McLaren 1976',
    35: 'Lotus 1972',
    36: 'Ferrari 1979',
    37: 'McLaren 1982',
    38: 'Williams 2003',
    39: 'Brawn 2009',
    40: 'Lotus 1978',
    63: 'Ferrari 1990',
    64: 'McLaren 2010',
    65: 'Ferrari 2010'
}

DriverIDs = {
    0: 'Carlos Sainz',
    1: 'Daniil Kvyat',
    2: 'Daniel Ricciardo',
    6: 'Kimi Räikkönen',
    7: 'Lewis Hamilton',
    9: 'Max Verstappen',
    10: 'Nico Hulkenberg',
    11: 'Kevin Magnussen',
    12: 'Romain Grosjean',
    13: 'Sebastian Vettel',
    14: 'Sergio Perez',
    15: 'Valtteri Bottas',
    19: 'Lance Stroll',
    20: 'Arron Barnes',
    21: 'Martin Giles',
    22: 'Alex Murray',
    23: 'Lucas Roth',
    24: 'Igor Correia',
    25: 'Sophie Levasseur',
    26: 'Jonas Schiffer',
    27: 'Alain Forest',
    28: 'Jay Letourneau',
    29: 'Esto Saari',
    30: 'Yasar Atiyeh',
    31: 'Callisto Calabresi',
    32: 'Naota Izum',
    33: 'Howard Clarke',
    34: 'Wilhelm Kaufmann',
    35: 'Marie Laursen',
    36: 'Flavio Nieves',
    37: 'Peter Belousov',
    38: 'Klimek Michalski',
    39: 'Santiago Moreno',
    40: 'Benjamin Coppens',
    41: 'Noah Visser',
    42: 'Gert Waldmuller',
    43: 'Julian Quesada',
    44: 'Daniel Jones',
    45: 'Artem Markelov',
    46: 'Tadasuke Makino',
    47: 'Sean Gelael',
    48: 'Nyck De Vries',
    49: 'Jack Aitken',
    50: 'George Russell',
    51: 'Maximilian Günther',
    52: 'Nirei Fukuzumi',
    53: 'Luca Ghiotto',
    54: 'Lando Norris',
    55: 'Sérgio Sette Câmara',
    56: 'Louis Delétraz',
    57: 'Antonio Fuoco',
    58: 'Charles Leclerc',
    59: 'Pierre Gasly',
    62: 'Alexander Albon',
    63: 'Nicholas Latifi',
    64: 'Dorian Boccolacci',
    65: 'Niko Kari',
    66: 'Roberto Merhi',
    67: 'Arjun Maini',
    68: 'Alessio Lorandi',
    69: 'Ruben Meijer',
    70: 'Rashid Nair',
    71: 'Jack Tremblay',
    74: 'Antonio Giovinazzi',
    75: 'Robert Kubica'
}

TrackIDs = {
    0: 'Melbourne',
    1: 'Paul Ricard',
    2: 'Shanghai',
    3: 'Sakhir (Bahrain)',
    4: 'Catalunya',
    5: 'Monaco',
    6: 'Montreal',
    7: 'Silverstone',
    8: 'Hockenheim',
    9: 'Hungaroring',
    10: 'Spa',
    11: 'Monza',
    12: 'Singapore',
    13: 'Suzuka',
    14: 'Abu Dhabi',
    15: 'Texas',
    16: 'Brazil',
    17: 'Austria',
    18: 'Sochi',
    19: 'Mexico',
    20: 'Baku (Azerbaijan)',
    21: 'Sakhir Short',
    22: 'Silverstone Short',
    23: 'Texas Short',
    24: 'Suzuka Short'
}

NationalityIDs = {
    1: 'American',
    2: 'Argentinian',
    3: 'Australian',
    4: 'Austrian',
    5: 'Azerbaijani',
    6: 'Bahraini',
    7: 'Belgian',
    8: 'Bolivian',
    9: 'Brazilian',
    10: 'British',
    11: 'Bulgarian',
    12: 'Cameroonian',
    13: 'Canadian',
    14: 'Chilean',
    15: 'Chinese',
    16: 'Colombian',
    17: 'Costa Rican',
    18: 'Croatian',
    19: 'Cypriot',
    20: 'Czech',
    21: 'Danish',
    22: 'Dutch',
    23: 'Ecuadorian',
    24: 'English',
    25: 'Emirian',
    26: 'Estonian',
    27: 'Finnish',
    28: 'French',
    29: 'German',
    30: 'Ghanaian',
    31: 'Greek',
    32: 'Guatemalan',
    33: 'Honduran',
    34: 'Hong Konger',
    35: 'Hungarian',
    36: 'Icelander',
    37: 'Indian',
    38: 'Indonesian',
    39: 'Irish',
    40: 'Israeli',
    41: 'Italian',
    42: 'Jamaican',
    43: 'Japanese',
    44: 'Jordanian',
    45: 'Kuwaiti',
    46: 'Latvian',
    47: 'Lebanese',
    48: 'Lithuanian',
    49: 'Luxembourger',
    50: 'Malaysian',
    51: 'Maltese',
    52: 'Mexican',
    53: 'Monegasque',
    54: 'New Zealander',
    55: 'Nicaraguan',
    56: 'North Korean',
    57: 'Northern Irish',
    58: 'Norwegian',
    59: 'Omani',
    60: 'Pakistani',
    61: 'Panamanian',
    62: 'Paraguayan',
    63: 'Peruvian',
    64: 'Polish',
    65: 'Portuguese',
    66: 'Qatari',
    67: 'Romanian',
    68: 'Russian',
    69: 'Salvadoran',
    70: 'Saudi',
    71: 'Scottish',
    72: 'Serbian',
    73: 'Singaporean',
    74: 'Slovakian',
    75: 'Slovenian',
    76: 'South Korean',
    77: 'South African',
    78: 'Spanish',
    79: 'Swedish',
    80: 'Swiss',
    81: 'Thai',
    82: 'Turkish',
    83: 'Uruguayan',
    84: 'Ukrainian',
    85: 'Venezuelan',
    86: 'Welsh'
}

# These surface types are from physics data and show what type of contact each wheel is experiencing.
SurfaceTypes = {
    0: 'Tarmac',
    1: 'Rumble strip',
    2: 'Concrete',
    3: 'Rock',
    4: 'Gravel',
    5: 'Mud',
    6: 'Sand',
    7: 'Grass',
    8: 'Water',
    9: 'Cobblestone',
    10: 'Metal',
    11: 'Ridged'
}


@enum.unique
class ButtonFlag(enum.IntEnum):
    """Bit-mask values for the 'button' field in Car Telemetry Data packets."""
    CROSS = 0x0001
    TRIANGLE = 0x0002
    CIRCLE = 0x0004
    SQUARE = 0x0008
    D_PAD_LEFT = 0x0010
    D_PAD_RIGHT = 0x0020
    D_PAD_UP = 0x0040
    D_PAD_DOWN = 0x0080
    OPTIONS = 0x0100
    L1 = 0x0200
    R1 = 0x0400
    L2 = 0x0800
    R2 = 0x1000
    LEFT_STICK_CLICK = 0x2000
    RIGHT_STICK_CLICK = 0x4000


ButtonFlag.description = {
    ButtonFlag.CROSS: "Cross or A",
    ButtonFlag.TRIANGLE: "Triangle or Y",
    ButtonFlag.CIRCLE: "Circle or B",
    ButtonFlag.SQUARE: "Square or X",
    ButtonFlag.D_PAD_LEFT: "D-pad Left",
    ButtonFlag.D_PAD_RIGHT: "D-pad Right",
    ButtonFlag.D_PAD_UP: "D-pad Up",
    ButtonFlag.D_PAD_DOWN: "D-pad Down",
    ButtonFlag.OPTIONS: "Options or Menu",
    ButtonFlag.L1: "L1 or LB",
    ButtonFlag.R1: "R1 or RB",
    ButtonFlag.L2: "L2 or LT",
    ButtonFlag.R2: "R2 or RT",
    ButtonFlag.LEFT_STICK_CLICK: "Left Stick Click",
    ButtonFlag.RIGHT_STICK_CLICK: "Right Stick Click"
}

##################################
#                                #
#  Decode UDP telemetry packets  #
#                                #
##################################

# Map from (packetFormat, packetVersion, packetId) to a specific packet type.
HeaderFieldsToPacketType = {
    (2019, 1, 0): PacketMotionDataV1,
    (2019, 1, 1): PacketSessionDataV1,
    (2019, 1, 2): PacketLapDataV1,
    (2019, 1, 3): PacketEventDataV1,
    (2019, 1, 4): PacketParticipantsDataV1,
    (2019, 1, 5): PacketCarSetupDataV1,
    (2019, 1, 6): PacketCarTelemetryDataV1,
    (2019, 1, 7): PacketCarStatusDataV1
}


class UnpackError(Exception):
    pass


def unpack_udp_packet(packet: bytes) -> PackedLittleEndianStructure:
    """Convert raw UDP packet to an appropriately-typed telemetry packet.

    Args:
        packet: the contents of the UDP packet to be unpacked.

    Returns:
        The decoded packet structure.

    Raises:
        UnpackError if a problem is detected.
    """
    actual_packet_size = len(packet)

    header_size = ctypes.sizeof(PacketHeader)

    if actual_packet_size < header_size:
        raise UnpackError("Bad telemetry packet: too short ({} bytes).".format(actual_packet_size))

    header = PacketHeader.from_buffer_copy(packet)
    key = (header.packetFormat, header.packetVersion, header.packetId)

    if key not in HeaderFieldsToPacketType:
        raise UnpackError("Bad telemetry packet: no match for key fields {!r}.".format(key))

    packet_type = HeaderFieldsToPacketType[key]

    expected_packet_size = ctypes.sizeof(packet_type)

    if actual_packet_size != expected_packet_size:
        raise UnpackError(
            "Bad telemetry packet: bad size for {} packet; expected {} bytes but received {} bytes.".format(
                packet_type.__name__, expected_packet_size, actual_packet_size))

    return packet_type.from_buffer_copy(packet)


#########################################################################
#                                                                       #
#  Verify packet sizes if this module is executed rather than imported  #
#                                                                       #
#########################################################################

if __name__ == "__main__":
    # Check all the packet sizes.

    assert ctypes.sizeof(PacketMotionDataV1) == 1464
    assert ctypes.sizeof(PacketSessionDataV1) == 625
    assert ctypes.sizeof(PacketLapDataV1) == 970
    assert ctypes.sizeof(PacketEventDataV1) == 36
    assert ctypes.sizeof(PacketParticipantsDataV1) == 1257
    assert ctypes.sizeof(PacketCarSetupDataV1) == 1102
    assert ctypes.sizeof(PacketCarTelemetryDataV1) == 1347  # TODO: Determine new size
    assert ctypes.sizeof(PacketCarStatusDataV1) == 1058
    assert ctypes.sizeof(PacketFinalClassificationDataV1) == 839
    assert ctypes.sizeof(PacketLobbyInfoDataV1) == 1191
