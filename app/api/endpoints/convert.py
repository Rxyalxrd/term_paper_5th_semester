from fastapi import APIRouter, HTTPException, status

from app.convert.convert import convert_number
from app.schemas.converted import ConvertedSchema


router = APIRouter()


@router.get(
    "/convert",
    response_model=ConvertedSchema,
    summary="Преобразование в другую систему счисления.",
    description="Преобразует число в строковое представление в указанной системе счисления."
)
def convert_input_number(input_number: int, radix: int) -> dict[str, str]:
    """
    Конвертирует входное число в указанную систему счисления.

    Parametrs
    ---------
    input_number : int
        Число для преобразования.
    radix : int
        Основание системы счисления (от 2 до 36).

    Returns
    -------
    dict[str, int]
        Словарь с результатом преобразования.

    Raises
    ------
    HTTPException
        Если произошла ошибка при конвертации.

    """

    try:
        return {"converted_num": convert_number(input_number, radix)}
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Неыерно введенные значения."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Непредвиденная ошибка: {str(e)}"
        )
