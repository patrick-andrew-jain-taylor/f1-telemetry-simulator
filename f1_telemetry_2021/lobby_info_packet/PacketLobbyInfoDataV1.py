import ctypes

from f1_telemetry_2021 import PackedLittleEndianStructure, PacketHeader
from LobbyInfoDataV1 import LobbyInfoDataV1


class PacketLobbyInfoDataV1(PackedLittleEndianStructure):
    """
    This packet details the players currently in a multiplayer lobby. It details each player’s selected car,
    any AI involved in the game and also the ready status of each of the participants.

    Frequency: Two every second when in the lobby
    Size: 1191 bytes
    Version: 1
    """
    _fields_ = [
        ('header', PacketHeader),  # Header
        ('numPlayers', ctypes.c_uint8),  # Number of players in the lobby data
        ('lobbyPlayers', LobbyInfoDataV1 * 22)
    ]
