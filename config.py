class Config:
    """Set Flask configuration vars."""

    # General Config
    IRACING_USER = 'Complx'


class ProdConfig(Config):
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    DEBUG = True
    TESTING = True
