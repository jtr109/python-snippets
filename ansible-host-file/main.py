import unittest
import configparser
from ansible.plugins.inventory.ini import InventoryModule

HOSTS_FILE = """
[inner]
106.75.97.40 ansible_user=root ansible_ssh_pass="000000Asd"

[outer]
117.50.20.166 ansible_user=root ansible_ssh_pass="000000Asd"
"""


class TestHostsFile(unittest.TestCase):

    def test_ini(self):
        # config = configparser.ConfigParser()
        # config.read_string(HOSTS_FILE)
        # print(list(config['inner'].keys()))
        path = 'foo'
        lines = HOSTS_FILE.split('\n')
        result = InventoryModule()._parse(path, lines)
        print(result)


if __name__ == "__main__":
    unittest.main()
