from typing import Optional, Union

from pydantic import BaseModel, Field


class Contract(BaseModel):
    first_name: str = Field(validation_alias="firstName")
    last_name: str = Field(validation_alias="lastName")
    middle_name: Optional[str] = Field(None, validation_alias="middleName")
    speciality: str = Field(validation_alias="specialty")
    contract_number: str = Field(validation_alias="contractNumber")
    competitive_point: Union[int, float] = Field(validation_alias="competitivePoint")
    date: str
