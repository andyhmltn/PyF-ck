import unittest
import sys
import os
import pyfuck


class TestPyFuck(unittest.TestCase):
    to_parse = ('++++++++++[>++++>++++++++>++++++++++>+++++++++++>++++++'
                '++++++<<<<<-]>>.>>>+.<<<----------.<++.>>-.>---.')
    test_file = '.test'

    def setUp(self):
        self.fd = open(self.test_file, 'w+')
        sys.stdout = self.fd

    def tearDown(self):
        self.fd.close()
        os.remove(self.test_file)
        sys.stdout = sys.__stdout__

    def assertion(self):
        # head to the start of the file for output
        self.fd.seek(0, 0)
        text = self.fd.read()
        self.assertEqual(text, 'PyF*ck\n')

    def test_evals_pyfuck(self):
        p = pyfuck.PyFuck(self.to_parse)
        p.parse()
        self.assertion()

    def test_api(self):
        pyfuck.parse(self.to_parse)
        self.assertion()


if __name__ == '__main__':
    unittest.main()
