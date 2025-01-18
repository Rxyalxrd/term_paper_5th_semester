import ctypes

from app.constnts import BUFFER_SIZE


def convert_number(num: int, radix: int) -> str:
    """
    Конвертирует число в строковое представление в указанной системе счисления.

    Parameters
    ----------
    num : int
        Целое число, которое требуется преобразовать.
    radix : uint
        Основание системы счисления, в которую нужно преобразовать число.

    Returns
    -------
    str
        Строковое представление числа в указанной системе счисления.

    Raises
    ------
    Exception
        Если преобразование не удалось, возбуждается исключение с сообщением "Conversion failed".

    Notes
    -----
    Эта функция использует DLL-библиотеку `convert.dll` для выполнения преобразования. 
    DLL должна быть доступна по указанному пути, иначе возникнет ошибка.

    Example
    -------
    >>> convert_number(255, 16)
    'FF'

    >>> convert_number(10, 2)
    '1010'

    """

    my_dll = ctypes.WinDLL(r"C:/Users/TheRo/.vscode/Dev/5_sem_project/kr_convert_sys_sc/convert.dll")

    my_dll.convert.argtypes = (ctypes.c_int, ctypes.c_uint, ctypes.c_char_p)
    my_dll.convert.restype = ctypes.c_uint

    buffer = ctypes.create_string_buffer(BUFFER_SIZE)

    result = my_dll.convert(num, radix, buffer)

    if result != 1:
        raise Exception("Conversion failed.")

    return buffer.value.decode('ascii')
