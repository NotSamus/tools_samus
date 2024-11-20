import unittest
from auto import helper

class TestHelper(unittest.TestCase):
    def test_binary(self):
        self.assertEqual(helper.identifier('101010'), 'binary')
        self.assertEqual(helper.identifier('1100'), 'binary')
        self.assertEqual(helper.identifier('1111'), 'binary')
        self.assertNotEqual(helper.identifier('11002'), 'binary')

    def test_hex(self):
        self.assertEqual(helper.identifier('68 65 6c 6c 6f'), 'hex')
        self.assertEqual(helper.identifier('68656c6c6f'), 'hex')
        self.assertNotEqual(helper.identifier('68 65 6c 6c 6g'), 'hex')

    def test_base64(self):
        self.assertEqual(helper.identifier('aGVsbG8='), 'base64')
        self.assertEqual(helper.identifier('aGVsbG8=='), 'base64')
        self.assertNotEqual(helper.identifier('aGVsbG8'), 'base64')

    def test_rot47(self):
        self.assertEqual(helper.identifier('~}|{'), 'rot47')
        self.assertNotEqual(helper.identifier('hello'), 'rot47')

    def test_unknown(self):
        self.assertEqual(helper.identifier(''), 'unknown')
        self.assertEqual(helper.identifier('12345'), 'unknown')

if __name__ == '__main__':
    unittest.main()