from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from typing import Optional

from static.noptis.ptshared.pt_shared_types import DeviationCaseRef

__NAMESPACE__ = 'http://www.pubtrans.com/RII/2.0'


class ChangeModel(Enum):
    MINIMAL = 'MINIMAL'
    LINEAR = 'LINEAR'
    STATISTIC = 'STATISTIC'


@dataclass
class ExternalCaseRef:
    """
    :ivar case_id: This is a unique case identification in scope of a
        certain external source system.
    :ivar system_id: This is the agreed identification of the external
        source system.
    """
    case_id: Optional[str] = field(default=None,
                                   metadata={
                                       'name': 'CaseID',
                                       'type': 'Attribute',
                                       'required': True,
                                       'max_length': 50,
                                   })
    system_id: Optional[str] = field(default=None,
                                     metadata={
                                         'name': 'SystemID',
                                         'type': 'Attribute',
                                         'required': True,
                                         'max_length': 50,
                                     })


class ProgressState(Enum):
    FASTPROGRESS = 'FASTPROGRESS'
    NORMALPROGRESS = 'NORMALPROGRESS'
    SLOWPROGRESS = 'SLOWPROGRESS'
    NOPROGRESS = 'NOPROGRESS'


class Status(Enum):
    LIMITEDACCESS = 'LIMITEDACCESS'
    CLOSED = 'CLOSED'
    ATTENTION = 'ATTENTION'


@dataclass
class User:
    """
    :ivar name:
    :ivar organisational_unit_code:
    :ivar organisation_code: This attribute can be omitted in systems
        where OrganisationalUnitCode is unique across all organisations.
    """
    name: Optional[str] = field(default=None,
                                metadata={
                                    'name': 'Name',
                                    'type': 'Attribute',
                                    'max_length': 50,
                                })
    organisational_unit_code: Optional[str] = field(
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
                                                })


@dataclass
class CaseRef:
    deviation_case_ref: Optional[DeviationCaseRef] = field(
        default=None,
        metadata={
            'name': 'DeviationCaseRef',
            'type': 'Element',
            'namespace': '',
        })
    external_case_ref: Optional[ExternalCaseRef] = field(default=None,
                                                         metadata={
                                                             'name':
                                                             'ExternalCaseRef',
                                                             'type': 'Element',
                                                             'namespace': '',
                                                         })


@dataclass
class DeviationMessageVersionRef:
    case_ref: Optional[CaseRef] = field(default=None,
                                        metadata={
                                            'name': 'CaseRef',
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
