import unittest


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    """Funcția ta nu returnează nimic."""

    def test01(self):
        x, y, z = [], [], []
        result = concat(x, y)
        self.assertIsNot(result, None)

    def test02(self):
        x, y, z = [1, 2], [], [1, 2]
        result = concat(x, y)
        self.assertIsNot(result, None)

    def test03(self):
        x, y, z = [], [1, 2], [1, 2]
        result = concat(x, y)
        self.assertIsNot(result, None)

    def test04(self):
        x, y, z = [1, 3], [2, 4], [1, 2, 3, 4]
        result = concat(x, y)
        self.assertIsNot(result, None)

    def test05(self):
        x, y, z = [1, 2, 3, 5], [4, 6], [1, 2, 3, 4, 5, 6]
        result = concat(x, y)
        self.assertIsNot(result, None)

    def test06(self):
        x, y, z = [0, 1, 9, 10], [-1], [-1, 0, 1, 9, 10]
        result = concat(x, y)
        self.assertIsNot(result, None)

    """Funcția ta nu returnează o listă de numere întregi."""

    def test07(self):
        x, y, z = [], [], []
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            for i in range(len(result)):
                self.assertIsInstance(result[i], int)

    def test08(self):
        x, y, z = [1, 2], [], [1, 2]
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            for i in range(len(result)):
                self.assertIsInstance(result[i], int)

    def test09(self):
        x, y, z = [], [1, 2], [1, 2]
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            for i in range(len(result)):
                self.assertIsInstance(result[i], int)

    def test10(self):
        x, y, z = [1, 3], [2, 4], [1, 2, 3, 4]
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            for i in range(len(result)):
                self.assertIsInstance(result[i], int)

    def test11(self):
        x, y, z = [1, 2, 3, 5], [4, 6], [1, 2, 3, 4, 5, 6]
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            for i in range(len(result)):
                self.assertIsInstance(result[i], int)

    def test12(self):
        x, y, z = [0, 1, 9, 10], [-1], [-1, 0, 1, 9, 10]
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            for i in range(len(result)):
                self.assertIsInstance(result[i], int)

    """Funcția ta nu returnează o listă ordonată crescător."""

    def test13(self):
        x, y, z = [], [], []
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            for i in range(len(result)):
                self.assertIsInstance(result[i], int)
            if len(result) > 1:
                for i in range(len(result) - 1):
                    self.assertLessEqual(result[i], result[i + 1])

    def test14(self):
        x, y, z = [1, 2], [], [1, 2]
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            for i in range(len(result)):
                self.assertIsInstance(result[i], int)
            if len(result) > 1:
                for i in range(len(result) - 1):
                    self.assertLessEqual(result[i], result[i + 1])

    def test15(self):
        x, y, z = [], [1, 2], [1, 2]
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            for i in range(len(result)):
                self.assertIsInstance(result[i], int)
            if len(result) > 1:
                for i in range(len(result) - 1):
                    self.assertLessEqual(result[i], result[i + 1])

    def test16(self):
        x, y, z = [1, 3], [2, 4], [1, 2, 3, 4]
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            for i in range(len(result)):
                self.assertIsInstance(result[i], int)
            if len(result) > 1:
                for i in range(len(result) - 1):
                    self.assertLessEqual(result[i], result[i + 1])

    def test17(self):
        x, y, z = [1, 2, 3, 5], [4, 6], [1, 2, 3, 4, 5, 6]
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            for i in range(len(result)):
                self.assertIsInstance(result[i], int)
            if len(result) > 1:
                for i in range(len(result) - 1):
                    self.assertLessEqual(result[i], result[i + 1])

    def test18(self):
        x, y, z = [0, 1, 9, 10], [-1], [-1, 0, 1, 9, 10]
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            for i in range(len(result)):
                self.assertIsInstance(result[i], int)
            if len(result) > 1:
                for i in range(len(result) - 1):
                    self.assertLessEqual(result[i], result[i + 1])

    """Lungimea listei returnate este diferită față de suma lungimilor listelor concatenate."""

    def test19(self):
        x, y, z = [], [], []
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            self.assertEqual(len(result), len(x)+len(y))

    def test20(self):
        x, y, z = [1, 2], [], [1, 2]
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            self.assertEqual(len(result), len(x)+len(y))

    def test21(self):
        x, y, z = [], [1, 2], [1, 2]
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            self.assertEqual(len(result), len(x)+len(y))

    def test22(self):
        x, y, z = [1, 3], [2, 4], [1, 2, 3, 4]
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            self.assertEqual(len(result), len(x)+len(y))

    def test23(self):
        x, y, z = [1, 2, 3, 5], [4, 6], [1, 2, 3, 4, 5, 6]
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            self.assertEqual(len(result), len(x)+len(y))

    def test24(self):
        x, y, z = [0, 1, 9, 10], [-1], [-1, 0, 1, 9, 10]
        result = concat(x, y)
        self.assertIsNot(result, None)
        self.assertIsInstance(result, list)
        if isinstance(result, list):
            self.assertEqual(len(result), len(x)+len(y))

    """Codul tău nu funcționează pe caz general. Regândește soluția sau consultă zona de hint."""

    def test25(self):
        x, y, z = [1], [2], [1, 2]
        result = concat(x, y)
        self.assertEqual(result, z)

    def test26(self):
        x, y, z = [1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]
        result = concat(x, y)
        self.assertEqual(result, z)

    def test27(self):
        x, y, z = [1, 2, 3, 5], [4, 6], [1, 2, 3, 4, 5, 6]
        result = concat(x, y)
        self.assertEqual(result, z)

    def test28(self):
        x, y, z = [1, 2, 3], [1, 2, 3], [1, 1, 2, 2, 3, 3]
        result = concat(x, y)
        self.assertEqual(result, z)

    def test29(self):
        x, y, z = [-24, -3, -3, 1, 4, 5, 13, 27], [-5, -4, 0, 1, 1, 1, 8, 9], [-24, -5, -4, -3, -3, 0, 1, 1, 1, 1, 4, 5, 8, 9, 13, 27]
        result = concat(x, y)
        self.assertEqual(result, z)

    """Codul tău nu funcționează dacă una dintre liste este vidă."""

    def test30(self):
        x, y, z = [], [], []
        result = concat(x, y)
        self.assertEqual(result, z)

    def test31(self):
        x, y, z = [1, 2], [], [1, 2]
        result = concat(x, y)
        self.assertEqual(result, z)

    def test32(self):
        x, y, z = [], [1, 2], [1, 2]
        result = concat(x, y)
        self.assertEqual(result, z)

    """Codul tău nu funcționează dacă a doua listă conține maximul dintre cele două."""

    def test33(self):
        x, y, z = [-5, 6], [0, 7, 8], [-5, 0, 6, 7, 8]
        result = concat(x, y)
        self.assertEqual(result, z)

    """Codul tău nu funcționează dacă prima listă conține maximul dintre cele două."""

    def test34(self):
        x, y, z = [0, 1, 9, 10], [-1], [-1, 0, 1, 9, 10]
        result = concat(x, y)
        self.assertEqual(result, z)


if __name__ == '__main__':
    outputFilename = "file/output.txt"
    compileFilename = "file/compile.txt"
    try:
        from implementation import concat
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


