from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic.v1 import StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic_schemaorg.Intangible import Intangible


class Rating(Intangible):
    """A rating is an evaluation on a numeric scale, such as 1 to 5 stars.

    See: https://schema.org/Rating
    Model depth: 3
    """
    type_: str = Field(default="Rating", alias='@type', const=True)
    worstRating: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str, 'Text']], StrictInt, StrictFloat, 'Number', str, 'Text']] = Field(
        default=None,
        description="The lowest value allowed in this rating system. If worstRating is omitted, 1 is assumed.",
    )
    author: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The author of this content or rating. Please note that author is special in that HTML 5"
     "provides a special mechanism for indicating authorship via the rel tag. That is equivalent"
     "to this and may be used interchangeably.",
    )
    reviewAspect: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="This Review or Rating is relevant to this part or facet of the itemReviewed.",
    )
    ratingValue: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str, 'Text']], StrictInt, StrictFloat, 'Number', str, 'Text']] = Field(
        default=None,
        description="The rating for the content. Usage guidelines: * Use values from 0123456789 (Unicode"
     "'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar"
     "Unicode symbols. * Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate"
     "a decimal point. Avoid using these symbols as a readability separator.",
    )
    ratingExplanation: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A short explanation (e.g. one to two sentences) providing background context and other"
     "information that led to the conclusion expressed in the rating. This is particularly"
     "applicable to ratings associated with \"fact check\" markup using [[ClaimReview]].",
    )
    bestRating: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str, 'Text']], StrictInt, StrictFloat, 'Number', str, 'Text']] = Field(
        default=None,
        description="The highest value allowed in this rating system. If bestRating is omitted, 5 is assumed.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
