def getProjects():
    spanTag = "<span style='color:#FF8A00'>{}</span>"
    return [
        {
            "id": "1",
            "name": "Cel mai mare divizor comun",
            "requirement": "Se dau două numere întregi a și b. Se cere să se calculeze cel mai mare divizor comun al "
                           "celor două numere.",
            "testPath": "data/1/test.py",
            "implementationFilename": "data/1/implementation.py",
            "functionDefinition": "def cmmdc(a, b)",
            "input": spanTag.format("a") + " = 12<br>" + spanTag.format("b") + " = 8",
            "output": "4",
            "difficulty": "medium",
            "algorithm": "Problema se poate rezolva aplicând <b><i>algoritmul lui Euclid</i></b> cu împărțiri "
                         "repetate astfel:<br>&nbsp;&nbsp;&nbsp;&nbsp;"
                         "Cât timp " + spanTag.format("a != 0") + "<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                         "Se calculează restul împărțirii lui b la a<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "
                         "b devine a, a devine r<br>&nbsp;&nbsp;&nbsp;&nbsp;"
                         "Sfârșit cât timp<br>"
                         "Valoarea lui " + spanTag.format("b") + " va reprezenta cel mai mare divizor comun al celor două numere.",

            "tests": [
                {
                    "testId": 1,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = 12; b = 6"
                },
                {
                    "testId": 2,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = 7; b = 21"
                },
                {
                    "testId": 3,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = 25; b = 13"
                },
                {
                    "testId": 4,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = 0; b = 5"
                },
                {
                    "testId": 5,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = 6; b = 0"
                },
                {
                    "testId": 6,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = -6; b = 3"
                },
                {
                    "testId": 7,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = 12; b = -8"
                },
                {
                    "testId": 8,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = -13; b = -27"
                },
                {
                    "testId": 9,
                    "errorMessage": "Funcția ta nu returnează un număr natural.",
                    "data": "a = 12; b = 6"
                },
                {
                    "testId": 10,
                    "errorMessage": "Funcția ta nu returnează un număr natural.",
                    "data": "a = 7; b = 21"
                },
                {
                    "testId": 11,
                    "errorMessage": "Funcția ta nu returnează un număr natural.",
                    "data": "a = 25; b = 13"
                },
                {
                    "testId": 12,
                    "errorMessage": "Funcția ta nu returnează un număr natural.",
                    "data": "a = 0; b = 5"
                },
                {
                    "testId": 13,
                    "errorMessage": "Funcția ta nu returnează un număr natural.",
                    "data": "a = 6; b = 0"
                },
                {
                    "testId": 14,
                    "errorMessage": "Funcția ta nu returnează un număr natural.",
                    "data": "a = -6; b = 3"
                },
                {
                    "testId": 15,
                    "errorMessage": "Funcția ta nu returnează un număr natural.",
                    "data": "a = 12; b = -8"
                },
                {
                    "testId": 16,
                    "errorMessage": "Funcția ta nu returnează un număr natural.",
                    "data": "a = -13; b = -27"
                },
                {
                    "testId": 17,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "a = 12; b = 6"
                },
                {
                    "testId": 18,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "a = 21; b = 7"
                },
                {
                    "testId": 19,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "a = 6; b = 12"
                },
                {
                    "testId": 20,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "a = 7; b = 21"
                },
                {
                    "testId": 21,
                    "errorMessage": "Codul tău nu funcționează dacă numerele sunt negative.",
                    "data": "a = -6; b = 3"
                },
                {
                    "testId": 22,
                    "errorMessage": "Codul tău nu funcționează dacă numerele sunt negative.",
                    "data": "a = 5; b = -25"
                },
                {
                    "testId": 23,
                    "errorMessage": "Codul tău nu funcționează dacă numerele sunt negative.",
                    "data": "a = -3; b = -6"
                },
                {
                    "testId": 24,
                    "errorMessage": "Codul tău nu funcționează dacă numerele sunt negative.",
                    "data": "a = -13; b = -27"
                },
                {
                    "testId": 25,
                    "errorMessage": "Codul tău nu funcționează dacă a este 0.",
                    "data": "a = 0; b = 5"
                },
                {
                    "testId": 26,
                    "errorMessage": "Codul tău nu funcționează dacă a este 0.",
                    "data": "a = 0; b = 6"
                },
                {
                    "testId": 27,
                    "errorMessage": "Codul tău nu funcționează dacă a este 0.",
                    "data": "a = 0; b = -5"
                },
                {
                    "testId": 28,
                    "errorMessage": "Codul tău nu funcționează dacă a este 0.",
                    "data": "a = 0; b = -6"
                },
                {
                    "testId": 29,
                    "errorMessage": "Codul tău nu funcționează dacă b este 0.",
                    "data": "a = 0; b = 0"
                },
                {
                    "testId": 30,
                    "errorMessage": "Codul tău nu funcționează dacă b este 0.",
                    "data": "a = 5; b = 0"
                },
                {
                    "testId": 31,
                    "errorMessage": "Codul tău nu funcționează dacă b este 0.",
                    "data": "a = 6; b = 0"
                },
                {
                    "testId": 32,
                    "errorMessage": "Codul tău nu funcționează dacă b este 0.",
                    "data": "a = -5; b = 0"
                },
                {
                    "testId": 33,
                    "errorMessage": "Codul tău nu funcționează dacă b este 0.",
                    "data": "a = -6; b = 0"
                },
                {
                    "testId": 34,
                    "errorMessage": "Codul tău nu funcționează dacă cele două numere sunt prime între ele.",
                    "data": "a = 13; b = 27"
                },
                {
                    "testId": 35,
                    "errorMessage": "Codul tău nu funcționează dacă cele două numere sunt prime între ele.",
                    "data": "a = 3; b = 1"
                },
                {
                    "testId": 36,
                    "errorMessage": "Codul tău nu funcționează dacă cele două numere sunt egale.",
                    "data": "a = 6; b = 6"
                }
            ]
        },
        {
            "id": "2",
            "name": "Concatenarea a două liste",
            "requirement": "Se dau două liste de numere întregi ordonate crescător x și y. Se cere să se concateneze "
                           "cele două liste într-o altă listă ordonată crescător.",
            "testPath": "data/2/test.py",
            "implementationFilename": "data/2/implementation.py",
            "functionDefinition": "def concat(x, y)",
            "input": spanTag.format("x") + " = [1, 2, 4]<br>" + spanTag.format("y") + " = [1, 3, 5, 10]",
            "output": "[1, 1, 2, 3, 4, 5, 10]",
            "difficulty": "hard",
            "algorithm": "Problema se poate rezolva aplicând următorul algoritm:<br>&nbsp;&nbsp;&nbsp;&nbsp;"
                         "Cât timp " + spanTag.format("x != 0 ") + " și " + spanTag.format("y != 0") + "<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                         "Se compară primul element din ambele liste<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                         "Se adaugă minimul în rezultat și se elimină din lista curentă<br>&nbsp;&nbsp;&nbsp;&nbsp;"
                         "Sfârșit cât timp<br>&nbsp;&nbsp;&nbsp;&nbsp;"
                         "Dacă listele mai conțin elemente<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                         "Se adaugă elementele rămase în rezultat<br>&nbsp;&nbsp;&nbsp;&nbsp;"
                         "Sfârșit dacă",

            "tests": [
                {
                    "testId": 1,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "x = []; y = []"
                },
                {
                    "testId": 2,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "x = [1, 2]; y = []"
                },
                {
                    "testId": 3,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "x = []; y = [1, 2]"
                },
                {
                    "testId": 4,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "x = [1, 3]; y = [2, 4]"
                },
                {
                    "testId": 5,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "x = [1, 2, 3, 5]; y = [4, 6]"
                },
                {
                    "testId": 6,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "x = [0, 1, 9, 10]; y = [-1]"
                },
                {
                    "testId": 7,
                    "errorMessage": "Funcția ta nu returnează o listă de numere întregi.",
                    "data": "x = []; y = []"
                },
                {
                    "testId": 8,
                    "errorMessage": "Funcția ta nu returnează o listă de numere întregi.",
                    "data": "x = [1, 2]; y = []"
                },
                {
                    "testId": 9,
                    "errorMessage": "Funcția ta nu returnează o listă de numere întregi.",
                    "data": "x = []; y = [1, 2]"
                },
                {
                    "testId": 10,
                    "errorMessage": "Funcția ta nu returnează o listă de numere întregi.",
                    "data": "x = [1, 3]; y = [2, 4]"
                },
                {
                    "testId": 11,
                    "errorMessage": "Funcția ta nu returnează o listă de numere întregi.",
                    "data": "x = [1, 2, 3, 5]; y = [4, 6]"
                },
                {
                    "testId": 12,
                    "errorMessage": "Funcția ta nu returnează o listă de numere întregi.",
                    "data": "x = [0, 1, 9, 10]; y = [-1]"
                },
                {
                    "testId": 13,
                    "errorMessage": "Funcția ta nu returnează o listă ordonată crescător.",
                    "data": "x = []; y = []"
                },
                {
                    "testId": 14,
                    "errorMessage": "Funcția ta nu returnează o listă ordonată crescător.",
                    "data": "x = [1, 2]; y = []"
                },
                {
                    "testId": 15,
                    "errorMessage": "Funcția ta nu returnează o listă ordonată crescător.",
                    "data": "x = []; y = [1, 2]"
                },
                {
                    "testId": 16,
                    "errorMessage": "Funcția ta nu returnează o listă ordonată crescător.",
                    "data": "x = [1, 3]; y = [2, 4]"
                },
                {
                    "testId": 17,
                    "errorMessage": "Funcția ta nu returnează o listă ordonată crescător.",
                    "data": "x = [1, 2, 3, 5]; y = [4, 6]"
                },
                {
                    "testId": 18,
                    "errorMessage": "Funcția ta nu returnează o listă ordonată crescător.",
                    "data": "x = [0, 1, 9, 10]; y = [-1]"
                },
                {
                    "testId": 19,
                    "errorMessage": "Lungimea listei returnate este diferită față de suma lungimilor listelor concatenate.",
                    "data": "x = []; y = []"
                },
                {
                    "testId": 20,
                    "errorMessage": "Lungimea listei returnate este diferită față de suma lungimilor listelor concatenate.",
                    "data": "x = [1, 2]; y = []"
                },
                {
                    "testId": 21,
                    "errorMessage": "Lungimea listei returnate este diferită față de suma lungimilor listelor concatenate.",
                    "data": "x = []; y = [1, 2]"
                },
                {
                    "testId": 22,
                    "errorMessage": "Lungimea listei returnate este diferită față de suma lungimilor listelor concatenate.",
                    "data": "x = [1, 3]; y = [2, 4]"
                },
                {
                    "testId": 23,
                    "errorMessage": "Lungimea listei returnate este diferită față de suma lungimilor listelor concatenate.",
                    "data": "x = [1, 2, 3, 5]; y = [4, 6]"
                },
                {
                    "testId": 24,
                    "errorMessage": "Lungimea listei returnate este diferită față de suma lungimilor listelor concatenate.",
                    "data": "x = [0, 1, 9, 10]; y = [-1]"
                },
                {
                    "testId": 25,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "x = [1]; y = [2]"
                },
                {
                    "testId": 26,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "x = [1, 3, 5]; y = [2, 4, 6]"
                },
                {
                    "testId": 27,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "x = [1, 2, 3, 5]; y = [4, 6]"
                },
                {
                    "testId": 28,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "x = [1, 2, 3]; y = [1, 2, 3]"
                },
                {
                    "testId": 29,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "x = [-24, -3, -3, 1, 4, 5, 13, 27]; y = [-5, -4, 0, 1, 1, 1, 8, 9]"
                },
                {
                    "testId": 30,
                    "errorMessage": "Codul tău nu funcționează dacă una dintre liste este vidă.",
                    "data": "x = []; y = []"
                },
                {
                    "testId": 31,
                    "errorMessage": "Codul tău nu funcționează dacă una dintre liste este vidă.",
                    "data": "x = [1, 2]; y = []"
                },
                {
                    "testId": 32,
                    "errorMessage": "Codul tău nu funcționează dacă una dintre liste este vidă.",
                    "data": "x = []; y = [1, 2]"
                },
                {
                    "testId": 33,
                    "errorMessage": "Codul tău nu funcționează dacă a doua listă conține maximul dintre cele două.",
                    "data": "x = [-5, 6]; y = [0, 7, 8]"
                },
                {
                    "testId": 34,
                    "errorMessage": "Codul tău nu funcționează dacă prima listă conține maximul dintre cele două.",
                    "data": "x = [0, 1, 9, 10]; y = [-1]"
                }
            ]
        },
        {
            "id": "3",
            "name": "Suma cifrelor unui număr",
            "requirement": "Se dă un număr natural a. Se cere să se calculeze suma cifrelor numărului respectiv.",
            "testPath": "data/3/test.py",
            "implementationFilename": "data/3/implementation.py",
            "functionDefinition": "def sumaCifrelor(a)",
            "input": spanTag.format("a") + " = 137",
            "output": "11",
            "difficulty": "easy",
            "algorithm": "Problema se poate rezolva aplicând următorul algoritm:<br>&nbsp;&nbsp;&nbsp;&nbsp;"
                         "Cât timp " + spanTag.format("a > 0 ") + "<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                         "Se calculează ultima cifră a lui a<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                         "Se adaugă la contor<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
                         "Se elimină ultima cifră din număr",
            "tests": [
                {
                    "testId": 1,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = 0"
                },
                {
                    "testId": 2,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = 1"
                },
                {
                    "testId": 3,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = 9"
                },
                {
                    "testId": 4,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = 99"
                },
                {
                    "testId": 5,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = 102"
                },
                {
                    "testId": 6,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = 123456"
                },
                {
                    "testId": 7,
                    "errorMessage": "Funcția ta nu returnează un număr natural.",
                    "data": "a = 0"
                },
                {
                    "testId": 8,
                    "errorMessage": "Funcția ta nu returnează un număr natural.",
                    "data": "a = 1"
                },
                {
                    "testId": 9,
                    "errorMessage": "Funcția ta nu returnează un număr natural.",
                    "data": "a = 9"
                },
                {
                    "testId": 10,
                    "errorMessage": "Funcția ta nu returnează un număr natural.",
                    "data": "a = 99"
                },
                {
                    "testId": 11,
                    "errorMessage": "Funcția ta nu returnează un număr natural.",
                    "data": "a = 102"
                },
                {
                    "testId": 12,
                    "errorMessage": "Funcția ta nu returnează un număr natural.",
                    "data": "a = 123456"
                },
                {
                    "testId": 13,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "a = 99"
                },
                {
                    "testId": 14,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "a = 102"
                },
                {
                    "testId": 15,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "a = 1000"
                },
                {
                    "testId": 16,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "a = 12345"
                },
                {
                    "testId": 17,
                    "errorMessage": "Codul tău nu funcționează pentru numere de o singură cifră.",
                    "data": "a = 1"
                },
                {
                    "testId": 18,
                    "errorMessage": "Codul tău nu funcționează pentru numere de o singură cifră.",
                    "data": "a = 4"
                },
                {
                    "testId": 19,
                    "errorMessage": "Codul tău nu funcționează pentru numere de o singură cifră.",
                    "data": "a = 9"
                },
                {
                    "testId": 20,
                    "errorMessage": "Codul tău nu funcționează dacă a este 0.",
                    "data": "a = 0"
                }
            ]
        },
        {
            "id": "4",
            "name": "Suma a două numere",
            "requirement": "Se dau două numere întregi a și b. Se cere să se calculeze suma celor două numere.",
            "testPath": "data/demo/test.py",
            "implementationFilename": "data/demo/implementation.py",
            "functionDefinition": "def suma(a, b)",
            "input": spanTag.format("a") + " = 2<br>" + spanTag.format("b") + " = 3",
            "output": "5",
            "difficulty": "easy",
            "algorithm": "Problema se poate rezolva aplicând următorul algoritm:<br>&nbsp;&nbsp;&nbsp;&nbsp;"
                         "Se adună " + spanTag.format("a") + " la " + spanTag.format("b"),
            "tests": [
                {
                    "testId": 1,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = 0; b = 5"
                },
                {
                    "testId": 2,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = 5; b = 0"
                },
                {
                    "testId": 3,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = 3; b = 4"
                },
                {
                    "testId": 4,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = -5; b = 9"
                },
                {
                    "testId": 5,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = 10; b = -10"
                },
                {
                    "testId": 6,
                    "errorMessage": "Funcția ta nu returnează nimic.",
                    "data": "a = -5; b = -5"
                },
                {
                    "testId": 7,
                    "errorMessage": "Funcția ta nu returnează un număr întreg.",
                    "data": "a = 0; b = 5"
                },
                {
                    "testId": 8,
                    "errorMessage": "Funcția ta nu returnează un număr întreg.",
                    "data": "a = 5; b = 0"
                },
                {
                    "testId": 9,
                    "errorMessage": "Funcția ta nu returnează un număr întreg.",
                    "data": "a = 3; b = 4"
                },
                {
                    "testId": 10,
                    "errorMessage": "Funcția ta nu returnează un număr întreg.",
                    "data": "a = -5; b = 9"
                },
                {
                    "testId": 11,
                    "errorMessage": "Funcția ta nu returnează un număr întreg.",
                    "data": "a = 10; b = -10"
                },
                {
                    "testId": 12,
                    "errorMessage": "Funcția ta nu returnează un număr întreg.",
                    "data": "a = -5; b = -5"
                },
                {
                    "testId": 13,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "a = 0; b = 5"
                },
                {
                    "testId": 14,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "a = 5; b = 0"
                },
                {
                    "testId": 15,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "a = 3; b = 4"
                },
                {
                    "testId": 16,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "a = -5; b = 9"
                },
                {
                    "testId": 17,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "a = 10; b = -10"
                },
                {
                    "testId": 18,
                    "errorMessage": "Codul tău nu funcționează nici pe cel mai banal test. Regândește soluția sau "
                                    "consultă tabul Algoritm pentru a ți se sugera un algoritm general de rezolvare. ",
                    "data": "a = -5; b = -5"
                }
            ]
        }
    ]
