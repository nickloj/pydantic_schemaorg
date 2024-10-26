from __future__ import annotations


from pydantic.v1 import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Season(CreativeWork):
    """A media season e.g. tv, radio, video game etc.

    See: https://schema.org/Season
    Model depth: 3
    """
    type_: str = Field(default="Season", alias='@type', const=True)
    
