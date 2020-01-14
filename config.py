class Config:
    """Set Flask configuration vars."""
    pass


class ProdConfig(Config):
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    DEBUG = True
    TESTING = True


class TestConfig(Config):
    DEBUG = False
    TESTING = True
