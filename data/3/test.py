import unittest


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    """Funcția ta nu returnează nimic."""

    def test01(self):
        a, s = 0, 0
        self.assertIsNot(sumaCifrelor(a), None)

    def test02(self):
        a, s = 1, 1
        self.assertIsNot(sumaCifrelor(a), None)

    def test03(self):
        a, s = 9, 9
        self.assertIsNot(sumaCifrelor(a), None)

    def test04(self):
        a, s = 99, 18
        self.assertIsNot(sumaCifrelor(a), None)

    def test05(self):
        a, s = 102, 3
        self.assertIsNot(sumaCifrelor(a), None)

    def test06(self):
        a, s = 123456, 21
        self.assertIsNot(sumaCifrelor(a), None)

    """Funcția ta nu returnează un număr natural."""

    def test07(self):
        a, s = 0, 0
        self.assertIsNot(sumaCifrelor(a), None)
        self.assertIsInstance(sumaCifrelor(a), int)
        if isinstance(sumaCifrelor(a), int):
            self.assertGreaterEqual(sumaCifrelor(a), 0)

    def test08(self):
        a, s = 1, 1
        self.assertIsNot(sumaCifrelor(a), None)
        self.assertIsInstance(sumaCifrelor(a), int)
        if isinstance(sumaCifrelor(a), int):
            self.assertGreaterEqual(sumaCifrelor(a), 0)

    def test09(self):
        a, s = 9, 9
        self.assertIsNot(sumaCifrelor(a), None)
        self.assertIsInstance(sumaCifrelor(a), int)
        if isinstance(sumaCifrelor(a), int):
            self.assertGreaterEqual(sumaCifrelor(a), 0)

    def test10(self):
        a, s = 99, 18
        self.assertIsNot(sumaCifrelor(a), None)
        self.assertIsInstance(sumaCifrelor(a), int)
        if isinstance(sumaCifrelor(a), int):
            self.assertGreaterEqual(sumaCifrelor(a), 0)

    def test11(self):
        a, s = 102, 3
        self.assertIsNot(sumaCifrelor(a), None)
        self.assertIsInstance(sumaCifrelor(a), int)
        if isinstance(sumaCifrelor(a), int):
            self.assertGreaterEqual(sumaCifrelor(a), 0)

    def test12(self):
        a, s = 123456, 21
        self.assertIsNot(sumaCifrelor(a), None)
        self.assertIsInstance(sumaCifrelor(a), int)
        if isinstance(sumaCifrelor(a), int):
            self.assertGreaterEqual(sumaCifrelor(a), 0)

    """Codul tău nu funcționează pe caz general. Regândește soluția sau consultă zona de hint."""

    def test13(self):
        a, s = 99, 18
        self.assertEqual(sumaCifrelor(a), s)

    def test14(self):
        a, s = 102, 3
        self.assertEqual(sumaCifrelor(a), s)

    def test15(self):
        a, s = 1000, 1
        self.assertEqual(sumaCifrelor(a), s)

    def test16(self):
        a, s = 12345, 15
        self.assertEqual(sumaCifrelor(a), s)

    """Codul tău nu funcționează pentru numere de o singură cifră."""

    def test17(self):
        a, s = 1, 1
        self.assertEqual(sumaCifrelor(a), s)

    def test18(self):
        a, s = 4, 4
        self.assertEqual(sumaCifrelor(a), s)

    def test19(self):
        a, s = 9, 9
        self.assertEqual(sumaCifrelor(a), s)

    """Codul tău nu funcționează dacă a este 0."""

    def test20(self):
        a, s = 0, 0
        self.assertEqual(sumaCifrelor(a), s)


if __name__ == '__main__':
    outputFilename = "file/output.txt"
    compileFilename = "file/compile.txt"
    try:
        from implementation import sumaCifrelor
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

