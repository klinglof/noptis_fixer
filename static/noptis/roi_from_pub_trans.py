from dataclasses import dataclass
from dataclasses import field
from decimal import Decimal
from enum import Enum
from typing import List
from typing import Optional

from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration

from static.noptis.ptshared.pt_shared_types import ArrivalType
from static.noptis.ptshared.pt_shared_types import BlockRef
from static.noptis.ptshared.pt_shared_types import BridgingDeviceRef
from static.noptis.ptshared.pt_shared_types import DepartureType
from static.noptis.ptshared.pt_shared_types import DirectionOfLineRef
from static.noptis.ptshared.pt_shared_types import DutyRef
from static.noptis.ptshared.pt_shared_types import EmployeeRef
from static.noptis.ptshared.pt_shared_types import InformPassengersCondition
from static.noptis.ptshared.pt_shared_types import JourneyPatternPointRef
from static.noptis.ptshared.pt_shared_types import LineRef
from static.noptis.ptshared.pt_shared_types import PlaceRef
from static.noptis.ptshared.pt_shared_types import SecondaryDestinationType
from static.noptis.ptshared.pt_shared_types import StationEntrancePointRef
from static.noptis.ptshared.pt_shared_types import StopAreaRef
from static.noptis.ptshared.pt_shared_types import StopPointRef
from static.noptis.ptshared.pt_shared_types import StopPointType
from static.noptis.ptshared.pt_shared_types import TransportAuthorityRef
from static.noptis.ptshared.pt_shared_types import TransportMode
from static.noptis.ptshared.pt_shared_types import VehicleJourneyRef
from static.noptis.ptshared.pt_shared_types import VehicleRef
from static.noptis.ptshared.pt_shared_types import YesNo
from static.noptis.ptshared.pt_xmlstream import ErrorReport
from static.noptis.ptshared.pt_xmlstream import \
    ErrorResponse as PtErrorResponse
from static.noptis.ptshared.pt_xmlstream import Messages
from static.noptis.ptshared.pt_xmlstream import Report
from static.noptis.ptshared.pt_xmlstream import Response
from static.noptis.ptshared.xmlstream import ErrorMessage
from static.noptis.ptshared.xmlstream import ErrorResponse as ErrorResponse
from static.noptis.ptshared.xmlstream import Idle
from static.noptis.ptshared.xmlstream import LastProcessedMessageRequest
from static.noptis.ptshared.xmlstream import LastProcessedMessageResponse
from static.noptis.roi_shared_types import ArrivalState
from static.noptis.roi_shared_types import AssignmentState
from static.noptis.roi_shared_types import BusSizeType
from static.noptis.roi_shared_types import ConnectionState
from static.noptis.roi_shared_types import ContentType
from static.noptis.roi_shared_types import DepartureState
from static.noptis.roi_shared_types import DeviationReasonCategory
from static.noptis.roi_shared_types import EmissionLevel
from static.noptis.roi_shared_types import FuelType
from static.noptis.roi_shared_types import OperationActionType
from static.noptis.roi_shared_types import PassengerLevel
from static.noptis.roi_shared_types import PredictionState
from static.noptis.roi_shared_types import Status
from static.noptis.roi_shared_types import VehicleJourneyState

__NAMESPACE__ = 'http://www.pubtrans.com/ROI/3.0'


@dataclass
class ArrivalRef:
    """
    :ivar id: This is the Instance Id of the referred Arrival.
    """
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })


@dataclass
class ConnectionRef:
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })


@dataclass
class DatedVehicleJourneyRef:
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })
    operating_day_date: Optional[XmlDate] = field(default=None,
                                                  metadata={
                                                      'name':
                                                      'OperatingDayDate',
                                                      'type': 'Attribute',
                                                      'required': True,
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
class DepartureRef:
    """
    :ivar id: This is the Instance Id of the referred Departure.
    """
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })


@dataclass
class DestinationDisplayRef:
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })


@dataclass
class DeviationCaseRef:
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9076000000000000,
                                   'max_inclusive': 9076999999999999,
                               })


@dataclass
class DeviationMessage:
    public_note: Optional[str] = field(default=None,
                                       metadata={
                                           'name': 'PublicNote',
                                           'type': 'Attribute',
                                           'required': True,
                                           'min_length': 1,
                                           'max_length': 255,
                                       })


@dataclass
class DeviationMessageVersionRef:
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })


class FromDocumentLayoutVersion(Enum):
    """The set of values in the enumeration indicates the range of schema versions
    that this schema version is backward compatible with.

    Used to ensure that the schema version that an incoming document was
    validated against is not in conflict with this schema version.
    """
    VALUE_3_0_8 = '3.0.8'
    VALUE_3_0_9 = '3.0.9'


@dataclass
class Instance:
    """
    :ivar id:
    :ivar timestamp: Time of last modification in PubTrans.
    """
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })
    timestamp: Optional[XmlDateTime] = field(default=None,
                                             metadata={
                                                 'name': 'Timestamp',
                                                 'type': 'Attribute',
                                                 'required': True,
                                             })


@dataclass
class LaxDatedVehicleJourneyRef:
    """
    :ivar id: Omitted only if assigned vehicle journey does not exist in
        production plan.
    :ivar operating_day_date:
    :ivar gid:
    """
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                              })
    operating_day_date: Optional[XmlDate] = field(default=None,
                                                  metadata={
                                                      'name':
                                                      'OperatingDayDate',
                                                      'type': 'Attribute',
                                                      'required': True,
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
class MonitoredVehicleJourneyRef:
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })


@dataclass
class OrganisationalUnitRef:
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })


@dataclass
class OriginalInstance:
    """
    :ivar id:
    :ivar timestamp: Time of last modification in PubTrans.
    :ivar created_timestamp: Time when originally created in PubTrans.
        Only provided if different from Timestamp.
    """
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })
    timestamp: Optional[XmlDateTime] = field(default=None,
                                             metadata={
                                                 'name': 'Timestamp',
                                                 'type': 'Attribute',
                                                 'required': True,
                                             })
    created_timestamp: Optional[XmlDateTime] = field(default=None,
                                                     metadata={
                                                         'name':
                                                         'CreatedTimestamp',
                                                         'type': 'Attribute',
                                                     })


@dataclass
class Priority:
    importance_level: Optional[int] = field(default=None,
                                            metadata={
                                                'name': 'ImportanceLevel',
                                                'type': 'Attribute',
                                                'required': True,
                                                'min_inclusive': 1,
                                                'max_inclusive': 9,
                                            })
    influence_level: Optional[int] = field(default=None,
                                           metadata={
                                               'name': 'InfluenceLevel',
                                               'type': 'Attribute',
                                               'required': True,
                                               'min_inclusive': 1,
                                               'max_inclusive': 9,
                                           })
    urgency_level: Optional[int] = field(default=None,
                                         metadata={
                                             'name': 'UrgencyLevel',
                                             'type': 'Attribute',
                                             'required': True,
                                             'min_inclusive': 1,
                                             'max_inclusive': 9,
                                         })


@dataclass
class PublicationScopeRef:
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })


@dataclass
class ServiceRequirementRef:
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })


@dataclass
class SourceControlAction:
    any_element: Optional[object] = field(default=None,
                                          metadata={
                                              'type': 'Wildcard',
                                              'namespace': '##any',
                                              'process_contents': 'skip',
                                          })


@dataclass
class StopArea:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9021000000000000,
                                   'max_inclusive': 9021999999999999,
                               })
    name: Optional[str] = field(default=None,
                                metadata={
                                    'name': 'Name',
                                    'type': 'Attribute',
                                    'required': True,
                                    'max_length': 50,
                                })
    short_name: Optional[str] = field(default=None,
                                      metadata={
                                          'name': 'ShortName',
                                          'type': 'Attribute',
                                          'max_length': 16,
                                      })


@dataclass
class TargetAudience:
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })
    type_code: Optional[str] = field(default=None,
                                     metadata={
                                         'name': 'TypeCode',
                                         'type': 'Attribute',
                                         'required': True,
                                         'min_length': 1,
                                         'max_length': 8,
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
class TransportAuthority:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9010000000000000,
                                   'max_inclusive': 9010999999999999,
                               })
    code: Optional[str] = field(default=None,
                                metadata={
                                    'name': 'Code',
                                    'type': 'Attribute',
                                    'required': True,
                                    'min_length': 1,
                                    'max_length': 8,
                                })
    name: Optional[str] = field(default=None,
                                metadata={
                                    'name': 'Name',
                                    'type': 'Attribute',
                                    'required': True,
                                    'max_length': 50,
                                })


@dataclass
class VehicleOperator:
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9013000000000000,
                                   'max_inclusive': 9013999999999999,
                               })
    code: Optional[str] = field(default=None,
                                metadata={
                                    'name': 'Code',
                                    'type': 'Attribute',
                                    'required': True,
                                    'min_length': 1,
                                    'max_length': 8,
                                })
    name: Optional[str] = field(default=None,
                                metadata={
                                    'name': 'Name',
                                    'type': 'Attribute',
                                    'required': True,
                                    'max_length': 50,
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
class BlockAssignment(OriginalInstance):
    block_ref: Optional[BlockRef] = field(default=None,
                                          metadata={
                                              'name': 'BlockRef',
                                              'type': 'Element',
                                              'namespace': '',
                                              'required': True,
                                          })
    assigned_vehicle_ref: Optional[VehicleRef] = field(
        default=None,
        metadata={
            'name': 'AssignedVehicleRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    state: Optional[AssignmentState] = field(default=None,
                                             metadata={
                                                 'name': 'State',
                                                 'type': 'Attribute',
                                                 'required': True,
                                             })
    operating_day_date: Optional[XmlDate] = field(default=None,
                                                  metadata={
                                                      'name':
                                                      'OperatingDayDate',
                                                      'type': 'Attribute',
                                                      'required': True,
                                                  })
    valid_from_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'ValidFromDateTime',
            'type': 'Attribute',
            'required': True,
        })
    invalid_from_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'InvalidFromDateTime',
            'type': 'Attribute',
        })


@dataclass
class Connection(OriginalInstance):
    """
    :ivar arrival_ref:
    :ivar departure_ref:
    :ivar wait_for_feeder_until_date_time:
    :ivar state: Expected, waiting, released,  failed, cancelled
    :ivar is_continuing_vehicle:
    :ivar is_exposed_to_staff:
    :ivar is_exposed_to_passengers:
    :ivar min_change_duration:
    :ivar max_replan_duration:
    :ivar alert_control_centre_after_duration:
    """
    arrival_ref: Optional[ArrivalRef] = field(default=None,
                                              metadata={
                                                  'name': 'ArrivalRef',
                                                  'type': 'Element',
                                                  'namespace': '',
                                                  'required': True,
                                              })
    departure_ref: Optional[DepartureRef] = field(default=None,
                                                  metadata={
                                                      'name': 'DepartureRef',
                                                      'type': 'Element',
                                                      'namespace': '',
                                                      'required': True,
                                                  })
    wait_for_feeder_until_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'WaitForFeederUntilDateTime',
            'type': 'Attribute',
            'required': True,
        })
    state: Optional[ConnectionState] = field(default=None,
                                             metadata={
                                                 'name': 'State',
                                                 'type': 'Attribute',
                                                 'required': True,
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
    min_change_duration: Optional[XmlDuration] = field(default=None,
                                                       metadata={
                                                           'name':
                                                           'MinChangeDuration',
                                                           'type': 'Attribute',
                                                       })
    max_replan_duration: Optional[XmlDuration] = field(default=None,
                                                       metadata={
                                                           'name':
                                                           'MaxReplanDuration',
                                                           'type': 'Attribute',
                                                       })
    alert_control_centre_after_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            'name': 'AlertControlCentreAfterDuration',
            'type': 'Attribute',
        })


@dataclass
class DatedVehicleJourneyDeleteEvent(Report):
    """
    This dated vehicle journey instance is invalid and should be removed as well as
    its arrivals and departures.
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
class DeletedConnection(Instance):
    arrival_ref: Optional[ArrivalRef] = field(default=None,
                                              metadata={
                                                  'name': 'ArrivalRef',
                                                  'type': 'Element',
                                                  'namespace': '',
                                                  'required': True,
                                              })
    departure_ref: Optional[DepartureRef] = field(default=None,
                                                  metadata={
                                                      'name': 'DepartureRef',
                                                      'type': 'Element',
                                                      'namespace': '',
                                                      'required': True,
                                                  })


@dataclass
class DestinationDisplay:
    primary_place_ref: Optional[PlaceRef] = field(default=None,
                                                  metadata={
                                                      'name':
                                                      'PrimaryPlaceRef',
                                                      'type': 'Element',
                                                      'namespace': '',
                                                  })
    secondary_place_ref: Optional[PlaceRef] = field(default=None,
                                                    metadata={
                                                        'name':
                                                        'SecondaryPlaceRef',
                                                        'type': 'Element',
                                                        'namespace': '',
                                                    })
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })
    line_designation: Optional[str] = field(default=None,
                                            metadata={
                                                'name': 'LineDesignation',
                                                'type': 'Attribute',
                                                'required': True,
                                                'min_length': 1,
                                                'max_length': 8,
                                            })
    primary_destination_name: Optional[str] = field(
        default=None,
        metadata={
            'name': 'PrimaryDestinationName',
            'type': 'Attribute',
            'required': True,
            'max_length': 50,
        })
    primary_destination_short_name: Optional[str] = field(
        default=None,
        metadata={
            'name': 'PrimaryDestinationShortName',
            'type': 'Attribute',
            'max_length': 16,
        })
    secondary_destination_name: Optional[str] = field(
        default=None,
        metadata={
            'name': 'SecondaryDestinationName',
            'type': 'Attribute',
            'max_length': 50,
        })
    secondary_destination_short_name: Optional[str] = field(
        default=None,
        metadata={
            'name': 'SecondaryDestinationShortName',
            'type': 'Attribute',
            'max_length': 16,
        })
    secondary_destination_type: Optional[SecondaryDestinationType] = field(
        default=None,
        metadata={
            'name': 'SecondaryDestinationType',
            'type': 'Attribute',
        })
    product_name: Optional[str] = field(default=None,
                                        metadata={
                                            'name': 'ProductName',
                                            'type': 'Attribute',
                                            'max_length': 50,
                                        })
    symbol_name: Optional[str] = field(default=None,
                                       metadata={
                                           'name': 'SymbolName',
                                           'type': 'Attribute',
                                           'max_length': 50,
                                       })


@dataclass
class DeviationReason:
    standard_category: Optional[DeviationReasonCategory] = field(
        default=None,
        metadata={
            'name': 'StandardCategory',
            'type': 'Attribute',
            'required': True,
        })
    custom_category: Optional[str] = field(default=None,
                                           metadata={
                                               'name': 'CustomCategory',
                                               'type': 'Attribute',
                                           })


@dataclass
class DriverAssignment(OriginalInstance):
    employee_ref: Optional[EmployeeRef] = field(default=None,
                                                metadata={
                                                    'name': 'EmployeeRef',
                                                    'type': 'Element',
                                                    'namespace': '',
                                                    'required': True,
                                                })
    assigned_vehicle_ref: Optional[VehicleRef] = field(
        default=None,
        metadata={
            'name': 'AssignedVehicleRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    state: Optional[AssignmentState] = field(default=None,
                                             metadata={
                                                 'name': 'State',
                                                 'type': 'Attribute',
                                                 'required': True,
                                             })
    operating_day_date: Optional[XmlDate] = field(default=None,
                                                  metadata={
                                                      'name':
                                                      'OperatingDayDate',
                                                      'type': 'Attribute',
                                                      'required': True,
                                                  })
    valid_from_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'ValidFromDateTime',
            'type': 'Attribute',
            'required': True,
        })
    invalid_from_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'InvalidFromDateTime',
            'type': 'Attribute',
        })


@dataclass
class DutyAssignment(OriginalInstance):
    duty_ref: Optional[DutyRef] = field(default=None,
                                        metadata={
                                            'name': 'DutyRef',
                                            'type': 'Element',
                                            'namespace': '',
                                            'required': True,
                                        })
    assigned_employee_ref: Optional[EmployeeRef] = field(
        default=None,
        metadata={
            'name': 'AssignedEmployeeRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    state: Optional[AssignmentState] = field(default=None,
                                             metadata={
                                                 'name': 'State',
                                                 'type': 'Attribute',
                                                 'required': True,
                                             })
    operating_day_date: Optional[XmlDate] = field(default=None,
                                                  metadata={
                                                      'name':
                                                      'OperatingDayDate',
                                                      'type': 'Attribute',
                                                      'required': True,
                                                  })
    valid_from_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'ValidFromDateTime',
            'type': 'Attribute',
            'required': True,
        })
    invalid_from_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'InvalidFromDateTime',
            'type': 'Attribute',
        })


@dataclass
class Line:
    transport_authority: Optional[TransportAuthority] = field(
        default=None,
        metadata={
            'name': 'TransportAuthority',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9011000000000000,
                                   'max_inclusive': 9011999999999999,
                               })
    designation: Optional[str] = field(default=None,
                                       metadata={
                                           'name': 'Designation',
                                           'type': 'Attribute',
                                           'min_length': 1,
                                           'max_length': 8,
                                       })
    name: Optional[str] = field(default=None,
                                metadata={
                                    'name': 'Name',
                                    'type': 'Attribute',
                                    'max_length': 50,
                                })
    product_code: Optional[str] = field(default=None,
                                        metadata={
                                            'name': 'ProductCode',
                                            'type': 'Attribute',
                                            'min_length': 1,
                                            'max_length': 8,
                                        })
    product_name: Optional[str] = field(default=None,
                                        metadata={
                                            'name': 'ProductName',
                                            'type': 'Attribute',
                                            'max_length': 50,
                                        })


@dataclass
class MessageVariant:
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })
    content: Optional[str] = field(default=None,
                                   metadata={
                                       'name': 'Content',
                                       'type': 'Attribute',
                                       'required': True,
                                   })
    content_type: Optional[ContentType] = field(default=None,
                                                metadata={
                                                    'name': 'ContentType',
                                                    'type': 'Attribute',
                                                    'required': True,
                                                })
    usage_type: Optional[str] = field(default=None,
                                      metadata={
                                          'name': 'UsageType',
                                          'type': 'Attribute',
                                          'required': True,
                                      })
    language: Optional[str] = field(default=None,
                                    metadata={
                                        'name': 'Language',
                                        'type': 'Attribute',
                                    })
    is_public: YesNo = field(default=YesNo.Y,
                             metadata={
                                 'name': 'IsPublic',
                                 'type': 'Attribute',
                             })


@dataclass
class NetworkDeviation(Instance):
    """
    :ivar stop_point_ref:
    :ivar bridging_device_ref:
    :ivar station_entrance_point_ref:
    :ivar deviation_case_ref:
    :ivar deviation_message_version_ref:
    :ivar deviation_message: Expanded data provided for subscriptions
        with option ExpandDeviationMessageData=TRUE.
    :ivar status:
    :ivar valid_from_date_time:
    :ivar invalid_from_date_time:
    """
    stop_point_ref: Optional[StopPointRef] = field(default=None,
                                                   metadata={
                                                       'name': 'StopPointRef',
                                                       'type': 'Element',
                                                       'namespace': '',
                                                   })
    bridging_device_ref: Optional[BridgingDeviceRef] = field(
        default=None,
        metadata={
            'name': 'BridgingDeviceRef',
            'type': 'Element',
            'namespace': '',
        })
    station_entrance_point_ref: Optional[StationEntrancePointRef] = field(
        default=None,
        metadata={
            'name': 'StationEntrancePointRef',
            'type': 'Element',
            'namespace': '',
        })
    deviation_case_ref: Optional[DeviationCaseRef] = field(
        default=None,
        metadata={
            'name': 'DeviationCaseRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    deviation_message_version_ref: Optional[
        DeviationMessageVersionRef] = field(default=None,
                                            metadata={
                                                'name':
                                                'DeviationMessageVersionRef',
                                                'type': 'Element',
                                                'namespace': '',
                                            })
    deviation_message: Optional[DeviationMessage] = field(
        default=None,
        metadata={
            'name': 'DeviationMessage',
            'type': 'Element',
            'namespace': '',
        })
    status: Optional[Status] = field(default=None,
                                     metadata={
                                         'name': 'Status',
                                         'type': 'Attribute',
                                         'required': True,
                                     })
    valid_from_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'ValidFromDateTime',
            'type': 'Attribute',
            'required': True,
        })
    invalid_from_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'InvalidFromDateTime',
            'type': 'Attribute',
        })


@dataclass
class ScopeElement:
    journey_transport_authority_ref: Optional[TransportAuthorityRef] = field(
        default=None,
        metadata={
            'name': 'JourneyTransportAuthorityRef',
            'type': 'Element',
            'namespace': '',
        })
    line_ref: Optional[LineRef] = field(default=None,
                                        metadata={
                                            'name': 'LineRef',
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
    vehicle_journey_ref: Optional[VehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'VehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
        })
    stop_transport_authority_ref: Optional[TransportAuthorityRef] = field(
        default=None,
        metadata={
            'name': 'StopTransportAuthorityRef',
            'type': 'Element',
            'namespace': '',
        })
    stop_area_ref: Optional[StopAreaRef] = field(default=None,
                                                 metadata={
                                                     'name': 'StopAreaRef',
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
    time_scope: Optional[TimeScope] = field(default=None,
                                            metadata={
                                                'name': 'TimeScope',
                                                'type': 'Element',
                                                'namespace': '',
                                                'required': True,
                                            })
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })
    visit_count_number: int = field(default=1,
                                    metadata={
                                        'name': 'VisitCountNumber',
                                        'type': 'Attribute',
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
class ServiceRequirement:
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })
    transport_mode: Optional[TransportMode] = field(default=None,
                                                    metadata={
                                                        'name':
                                                        'TransportMode',
                                                        'type': 'Attribute',
                                                        'required': True,
                                                    })
    capacity_seatings: Optional[int] = field(default=None,
                                             metadata={
                                                 'name': 'CapacitySeatings',
                                                 'type': 'Attribute',
                                             })
    capacity_total: Optional[int] = field(default=None,
                                          metadata={
                                              'name': 'CapacityTotal',
                                              'type': 'Attribute',
                                          })
    capacity_prams: Optional[int] = field(default=None,
                                          metadata={
                                              'name': 'CapacityPrams',
                                              'type': 'Attribute',
                                          })
    capacity_wheelchairs: Optional[int] = field(default=None,
                                                metadata={
                                                    'name':
                                                    'CapacityWheelchairs',
                                                    'type': 'Attribute',
                                                })
    bus_size_type: Optional[BusSizeType] = field(default=None,
                                                 metadata={
                                                     'name': 'BusSizeType',
                                                     'type': 'Attribute',
                                                 })
    train_size_cars: Optional[int] = field(default=None,
                                           metadata={
                                               'name': 'TrainSizeCars',
                                               'type': 'Attribute',
                                           })
    train_size_short: Optional[YesNo] = field(default=None,
                                              metadata={
                                                  'name': 'TrainSizeShort',
                                                  'type': 'Attribute',
                                              })
    required_emission_level: Optional[EmissionLevel] = field(
        default=None,
        metadata={
            'name': 'RequiredEmissionLevel',
            'type': 'Attribute',
        })
    required_fuel_type: Optional[FuelType] = field(default=None,
                                                   metadata={
                                                       'name':
                                                       'RequiredFuelType',
                                                       'type': 'Attribute',
                                                   })
    accessibility_low_entrance: Optional[YesNo] = field(
        default=None,
        metadata={
            'name': 'AccessibilityLowEntrance',
            'type': 'Attribute',
        })
    accessibility_lift_or_ramp: Optional[YesNo] = field(
        default=None,
        metadata={
            'name': 'AccessibilityLiftOrRamp',
            'type': 'Attribute',
        })
    accessibility_low_floor: Optional[YesNo] = field(
        default=None,
        metadata={
            'name': 'AccessibilityLowFloor',
            'type': 'Attribute',
        })


@dataclass
class StopPoint:
    stop_area: Optional[StopArea] = field(default=None,
                                          metadata={
                                              'name': 'StopArea',
                                              'type': 'Element',
                                              'namespace': '',
                                              'required': True,
                                          })
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9022000000000000,
                                   'max_inclusive': 9022999999999999,
                               })
    name: Optional[str] = field(default=None,
                                metadata={
                                    'name': 'Name',
                                    'type': 'Attribute',
                                    'required': True,
                                    'max_length': 50,
                                })
    short_name: Optional[str] = field(default=None,
                                      metadata={
                                          'name': 'ShortName',
                                          'type': 'Attribute',
                                          'max_length': 16,
                                      })
    designation: Optional[str] = field(default=None,
                                       metadata={
                                           'name': 'Designation',
                                           'type': 'Attribute',
                                           'min_length': 1,
                                           'max_length': 4,
                                       })
    type_value: Optional[StopPointType] = field(default=None,
                                                metadata={
                                                    'name': 'Type',
                                                    'type': 'Attribute',
                                                    'required': True,
                                                })


@dataclass
class StopScope:
    stop_transport_authority_ref: Optional[TransportAuthorityRef] = field(
        default=None,
        metadata={
            'name': 'StopTransportAuthorityRef',
            'type': 'Element',
            'namespace': '',
        })
    stop_area_ref: Optional[StopAreaRef] = field(default=None,
                                                 metadata={
                                                     'name': 'StopAreaRef',
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
class SubscriptionErrorReport(ErrorReport):
    """
    :ivar subscription_id: If omitted, then this concerns all the client
        Peers subscriptions.
    """
    subscription_id: Optional[int] = field(default=None,
                                           metadata={
                                               'name': 'SubscriptionId',
                                               'type': 'Attribute',
                                           })


@dataclass
class SubscriptionErrorResponse(PtErrorResponse):
    """Sent if data of interest for a subscription has been purged from the
    production plan before it could be transfered.

    This could be the case if the connection to a subscriber is broken
    for several days. It could also be sent if the subscriber has
    requested a start time so far back in time that data is already
    purged. It could also be sent if the subscriber requests a start
    time earlier than the start time in a previous request for the same
    subscription.

    :ivar subscription_id: If omitted, then this concerns all the client
        Peers subscriptions.
    """
    subscription_id: Optional[int] = field(default=None,
                                           metadata={
                                               'name': 'SubscriptionId',
                                               'type': 'Attribute',
                                           })


@dataclass
class SubscriptionResponse(Response):
    subscription_id: Optional[int] = field(default=None,
                                           metadata={
                                               'name': 'SubscriptionId',
                                               'type': 'Attribute',
                                               'required': True,
                                           })


@dataclass
class SubscriptionResumeResponse(Response):
    """
    :ivar subscription_id: If the resume request did not pinpoint a
        specific subscription, then all current subscriptions held by
        the requesting Peer will be resumed and this attribute omitted
        in the response.
    """
    subscription_id: Optional[int] = field(default=None,
                                           metadata={
                                               'name': 'SubscriptionId',
                                               'type': 'Attribute',
                                           })


@dataclass
class SubscriptionTerminationResponse(Response):
    """
    :ivar subscription_id: If the termination request did not pinpoint a
        specific subscription, then all current subscriptions held by
        the requesting Peer will be terminated and this attribute
        omitted in the response.
    """
    subscription_id: Optional[int] = field(default=None,
                                           metadata={
                                               'name': 'SubscriptionId',
                                               'type': 'Attribute',
                                           })


@dataclass
class SynchronisationReport(Report):
    on_subscription_id: Optional[int] = field(default=None,
                                              metadata={
                                                  'name': 'OnSubscriptionId',
                                                  'type': 'Attribute',
                                                  'required': True,
                                              })
    synchronised_upto_utc_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'SynchronisedUptoUtcDateTime',
            'type': 'Attribute',
            'required': True,
        })
    has_completed_recovery_phase: Optional[YesNo] = field(
        default=None,
        metadata={
            'name': 'HasCompletedRecoveryPhase',
            'type': 'Attribute',
            'required': True,
        })


@dataclass
class TargetAudiences:
    target_audience: List[TargetAudience] = field(default_factory=list,
                                                  metadata={
                                                      'name': 'TargetAudience',
                                                      'type': 'Element',
                                                      'namespace': '',
                                                      'min_occurs': 1,
                                                  })


@dataclass
class UpdatedConnection(Instance):
    """
    :ivar arrival_ref:
    :ivar departure_ref:
    :ivar wait_for_feeder_until_date_time: Only provided if changed.
    :ivar state: Expected, waiting, released, failed, cancelled
    """
    arrival_ref: Optional[ArrivalRef] = field(default=None,
                                              metadata={
                                                  'name': 'ArrivalRef',
                                                  'type': 'Element',
                                                  'namespace': '',
                                                  'required': True,
                                              })
    departure_ref: Optional[DepartureRef] = field(default=None,
                                                  metadata={
                                                      'name': 'DepartureRef',
                                                      'type': 'Element',
                                                      'namespace': '',
                                                      'required': True,
                                                  })
    wait_for_feeder_until_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'WaitForFeederUntilDateTime',
            'type': 'Attribute',
        })
    state: Optional[ConnectionState] = field(default=None,
                                             metadata={
                                                 'name': 'State',
                                                 'type': 'Attribute',
                                                 'required': True,
                                             })


@dataclass
class UpdatedDatedVehicleJourney(Instance):
    """
    :ivar state: A dated vehicle journey can be expected, not expected
        or cancelled.
    :ivar origin_name:
    :ivar origin_short_name:
    """
    state: Optional[VehicleJourneyState] = field(default=None,
                                                 metadata={
                                                     'name': 'State',
                                                     'type': 'Attribute',
                                                     'required': True,
                                                 })
    origin_name: Optional[str] = field(default=None,
                                       metadata={
                                           'name': 'OriginName',
                                           'type': 'Attribute',
                                           'max_length': 50,
                                       })
    origin_short_name: Optional[str] = field(default=None,
                                             metadata={
                                                 'name': 'OriginShortName',
                                                 'type': 'Attribute',
                                                 'max_length': 16,
                                             })


@dataclass
class User:
    organisational_unit_ref: Optional[OrganisationalUnitRef] = field(
        default=None,
        metadata={
            'name': 'OrganisationalUnitRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    name: Optional[str] = field(default=None,
                                metadata={
                                    'name': 'Name',
                                    'type': 'Attribute',
                                    'max_length': 50,
                                })
    organisational_unit_code: Optional[object] = field(
        default=None,
        metadata={
            'name': 'OrganisationalUnitCode',
            'type': 'Attribute',
            'required': True,
        })
    organisation_code: Optional[object] = field(default=None,
                                                metadata={
                                                    'name': 'OrganisationCode',
                                                    'type': 'Attribute',
                                                    'required': True,
                                                })


@dataclass
class Vehicle:
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })
    classified_as_transport_mode: Optional[TransportMode] = field(
        default=None,
        metadata={
            'name': 'ClassifiedAsTransportMode',
            'type': 'Attribute',
            'required': True,
        })
    capacity_standings: Optional[int] = field(default=None,
                                              metadata={
                                                  'name': 'CapacityStandings',
                                                  'type': 'Attribute',
                                              })
    capacity_seatings: Optional[int] = field(default=None,
                                             metadata={
                                                 'name': 'CapacitySeatings',
                                                 'type': 'Attribute',
                                             })
    capacity_prams: Optional[int] = field(default=None,
                                          metadata={
                                              'name': 'CapacityPrams',
                                              'type': 'Attribute',
                                          })
    capacity_wheelchairs: Optional[int] = field(default=None,
                                                metadata={
                                                    'name':
                                                    'CapacityWheelchairs',
                                                    'type': 'Attribute',
                                                })
    accessibility_low_entrance: Optional[YesNo] = field(
        default=None,
        metadata={
            'name': 'AccessibilityLowEntrance',
            'type': 'Attribute',
        })
    accessibility_lift: Optional[YesNo] = field(default=None,
                                                metadata={
                                                    'name':
                                                    'AccessibilityLift',
                                                    'type': 'Attribute',
                                                })
    accessibility_ramp: Optional[YesNo] = field(default=None,
                                                metadata={
                                                    'name':
                                                    'AccessibilityRamp',
                                                    'type': 'Attribute',
                                                })
    accessibility_low_floor: Optional[YesNo] = field(
        default=None,
        metadata={
            'name': 'AccessibilityLowFloor',
            'type': 'Attribute',
        })
    size_length_meters: Optional[Decimal] = field(default=None,
                                                  metadata={
                                                      'name':
                                                      'SizeLengthMeters',
                                                      'type':
                                                      'Attribute',
                                                      'min_inclusive':
                                                      Decimal('0.00'),
                                                      'total_digits':
                                                      12,
                                                      'fraction_digits':
                                                      2,
                                                  })


@dataclass
class VehicleJourneyAssignment(OriginalInstance):
    dated_vehicle_journey_ref: Optional[LaxDatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    assigned_vehicle_ref: Optional[VehicleRef] = field(
        default=None,
        metadata={
            'name': 'AssignedVehicleRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    state: Optional[AssignmentState] = field(default=None,
                                             metadata={
                                                 'name': 'State',
                                                 'type': 'Attribute',
                                                 'required': True,
                                             })
    train_size_car_count: Optional[int] = field(default=None,
                                                metadata={
                                                    'name':
                                                    'TrainSizeCarCount',
                                                    'type': 'Attribute',
                                                })
    valid_from_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'ValidFromDateTime',
            'type': 'Attribute',
            'required': True,
        })
    invalid_from_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'InvalidFromDateTime',
            'type': 'Attribute',
        })


@dataclass
class VehicleJourneyDeviation(Instance):
    """
    :ivar dated_vehicle_journey_ref:
    :ivar deviation_case_ref:
    :ivar deviation_message_version_ref:
    :ivar deviation_message: Expanded data provided for subscriptions
        with option ExpandDeviationMessageData=TRUE.
    :ivar consequence:
    :ivar is_valid: IsValid=N means that this Vehicle Journey Deviation
        is not valid anymore and should be removed.
    """
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    deviation_case_ref: Optional[DeviationCaseRef] = field(
        default=None,
        metadata={
            'name': 'DeviationCaseRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    deviation_message_version_ref: Optional[
        DeviationMessageVersionRef] = field(default=None,
                                            metadata={
                                                'name':
                                                'DeviationMessageVersionRef',
                                                'type': 'Element',
                                                'namespace': '',
                                            })
    deviation_message: Optional[DeviationMessage] = field(
        default=None,
        metadata={
            'name': 'DeviationMessage',
            'type': 'Element',
            'namespace': '',
        })
    consequence: Optional[str] = field(default=None,
                                       metadata={
                                           'name': 'Consequence',
                                           'type': 'Attribute',
                                           'required': True,
                                           'max_length': 16,
                                       })
    is_valid: YesNo = field(default=YesNo.Y,
                            metadata={
                                'name': 'IsValid',
                                'type': 'Attribute',
                            })


@dataclass
class Arrival(Instance):
    """
    :ivar dated_vehicle_journey_ref:
    :ivar direction_of_line_ref: Provided for Service Journeys.
    :ivar monitored_vehicle_journey_ref: Provided if the vehicle journey
        is already, or has been, in progress when this event is
        transferred.
    :ivar target_journey_pattern_point_ref:
    :ivar target_stop_point: Expanded data provided for subscriptions
        with option ExpandStopData=TRUE if the journey pattern point is
        a stop point. Alternatively, stop point information can be
        obtained by joining view StopPoint and JourneyPatternPoint in
        DOI.
    :ivar timetabled_journey_pattern_point_ref: If this element is
        omitted then the timetabled journey pattern point is the same as
        the target journey pattern point. If there has been a change of
        stop point, this element will be provided as a reference to the
        original stop point.
    :ivar timetabled_stop_point: Expanded data provided for
        subscriptions with option ExpandStopData=TRUE if the timetabled
        journey pattern point is different from the target journey
        pattern point and it is a stop point. Alternatively, stop point
        information can be obtained by joining view StopPoint and
        JourneyPatternPoint in DOI.
    :ivar observed_journey_pattern_point_ref: The observed stop point.
    :ivar observed_stop_point: Expanded data provided for subscriptions
        with option ExpandStopData=TRUE if the journey pattern point is
        a stop point. Alternatively, stop point information can be
        obtained by joining view StopPoint and JourneyPatternPoint in
        DOI.
    :ivar timetabled_latest_date_time:
    :ivar target_date_time:
    :ivar estimated_date_time:
    :ivar observed_date_time:
    :ivar state:
    :ivar type_value:
    :ivar journey_pattern_sequence_number:
    :ivar visit_count_number: Normally a journey pattern point is
        visited only once during a vehicle journey. However, some
        vehicle journeys have such journey patterns that the same
        journey pattern point is visited again. In such instances more
        information must be provided to distinguish between the first
        and consecutive visits. VisitCount =  2 means that it is the
        second time a journey pattern point is visited according to the
        journey pattern.
    """
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    direction_of_line_ref: Optional[DirectionOfLineRef] = field(
        default=None,
        metadata={
            'name': 'DirectionOfLineRef',
            'type': 'Element',
            'namespace': '',
        })
    monitored_vehicle_journey_ref: Optional[
        MonitoredVehicleJourneyRef] = field(default=None,
                                            metadata={
                                                'name':
                                                'MonitoredVehicleJourneyRef',
                                                'type': 'Element',
                                                'namespace': '',
                                            })
    target_journey_pattern_point_ref: Optional[JourneyPatternPointRef] = field(
        default=None,
        metadata={
            'name': 'TargetJourneyPatternPointRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    target_stop_point: Optional[StopPoint] = field(default=None,
                                                   metadata={
                                                       'name':
                                                       'TargetStopPoint',
                                                       'type': 'Element',
                                                       'namespace': '',
                                                   })
    timetabled_journey_pattern_point_ref: Optional[
        JourneyPatternPointRef] = field(default=None,
                                        metadata={
                                            'name':
                                            'TimetabledJourneyPatternPointRef',
                                            'type': 'Element',
                                            'namespace': '',
                                        })
    timetabled_stop_point: Optional[StopPoint] = field(
        default=None,
        metadata={
            'name': 'TimetabledStopPoint',
            'type': 'Element',
            'namespace': '',
        })
    observed_journey_pattern_point_ref: Optional[
        JourneyPatternPointRef] = field(default=None,
                                        metadata={
                                            'name':
                                            'ObservedJourneyPatternPointRef',
                                            'type': 'Element',
                                            'namespace': '',
                                        })
    observed_stop_point: Optional[StopPoint] = field(default=None,
                                                     metadata={
                                                         'name':
                                                         'ObservedStopPoint',
                                                         'type': 'Element',
                                                         'namespace': '',
                                                     })
    timetabled_latest_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'TimetabledLatestDateTime',
            'type': 'Attribute',
            'required': True,
        })
    target_date_time: Optional[XmlDateTime] = field(default=None,
                                                    metadata={
                                                        'name':
                                                        'TargetDateTime',
                                                        'type': 'Attribute',
                                                        'required': True,
                                                    })
    estimated_date_time: Optional[XmlDateTime] = field(default=None,
                                                       metadata={
                                                           'name':
                                                           'EstimatedDateTime',
                                                           'type': 'Attribute',
                                                       })
    observed_date_time: Optional[XmlDateTime] = field(default=None,
                                                      metadata={
                                                          'name':
                                                          'ObservedDateTime',
                                                          'type': 'Attribute',
                                                      })
    state: Optional[ArrivalState] = field(default=None,
                                          metadata={
                                              'name': 'State',
                                              'type': 'Attribute',
                                              'required': True,
                                          })
    type_value: ArrivalType = field(default=ArrivalType.STOP_IF_ALIGHTING,
                                    metadata={
                                        'name': 'Type',
                                        'type': 'Attribute',
                                    })
    journey_pattern_sequence_number: Optional[int] = field(
        default=None,
        metadata={
            'name': 'JourneyPatternSequenceNumber',
            'type': 'Attribute',
            'required': True,
            'max_inclusive': 10000,
        })
    visit_count_number: int = field(default=1,
                                    metadata={
                                        'name': 'VisitCountNumber',
                                        'type': 'Attribute',
                                    })


@dataclass
class AssignmentEvent(Report):
    block_assignment: Optional[BlockAssignment] = field(default=None,
                                                        metadata={
                                                            'name':
                                                            'BlockAssignment',
                                                            'type': 'Element',
                                                            'namespace': '',
                                                        })
    vehicle_journey_assignment: Optional[VehicleJourneyAssignment] = field(
        default=None,
        metadata={
            'name': 'VehicleJourneyAssignment',
            'type': 'Element',
            'namespace': '',
        })
    duty_assignment: Optional[DutyAssignment] = field(default=None,
                                                      metadata={
                                                          'name':
                                                          'DutyAssignment',
                                                          'type': 'Element',
                                                          'namespace': '',
                                                      })
    driver_assignment: Optional[DriverAssignment] = field(
        default=None,
        metadata={
            'name': 'DriverAssignment',
            'type': 'Element',
            'namespace': '',
        })


@dataclass
class CallRef:
    """
    :ivar dated_vehicle_journey_ref:
    :ivar journey_pattern_point_ref:
    :ivar stop_point: Expanded data provided for subscriptions with
        option ExpandStopData=TRUE if the journey pattern point is a
        stop point. Alternatively, stop point information can be
        obtained by joining view StopPoint and JourneyPatternPoint in
        DOI.
    :ivar journey_pattern_sequence_number:
    """
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    journey_pattern_point_ref: Optional[JourneyPatternPointRef] = field(
        default=None,
        metadata={
            'name': 'JourneyPatternPointRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    stop_point: Optional[StopPoint] = field(default=None,
                                            metadata={
                                                'name': 'StopPoint',
                                                'type': 'Element',
                                                'namespace': '',
                                            })
    journey_pattern_sequence_number: Optional[int] = field(
        default=None,
        metadata={
            'name': 'JourneyPatternSequenceNumber',
            'type': 'Attribute',
            'required': True,
            'max_inclusive': 10000,
        })


@dataclass
class ConnectionCreateEvent(Report):
    connection: Optional[Connection] = field(default=None,
                                             metadata={
                                                 'name': 'Connection',
                                                 'type': 'Element',
                                                 'namespace': '',
                                                 'required': True,
                                             })


@dataclass
class ConnectionDeleteEvent(Report):
    """
    This connection instance is invalid and should be removed.
    """
    connection: Optional[DeletedConnection] = field(default=None,
                                                    metadata={
                                                        'name': 'Connection',
                                                        'type': 'Element',
                                                        'namespace': '',
                                                        'required': True,
                                                    })


@dataclass
class ConnectionUpdateEvent(Report):
    connection: Optional[UpdatedConnection] = field(default=None,
                                                    metadata={
                                                        'name': 'Connection',
                                                        'type': 'Element',
                                                        'namespace': '',
                                                        'required': True,
                                                    })


@dataclass
class DatedVehicleJourney(OriginalInstance):
    """
    :ivar direction_of_line_ref:
    :ivar line: Expanded data provided for subscriptions with option
        ExpandLineData=TRUE if the dated vehicle journey is a service
        journey. Alternatively, line information can be obtained by
        joining view DirectionOfLine and Line in DOI.
    :ivar vehicle_operator_ref:
    :ivar vehicle_operator: Expanded data provided for subscriptions
        with option ExpandVehicleOperatorData=TRUE. Alternatively,
        vehicle operator information can be obtained by joining view
        Organisation and Contractor in DOI.
    :ivar operating_day_date:
    :ivar gid:
    :ivar timetabled_start_date_time:
    :ivar timetabled_end_date_time:
    :ivar state: A dated vehicle journey can be expected, not expected
        or cancelled.
    :ivar planned_type_code:
    :ivar origin_name: This attribute is omitted only for dead runs.
    :ivar origin_short_name:
    :ivar inform_passengers_condition:
    :ivar is_expected_to_be_monitored:
    :ivar uses_named_journey_pattern_id: This attribute is provided for
        extra dated vehicle journeys.
    :ivar reinforced_dated_vehicle_journey_id: This attribute is
        provided for extra dated vehicle journeys that are reinforcing
        or replacing a specifed dated vehicle journey.
    :ivar reinforced_vehicle_journey_gid: This attribute is provided for
        extra dated vehicle journeys that are reinforcing or replacing a
        specifed dated vehicle journey.
    """
    direction_of_line_ref: Optional[DirectionOfLineRef] = field(
        default=None,
        metadata={
            'name': 'DirectionOfLineRef',
            'type': 'Element',
            'namespace': '',
        })
    line: Optional[Line] = field(default=None,
                                 metadata={
                                     'name': 'Line',
                                     'type': 'Element',
                                     'namespace': '',
                                 })
    vehicle_operator_ref: Optional[VehicleOperatorRef] = field(
        default=None,
        metadata={
            'name': 'VehicleOperatorRef',
            'type': 'Element',
            'namespace': '',
        })
    vehicle_operator: Optional[VehicleOperator] = field(default=None,
                                                        metadata={
                                                            'name':
                                                            'VehicleOperator',
                                                            'type': 'Element',
                                                            'namespace': '',
                                                        })
    operating_day_date: Optional[XmlDate] = field(default=None,
                                                  metadata={
                                                      'name':
                                                      'OperatingDayDate',
                                                      'type': 'Attribute',
                                                      'required': True,
                                                  })
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9015000000000000,
                                   'max_inclusive': 9016999999999999,
                               })
    timetabled_start_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'TimetabledStartDateTime',
            'type': 'Attribute',
            'required': True,
        })
    timetabled_end_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'TimetabledEndDateTime',
            'type': 'Attribute',
            'required': True,
        })
    state: Optional[VehicleJourneyState] = field(default=None,
                                                 metadata={
                                                     'name': 'State',
                                                     'type': 'Attribute',
                                                     'required': True,
                                                 })
    planned_type_code: str = field(default='NORMAL',
                                   metadata={
                                       'name': 'PlannedTypeCode',
                                       'type': 'Attribute',
                                       'min_length': 1,
                                       'max_length': 8,
                                   })
    origin_name: Optional[str] = field(default=None,
                                       metadata={
                                           'name': 'OriginName',
                                           'type': 'Attribute',
                                           'max_length': 50,
                                       })
    origin_short_name: Optional[str] = field(default=None,
                                             metadata={
                                                 'name': 'OriginShortName',
                                                 'type': 'Attribute',
                                                 'max_length': 16,
                                             })
    inform_passengers_condition: Optional[InformPassengersCondition] = field(
        default=None,
        metadata={
            'name': 'InformPassengersCondition',
            'type': 'Attribute',
        })
    is_expected_to_be_monitored: YesNo = field(default=YesNo.N,
                                               metadata={
                                                   'name':
                                                   'IsExpectedToBeMonitored',
                                                   'type': 'Attribute',
                                               })
    uses_named_journey_pattern_id: Optional[int] = field(
        default=None,
        metadata={
            'name': 'UsesNamedJourneyPatternId',
            'type': 'Attribute',
        })
    reinforced_dated_vehicle_journey_id: Optional[int] = field(
        default=None,
        metadata={
            'name': 'ReinforcedDatedVehicleJourneyId',
            'type': 'Attribute',
        })
    reinforced_vehicle_journey_gid: Optional[int] = field(
        default=None,
        metadata={
            'name': 'ReinforcedVehicleJourneyGid',
            'type': 'Attribute',
            'min_inclusive': 9015000000000000,
            'max_inclusive': 9016999999999999,
        })


@dataclass
class Departure(Instance):
    """
    :ivar dated_vehicle_journey_ref:
    :ivar direction_of_line_ref: Provided for Service Journeys.
    :ivar monitored_vehicle_journey_ref: Provided if the vehicle journey
        is already, or has been, in progress when this event is
        transferred.
    :ivar target_journey_pattern_point_ref:
    :ivar target_stop_point: Expanded data provided for subscriptions
        with option ExpandStopData=TRUE if the journey pattern point is
        a stop point. Alternatively, stop point information can be
        obtained by joining view StopPoint and JourneyPatternPoint in
        DOI.
    :ivar timetabled_journey_pattern_point_ref: If this element is
        omitted then the timetabled journey pattern point is the same as
        the target journey pattern point. If there has been a change of
        stop point, this element will be provided as a reference to the
        original stop point.
    :ivar timetabled_stop_point: Expanded data provided for
        subscriptions with option ExpandStopData=TRUE if the timetabled
        journey pattern point is different from the target journey
        pattern point and it is a stop point. Alternatively, stop point
        information can be obtained by joining view StopPoint and
        JourneyPatternPoint in DOI.
    :ivar destination_display_ref: Reference to row in view
        DestinationDisplay of DOI
    :ivar destination_display: Expanded data provided for subscriptions
        with option ExpandDestinationData=TRUE. Alternatively available
        by joining with view DestinationDisplay in DOI.
    :ivar destination_stop_area_ref: Reference to the end stop area of
        the vehicle journey.
    :ivar stop_area: Expanded data provided for subscriptions with
        option ExpandStopData=TRUE Alternatively, stop area information
        can be obtained from DOI.
    :ivar service_requirement_ref: Omitted only for extra dated vehicle
        journeys where the service requirements are unknown.
    :ivar service_requirement: Expanded data provided for subscriptions
        with option ExpandServiceRequirementData=TRUE. Alternatively
        available by joining with view ServiceRequirement in DOI.
    :ivar observed_journey_pattern_point_ref: The observed stop point.
    :ivar observed_stop_point: Expanded data provided for subscriptions
        with option ExpandStopData=TRUE if the journey pattern point is
        a stop point. Alternatively, stop point information can be
        obtained by joining view StopPoint and JourneyPatternPoint in
        DOI.
    :ivar timetabled_earliest_date_time:
    :ivar target_date_time:
    :ivar estimated_date_time:
    :ivar observed_date_time:
    :ivar state:
    :ivar type_value:
    :ivar journey_pattern_sequence_number:
    :ivar visit_count_number: Normally each stop is called only once on
        a Journey. However, some Journeys have such JourneyPatterns that
        the same stop is called again. In such instances more
        information must be provided so that the central system can
        distinguish between the first call and consecutive calls. A call
        refering to the first time a stop is called occurs in the
        JourneyPattern has VisitCount =  1. The next time the same stop
        is called  the value 2 should be used.
    """
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    direction_of_line_ref: Optional[DirectionOfLineRef] = field(
        default=None,
        metadata={
            'name': 'DirectionOfLineRef',
            'type': 'Element',
            'namespace': '',
        })
    monitored_vehicle_journey_ref: Optional[
        MonitoredVehicleJourneyRef] = field(default=None,
                                            metadata={
                                                'name':
                                                'MonitoredVehicleJourneyRef',
                                                'type': 'Element',
                                                'namespace': '',
                                            })
    target_journey_pattern_point_ref: Optional[JourneyPatternPointRef] = field(
        default=None,
        metadata={
            'name': 'TargetJourneyPatternPointRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    target_stop_point: Optional[StopPoint] = field(default=None,
                                                   metadata={
                                                       'name':
                                                       'TargetStopPoint',
                                                       'type': 'Element',
                                                       'namespace': '',
                                                   })
    timetabled_journey_pattern_point_ref: Optional[
        JourneyPatternPointRef] = field(default=None,
                                        metadata={
                                            'name':
                                            'TimetabledJourneyPatternPointRef',
                                            'type': 'Element',
                                            'namespace': '',
                                        })
    timetabled_stop_point: Optional[StopPoint] = field(
        default=None,
        metadata={
            'name': 'TimetabledStopPoint',
            'type': 'Element',
            'namespace': '',
        })
    destination_display_ref: Optional[DestinationDisplayRef] = field(
        default=None,
        metadata={
            'name': 'DestinationDisplayRef',
            'type': 'Element',
            'namespace': '',
        })
    destination_display: Optional[DestinationDisplay] = field(
        default=None,
        metadata={
            'name': 'DestinationDisplay',
            'type': 'Element',
            'namespace': '',
        })
    destination_stop_area_ref: Optional[StopAreaRef] = field(
        default=None,
        metadata={
            'name': 'DestinationStopAreaRef',
            'type': 'Element',
            'namespace': '',
        })
    stop_area: Optional[StopArea] = field(default=None,
                                          metadata={
                                              'name': 'StopArea',
                                              'type': 'Element',
                                              'namespace': '',
                                          })
    service_requirement_ref: Optional[ServiceRequirementRef] = field(
        default=None,
        metadata={
            'name': 'ServiceRequirementRef',
            'type': 'Element',
            'namespace': '',
        })
    service_requirement: Optional[ServiceRequirement] = field(
        default=None,
        metadata={
            'name': 'ServiceRequirement',
            'type': 'Element',
            'namespace': '',
        })
    observed_journey_pattern_point_ref: Optional[
        JourneyPatternPointRef] = field(default=None,
                                        metadata={
                                            'name':
                                            'ObservedJourneyPatternPointRef',
                                            'type': 'Element',
                                            'namespace': '',
                                        })
    observed_stop_point: Optional[StopPoint] = field(default=None,
                                                     metadata={
                                                         'name':
                                                         'ObservedStopPoint',
                                                         'type': 'Element',
                                                         'namespace': '',
                                                     })
    timetabled_earliest_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'TimetabledEarliestDateTime',
            'type': 'Attribute',
            'required': True,
        })
    target_date_time: Optional[XmlDateTime] = field(default=None,
                                                    metadata={
                                                        'name':
                                                        'TargetDateTime',
                                                        'type': 'Attribute',
                                                        'required': True,
                                                    })
    estimated_date_time: Optional[XmlDateTime] = field(default=None,
                                                       metadata={
                                                           'name':
                                                           'EstimatedDateTime',
                                                           'type': 'Attribute',
                                                       })
    observed_date_time: Optional[XmlDateTime] = field(default=None,
                                                      metadata={
                                                          'name':
                                                          'ObservedDateTime',
                                                          'type': 'Attribute',
                                                      })
    state: Optional[DepartureState] = field(default=None,
                                            metadata={
                                                'name': 'State',
                                                'type': 'Attribute',
                                                'required': True,
                                            })
    type_value: DepartureType = field(default=DepartureType.STOP_IF_BOARDING,
                                      metadata={
                                          'name': 'Type',
                                          'type': 'Attribute',
                                      })
    journey_pattern_sequence_number: Optional[int] = field(
        default=None,
        metadata={
            'name': 'JourneyPatternSequenceNumber',
            'type': 'Attribute',
            'required': True,
            'max_inclusive': 10000,
        })
    visit_count_number: int = field(default=1,
                                    metadata={
                                        'name': 'VisitCountNumber',
                                        'type': 'Attribute',
                                    })


@dataclass
class MessageVariants:
    message_variant: List[MessageVariant] = field(default_factory=list,
                                                  metadata={
                                                      'name': 'MessageVariant',
                                                      'type': 'Element',
                                                      'namespace': '',
                                                      'min_occurs': 1,
                                                  })


@dataclass
class NetworkDeviationEvent(Report):
    network_deviation: Optional[NetworkDeviation] = field(
        default=None,
        metadata={
            'name': 'NetworkDeviation',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })


@dataclass
class ObservedCallRef:
    """
    :ivar dated_vehicle_journey_ref:
    :ivar journey_pattern_point_ref:
    :ivar stop_point: Expanded data provided for subscriptions with
        option ExpandStopData=TRUE if the journey pattern point is a
        stop point. Alternatively, stop point information can be
        obtained by joining view StopPoint and JourneyPatternPoint in
        DOI.
    :ivar journey_pattern_sequence_number:
    :ivar observed_date_time:
    """
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    journey_pattern_point_ref: Optional[JourneyPatternPointRef] = field(
        default=None,
        metadata={
            'name': 'JourneyPatternPointRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    stop_point: Optional[StopPoint] = field(default=None,
                                            metadata={
                                                'name': 'StopPoint',
                                                'type': 'Element',
                                                'namespace': '',
                                            })
    journey_pattern_sequence_number: Optional[int] = field(
        default=None,
        metadata={
            'name': 'JourneyPatternSequenceNumber',
            'type': 'Attribute',
            'required': True,
            'max_inclusive': 10000,
        })
    observed_date_time: Optional[XmlDateTime] = field(default=None,
                                                      metadata={
                                                          'name':
                                                          'ObservedDateTime',
                                                          'type': 'Attribute',
                                                          'required': True,
                                                      })


@dataclass
class PublicationDecision(OriginalInstance):
    """
    :ivar publication_scope_ref:
    :ivar decided_by_user:
    :ivar is_approved:
    :ivar is_valid: IsValid=N means that this Publication Decision is
        not valid any more and should be removed.
    """
    publication_scope_ref: Optional[PublicationScopeRef] = field(
        default=None,
        metadata={
            'name': 'PublicationScopeRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    decided_by_user: Optional[User] = field(default=None,
                                            metadata={
                                                'name': 'DecidedByUser',
                                                'type': 'Element',
                                                'namespace': '',
                                                'required': True,
                                            })
    is_approved: Optional[YesNo] = field(default=None,
                                         metadata={
                                             'name': 'IsApproved',
                                             'type': 'Attribute',
                                             'required': True,
                                         })
    is_valid: YesNo = field(default=YesNo.Y,
                            metadata={
                                'name': 'IsValid',
                                'type': 'Attribute',
                            })


@dataclass
class ScopeElements:
    scope_element: List[ScopeElement] = field(default_factory=list,
                                              metadata={
                                                  'name': 'ScopeElement',
                                                  'type': 'Element',
                                                  'namespace': '',
                                                  'min_occurs': 1,
                                              })


@dataclass
class StopScopes:
    stop_scope: List[StopScope] = field(default_factory=list,
                                        metadata={
                                            'name': 'StopScope',
                                            'type': 'Element',
                                            'namespace': '',
                                            'min_occurs': 1,
                                        })


@dataclass
class UpdatedArrival(Instance):
    """
    :ivar monitored_vehicle_journey_ref:
    :ivar target_journey_pattern_point_ref: The current target stop
        point.
    :ivar target_stop_point: Expanded data provided for subscriptions
        with option ExpandStopData=TRUE if the journey pattern point is
        a stop point. Alternatively, stop point information can be
        obtained by joining view StopPoint and JourneyPatternPoint in
        DOI.
    :ivar timetabled_journey_pattern_point_ref: After a change of stop
        point, this element will be provided as a reference to the stop
        point where the vehicle originally was intended to dock.
    :ivar timetabled_stop_point: Expanded data provided for
        subscriptions with option ExpandStopData=TRUE if the timetabled
        journey pattern point is different from the target journey
        pattern point and it is a stop point. Alternatively, stop point
        information can be obtained by joining view StopPoint and
        JourneyPatternPoint in DOI.
    :ivar observed_journey_pattern_point_ref: The observed stop point.
    :ivar observed_stop_point: Expanded data provided for subscriptions
        with option ExpandStopData=TRUE if the journey pattern point is
        a stop point. Alternatively, stop point information can be
        obtained by joining view StopPoint and JourneyPatternPoint in
        DOI.
    :ivar target_date_time:
    :ivar estimated_date_time:
    :ivar observed_date_time:
    :ivar state:
    """
    monitored_vehicle_journey_ref: Optional[
        MonitoredVehicleJourneyRef] = field(default=None,
                                            metadata={
                                                'name':
                                                'MonitoredVehicleJourneyRef',
                                                'type': 'Element',
                                                'namespace': '',
                                            })
    target_journey_pattern_point_ref: Optional[JourneyPatternPointRef] = field(
        default=None,
        metadata={
            'name': 'TargetJourneyPatternPointRef',
            'type': 'Element',
            'namespace': '',
        })
    target_stop_point: Optional[StopPoint] = field(default=None,
                                                   metadata={
                                                       'name':
                                                       'TargetStopPoint',
                                                       'type': 'Element',
                                                       'namespace': '',
                                                   })
    timetabled_journey_pattern_point_ref: Optional[
        JourneyPatternPointRef] = field(default=None,
                                        metadata={
                                            'name':
                                            'TimetabledJourneyPatternPointRef',
                                            'type': 'Element',
                                            'namespace': '',
                                        })
    timetabled_stop_point: Optional[StopPoint] = field(
        default=None,
        metadata={
            'name': 'TimetabledStopPoint',
            'type': 'Element',
            'namespace': '',
        })
    observed_journey_pattern_point_ref: Optional[
        JourneyPatternPointRef] = field(default=None,
                                        metadata={
                                            'name':
                                            'ObservedJourneyPatternPointRef',
                                            'type': 'Element',
                                            'namespace': '',
                                        })
    observed_stop_point: Optional[StopPoint] = field(default=None,
                                                     metadata={
                                                         'name':
                                                         'ObservedStopPoint',
                                                         'type': 'Element',
                                                         'namespace': '',
                                                     })
    target_date_time: Optional[XmlDateTime] = field(default=None,
                                                    metadata={
                                                        'name':
                                                        'TargetDateTime',
                                                        'type': 'Attribute',
                                                    })
    estimated_date_time: Optional[XmlDateTime] = field(default=None,
                                                       metadata={
                                                           'name':
                                                           'EstimatedDateTime',
                                                           'type': 'Attribute',
                                                       })
    observed_date_time: Optional[XmlDateTime] = field(default=None,
                                                      metadata={
                                                          'name':
                                                          'ObservedDateTime',
                                                          'type': 'Attribute',
                                                      })
    state: Optional[ArrivalState] = field(default=None,
                                          metadata={
                                              'name': 'State',
                                              'type': 'Attribute',
                                              'required': True,
                                          })


@dataclass
class UpdatedDeparture(Instance):
    """
    :ivar monitored_vehicle_journey_ref:
    :ivar target_journey_pattern_point_ref: The current target stop
        point.
    :ivar target_stop_point: Expanded data provided for subscriptions
        with option ExpandStopData=TRUE if the journey pattern point is
        a stop point. Alternatively, stop point information can be
        obtained by joining view StopPoint and JourneyPatternPoint in
        DOI.
    :ivar timetabled_journey_pattern_point_ref: After a change of stop
        point, this element will be provided as a reference to the stop
        point where the vehicle originally was intended to dock.
    :ivar timetabled_stop_point: Expanded data provided for
        subscriptions with option ExpandStopData=TRUE if the timetabled
        journey pattern point is different from the target journey
        pattern point and it is a stop point. Alternatively, stop point
        information can be obtained by joining view StopPoint and
        JourneyPatternPoint in DOI.
    :ivar destination_stop_area_ref: Reference to the end stop area of
        the vehicle journey.
    :ivar stop_area: Expanded data provided for subscriptions with
        option ExpandStopData=TRUE Alternatively, stop area information
        can be obtained from DOI.
    :ivar observed_journey_pattern_point_ref: The observed stop point.
    :ivar observed_stop_point: Expanded data provided for subscriptions
        with option ExpandStopData=TRUE if the journey pattern point is
        a stop point. Alternatively, stop point information can be
        obtained by joining view StopPoint and JourneyPatternPoint in
        DOI.
    :ivar target_date_time:
    :ivar estimated_date_time:
    :ivar observed_date_time:
    :ivar state:
    """
    monitored_vehicle_journey_ref: Optional[
        MonitoredVehicleJourneyRef] = field(default=None,
                                            metadata={
                                                'name':
                                                'MonitoredVehicleJourneyRef',
                                                'type': 'Element',
                                                'namespace': '',
                                            })
    target_journey_pattern_point_ref: Optional[JourneyPatternPointRef] = field(
        default=None,
        metadata={
            'name': 'TargetJourneyPatternPointRef',
            'type': 'Element',
            'namespace': '',
        })
    target_stop_point: Optional[StopPoint] = field(default=None,
                                                   metadata={
                                                       'name':
                                                       'TargetStopPoint',
                                                       'type': 'Element',
                                                       'namespace': '',
                                                   })
    timetabled_journey_pattern_point_ref: Optional[
        JourneyPatternPointRef] = field(default=None,
                                        metadata={
                                            'name':
                                            'TimetabledJourneyPatternPointRef',
                                            'type': 'Element',
                                            'namespace': '',
                                        })
    timetabled_stop_point: Optional[StopPoint] = field(
        default=None,
        metadata={
            'name': 'TimetabledStopPoint',
            'type': 'Element',
            'namespace': '',
        })
    destination_stop_area_ref: Optional[StopAreaRef] = field(
        default=None,
        metadata={
            'name': 'DestinationStopAreaRef',
            'type': 'Element',
            'namespace': '',
        })
    stop_area: Optional[StopArea] = field(default=None,
                                          metadata={
                                              'name': 'StopArea',
                                              'type': 'Element',
                                              'namespace': '',
                                          })
    observed_journey_pattern_point_ref: Optional[
        JourneyPatternPointRef] = field(default=None,
                                        metadata={
                                            'name':
                                            'ObservedJourneyPatternPointRef',
                                            'type': 'Element',
                                            'namespace': '',
                                        })
    observed_stop_point: Optional[StopPoint] = field(default=None,
                                                     metadata={
                                                         'name':
                                                         'ObservedStopPoint',
                                                         'type': 'Element',
                                                         'namespace': '',
                                                     })
    target_date_time: Optional[XmlDateTime] = field(default=None,
                                                    metadata={
                                                        'name':
                                                        'TargetDateTime',
                                                        'type': 'Attribute',
                                                    })
    estimated_date_time: Optional[XmlDateTime] = field(default=None,
                                                       metadata={
                                                           'name':
                                                           'EstimatedDateTime',
                                                           'type': 'Attribute',
                                                       })
    observed_date_time: Optional[XmlDateTime] = field(default=None,
                                                      metadata={
                                                          'name':
                                                          'ObservedDateTime',
                                                          'type': 'Attribute',
                                                      })
    state: Optional[DepartureState] = field(default=None,
                                            metadata={
                                                'name': 'State',
                                                'type': 'Attribute',
                                                'required': True,
                                            })


@dataclass
class VehicleJourneyDeviationEvent(Report):
    """
    :ivar vehicle_journey_deviation: A deviation that concern all
        arrivals and departures on a vehicle journey  is exposed as a
        vehicle journey deviation instead of individual arrival and
        departure deviations.
    """
    vehicle_journey_deviation: Optional[VehicleJourneyDeviation] = field(
        default=None,
        metadata={
            'name': 'VehicleJourneyDeviation',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })


@dataclass
class ArrivalCreateEvent(Report):
    arrival: Optional[Arrival] = field(default=None,
                                       metadata={
                                           'name': 'Arrival',
                                           'type': 'Element',
                                           'namespace': '',
                                           'required': True,
                                       })


@dataclass
class ArrivalDeviation(Instance):
    """
    :ivar arrival_ref:
    :ivar call_ref:
    :ivar deviation_case_ref:
    :ivar deviation_message_version_ref:
    :ivar deviation_message: Expanded data provided for subscriptions
        with option ExpandDeviationMessageData=TRUE.
    :ivar consequence:
    :ivar is_valid: IsValid=N means that this Arrival Deviation is not
        valid anymore and should be removed.
    """
    arrival_ref: Optional[ArrivalRef] = field(default=None,
                                              metadata={
                                                  'name': 'ArrivalRef',
                                                  'type': 'Element',
                                                  'namespace': '',
                                                  'required': True,
                                              })
    call_ref: Optional[CallRef] = field(default=None,
                                        metadata={
                                            'name': 'CallRef',
                                            'type': 'Element',
                                            'namespace': '',
                                        })
    deviation_case_ref: Optional[DeviationCaseRef] = field(
        default=None,
        metadata={
            'name': 'DeviationCaseRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    deviation_message_version_ref: Optional[
        DeviationMessageVersionRef] = field(default=None,
                                            metadata={
                                                'name':
                                                'DeviationMessageVersionRef',
                                                'type': 'Element',
                                                'namespace': '',
                                            })
    deviation_message: Optional[DeviationMessage] = field(
        default=None,
        metadata={
            'name': 'DeviationMessage',
            'type': 'Element',
            'namespace': '',
        })
    consequence: Optional[str] = field(default=None,
                                       metadata={
                                           'name': 'Consequence',
                                           'type': 'Attribute',
                                           'required': True,
                                           'max_length': 16,
                                       })
    is_valid: YesNo = field(default=YesNo.Y,
                            metadata={
                                'name': 'IsValid',
                                'type': 'Attribute',
                            })


@dataclass
class ArrivalUpdateEvent(Report):
    arrival: Optional[UpdatedArrival] = field(default=None,
                                              metadata={
                                                  'name': 'Arrival',
                                                  'type': 'Element',
                                                  'namespace': '',
                                                  'required': True,
                                              })


@dataclass
class DepartureCreateEvent(Report):
    departure: Optional[Departure] = field(default=None,
                                           metadata={
                                               'name': 'Departure',
                                               'type': 'Element',
                                               'namespace': '',
                                               'required': True,
                                           })


@dataclass
class DepartureDeviation(Instance):
    """
    :ivar departure_ref:
    :ivar call_ref:
    :ivar deviation_case_ref:
    :ivar deviation_message_version_ref:
    :ivar deviation_message: Expanded data provided for subscriptions
        with option ExpandDeviationMessageData=TRUE.
    :ivar consequence:
    :ivar is_valid: IsValid=N means that this Departure Deviation is not
        valid anymore and should be removed.
    """
    departure_ref: Optional[DepartureRef] = field(default=None,
                                                  metadata={
                                                      'name': 'DepartureRef',
                                                      'type': 'Element',
                                                      'namespace': '',
                                                      'required': True,
                                                  })
    call_ref: Optional[CallRef] = field(default=None,
                                        metadata={
                                            'name': 'CallRef',
                                            'type': 'Element',
                                            'namespace': '',
                                        })
    deviation_case_ref: Optional[DeviationCaseRef] = field(
        default=None,
        metadata={
            'name': 'DeviationCaseRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    deviation_message_version_ref: Optional[
        DeviationMessageVersionRef] = field(default=None,
                                            metadata={
                                                'name':
                                                'DeviationMessageVersionRef',
                                                'type': 'Element',
                                                'namespace': '',
                                            })
    deviation_message: Optional[DeviationMessage] = field(
        default=None,
        metadata={
            'name': 'DeviationMessage',
            'type': 'Element',
            'namespace': '',
        })
    consequence: Optional[str] = field(default=None,
                                       metadata={
                                           'name': 'Consequence',
                                           'type': 'Attribute',
                                           'required': True,
                                           'max_length': 16,
                                       })
    is_valid: YesNo = field(default=YesNo.Y,
                            metadata={
                                'name': 'IsValid',
                                'type': 'Attribute',
                            })


@dataclass
class DepartureUpdateEvent(Report):
    departure: Optional[UpdatedDeparture] = field(default=None,
                                                  metadata={
                                                      'name': 'Departure',
                                                      'type': 'Element',
                                                      'namespace': '',
                                                      'required': True,
                                                  })


@dataclass
class DeviationCase(OriginalInstance):
    """
    :ivar scope_elements:
    :ivar master_deviation_case_ref: Supplied if this deviation case is
        grouped under another deviation case. The id attribute indicates
        the master deviation case instance that was valid when the
        grouping was performed.
    :ivar deviation_reason:
    :ivar replaced_by_deviation_case_ref: Supplied if this instance of
        the deviation case is revoked and a new instance is available.
    :ivar reported_by_user:
    :ivar revoked_by_user:
    :ivar source_control_action: This element is provided for
        subscriptions with option IncludeSourceControlAction =TRUE The
        structure is according to current RII-ControlAction.xsd
    :ivar operation_action_type:
    :ivar gid:
    :ivar external_id:
    :ivar external_system_id:
    :ivar official_registration_date_time:
    :ivar source_note:
    :ivar revoked_from_date_time:
    """
    scope_elements: Optional[ScopeElements] = field(default=None,
                                                    metadata={
                                                        'name':
                                                        'ScopeElements',
                                                        'type': 'Element',
                                                        'namespace': '',
                                                    })
    master_deviation_case_ref: Optional[DeviationCaseRef] = field(
        default=None,
        metadata={
            'name': 'MasterDeviationCaseRef',
            'type': 'Element',
            'namespace': '',
        })
    deviation_reason: Optional[DeviationReason] = field(default=None,
                                                        metadata={
                                                            'name':
                                                            'DeviationReason',
                                                            'type': 'Element',
                                                            'namespace': '',
                                                        })
    replaced_by_deviation_case_ref: Optional[DeviationCaseRef] = field(
        default=None,
        metadata={
            'name': 'ReplacedByDeviationCaseRef',
            'type': 'Element',
            'namespace': '',
        })
    reported_by_user: Optional[User] = field(default=None,
                                             metadata={
                                                 'name': 'ReportedByUser',
                                                 'type': 'Element',
                                                 'namespace': '',
                                             })
    revoked_by_user: Optional[User] = field(default=None,
                                            metadata={
                                                'name': 'RevokedByUser',
                                                'type': 'Element',
                                                'namespace': '',
                                            })
    source_control_action: Optional[SourceControlAction] = field(
        default=None,
        metadata={
            'name': 'SourceControlAction',
            'type': 'Element',
            'namespace': '',
        })
    operation_action_type: Optional[OperationActionType] = field(
        default=None,
        metadata={
            'name': 'OperationActionType',
            'type': 'Attribute',
            'required': True,
        })
    gid: Optional[int] = field(default=None,
                               metadata={
                                   'name': 'Gid',
                                   'type': 'Attribute',
                                   'required': True,
                                   'min_inclusive': 9076000000000000,
                                   'max_inclusive': 9076999999999999,
                               })
    external_id: Optional[str] = field(default=None,
                                       metadata={
                                           'name': 'ExternalID',
                                           'type': 'Attribute',
                                       })
    external_system_id: Optional[str] = field(default=None,
                                              metadata={
                                                  'name': 'ExternalSystemID',
                                                  'type': 'Attribute',
                                              })
    official_registration_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'OfficialRegistrationDateTime',
            'type': 'Attribute',
        })
    source_note: Optional[str] = field(default=None,
                                       metadata={
                                           'name': 'SourceNote',
                                           'type': 'Attribute',
                                           'min_length': 1,
                                           'max_length': 255,
                                       })
    revoked_from_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'RevokedFromDateTime',
            'type': 'Attribute',
        })


@dataclass
class MonitoredVehicleJourney(OriginalInstance):
    """
    :ivar dated_vehicle_journey_ref:
    :ivar assigned_vehicle_ref:
    :ivar assigned_vehicle: Expanded data provided for subscriptions
        with option ExpandVehicleData=TRUE. Alternatively available by
        joining with view Vehicle in DOI.
    :ivar last_observed_departure_ref:
    :ivar last_observed_arrival_ref:
    :ivar state: After the vehicle journey becomes monitored (in
        progress) this vehicle journey state overrides the dated vehicle
        journey state.
    :ivar passenger_level: Provided if information is available.
    :ivar in_progress_from_date_time:
    :ivar final_state_date_time: Provided when the vehicle journey
        reaches a final state.
    :ivar prediction_state:
    """
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourneyRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    assigned_vehicle_ref: Optional[VehicleRef] = field(
        default=None,
        metadata={
            'name': 'AssignedVehicleRef',
            'type': 'Element',
            'namespace': '',
        })
    assigned_vehicle: Optional[Vehicle] = field(default=None,
                                                metadata={
                                                    'name': 'AssignedVehicle',
                                                    'type': 'Element',
                                                    'namespace': '',
                                                })
    last_observed_departure_ref: Optional[ObservedCallRef] = field(
        default=None,
        metadata={
            'name': 'LastObservedDepartureRef',
            'type': 'Element',
            'namespace': '',
        })
    last_observed_arrival_ref: Optional[ObservedCallRef] = field(
        default=None,
        metadata={
            'name': 'LastObservedArrivalRef',
            'type': 'Element',
            'namespace': '',
        })
    state: Optional[VehicleJourneyState] = field(default=None,
                                                 metadata={
                                                     'name': 'State',
                                                     'type': 'Attribute',
                                                     'required': True,
                                                 })
    passenger_level: Optional[PassengerLevel] = field(default=None,
                                                      metadata={
                                                          'name':
                                                          'PassengerLevel',
                                                          'type': 'Attribute',
                                                      })
    in_progress_from_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'InProgressFromDateTime',
            'type': 'Attribute',
            'required': True,
        })
    final_state_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'FinalStateDateTime',
            'type': 'Attribute',
        })
    prediction_state: Optional[PredictionState] = field(default=None,
                                                        metadata={
                                                            'name':
                                                            'PredictionState',
                                                            'type':
                                                            'Attribute',
                                                            'required': True,
                                                        })


@dataclass
class PublicationDecisionEvent(Report):
    publication_decision: Optional[PublicationDecision] = field(
        default=None,
        metadata={
            'name': 'PublicationDecision',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })


@dataclass
class PublicationScope:
    """
    :ivar stop_scopes: If this element is not provided, then then there
        is no restriction on stop scope.
    :ivar line_ref:
    :ivar id:
    :ivar is_restricted_to_deviation_scope:
    """
    stop_scopes: Optional[StopScopes] = field(default=None,
                                              metadata={
                                                  'name': 'StopScopes',
                                                  'type': 'Element',
                                                  'namespace': '',
                                              })
    line_ref: Optional[LineRef] = field(default=None,
                                        metadata={
                                            'name': 'LineRef',
                                            'type': 'Element',
                                            'namespace': '',
                                            'required': True,
                                        })
    id: Optional[int] = field(default=None,
                              metadata={
                                  'name': 'Id',
                                  'type': 'Attribute',
                                  'required': True,
                              })
    is_restricted_to_deviation_scope: YesNo = field(
        default=YesNo.N,
        metadata={
            'name': 'IsRestrictedToDeviationScope',
            'type': 'Attribute',
        })


@dataclass
class ArrivalDeviationEvent(Report):
    arrival_deviation: Optional[ArrivalDeviation] = field(
        default=None,
        metadata={
            'name': 'ArrivalDeviation',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })


@dataclass
class DatedVehicleJourneyCreateEvent(Report):
    """
    :ivar dated_vehicle_journey:
    :ivar monitored_vehicle_journey: Provided if the vehicle journey is
        already, or has been, in progress when this event is
        transferred.
    """
    dated_vehicle_journey: Optional[DatedVehicleJourney] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourney',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    monitored_vehicle_journey: Optional[MonitoredVehicleJourney] = field(
        default=None,
        metadata={
            'name': 'MonitoredVehicleJourney',
            'type': 'Element',
            'namespace': '',
        })


@dataclass
class DepartureDeviationEvent(Report):
    departure_deviation: Optional[DepartureDeviation] = field(
        default=None,
        metadata={
            'name': 'DepartureDeviation',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })


@dataclass
class DeviationCaseEvent(Report):
    deviation_case: Optional[DeviationCase] = field(default=None,
                                                    metadata={
                                                        'name':
                                                        'DeviationCase',
                                                        'type': 'Element',
                                                        'namespace': '',
                                                        'required': True,
                                                    })


@dataclass
class PublicationScopes:
    publication_scope: List[PublicationScope] = field(default_factory=list,
                                                      metadata={
                                                          'name':
                                                          'PublicationScope',
                                                          'type': 'Element',
                                                          'namespace': '',
                                                          'min_occurs': 1,
                                                      })


@dataclass
class VehicleJourneyUpdateEvent(Report):
    dated_vehicle_journey: Optional[UpdatedDatedVehicleJourney] = field(
        default=None,
        metadata={
            'name': 'DatedVehicleJourney',
            'type': 'Element',
            'namespace': '',
        })
    monitored_vehicle_journey: Optional[MonitoredVehicleJourney] = field(
        default=None,
        metadata={
            'name': 'MonitoredVehicleJourney',
            'type': 'Element',
            'namespace': '',
        })


@dataclass
class DeviationMessageVersion(OriginalInstance):
    """
    :ivar deviation_case_ref:
    :ivar target_audiences:
    :ivar message_variants:
    :ivar priority:
    :ivar publication_scopes:
    :ivar reported_by_user:
    :ivar version_number:
    :ivar publish_from_date_time:
    :ivar publish_upto_date_time:
    :ivar requires_publication_approval:
    :ivar reminder_date_time:
    :ivar reminder_hyperlink:
    :ivar is_valid: IsValid=N means that this Deviation Message Version
        is not valid anymore and should be removed.
    :ivar internal_note:
    :ivar public_note:
    """
    deviation_case_ref: Optional[DeviationCaseRef] = field(
        default=None,
        metadata={
            'name': 'DeviationCaseRef',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    target_audiences: Optional[TargetAudiences] = field(default=None,
                                                        metadata={
                                                            'name':
                                                            'TargetAudiences',
                                                            'type': 'Element',
                                                            'namespace': '',
                                                        })
    message_variants: Optional[MessageVariants] = field(default=None,
                                                        metadata={
                                                            'name':
                                                            'MessageVariants',
                                                            'type': 'Element',
                                                            'namespace': '',
                                                            'required': True,
                                                        })
    priority: Optional[Priority] = field(default=None,
                                         metadata={
                                             'name': 'Priority',
                                             'type': 'Element',
                                             'namespace': '',
                                             'required': True,
                                         })
    publication_scopes: Optional[PublicationScopes] = field(
        default=None,
        metadata={
            'name': 'PublicationScopes',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })
    reported_by_user: Optional[User] = field(default=None,
                                             metadata={
                                                 'name': 'ReportedByUser',
                                                 'type': 'Element',
                                                 'namespace': '',
                                                 'required': True,
                                             })
    version_number: Optional[int] = field(default=None,
                                          metadata={
                                              'name': 'VersionNumber',
                                              'type': 'Attribute',
                                              'required': True,
                                          })
    publish_from_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'PublishFromDateTime',
            'type': 'Attribute',
            'required': True,
        })
    publish_upto_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            'name': 'PublishUptoDateTime',
            'type': 'Attribute',
        })
    requires_publication_approval: YesNo = field(
        default=YesNo.Y,
        metadata={
            'name': 'RequiresPublicationApproval',
            'type': 'Attribute',
        })
    reminder_date_time: Optional[XmlDateTime] = field(default=None,
                                                      metadata={
                                                          'name':
                                                          'ReminderDateTime',
                                                          'type': 'Attribute',
                                                      })
    reminder_hyperlink: Optional[str] = field(default=None,
                                              metadata={
                                                  'name': 'ReminderHyperlink',
                                                  'type': 'Attribute',
                                              })
    is_valid: YesNo = field(default=YesNo.Y,
                            metadata={
                                'name': 'IsValid',
                                'type': 'Attribute',
                            })
    internal_note: Optional[str] = field(default=None,
                                         metadata={
                                             'name': 'InternalNote',
                                             'type': 'Attribute',
                                             'min_length': 1,
                                             'max_length': 255,
                                         })
    public_note: Optional[str] = field(default=None,
                                       metadata={
                                           'name': 'PublicNote',
                                           'type': 'Attribute',
                                           'required': True,
                                           'min_length': 1,
                                           'max_length': 255,
                                       })


@dataclass
class DeviationMessageVersionEvent(Report):
    deviation_message_version: Optional[DeviationMessageVersion] = field(
        default=None,
        metadata={
            'name': 'DeviationMessageVersion',
            'type': 'Element',
            'namespace': '',
            'required': True,
        })


@dataclass
class FromPubTransMessages(Messages):
    """
    :ivar last_processed_message_request:
    :ivar last_processed_message_response:
    :ivar idle: If no other messages are sent after half the timespan
        indicated by the attribute MaxMessageInterval in the MessageBath
        element, an Idle message must be sent as a reassurance that the
        communication is OK.
    :ivar error_message:
    :ivar error_response:
    :ivar vehicle_journey_create_event:
    :ivar arrival_create_event:
    :ivar departure_create_event:
    :ivar connection_create_event:
    :ivar dated_vehicle_journey_delete_event: This event is only
        relevant for dated vehicle journeys that are removed before
        there intended operating day.
    :ivar connection_delete_event:
    :ivar vehicle_journey_update_event:
    :ivar arrival_update_event:
    :ivar departure_update_event:
    :ivar vehicle_journey_deviation_event:
    :ivar arrival_deviation_event:
    :ivar departure_deviation_event:
    :ivar connection_update_event:
    :ivar deviation_case_create_event:
    :ivar deviation_case_update_event:
    :ivar deviation_message_version_event:
    :ivar publication_decision_event:
    :ivar assignment_event:
    :ivar network_deviation_event:
    :ivar synchronisation_report:
    :ivar subscription_response:
    :ivar subscription_update_response:
    :ivar subscription_resume_response:
    :ivar subscription_termination_response:
    :ivar subscription_error_report:
    :ivar subscription_error_response:
    :ivar document_layout_version:
    :ivar local_time_zone_offset_time: Describes the local time zone
        offset without compensation for daylight saving time ( i.e.
        always +1 hour for Sweden)
    :ivar local_language: Describes the default language for texts
    """

    class Meta:
        namespace = 'http://www.pubtrans.com/ROI/3.0'

    last_processed_message_request: List[LastProcessedMessageRequest] = field(
        default_factory=list,
        metadata={
            'name': 'LastProcessedMessageRequest',
            'type': 'Element',
            'namespace': '',
        })
    last_processed_message_response: List[
        LastProcessedMessageResponse] = field(
            default_factory=list,
            metadata={
                'name': 'LastProcessedMessageResponse',
                'type': 'Element',
                'namespace': '',
            })
    idle: List[Idle] = field(default_factory=list,
                             metadata={
                                 'name': 'Idle',
                                 'type': 'Element',
                                 'namespace': '',
                             })
    error_message: List[ErrorMessage] = field(default_factory=list,
                                              metadata={
                                                  'name': 'ErrorMessage',
                                                  'type': 'Element',
                                                  'namespace': '',
                                              })
    error_response: List[ErrorResponse] = field(default_factory=list,
                                                metadata={
                                                    'name': 'ErrorResponse',
                                                    'type': 'Element',
                                                    'namespace': '',
                                                })
    vehicle_journey_create_event: List[DatedVehicleJourneyCreateEvent] = field(
        default_factory=list,
        metadata={
            'name': 'VehicleJourneyCreateEvent',
            'type': 'Element',
            'namespace': '',
        })
    arrival_create_event: List[ArrivalCreateEvent] = field(
        default_factory=list,
        metadata={
            'name': 'ArrivalCreateEvent',
            'type': 'Element',
            'namespace': '',
        })
    departure_create_event: List[DepartureCreateEvent] = field(
        default_factory=list,
        metadata={
            'name': 'DepartureCreateEvent',
            'type': 'Element',
            'namespace': '',
        })
    connection_create_event: List[ConnectionCreateEvent] = field(
        default_factory=list,
        metadata={
            'name': 'ConnectionCreateEvent',
            'type': 'Element',
            'namespace': '',
        })
    dated_vehicle_journey_delete_event: List[
        DatedVehicleJourneyDeleteEvent] = field(
            default_factory=list,
            metadata={
                'name': 'DatedVehicleJourneyDeleteEvent',
                'type': 'Element',
                'namespace': '',
            })
    connection_delete_event: List[ConnectionDeleteEvent] = field(
        default_factory=list,
        metadata={
            'name': 'ConnectionDeleteEvent',
            'type': 'Element',
            'namespace': '',
        })
    vehicle_journey_update_event: List[VehicleJourneyUpdateEvent] = field(
        default_factory=list,
        metadata={
            'name': 'VehicleJourneyUpdateEvent',
            'type': 'Element',
            'namespace': '',
        })
    arrival_update_event: List[ArrivalUpdateEvent] = field(
        default_factory=list,
        metadata={
            'name': 'ArrivalUpdateEvent',
            'type': 'Element',
            'namespace': '',
        })
    departure_update_event: List[DepartureUpdateEvent] = field(
        default_factory=list,
        metadata={
            'name': 'DepartureUpdateEvent',
            'type': 'Element',
            'namespace': '',
        })
    vehicle_journey_deviation_event: List[
        VehicleJourneyDeviationEvent] = field(
            default_factory=list,
            metadata={
                'name': 'VehicleJourneyDeviationEvent',
                'type': 'Element',
                'namespace': '',
            })
    arrival_deviation_event: List[ArrivalDeviationEvent] = field(
        default_factory=list,
        metadata={
            'name': 'ArrivalDeviationEvent',
            'type': 'Element',
            'namespace': '',
        })
    departure_deviation_event: List[DepartureDeviationEvent] = field(
        default_factory=list,
        metadata={
            'name': 'DepartureDeviationEvent',
            'type': 'Element',
            'namespace': '',
        })
    connection_update_event: List[ConnectionUpdateEvent] = field(
        default_factory=list,
        metadata={
            'name': 'ConnectionUpdateEvent',
            'type': 'Element',
            'namespace': '',
        })
    deviation_case_create_event: List[DeviationCaseEvent] = field(
        default_factory=list,
        metadata={
            'name': 'DeviationCaseCreateEvent',
            'type': 'Element',
            'namespace': '',
        })
    deviation_case_update_event: List[DeviationCaseEvent] = field(
        default_factory=list,
        metadata={
            'name': 'DeviationCaseUpdateEvent',
            'type': 'Element',
            'namespace': '',
        })
    deviation_message_version_event: List[
        DeviationMessageVersionEvent] = field(
            default_factory=list,
            metadata={
                'name': 'DeviationMessageVersionEvent',
                'type': 'Element',
                'namespace': '',
            })
    publication_decision_event: List[PublicationDecisionEvent] = field(
        default_factory=list,
        metadata={
            'name': 'PublicationDecisionEvent',
            'type': 'Element',
            'namespace': '',
        })
    assignment_event: List[AssignmentEvent] = field(default_factory=list,
                                                    metadata={
                                                        'name':
                                                        'AssignmentEvent',
                                                        'type': 'Element',
                                                        'namespace': '',
                                                    })
    network_deviation_event: List[NetworkDeviationEvent] = field(
        default_factory=list,
        metadata={
            'name': 'NetworkDeviationEvent',
            'type': 'Element',
            'namespace': '',
        })
    synchronisation_report: List[SynchronisationReport] = field(
        default_factory=list,
        metadata={
            'name': 'SynchronisationReport',
            'type': 'Element',
            'namespace': '',
        })
    subscription_response: List[SubscriptionResponse] = field(
        default_factory=list,
        metadata={
            'name': 'SubscriptionResponse',
            'type': 'Element',
            'namespace': '',
        })
    subscription_update_response: List[SubscriptionResponse] = field(
        default_factory=list,
        metadata={
            'name': 'SubscriptionUpdateResponse',
            'type': 'Element',
            'namespace': '',
        })
    subscription_resume_response: List[SubscriptionResumeResponse] = field(
        default_factory=list,
        metadata={
            'name': 'SubscriptionResumeResponse',
            'type': 'Element',
            'namespace': '',
        })
    subscription_termination_response: List[
        SubscriptionTerminationResponse] = field(
            default_factory=list,
            metadata={
                'name': 'SubscriptionTerminationResponse',
                'type': 'Element',
                'namespace': '',
            })
    subscription_error_report: List[SubscriptionErrorReport] = field(
        default_factory=list,
        metadata={
            'name': 'SubscriptionErrorReport',
            'type': 'Element',
            'namespace': '',
        })
    subscription_error_response: List[SubscriptionErrorResponse] = field(
        default_factory=list,
        metadata={
            'name': 'SubscriptionErrorResponse',
            'type': 'Element',
            'namespace': '',
        })
    document_layout_version: Optional[FromDocumentLayoutVersion] = field(
        default=None,
        metadata={
            'name': 'DocumentLayoutVersion',
            'type': 'Attribute',
            'required': True,
        })
    local_time_zone_offset_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            'name': 'LocalTimeZoneOffsetTime',
            'type': 'Attribute',
            'required': True,
        })
    local_language: Optional[str] = field(default=None,
                                          metadata={
                                              'name': 'LocalLanguage',
                                              'type': 'Attribute',
                                              'required': True,
                                          })
