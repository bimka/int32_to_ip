import unittest
import ipaddress

from int32_to_ip import int32_to_ip

class ValuesTestCase(unittest.TestCase):

    def test_argument_is_integer(self):
        result = int32_to_ip(2154959208)
        self.assertEqual(result, ipaddress.IPv4Address("128.114.17.104"))

if __name__ == "__main__":
  unittest.main()