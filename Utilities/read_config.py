from configparser import ConfigParser
import pytest

def read_configuration(category, key):
    config = ConfigParser()
    config.read("/Users/chethangopal/Desktop/SwagSuace/Config/config.ini")
    return config.get(category, key)

