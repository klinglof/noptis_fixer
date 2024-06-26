from dataclasses import dataclass
from dataclasses import field
from typing import List
from typing import Optional

from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlTime

from static.noptis.ptshared.pt_shared_types import BridgingDeviceRef
from static.noptis.ptshared.pt_shared_types import DirectionOfLineRef
from static.noptis.ptshared.pt_shared_types import InformPassengersCondition
from static.noptis.ptshared.pt_shared_types import JourneyPatternPointRef
from static.noptis.ptshared.pt_shared_types import LineRef
from static.noptis.ptshared.pt_shared_types import NamedJourneyPatternRef
from static.noptis.ptshared.pt_shared_types import StationEntrancePointRef
from static.noptis.ptshared.pt_shared_types import StopAreaRef
from static.noptis.ptshared.pt_shared_types import StopPointRef
from static.noptis.ptshared.pt_shared_types import TransportAuthorityRef
from static.noptis.ptshared.pt_shared_types import VehicleJourneyRef
from static.noptis.ptshared.pt_shared_types import VehicleRef
from static.noptis.ptshared.pt_shared_types import YesNo
from static.noptis.rii_shared_types import ChangeModel
from static.noptis.rii_shared_types import ProgressState
from static.noptis.rii_shared_types import Status

__NAMESPACE__ = 'http://www.pubtrans.com/RII/2.0'


@dataclass
class DatedBlockRef:
    """
    :ivar operating_day_date: Defaults to current date
    :ivar gid:
    """
    operating_day_date: Optional[XmlDate] = field(default=None,
                                                  metadata={
                                                      'name':
                                                      'OperatingDayDate',
                                                      'type': 'Attribute',
                                                  })
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9041000000000000,
                                   'max_inclusive': 9041999999999999,
                               })


@dataclass
class DatedVehicleJourneyRef:
    """
    :ivar operating_day_date: Defaults to current date
    :ivar gid: It is acceptable to provide the DOI Id of the
        VehicleJourney instead of Gid
    """
    operating_day_date: Optional[XmlDate] = field(default=None,
                                                  metadata={
                                                      'name':
                                                      'OperatingDayDate',
                                                      'type': 'Attribute',
                                                  })
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9015000000000000,
                                   'max_inclusive': 9016999999999999,
                               })


@dataclass
class StopPointStatusTimeScope:
    """
    :ivar from_date_time:
    :ivar upto_date_time:
    :ivar from_time_offset: If FromTimeOffset is provided UptoTimeOffset
        must also be provided. If provided these two values further
        restricts the control action to only apply during part of each
        day that is within FromDateTime - UptoDateTime period.
    :ivar upto_time_offset: If the value of UptoTimeOffset is less than
        FromTimeOffset it should be interpreted as beeing on the
        following date.
    """
    from_date_time: Optional[XmlDateTime] = field(default=None,
                                                  metadata={
                                                      'name': 'FromDateTime',
                                                      'type': 'Attribute',
                                                      'required': True,
                                                  })
    upto_date_time: Optional[XmlDateTime] = field(default=None,
                                                  metadata={
                                                      'name': 'UptoDateTime',
                                                      'type': 'Attribute',
                                                      'required': True,
                                                  })
    from_time_offset: Optional[XmlTime] = field(default=None,
                                                metadata={
                                                    'name': 'FromTimeOffset',
                                                    'type': 'Attribute',
                                                })
    upto_time_offset: Optional[XmlTime] = field(default=None,
                                                metadata={
                                                    'name': 'UptoTimeOffset',
                                                    'type': 'Attribute',
                                                })


@dataclass
class TimeScope:
    from_date_time: Optional[XmlDateTime] = field(default=None,
                                                  metadata={
                                                      'name': 'FromDateTime',
                                                      'type': 'Attribute',
                                                      'required': True,
                                                  })
    upto_date_time: Optional[XmlDateTime] = field(default=None,
                                                  metadata={
                                                      'name': 'UptoDateTime',
                                                      'type': 'Attribute',
                                                      'required': True,
                                                  })


@dataclass
class VehicleOperatorOrDepartmentRef:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9013000000000000,
                                   'max_inclusive': 9013999999999999,
                               })


@dataclass
class AllocatedStopPoint:
    """
    :ivar stop_point_ref:
    :ivar journey_pattern_point_ref:
    :ivar reserved_from_date_time: Stop point is not available before
        this time.
    :ivar reserved_upto_date_time: Stop point is not available from this
        time.
    """
    stop_point_ref: Optional[StopPointRef] = field(default=None,
                                                   metadata={
                                                       'name': 'StopPointRef',
                                                       'type': 'Element',
                                                       'namespace': '',
                                                   })
    journey_pattern_point_ref: Optional[JourneyPatternPointRef] = field(
        default=None,
        metadata={
            'name': 'JourneyPatternPointRef',
            'type': 'Element',
            'namespace': '',
        })
    reserved_from_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'ReservedFromDateTime',
            'type': 'Attribute',
        })
    reserved_upto_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'ReservedUptoDateTime',
            'type': 'Attribute',
        })


@dataclass
class ChangeOfBridgingDeviceStatus:
    bridging_device_ref: Optional[BridgingDeviceRef] = field(
        default=None,
        metadata={
            'name': 'BridgingDeviceRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    time_scope: Optional[TimeScope] = field(default=None,
                                            metadata={
                                                'name': 'TimeScope',
                                                'type': 'Element',
                                                'namespace': '',
                                                'required': True,
                                            })
    status: Optional[Status] = field(default=None,
                                     metadata={
                                         'name': 'Status',
                                         'type': 'Attribute',
                                         'required': True,
                                     })


@dataclass
class ChangeOfJourneyProgress:
    monitored_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'MonitoredVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    progress_state: Optional[ProgressState] = field(default=None,
                                                    metadata={
                                                        'name':
                                                        'ProgressState',
                                                        'type': 'Attribute',
                                                        'required': True,
                                                    })


@dataclass
class ChangeOfStationEntrancePointStatus:
    station_entrance_point_ref: Optional[StationEntrancePointRef] = field(
        default=None,
        metadata={
            'name': 'StationEntrancePointRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    time_scope: Optional[TimeScope] = field(default=None,
                                            metadata={
                                                'name': 'TimeScope',
                                                'type': 'Element',
                                                'namespace': '',
                                                'required': True,
                                            })
    status: Optional[Status] = field(default=None,
                                     metadata={
                                         'name': 'Status',
                                         'type': 'Attribute',
                                         'required': True,
                                     })


@dataclass
class DatedCallRef:
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    stop_point_ref: Optional[StopPointRef] = field(default=None,
                                                   metadata={
                                                       'name': 'StopPointRef',
                                                       'type': 'Element',
                                                       'namespace': '',
                                                   })
    journey_pattern_point_ref: Optional[JourneyPatternPointRef] = field(
        default=None,
        metadata={
            'name': 'JourneyPatternPointRef',
            'type': 'Element',
            'namespace': '',
        })
    visit_count: int = field(default=1,
                             metadata={
                                 'name': 'VisitCount',
                                 'type': 'Attribute',
                             })


@dataclass
class JourneyCancellation:
    vehicle_journey_ref: Optional[VehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'VehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
        })
    direction_of_line_ref: Optional[DirectionOfLineRef] = field(
        default=None,
        metadata={
            'name': 'DirectionOfLineRef',
            'type': 'Element',
            'namespace': '',
        })
    line_ref: Optional[LineRef] = field(default=None,
                                        metadata={
                                            'name': 'LineRef',
                                            'type': 'Element',
                                            'namespace': '',
                                        })
    transport_authority_ref: Optional[TransportAuthorityRef] = field(
        default=None,
        metadata={
            'name': 'TransportAuthorityRef',
            'type': 'Element',
            'namespace': '',
        })
    time_scope: Optional[TimeScope] = field(default=None,
                                            metadata={
                                                'name': 'TimeScope',
                                                'type': 'Element',
                                                'namespace': '',
                                            })
    vehicle_operator_ref: Optional[VehicleOperatorOrDepartmentRef] = field(
        default=None,
        metadata={
            'name': 'VehicleOperatorRef',
            'type': 'Element',
            'namespace': '',
        })
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
        })


@dataclass
class JourneyEnd:
    stop_point_ref: Optional[StopPointRef] = field(default=None,
                                                   metadata={
                                                       'name': 'StopPointRef',
                                                       'type': 'Element',
                                                       'namespace': '',
                                                   })
    journey_pattern_point_ref: Optional[JourneyPatternPointRef] = field(
        default=None,
        metadata={
            'name': 'JourneyPatternPointRef',
            'type': 'Element',
            'namespace': '',
        })
    latest_arrival_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'LatestArrivalDateTime',
            'type': 'Attribute',
            'required': True,
        })
    visit_count: int = field(default=1,
                             metadata={
                                 'name': 'VisitCount',
                                 'type': 'Attribute',
                             })


@dataclass
class JourneyOrdering:
    """
    To revoke this operation use JourneyCancellation.
    """
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })


@dataclass
class JourneyStart:
    stop_point_ref: Optional[StopPointRef] = field(default=None,
                                                   metadata={
                                                       'name': 'StopPointRef',
                                                       'type': 'Element',
                                                       'namespace': '',
                                                   })
    journey_pattern_point_ref: Optional[JourneyPatternPointRef] = field(
        default=None,
        metadata={
            'name': 'JourneyPatternPointRef',
            'type': 'Element',
            'namespace': '',
        })
    earliest_departure_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'EarliestDepartureDateTime',
            'type': 'Attribute',
            'required': True,
        })
    visit_count: int = field(default=1,
                             metadata={
                                 'name': 'VisitCount',
                                 'type': 'Attribute',
                             })


@dataclass
class PointInJourneyPatternRef:
    stop_point_ref: Optional[StopPointRef] = field(default=None,
                                                   metadata={
                                                       'name': 'StopPointRef',
                                                       'type': 'Element',
                                                       'namespace': '',
                                                   })
    journey_pattern_point_ref: Optional[JourneyPatternPointRef] = field(
        default=None,
        metadata={
            'name': 'JourneyPatternPointRef',
            'type': 'Element',
            'namespace': '',
        })
    visit_count: Optional[int] = field(default=None,
                                       metadata={
                                           'name': 'VisitCount',
                                           'type': 'Attribute',
                                       })


@dataclass
class StopRefs:
    stop_point_ref: List[StopPointRef] = field(default_factory=list,
                                               metadata={
                                                   'name': 'StopPointRef',
                                                   'type': 'Element',
                                                   'namespace': '',
                                                   'sequence': 1,
                                               })
    stop_area_ref: List[StopAreaRef] = field(default_factory=list,
                                             metadata={
                                                 'name': 'StopAreaRef',
                                                 'type': 'Element',
                                                 'namespace': '',
                                                 'sequence': 1,
                                             })


@dataclass
class TargetPoint:
    stop_point_ref: Optional[StopPointRef] = field(default=None,
                                                   metadata={
                                                       'name': 'StopPointRef',
                                                       'type': 'Element',
                                                       'namespace': '',
                                                   })
    journey_pattern_point_ref: Optional[JourneyPatternPointRef] = field(
        default=None,
        metadata={
            'name': 'JourneyPatternPointRef',
            'type': 'Element',
            'namespace': '',
        })


@dataclass
class VehicleWorkAssignment:
    vehicle_ref: Optional[VehicleRef] = field(default=None,
                                              metadata={
                                                  'name': 'VehicleRef',
                                                  'type': 'Element',
                                                  'namespace': '',
                                                  'required': True,
                                              })
    dated_block_ref: Optional[DatedBlockRef] = field(default=None,
                                                     metadata={
                                                         'name':
                                                         'DatedBlockRef',
                                                         'type': 'Element',
                                                         'namespace': '',
                                                     })
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
        })


@dataclass
class VehicleWorkDeassignment:
    vehicle_ref: Optional[VehicleRef] = field(default=None,
                                              metadata={
                                                  'name': 'VehicleRef',
                                                  'type': 'Element',
                                                  'namespace': '',
                                                  'required': True,
                                              })
    dated_block_ref: Optional[DatedBlockRef] = field(default=None,
                                                     metadata={
                                                         'name':
                                                         'DatedBlockRef',
                                                         'type': 'Element',
                                                         'namespace': '',
                                                     })
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
        })


@dataclass
class Call:
    """
    :ivar point_in_journey_pattern_ref: If attribute VisitCount is
        omitted then VisitCount = 1 is assumed.
    :ivar departure:
    :ivar arrival:
    """
    point_in_journey_pattern_ref: Optional[PointInJourneyPatternRef] = field(
        default=None,
        metadata={
            'name': 'PointInJourneyPatternRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    departure: Optional['Call.Departure'] = field(default=None,
                                                  metadata={
                                                      'name': 'Departure',
                                                      'type': 'Element',
                                                      'namespace': '',
                                                  })
    arrival: Optional['Call.Arrival'] = field(default=None,
                                              metadata={
                                                  'name': 'Arrival',
                                                  'type': 'Element',
                                                  'namespace': '',
                                              })

    @dataclass
    class Departure:
        earliest_date_time: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                'name': 'EarliestDateTime',
                'type': 'Attribute',
            })

    @dataclass
    class Arrival:
        latest_date_time: Optional[XmlDateTime] = field(default=None,
                                                        metadata={
                                                            'name':
                                                            'LatestDateTime',
                                                            'type':
                                                            'Attribute',
                                                        })


@dataclass
class CallCancellation:
    """
    :ivar vehicle_journey_ref:
    :ivar direction_of_line_ref:
    :ivar line_ref:
    :ivar transport_authority_ref:
    :ivar time_scope:
    :ivar vehicle_operator_ref:
    :ivar dated_vehicle_journey_ref:
    :ivar all_calls_before_point_in_journey_patter_ref: If attribute
        VisitCount is omitted then VisitCount = 1 is assumed.
    :ivar all_calls_after_point_in_journey_pattern_ref: If attribute
        VisitCount is omitted then VisitCount = 1 is assumed.
    :ivar selected_calls:
    :ivar calls_between_points: All Calls between, but not including,
        the from and to points.
    :ivar concerns_arrivals:
    :ivar concerns_departures:
    """
    vehicle_journey_ref: Optional[VehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'VehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
        })
    direction_of_line_ref: Optional[DirectionOfLineRef] = field(
        default=None,
        metadata={
            'name': 'DirectionOfLineRef',
            'type': 'Element',
            'namespace': '',
        })
    line_ref: Optional[LineRef] = field(default=None,
                                        metadata={
                                            'name': 'LineRef',
                                            'type': 'Element',
                                            'namespace': '',
                                        })
    transport_authority_ref: Optional[TransportAuthorityRef] = field(
        default=None,
        metadata={
            'name': 'TransportAuthorityRef',
            'type': 'Element',
            'namespace': '',
        })
    time_scope: Optional[TimeScope] = field(default=None,
                                            metadata={
                                                'name': 'TimeScope',
                                                'type': 'Element',
                                                'namespace': '',
                                            })
    vehicle_operator_ref: Optional[VehicleOperatorOrDepartmentRef] = field(
        default=None,
        metadata={
            'name': 'VehicleOperatorRef',
            'type': 'Element',
            'namespace': '',
        })
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
        })
    all_calls_before_point_in_journey_patter_ref: Optional[
        PointInJourneyPatternRef] = field(
            default=None,
            metadata={
                'name': 'AllCallsBeforePointInJourneyPatterRef',
                'type': 'Element',
                'namespace': '',
            })
    all_calls_after_point_in_journey_pattern_ref: Optional[
        PointInJourneyPatternRef] = field(
            default=None,
            metadata={
                'name': 'AllCallsAfterPointInJourneyPatternRef',
                'type': 'Element',
                'namespace': '',
            })
    selected_calls: Optional['CallCancellation.SelectedCalls'] = field(
        default=None,
        metadata={
            'name': 'SelectedCalls',
            'type': 'Element',
            'namespace': '',
        })
    calls_between_points: Optional[
        'CallCancellation.CallsBetweenPoints'] = field(
            default=None,
            metadata={
                'name': 'CallsBetweenPoints',
                'type': 'Element',
                'namespace': '',
            })
    concerns_arrivals: YesNo = field(default=YesNo.Y,
                                     metadata={
                                         'name': 'ConcernsArrivals',
                                         'type': 'Attribute',
                                     })
    concerns_departures: YesNo = field(default=YesNo.Y,
                                       metadata={
                                           'name': 'ConcernsDepartures',
                                           'type': 'Attribute',
                                       })

    @dataclass
    class SelectedCalls:
        """
        :ivar point_in_journey_pattern_ref: If attribute VisitCount is
            omitted then there will be no filtering based on VisitCount.
            I.e. if this stop is visited several times in the same
            vehicle journey then all those calls are affected.
        """
        point_in_journey_pattern_ref: List[PointInJourneyPatternRef] = field(
            default_factory=list,
            metadata={
                'name': 'PointInJourneyPatternRef',
                'type': 'Element',
                'namespace': '',
                'min_occurs': 1,
            })

    @dataclass
    class CallsBetweenPoints:
        """
        :ivar from_point_in_journey_pattern_ref: If attribute VisitCount
            is omitted then VisitCount = 1 is assumed.
        :ivar to_point_in_journey_pattern_ref: If attribute VisitCount
            is omitted then the highest applicable VisitCount is
            assumed. I.e. the last call at this stop is assumed.
        """
        from_point_in_journey_pattern_ref: Optional[
            PointInJourneyPatternRef] = field(
                default=None,
                metadata={
                    'name': 'FromPointInJourneyPatternRef',
                    'type': 'Element',
                    'namespace': '',
                    'required': True,
                })
        to_point_in_journey_pattern_ref: Optional[
            PointInJourneyPatternRef] = field(default=None,
                                              metadata={
                                                  'name':
                                                  'ToPointInJourneyPatternRef',
                                                  'type': 'Element',
                                                  'namespace': '',
                                                  'required': True,
                                              })


@dataclass
class CancelledConnection:
    feeder_call_ref: Optional[DatedCallRef] = field(default=None,
                                                    metadata={
                                                        'name':
                                                        'FeederCallRef',
                                                        'type': 'Element',
                                                        'namespace': '',
                                                        'required': True,
                                                    })
    fetcher_call_ref: Optional[DatedCallRef] = field(default=None,
                                                     metadata={
                                                         'name':
                                                         'FetcherCallRef',
                                                         'type': 'Element',
                                                         'namespace': '',
                                                         'required': True,
                                                     })


@dataclass
class ChangeOfStopPointStatus:
    """
    :ivar stop_point_ref: Deprecated. Use StopRefs instead.
    :ivar stop_area_ref: Deprecated. Use StopRefs instead.
    :ivar stop_refs:
    :ivar time_scope:
    :ivar status:
    """
    stop_point_ref: Optional[StopPointRef] = field(default=None,
                                                   metadata={
                                                       'name': 'StopPointRef',
                                                       'type': 'Element',
                                                       'namespace': '',
                                                   })
    stop_area_ref: Optional[StopAreaRef] = field(default=None,
                                                 metadata={
                                                     'name': 'StopAreaRef',
                                                     'type': 'Element',
                                                     'namespace': '',
                                                 })
    stop_refs: Optional[StopRefs] = field(default=None,
                                          metadata={
                                              'name': 'StopRefs',
                                              'type': 'Element',
                                              'namespace': '',
                                          })
    time_scope: Optional[StopPointStatusTimeScope] = field(default=None,
                                                           metadata={
                                                               'name':
                                                               'TimeScope',
                                                               'type':
                                                               'Element',
                                                               'namespace': '',
                                                               'required':
                                                               True,
                                                           })
    status: Optional[Status] = field(default=None,
                                     metadata={
                                         'name': 'Status',
                                         'type': 'Attribute',
                                         'required': True,
                                     })


@dataclass
class ExtraConnection:
    feeder_call_ref: Optional[DatedCallRef] = field(default=None,
                                                    metadata={
                                                        'name':
                                                        'FeederCallRef',
                                                        'type': 'Element',
                                                        'namespace': '',
                                                        'required': True,
                                                    })
    fetcher_call_ref: Optional[DatedCallRef] = field(default=None,
                                                     metadata={
                                                         'name':
                                                         'FetcherCallRef',
                                                         'type': 'Element',
                                                         'namespace': '',
                                                         'required': True,
                                                     })
    max_wait_for_feeder_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            'name': 'MaxWaitForFeederDuration',
            'type': 'Attribute',
            'required': True,
        })
    min_change_duration: Optional[XmlDuration] = field(default=None,
                                                       metadata={
                                                           'name':
                                                           'MinChangeDuration',
                                                           'type': 'Attribute',
                                                       })
    is_continuing_vehicle: YesNo = field(default=YesNo.N,
                                         metadata={
                                             'name': 'IsContinuingVehicle',
                                             'type': 'Attribute',
                                         })
    is_exposed_to_staff: YesNo = field(default=YesNo.Y,
                                       metadata={
                                           'name': 'IsExposedToStaff',
                                           'type': 'Attribute',
                                       })
    is_exposed_to_passengers: YesNo = field(default=YesNo.Y,
                                            metadata={
                                                'name':
                                                'IsExposedToPassengers',
                                                'type': 'Attribute',
                                            })


@dataclass
class ModifiedConnection:
    feeder_call_ref: Optional[DatedCallRef] = field(default=None,
                                                    metadata={
                                                        'name':
                                                        'FeederCallRef',
                                                        'type': 'Element',
                                                        'namespace': '',
                                                        'required': True,
                                                    })
    original_fetcher_call_ref: Optional[DatedCallRef] = field(
        default=None,
        metadata={
            'name': 'OriginalFetcherCallRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    new_fetcher_call_ref: Optional[DatedCallRef] = field(
        default=None,
        metadata={
            'name': 'NewFetcherCallRef',
            'type': 'Element',
            'namespace': '',
        })
    wait_for_feeder_until_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'WaitForFeederUntilDateTime',
            'type': 'Attribute',
        })


@dataclass
class ModifiedPointInJourneyPattern:
    """
    :ivar timetabled_point_in_journey_pattern_ref: If attribute
        VisitCount is omitted then there will be no filtering based on
        VisitCount. I.e. if this stop is visited several times in the
        same vehicle journey then all those calls are affected.
    :ivar target_departure_point:
    :ivar target_arrival_point:
    """
    timetabled_point_in_journey_pattern_ref: Optional[
        PointInJourneyPatternRef] = field(
            default=None,
            metadata={
                'name': 'TimetabledPointInJourneyPatternRef',
                'type': 'Element',
                'namespace': '',
                'required': True,
            })
    target_departure_point: Optional[TargetPoint] = field(
        default=None,
        metadata={
            'name': 'TargetDeparturePoint',
            'type': 'Element',
            'namespace': '',
        })
    target_arrival_point: Optional[TargetPoint] = field(
        default=None,
        metadata={
            'name': 'TargetArrivalPoint',
            'type': 'Element',
            'namespace': '',
        })


@dataclass
class RelativeTime:
    from_point_in_journey_pattern_ref: Optional[
        PointInJourneyPatternRef] = field(default=None,
                                          metadata={
                                              'name':
                                              'FromPointInJourneyPatternRef',
                                              'type': 'Element',
                                              'namespace': '',
                                          })
    offset: Optional[XmlDuration] = field(default=None,
                                          metadata={
                                              'name': 'Offset',
                                              'type': 'Attribute',
                                              'required': True,
                                          })
    change_model: ChangeModel = field(default=ChangeModel.MINIMAL,
                                      metadata={
                                          'name': 'ChangeModel',
                                          'type': 'Attribute',
                                      })


@dataclass
class StopPointAllocation:
    """
    :ivar dated_vehicle_journey_ref:
    :ivar timetabled_point_in_journey_pattern_ref: If attribute
        VisitCount is omitted then VisitCount = 1 is assumed.
    :ivar target_point:
    :ivar target_arrival_point:
    :ivar target_departure_point:
    :ivar message_to_driver: Contains additional information to the
        driver that can not be expressed in data.
    """
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    timetabled_point_in_journey_pattern_ref: Optional[
        PointInJourneyPatternRef] = field(
            default=None,
            metadata={
                'name': 'TimetabledPointInJourneyPatternRef',
                'type': 'Element',
                'namespace': '',
                'required': True,
            })
    target_point: Optional[AllocatedStopPoint] = field(default=None,
                                                       metadata={
                                                           'name':
                                                           'TargetPoint',
                                                           'type': 'Element',
                                                           'namespace': '',
                                                       })
    target_arrival_point: Optional[AllocatedStopPoint] = field(
        default=None,
        metadata={
            'name': 'TargetArrivalPoint',
            'type': 'Element',
            'namespace': '',
        })
    target_departure_point: Optional[AllocatedStopPoint] = field(
        default=None,
        metadata={
            'name': 'TargetDeparturePoint',
            'type': 'Element',
            'namespace': '',
        })
    message_to_driver: Optional[str] = field(default=None,
                                             metadata={
                                                 'name': 'MessageToDriver',
                                                 'type': 'Attribute',
                                             })


@dataclass
class TimedCall:
    """
    :ivar point_in_journey_pattern_ref: If attribute VisitCount is
        omitted then VisitCount = 1 is assumed.
    :ivar departure:
    :ivar arrival:
    """
    point_in_journey_pattern_ref: Optional[PointInJourneyPatternRef] = field(
        default=None,
        metadata={
            'name': 'PointInJourneyPatternRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    departure: Optional['TimedCall.Departure'] = field(default=None,
                                                       metadata={
                                                           'name': 'Departure',
                                                           'type': 'Element',
                                                           'namespace': '',
                                                       })
    arrival: Optional['TimedCall.Arrival'] = field(default=None,
                                                   metadata={
                                                       'name': 'Arrival',
                                                       'type': 'Element',
                                                       'namespace': '',
                                                   })

    @dataclass
    class Departure:
        earliest_date_time: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                'name': 'EarliestDateTime',
                'type': 'Attribute',
            })

    @dataclass
    class Arrival:
        latest_date_time: Optional[XmlDateTime] = field(default=None,
                                                        metadata={
                                                            'name':
                                                            'LatestDateTime',
                                                            'type':
                                                            'Attribute',
                                                        })


@dataclass
class ChangedPoints:
    changed_point: List[ModifiedPointInJourneyPattern] = field(
        default_factory=list,
        metadata={
            'name': 'ChangedPoint',
            'type': 'Element',
            'namespace': '',
            'min_occurs': 1,
        })


@dataclass
class JourneyCreation:
    """.

    :ivar start:
    :ivar end: Only required if the created journey ends before the last
        point in the cloned vehicle journey or if the created journey is
        based on a journey pattern.
    :ivar cloned_vehicle_journey_ref:
    :ivar journey_pattern_ref:
    :ivar middle_call:
    :ivar reinforced_vehicle_journey_ref:
    :ivar new_journey_gid:
    :ivar operating_day_date: Defaults to current date
    :ivar inform_passengers_condition:
    """
    start: Optional[JourneyStart] = field(default=None,
                                          metadata={
                                              'name': 'Start',
                                              'type': 'Element',
                                              'namespace': '',
                                              'required': True,
                                          })
    end: Optional[JourneyEnd] = field(default=None,
                                      metadata={
                                          'name': 'End',
                                          'type': 'Element',
                                          'namespace': '',
                                      })
    cloned_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'ClonedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
        })
    journey_pattern_ref: Optional[NamedJourneyPatternRef] = field(
        default=None,
        metadata={
            'name': 'JourneyPatternRef',
            'type': 'Element',
            'namespace': '',
        })
    middle_call: List[Call] = field(default_factory=list,
                                    metadata={
                                        'name': 'MiddleCall',
                                        'type': 'Element',
                                        'namespace': '',
                                    })
    reinforced_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'ReinforcedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
        })
    new_journey_gid: Optional[int] = field(default=None,
                                           metadata={
                                               'name': 'NewJourneyGid',
                                               'type': 'Attribute',
                                               'required': True,
                                               'min_inclusive':
                                               9015000000000000,
                                               'max_inclusive':
                                               9016999999999999,
                                           })
    operating_day_date: Optional[XmlDate] = field(default=None,
                                                  metadata={
                                                      'name':
                                                      'OperatingDayDate',
                                                      'type': 'Attribute',
                                                  })
    inform_passengers_condition: InformPassengersCondition = field(
        default=InformPassengersCondition.ALWAYS,
        metadata={
            'name': 'InformPassengersCondition',
            'type': 'Attribute',
        })


@dataclass
class TimedCalls:
    timed_call: List[TimedCall] = field(default_factory=list,
                                        metadata={
                                            'name': 'TimedCall',
                                            'type': 'Element',
                                            'namespace': '',
                                            'min_occurs': 1,
                                        })


@dataclass
class ChangeOfJourneyTiming:
    """
    :ivar dated_vehicle_journey_ref:
    :ivar relative_time: Changes to subsequent Calls can be applied
        using different change models. MINIMAL, LINEAR, STATISTIC
    :ivar timed_calls:
    """
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    relative_time: Optional[RelativeTime] = field(default=None,
                                                  metadata={
                                                      'name': 'RelativeTime',
                                                      'type': 'Element',
                                                      'namespace': '',
                                                  })
    timed_calls: Optional[TimedCalls] = field(default=None,
                                              metadata={
                                                  'name': 'TimedCalls',
                                                  'type': 'Element',
                                                  'namespace': '',
                                              })


@dataclass
class JourneyPatternModification:
    vehicle_journey_ref: Optional[VehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'VehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
        })
    direction_of_line_ref: Optional[DirectionOfLineRef] = field(
        default=None,
        metadata={
            'name': 'DirectionOfLineRef',
            'type': 'Element',
            'namespace': '',
        })
    line_ref: Optional[LineRef] = field(default=None,
                                        metadata={
                                            'name': 'LineRef',
                                            'type': 'Element',
                                            'namespace': '',
                                        })
    transport_authority_ref: Optional[TransportAuthorityRef] = field(
        default=None,
        metadata={
            'name': 'TransportAuthorityRef',
            'type': 'Element',
            'namespace': '',
        })
    time_scope: Optional[TimeScope] = field(default=None,
                                            metadata={
                                                'name': 'TimeScope',
                                                'type': 'Element',
                                                'namespace': '',
                                            })
    vehicle_operator_ref: Optional[VehicleOperatorOrDepartmentRef] = field(
        default=None,
        metadata={
            'name': 'VehicleOperatorRef',
            'type': 'Element',
            'namespace': '',
        })
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
        })
    changed_points: Optional[ChangedPoints] = field(default=None,
                                                    metadata={
                                                        'name':
                                                        'ChangedPoints',
                                                        'type': 'Element',
                                                        'namespace': '',
                                                        'required': True,
                                                    })


@dataclass
class ControlAction:
    """
    :ivar journey_creation:
    :ivar journey_cancellation:
    :ivar partial_journey_cancellation: This report can be used for
        shortened journeys and when stops are bypassed by certain
        journeys
    :ivar journey_ordering:
    :ivar change_of_journey_pattern: This report can be used  when stops
        are replaced by other stops on certain journeys
    :ivar change_of_journey_progress:
    :ivar change_of_journey_timing:
    :ivar stop_point_allocation:
    :ivar change_of_stop_point_status: This report can be used when a
        stop is closed for all journeys.
    :ivar change_of_bridging_device_status:
    :ivar change_of_station_entrance_point_status:
    :ivar connection_creation:
    :ivar connection_cancellation:
    :ivar connection_modification:
    :ivar vehicle_work_assignment:
    :ivar vehicle_work_deassignment:
    :ivar registration_date_time: This is the offical time used for
        penalty-decisions. It could be the time a fax or phone call
        laying the basis for a control action reached the transport
        authority.
    :ivar source_note: This is a note including a hint of who originally
        supplied a manual report leading to this control action. It
        could include name and organisational unit of the information
        provider.
    """
    journey_creation: Optional[JourneyCreation] = field(default=None,
                                                        metadata={
                                                            'name':
                                                            'JourneyCreation',
                                                            'type': 'Element',
                                                            'namespace': '',
                                                        })
    journey_cancellation: Optional[JourneyCancellation] = field(
        default=None,
        metadata={
            'name': 'JourneyCancellation',
            'type': 'Element',
            'namespace': '',
        })
    partial_journey_cancellation: Optional[CallCancellation] = field(
        default=None,
        metadata={
            'name': 'PartialJourneyCancellation',
            'type': 'Element',
            'namespace': '',
        })
    journey_ordering: Optional[JourneyOrdering] = field(default=None,
                                                        metadata={
                                                            'name':
                                                            'JourneyOrdering',
                                                            'type': 'Element',
                                                            'namespace': '',
                                                        })
    change_of_journey_pattern: Optional[JourneyPatternModification] = field(
        default=None,
        metadata={
            'name': 'ChangeOfJourneyPattern',
            'type': 'Element',
            'namespace': '',
        })
    change_of_journey_progress: Optional[ChangeOfJourneyProgress] = field(
        default=None,
        metadata={
            'name': 'ChangeOfJourneyProgress',
            'type': 'Element',
            'namespace': '',
        })
    change_of_journey_timing: Optional[ChangeOfJourneyTiming] = field(
        default=None,
        metadata={
            'name': 'ChangeOfJourneyTiming',
            'type': 'Element',
            'namespace': '',
        })
    stop_point_allocation: Optional[StopPointAllocation] = field(
        default=None,
        metadata={
            'name': 'StopPointAllocation',
            'type': 'Element',
            'namespace': '',
        })
    change_of_stop_point_status: Optional[ChangeOfStopPointStatus] = field(
        default=None,
        metadata={
            'name': 'ChangeOfStopPointStatus',
            'type': 'Element',
            'namespace': '',
        })
    change_of_bridging_device_status: Optional[
        ChangeOfBridgingDeviceStatus] = field(
            default=None,
            metadata={
                'name': 'ChangeOfBridgingDeviceStatus',
                'type': 'Element',
                'namespace': '',
            })
    change_of_station_entrance_point_status: Optional[
        ChangeOfStationEntrancePointStatus] = field(
            default=None,
            metadata={
                'name': 'ChangeOfStationEntrancePointStatus',
                'type': 'Element',
                'namespace': '',
            })
    connection_creation: Optional[ExtraConnection] = field(
        default=None,
        metadata={
            'name': 'ConnectionCreation',
            'type': 'Element',
            'namespace': '',
        })
    connection_cancellation: Optional[CancelledConnection] = field(
        default=None,
        metadata={
            'name': 'ConnectionCancellation',
            'type': 'Element',
            'namespace': '',
        })
    connection_modification: Optional[ModifiedConnection] = field(
        default=None,
        metadata={
            'name': 'ConnectionModification',
            'type': 'Element',
            'namespace': '',
        })
    vehicle_work_assignment: Optional[VehicleWorkAssignment] = field(
        default=None,
        metadata={
            'name': 'VehicleWorkAssignment',
            'type': 'Element',
            'namespace': '',
        })
    vehicle_work_deassignment: Optional[VehicleWorkDeassignment] = field(
        default=None,
        metadata={
            'name': 'VehicleWorkDeassignment',
            'type': 'Element',
            'namespace': '',
        })
    registration_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'RegistrationDateTime',
            'type': 'Attribute',
        })
    source_note: Optional[str] = field(default=None,
                                       metadata={
                                           'name': 'SourceNote',
                                           'type': 'Attribute',
                                       })
