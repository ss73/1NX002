import unittest
import copy

class TestGotchas(unittest.TestCase):

    def setup(self):
        pass

    def test_immutable_assignments(self):
        a = 5
        b = a
        b = 8
        self.assertEqual(a, 5)
        self.assertEqual(b, 8)

    def test_mutable_assignments(self):
        a = [5]
        b = a
        b[0] = 8
        self.assertEqual(id(a), id(b))
        self.assertNotEqual(a[0], 5)
        self.assertEqual(a[0], 8)
        self.assertEqual(b[0], 8)

    def test_shallow_copy(self):
        m1 = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
        m2 = copy.copy(m1)
        self.assertNotEqual(id(m1), id(m2))
        m1[0][0] = 'AA'
        self.assertEqual(m1[0][0], m2[0][0])
    
    def test_deep_copy(self):
        m1 = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
        m2 = copy.deepcopy(m1)
        m1[0][0] = 'AA'
        self.assertNotEqual(m1[0][0], m2[0][0])

    def test_decimal_base2(self):
        a = 0.1 + 0.1 + 0.1
        b = 0.3
        self.assertNotEqual(a, b)
        self.assertAlmostEqual(a, b)

    def test_mutate_list_while_iterating(self):
        l = list('abba')
        for i, c in enumerate(l):
            if c == 'b':
                del l[i]
        self.assertNotEqual(''.join(l), 'aa')
        self.assertEqual(''.join(l), 'aba')

if __name__ == 'main':
    unittest.main()
