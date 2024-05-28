from Utilities.read_config import read_configuration
import pytest
class BaseTestPage:
    @classmethod
    @pytest.fixture(scope="module")

    def credentials(self):
        """Read and return the username and password."""
        Uname = read_configuration('Default', 'Uname')
        password = read_configuration('Default', 'Password')
        return Uname, password


