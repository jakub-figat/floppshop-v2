from pydantic import BaseSettings


class EmailSettings(BaseSettings):
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    MAIL_TLS: bool = True
    MAIL_SSL: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True

    @property
    def email_sender_class(self):
        from src.utils.email import ConsoleEmailSender, EmailSender

        return ConsoleEmailSender if self.ENV == "development" else EmailSender
