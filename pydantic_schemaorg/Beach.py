from __future__ import annotations


from pydantic.v1 import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Beach(CivicStructure):
    """Beach.

    See: https://schema.org/Beach
    Model depth: 4
    """
    type_: str = Field(default="Beach", alias='@type', const=True)
    
