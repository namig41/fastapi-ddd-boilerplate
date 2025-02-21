from dataclasses import dataclass
from typing import Self

import aiosmtplib

from infrastructure.email.config import SMTPConfig


@dataclass
class SMTPEmailService:
    """
    Сервис для оправки email с помощью протокола SMTP.
    """

    config: SMTPConfig

    async def send(self: Self, to_email: str, message: str) -> None:
        """
        Отправляем email.
        """
        async with aiosmtplib.SMTP(hostname=self.config.host, port=self.config.port) as server:
            await server.login(self.config.username, self.config.password)
            await server.sendmail(self.config.username, to_email, message)
