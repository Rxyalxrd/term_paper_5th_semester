from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Настройки проекта для запуска приложения.

    Параметры задаются через переменные окружения, указанные в `.env`.

    Attributes
    ----------
    app_title : str
        Название приложения.
    app_description : str
        Описание приложения.

    """

    app_title: str
    app_description: str

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()
