from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from typing import Optional

__NAMESPACE__ = 'http://www.pubtrans.com/PT/1.0'


class ArrivalType(Enum):
    """
    Denotes conditions for alighting at a stop or flexible alighting up to this
    point.
    """
    NO_STOP = 'NO_STOP'
    NO_ALIGHTING = 'NO_ALIGHTING'
    STOP_IF_ALIGHTING = 'STOP_IF_ALIGHTING'
    ALWAYS_STOP = 'ALWAYS_STOP'
    FLEXIBLE_ALIGHTING_UPTO_HERE = 'FLEXIBLE_ALIGHTING_UPTO_HERE'


@dataclass
class BlockRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9041000000000000,
                                   'max_inclusive': 9041999999999999,
                               })


@dataclass
class BridgingDeviceRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9095000000000000,
                                   'max_inclusive': 9095999999999999,
                               })


class DepartureType(Enum):
    """
    Denotes conditions for boarding at a stop or flexible boarding from this point.
    """
    NO_STOP = 'NO_STOP'
    NO_BOARDING = 'NO_BOARDING'
    STOP_IF_BOARDING = 'STOP_IF_BOARDING'
    ALWAYS_STOP = 'ALWAYS_STOP'
    FLEXIBLE_BOARDING_FROM_HERE = 'FLEXIBLE_BOARDING_FROM_HERE'


@dataclass
class DeviationCaseRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9076000000000000,
                                   'max_inclusive': 9076999999999999,
                               })


@dataclass
class DirectionOfLineRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9014000000000000,
                                   'max_inclusive': 9014999999999999,
                               })


@dataclass
class DutyRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9000000000000000,
                                   'max_inclusive': 9999999999999999,
                               })


@dataclass
class EmployeeRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9051000000000000,
                                   'max_inclusive': 9051999999999999,
                               })


class InformPassengersCondition(Enum):
    """
    Describes under which conditions passengers should be informed.
    """
    ALWAYS = 'ALWAYS'
    ONLY_IF_ORDERED = 'ONLY_IF_ORDERED'
    ONLY_IF_SIGNED_ON = 'ONLY_IF_SIGNED_ON'
    NEVER = 'NEVER'


@dataclass
class JourneyPatternPointRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9025000000000000,
                                   'max_inclusive': 9025999999999999,
                               })


@dataclass
class LineRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9011000000000000,
                                   'max_inclusive': 9011999999999999,
                               })


@dataclass
class NamedJourneyPatternRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 0,
                                   'max_inclusive': 8999999999999999,
                               })


@dataclass
class PlaceRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9091000000000000,
                                   'max_inclusive': 9091999999999999,
                               })


class SecondaryDestinationType(Enum):
    """Denotes how the second "row" of the destination text should be interpreted.

    I. e.  a via destination

    :cvar ENDS_AT: Denotes that the Secondary Destination is a more
        precise identification of the Primary Destination, like a
        terminal name when the Primary Destination is a city.
    :cvar VIA: Denotes that the Secondary Destination is a via-name.
    :cvar TRANSFER_AT: Transfer at secondary destination and continue to
        primary destination.
    :cvar CONTINUE_TO: Continue to secondary destination after
        transferring at primary destination.
    :cvar MESSAGE: Denotes that the Secondary Destination is a message
        of some kind, like when announcing the VehicleJourney as an
        extra run.
    :cvar UNKNOWN: Denotes that the Secondary Destination is undefined.
    """
    ENDS_AT = 'ENDS_AT'
    VIA = 'VIA'
    TRANSFER_AT = 'TRANSFER_AT'
    CONTINUE_TO = 'CONTINUE_TO'
    MESSAGE = 'MESSAGE'
    UNKNOWN = 'UNKNOWN'


@dataclass
class StationEntrancePointRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9023000000000000,
                                   'max_inclusive': 9023999999999999,
                               })


@dataclass
class StopAreaRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9021000000000000,
                                   'max_inclusive': 9021999999999999,
                               })


@dataclass
class StopPointRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9022000000000000,
                                   'max_inclusive': 9022999999999999,
                               })


class StopPointType(Enum):
    """I.e.

    A plattform or a refuge.
    """
    BUSSTOP = 'BUSSTOP'
    REFUGE = 'REFUGE'
    PLATFORM = 'PLATFORM'
    TRACK = 'TRACK'
    GATE = 'GATE'
    PIER = 'PIER'
    ENTRANCE = 'ENTRANCE'
    EXIT = 'EXIT'
    UNSPECIFIED = 'UNSPECIFIED'


@dataclass
class TransportAuthorityRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9010000000000000,
                                   'max_inclusive': 9010999999999999,
                               })


class TransportMode(Enum):
    """Classification of transport systems.

    I. e. TRAIN, FERRY
    """
    BUS = 'BUS'
    TRAM = 'TRAM'
    METRO = 'METRO'
    TRAIN = 'TRAIN'
    FERRY = 'FERRY'
    SHIP = 'SHIP'
    TAXI = 'TAXI'


@dataclass
class VehicleJourneyRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9015000000000000,
                                   'max_inclusive': 9016999999999999,
                               })


@dataclass
class VehicleOperatorRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9013000000000000,
                                   'max_inclusive': 9013999999999999,
                               })


@dataclass
class VehicleRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9031000000000000,
                                   'max_inclusive': 9031999999999999,
                               })


class YesNo(Enum):
    Y = 'Y'
    N = 'N'
