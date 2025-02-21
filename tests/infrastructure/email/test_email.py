import pytest
from punq import Container

from infrastructure.email.smtp_client import SMTPEmailService


@pytest.mark.asyncio
async def test_send_email(mocker, container: Container):
    email_service: SMTPEmailService = container.resolve(SMTPEmailService)

    mock_smtp_class = mocker.patch('aiosmtplib.SMTP')

    mock_smtp_instance = mocker.AsyncMock()
    mock_smtp_class.return_value = mock_smtp_instance

    mock_smtp_instance.__aenter__.return_value = mock_smtp_instance

    to_email = 'recipient@example.com'
    message = 'Test message'
    await email_service.send(to_email, message)

    mock_smtp_class.assert_called_once_with(hostname=email_service.config.host, port=email_service.config.port)

    mock_smtp_instance.login.assert_called_once_with(email_service.config.username, email_service.config.password)
    mock_smtp_instance.sendmail.assert_called_once_with(
        email_service.config.username,
        to_email,
        message,
    )
