import unittest


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    """Funcția ta nu returnează nimic."""

    def test01(self):
        a, b, c = 0, 5, 5
        self.assertIsNot(suma(a, b), None)

    def test02(self):
        a, b, c = 5, 0, 5
        self.assertIsNot(suma(a, b), None)

    def test03(self):
        a, b, c = 3, 4, 7
        self.assertIsNot(suma(a, b), None)

    def test04(self):
        a, b, c = -5, 9, 4
        self.assertIsNot(suma(a, b), None)

    def test05(self):
        a, b, c = 10, -10, 0
        self.assertIsNot(suma(a, b), None)

    def test06(self):
        a, b, c = -5, -5, -10
        self.assertIsNot(suma(a, b), None)

    """Funcția ta nu returnează un număr întreg."""

    def test07(self):
        a, b, c = 0, 5, 5
        self.assertIsNot(suma(a, b), None)
        self.assertIsInstance(suma(a, b), int)

    def test08(self):
        a, b, c = 5, 0, 5
        self.assertIsNot(suma(a, b), None)
        self.assertIsInstance(suma(a, b), int)

    def test09(self):
        a, b, c = 3, 4, 7
        self.assertIsNot(suma(a, b), None)
        self.assertIsInstance(suma(a, b), int)

    def test10(self):
        a, b, c = -5, 9, 4
        self.assertIsNot(suma(a, b), None)
        self.assertIsInstance(suma(a, b), int)

    def test11(self):
        a, b, c = 10, -10, 0
        self.assertIsNot(suma(a, b), None)
        self.assertIsInstance(suma(a, b), int)

    def test12(self):
        a, b, c = -5, -5, -10
        self.assertIsNot(suma(a, b), None)
        self.assertIsInstance(suma(a, b), int)

    """Codul tău nu funcționează pe caz general. Regândește soluția sau consultă zona de hint."""

    def test13(self):
        a, b, c = 0, 5, 5
        self.assertIsNot(suma(a, b), None)
        if isinstance(suma(a, b), int):
            self.assertEqual(suma(a, b), c)

    def test14(self):
        a, b, c = 5, 0, 5
        self.assertIsNot(suma(a, b), None)
        if isinstance(suma(a, b), int):
            self.assertEqual(suma(a, b), c)

    def test15(self):
        a, b, c = 3, 4, 7
        self.assertIsNot(suma(a, b), None)
        if isinstance(suma(a, b), int):
            self.assertEqual(suma(a, b), c)

    def test16(self):
        a, b, c = -5, 9, 4
        self.assertIsNot(suma(a, b), None)
        if isinstance(suma(a, b), int):
            self.assertEqual(suma(a, b), c)

    def test17(self):
        a, b, c = 10, -10, 0
        self.assertIsNot(suma(a, b), None)
        if isinstance(suma(a, b), int):
            self.assertEqual(suma(a, b), c)

    def test18(self):
        a, b, c = -5, -5, -10
        self.assertIsNot(suma(a, b), None)
        if isinstance(suma(a, b), int):
            self.assertEqual(suma(a, b), c)


if __name__ == '__main__':
    outputFilename = "file/output.txt"
    compileFilename = "file/compile.txt"
    try:
        from implementation import suma
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