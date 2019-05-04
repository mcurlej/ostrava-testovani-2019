from fizzbuzz import fizzbuzz


# ak je cislo delitelne 3 bez zvysku tak fizz
# ak je cislo delitelne 5 bez zvysku tak buzz
# ak je cislo delitelne 3 a 5 bez zvysku tak fizzbuzz
# inak vypiseme dane cislo


def test_return_number():
    assert fizzbuzz(1) == 1

def test_return_fizz():
    assert fizzbuzz(3) == "fizz"

def test_return_buzz():
    assert fizzbuzz(5) == "buzz"

def test_return_fizzbuzz():
    assert fizzbuzz(15) == "fizzbuzz"
