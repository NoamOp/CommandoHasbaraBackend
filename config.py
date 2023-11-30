from dataclasses import dataclass


@dataclass
class Config:
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///site.db'
    SECRET_KEY: str = 'your_secret_key'
    SECURITY_PASSWORD_SALT: str = 'your_salt'
    MAIL_SERVER: str = 'smtp.example.com'
    MAIL_PORT: int = 587
    MAIL_USE_TLS: bool = True
    MAIL_USERNAME: str = 'your_email@example.com'
    MAIL_PASSWORD: str = 'your_email_password'
    MAIL_DEFAULT_SENDER: str = 'your_email@example.com'
