from dataclasses import dataclass
import smtplib
import ssl
from pathlib import Path
from typing import Self

from infrastructure.email.config import SMTPConfig
from settings.config import Settings


@dataclass
class SMTPEmailService:
    """
    Сервис для оправки email с помощью протокола SMTP.
    """
    
    smtp_config: SMTPConfig

    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    async def send(self: Self, to_email: str, message: str) -> None:
        """
        Отправляем email.
        """
        with smtplib.SMTP(self.smtp_config.host, self.smtp_config.port) as server:
            server.login(self.smtp_config.username, self.smtp_config.password)
            server.sendmail(self.smtp_config.username, to_email, message)