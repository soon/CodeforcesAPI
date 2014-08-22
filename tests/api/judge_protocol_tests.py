"""
This module provides classes for testing JudgeProtocol object
"""
import unittest

from codeforces import JudgeProtocol


class JudgeProtocolTests(unittest.TestCase):

    def setUp(self):
        self.protocol = JudgeProtocol()

    def test_load_from_dict(self):
        protocol = (b"Solution verdict:\nWRONG_ANSWER\n\nChecker:\nwrong answer 1st words differ - "
                    b"expected: \u0027Poor\u0027, found: \u00272\u0027\r\n\n\nInput:\n1 5 1 3 1 1\r\n\n\n"
                    b"Output:\n2\r\n\n\nAnswer:\nPoor Inna and pony!\r\n\n\nTime:\n62\n\nMemory:\n0\n")

        protocol = protocol.decode('utf-8')

        d = {
            "manual": "true",
            "protocol": protocol,
            "verdict": "Successful hacking attempt"
        }

        self.protocol.load_from_dict(d)

        self.assertEqual(True, self.protocol.manual)
        self.assertEqual(protocol, self.protocol.protocol)
        self.assertEqual('Successful hacking attempt', self.protocol.verdict)

    def test_load_from_json(self):
        protocol = ("Solution verdict:\nWRONG_ANSWER\n\nChecker:\nwrong answer 1st words differ - "
                    "expected: \u0027Poor\u0027, found: \u00272\u0027\r\n\n\nInput:\n1 5 1 3 1 1\r\n\n\n"
                    "Output:\n2\r\n\n\nAnswer:\nPoor Inna and pony!\r\n\n\nTime:\n62\n\nMemory:\n0\n")

        json = r''' {
            "manual":"true",
            "protocol":"Solution verdict:\nWRONG_ANSWER\n\nChecker:\nwrong answer 1st words differ - ''' \
                       r'''expected: \u0027Poor\u0027, found: \u00272\u0027\r\n\n\nInput:\n1 5 1 3 1 1\r\n\n\n''' \
                       r'''Output:\n2\r\n\n\nAnswer:\nPoor Inna and pony!\r\n\n\nTime:\n62\n\nMemory:\n0\n",
            "verdict":"Successful hacking attempt"
        }'''

        self.protocol.load_from_json(json)

        self.assertEqual(True, self.protocol.manual)
        self.assertEqual(protocol, self.protocol.protocol)
        self.assertEqual('Successful hacking attempt', self.protocol.verdict)


if __name__ == '__main__':
    unittest.main()
