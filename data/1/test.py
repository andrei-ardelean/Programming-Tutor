import unittest


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    """Funcția ta nu returnează nimic."""

    def test01(self):
        el = (12, 6, 6)
        a, b, c = el[0], el[1], el[2]
        self.assertIsNot(cmmdc(a, b), None)

    def test02(self):
        el = (7, 21, 7)
        a, b, c = el[0], el[1], el[2]
        self.assertIsNot(cmmdc(a, b), None)

    def test03(self):
        el = (25, 13, 1)
        a, b, c = el[0], el[1], el[2]
        self.assertIsNot(cmmdc(a, b), None)

    def test04(self):
        el = (0, 5, 5)
        a, b, c = el[0], el[1], el[2]
        self.assertIsNot(cmmdc(a, b), None)

    def test05(self):
        el = (6, 0, 6)
        a, b, c = el[0], el[1], el[2]
        self.assertIsNot(cmmdc(a, b), None)

    def test06(self):
        el = (-6, 3, 3)
        a, b, c = el[0], el[1], el[2]
        self.assertIsNot(cmmdc(a, b), None)

    def test07(self):
        el = (12, -8, 4)
        a, b, c = el[0], el[1], el[2]
        self.assertIsNot(cmmdc(a, b), None)

    def test08(self):
        el = (-13, -27, 1)
        a, b, c = el[0], el[1], el[2]
        self.assertIsNot(cmmdc(a, b), None)

    """Funcția ta nu returnează un număr natural."""

    def test09(self):
        el = (12, 6, 6)
        a, b, c = el[0], el[1], el[2]
        self.assertIsNot(cmmdc(a, b), None)
        self.assertIsInstance(cmmdc(a, b), int)
        if isinstance(cmmdc(a, b), int):
            self.assertGreaterEqual(cmmdc(a, b), 0)

    def test10(self):
        el = (7, 21, 7)
        a, b, c = el[0], el[1], el[2]
        self.assertIsNot(cmmdc(a, b), None)
        if isinstance(cmmdc(a, b), int):
            self.assertGreaterEqual(cmmdc(a, b), 0)

    def test11(self):
        el = (25, 13, 1)
        a, b, c = el[0], el[1], el[2]
        self.assertIsNot(cmmdc(a, b), None)
        if isinstance(cmmdc(a, b), int):
            self.assertGreaterEqual(cmmdc(a, b), 0)

    def test12(self):
        el = (0, 5, 5)
        a, b, c = el[0], el[1], el[2]
        self.assertIsNot(cmmdc(a, b), None)
        if isinstance(cmmdc(a, b), int):
            self.assertGreaterEqual(cmmdc(a, b), 0)

    def test13(self):
        el = (6, 0, 6)
        a, b, c = el[0], el[1], el[2]
        self.assertIsNot(cmmdc(a, b), None)
        if isinstance(cmmdc(a, b), int):
            self.assertGreaterEqual(cmmdc(a, b), 0)

    def test14(self):
        el = (-6, 3, 3)
        a, b, c = el[0], el[1], el[2]
        self.assertIsNot(cmmdc(a, b), None)
        if isinstance(cmmdc(a, b), int):
            self.assertGreaterEqual(cmmdc(a, b), 0)

    def test15(self):
        el = (12, -8, 4)
        a, b, c = el[0], el[1], el[2]
        self.assertIsNot(cmmdc(a, b), None)
        if isinstance(cmmdc(a, b), int):
            self.assertGreaterEqual(cmmdc(a, b), 0)

    def test16(self):
        el = (-13, -27, 1)
        a, b, c = el[0], el[1], el[2]
        self.assertIsNot(cmmdc(a, b), None)
        if isinstance(cmmdc(a, b), int):
            self.assertGreaterEqual(cmmdc(a, b), 0)

    """Codul tău nu funcționează pe caz general. Regândește soluția sau consultă zona de hint."""

    def test17(self):
        el = (12, 6, 6)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    def test18(self):
        el = (21, 7, 7)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    def test19(self):
        el = (6, 12, 6)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    def test20(self):
        el = (7, 21, 7)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    """Codul tău nu funcționează dacă numerele sunt negative."""

    def test21(self):
        el = (-6, 3, 3)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    def test22(self):
        el = (5, -25, 5)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    def test23(self):
        el = (-3, -6, 3)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    def test24(self):
        el = (-13, -27, 1)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    """Codul tău nu funcționează dacă a este 0."""

    def test25(self):
        el = (0, 5, 5)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    def test26(self):
        el = (0, 6, 6)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    def test27(self):
        el = (0, -5, 5)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    def test28(self):
        el = (0, -6, 6)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    """Codul tău nu funcționează dacă b este 0."""

    def test29(self):
        el = (0, 0, 0)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    def test30(self):
        el = (5, 0, 5)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    def test31(self):
        el = (6, 0, 6)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    def test32(self):
        el = (-5, 0, 5)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    def test33(self):
        el = (-6, 0, 6)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    """Codul tău nu funcționează dacă cele două numere sunt prime între ele."""

    def test34(self):
        el = (13, 27, 1)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    def test35(self):
        el = (3, 1, 1)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)

    """Codul tău nu funcționează dacă cele două numere sunt egale."""

    def test36(self):
        el = (6, 6, 6)
        a, b, c = el[0], el[1], el[2]
        self.assertEqual(cmmdc(a, b), c)


if __name__ == '__main__':
    outputFilename = "file/output.txt"
    compileFilename = "file/compile.txt"
    try:
        from implementation import cmmdc
        # clear compilation file
        with open(compileFilename, 'w') as f:
            f.write("")

        # write the unittest result to file
        with open(outputFilename, 'w') as f:
            runner = unittest.TextTestRunner(f)
            unittest.main(testRunner=runner)
    except ModuleNotFoundError as e:
        with open(compileFilename, 'w') as f:
            f.write(str(e))
    except IndentationError as e:
        with open(compileFilename, 'w') as f:
            f.write(str(e))
    except SyntaxError as e:
        with open(compileFilename, 'w') as f:
            f.write(str(e))
    except Exception as e:
        with open(compileFilename, 'w') as f:
            f.write(str(e))
