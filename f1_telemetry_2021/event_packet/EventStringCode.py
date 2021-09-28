import enum


@enum.unique
class EventStringCode(enum.Enum):
    """Value as specified in the PacketEventData_V1.eventStringCode header field, used to distinguish packet types."""
    SSTA = b'SSTA'
    SEND = b'SEND'
    FTLP = b'FTLP'
    RTMT = b'RTMT'
    DRSE = b'DRSE'
    DRSD = b'DRSD'
    TMPT = b'TMPT'
    CHQF = b'CHQF'
    RCWN = b'RCWN'
    PENA = b'PENA'
    SPTP = b'SPTP'
    STLG = b'STLG'
    LGOT = b'LGOT'
    DTSV = b'DTSV'
    SGSV = b'SGSV'
    FLBK = b'FLBK'
    BUTN = b'BUTN'


EventStringCode.short_description = {
    EventStringCode.SSTA: 'Session Started',
    EventStringCode.SEND: 'Session Ended',
    EventStringCode.FTLP: 'Fastest Lap',
    EventStringCode.RTMT: 'Retirement',
    EventStringCode.DRSE: 'DRS enabled',
    EventStringCode.DRSD: 'DRS disabled',
    EventStringCode.TMPT: 'Team mate in pits',
    EventStringCode.CHQF: 'Chequered flag',
    EventStringCode.RCWN: 'Race Winner',
    EventStringCode.PENA: 'Penalty Issued',
    EventStringCode.SPTP: 'Speed Trap Triggered',
    EventStringCode.STLG: 'Start lights',
    EventStringCode.LGOT: 'Lights out',
    EventStringCode.DTSV: 'Drive through served',
    EventStringCode.SGSV: 'Stop go served',
    EventStringCode.FLBK: 'Flashback',
    EventStringCode.BUTN: 'Button status'
}

EventStringCode.long_description = {
    EventStringCode.SSTA: 'Sent when the session starts',
    EventStringCode.SEND: 'Sent when the session ends',
    EventStringCode.FTLP: 'When a driver achieves the fastest lap',
    EventStringCode.RTMT: 'When a driver retires',
    EventStringCode.DRSE: 'Race control have enabled DRS',
    EventStringCode.DRSD: 'Race control have disabled DRS',
    EventStringCode.TMPT: 'Your team mate has entered the pits',
    EventStringCode.CHQF: 'The chequered flag has been waved',
    EventStringCode.RCWN: 'The race winner is announced',
    EventStringCode.PENA: 'A penalty has been issued – details in event',
    EventStringCode.SPTP: 'Speed trap has been triggered by fastest speed',
    EventStringCode.STLG: 'Start lights – number shown',
    EventStringCode.LGOT: 'Lights out',
    EventStringCode.DTSV: 'Drive through penalty served',
    EventStringCode.SGSV: 'Stop go penalty served',
    EventStringCode.FLBK: 'Flashback activated',
    EventStringCode.BUTN: 'Button status changed'
}
