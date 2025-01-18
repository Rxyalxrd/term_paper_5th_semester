from pydantic import BaseModel


class ConvertedSchema(BaseModel):
    """
    Схема для конвертированного числа.

    Attributes
    ----------
    converted_num : str
        Конвертированное число.

    """

    converted_num: str

    class Config:
        json_schema_extra = {
            "example": {
                "converted_num": "FF"
            },
        }