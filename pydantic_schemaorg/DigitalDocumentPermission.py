from pydantic import Field
from pydantic_schemaorg.DigitalDocumentPermissionType import DigitalDocumentPermissionType
from typing import List, Optional, Union
from pydantic_schemaorg.ContactPoint import ContactPoint
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Intangible import Intangible


class DigitalDocumentPermission(Intangible):
    """A permission for a particular person or group to access a particular file.

    See https://schema.org/DigitalDocumentPermission.

    """
    type_: str = Field("DigitalDocumentPermission", const=True, alias='@type')
    permissionType: Optional[Union[List[Union[DigitalDocumentPermissionType, str]], Union[DigitalDocumentPermissionType, str]]] = Field(
        None,
        description="The type of permission granted the person, organization, or audience.",
    )
    grantee: Optional[Union[List[Union[ContactPoint, Audience, Organization, Person, str]], Union[ContactPoint, Audience, Organization, Person, str]]] = Field(
        None,
        description="The person, organization, contact point, or audience that has been granted this permission.",
    )
    

DigitalDocumentPermission.update_forward_refs()
