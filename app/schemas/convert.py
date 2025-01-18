from pydantic import BaseModel, Field

from app.constnts import MIN_REDIX, MAX_REDIX


class ConvertSchema(BaseModel):
    """
    Схема валидации данных для конвертации.

    Attributes
    ----------

    input_number : int
        Число, которое нужно конвертировать
    redix : int
        "Основание системы счисления (от 2 до 36)"

    """
    input_number: int = Field(
        ...,
        description="Число, которое нужно конвертировать"
    )
    redix: int = Field(
        ...,
        ge=MIN_REDIX,
        le=MAX_REDIX,
        description="Основание системы счисления (от 2 до 36)"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "input_number": 255,
                "redix": 16
            },
            "description": "Модель данных для конвертации числа в заданную систему счисления."
        }
