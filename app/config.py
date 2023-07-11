from typing import Optional

from pydantic import BaseSettings, EmailStr, HttpUrl, validator


class Settings(BaseSettings):
    """
    Config parameters from environment
    """

    # Service:

    SESSION_SECRET_KEY: Optional[str] = "MyAwEsOmEKEY"
    SLACK_BOT_TOKEN: str = None

    ENVIRONMENT: Optional[str] = "local"
    DEBUG: bool = False

    class Config:
        """
        https://pydantic-docs.helpmanual.io/usage/settings/
        """

        case_sensitive = True
        # Whether to populate models with the value property of enums, rather than the raw enum.
        use_enum_values = True


settings = Settings()
