from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class MedicalClinic(MedicalBusiness, MedicalOrganization):
    """A facility, often associated with a hospital or medical school, that is devoted to the"
     "specific diagnosis and/or healthcare. Previously limited to outpatients but with"
     "evolution it may be open to inpatients as well.

    See: https://schema.org/MedicalClinic
    Model depth: 4
    """
    type_: str = Field(default="MedicalClinic", alias='@type', const=True)
    medicalSpecialty: Optional[Union[List[Union['MedicalSpecialty', str]], 'MedicalSpecialty', str]] = Field(
        default=None,
        description="A medical specialty of the provider.",
    )
    availableService: Optional[Union[List[Union['MedicalTherapy', 'MedicalProcedure', 'MedicalTest', str]], 'MedicalTherapy', 'MedicalProcedure', 'MedicalTest', str]] = Field(
        default=None,
        description="A medical service available from this provider.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
    from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
    from pydantic_schemaorg.MedicalProcedure import MedicalProcedure
    from pydantic_schemaorg.MedicalTest import MedicalTest
