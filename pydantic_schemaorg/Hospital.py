from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic_schemaorg.EmergencyService import EmergencyService
from pydantic_schemaorg.CivicStructure import CivicStructure
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class Hospital(MedicalOrganization, EmergencyService, CivicStructure):
    """A hospital.

    See: https://schema.org/Hospital
    Model depth: 4
    """
    type_: str = Field(default="Hospital", alias='@type', const=True)
    medicalSpecialty: Optional[Union[List[Union['MedicalSpecialty', str]], 'MedicalSpecialty', str]] = Field(
        default=None,
        description="A medical specialty of the provider.",
    )
    healthcareReportingData: Optional[Union[List[Union['Dataset', 'CDCPMDRecord', str]], 'Dataset', 'CDCPMDRecord', str]] = Field(
        default=None,
        description="Indicates data describing a hospital, e.g. a CDC [[CDCPMDRecord]] or as some kind of"
     "[[Dataset]].",
    )
    availableService: Optional[Union[List[Union['MedicalTherapy', 'MedicalProcedure', 'MedicalTest', str]], 'MedicalTherapy', 'MedicalProcedure', 'MedicalTest', str]] = Field(
        default=None,
        description="A medical service available from this provider.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
    from pydantic_schemaorg.Dataset import Dataset
    from pydantic_schemaorg.CDCPMDRecord import CDCPMDRecord
    from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
    from pydantic_schemaorg.MedicalProcedure import MedicalProcedure
    from pydantic_schemaorg.MedicalTest import MedicalTest
