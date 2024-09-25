import pytest
from string_utils import StringUtils


# capitilize
@pytest.mark.parametrize("input, expected_output",
                         # Позитивные проверки
                         [("привет", "Привет"),
                          ("Привет", "Привет"),
                          ("МЫ идем", "Мы идем"),
                          # Негативные проверки
                          ("", ""),
                          (",./", ",./"),])

def test_capitilize(input, expected_output):
    res = StringUtils()
    assert res.capitilize(input) == expected_output


# trim
@pytest.mark.parametrize("input, expected_output",
                         # Позитивные проверки
                         [("   привет", "привет"),
                          ("   Привет", "Привет"),
                          # Негативные проверки
                          ("123", "123"),
                          ("", ""),
                          ("  ", ""),])

def test_trim_nedative(input, expected_output):
    res = StringUtils()
    assert res.trim(input) == expected_output


# to_list
@pytest.mark.parametrize("input, delimeter, result",
                         # Позитивные проверки
                         [("а,б,в,г", ",", ["а", "б", "в", "г"]),
                          ("1.2.3.4", ".", ["1", "2", "3", "4"]),
                          ("Москва:Екатеринбург:Мурманск", ":",
                          ["Москва", "Екатеринбург", "Мурманск"]),
                          # Негативные проверки
                          ("а,б,в,г", None, ["а", "б", "в", "г"]),
                          ((""), ",", []),])

def test_to_list(input, delimeter, result):
    res = StringUtils()
    if delimeter is None:
        res = res.to_list(input)
    else:
        res = res.to_list(input, delimeter)
    assert res == result


# contains
@pytest.mark.parametrize("string, symbol, result",
                         # Позитивные проверки
                         [("друг", "р", True),
                          ("варежка", "ж", True),
                          ("поляна", "я", True),
                          ("обучение", "з", False),
                          ("варенье", "д", False),
                          ("обучение", "з", False),
                          ("5864", "1", False),
                          # Негативные проверки
                          ("45678", "", False),
                          ("", "б", False),])

def test_contains(string, symbol, result):
    res = StringUtils()
    assert res.contains(string, symbol) == result


# delete_symbol
@pytest.mark.parametrize("string, symbol, result",
                         # Позитивные проверки
                         [("пряжа", "ж", "пряа"),
                          ("Пойдем гулять", "лять", "Пойдем гу"),
                          # Негативные проверки
                          ("варенье", "", "варенье"),
                          ("", "", ""),])
def test_delete_symbol(string, symbol, result):
    res = StringUtils()
    assert res.delete_symbol(string, symbol) == result


# starts_with
@pytest.mark.parametrize("string, symbol, result",
                         # Позитивные проверки
                         [("Провод", "П", True),
                          ("Провод электрический", "В", False),
                          ("провод", "П", False),
                          # Негативные проверки
                          ("", "", True),
                          ("Провод", "", False),])
def test_starts_with(string, symbol, result):
    res = StringUtils()
    assert res.starts_with(string, symbol) == result


# end_with
@pytest.mark.parametrize("string, symbol, result",
                         # Позитивные проверки
                         [("Масло", "о", True),
                          ("Масло подсолнечное", "е", True),
                          ("Масло подсолнечное", "О", False),
                          ("Масло подсолнечное", "е", True),
                          # Негативные проверки
                          ("Масло подсолнечное", "Е", False),
                          ("", "", True),
                          ("Масло подсолнечное", "", False),
                          ("  ", "е", False),])
def test_end_with(string, symbol, result):
    res = StringUtils()
    assert res.end_with(string, symbol) == result


# is_empty
@pytest.mark.parametrize("string, result",
                         # Позитивные проверки
                         [("", True),
                          ("   ", True),
                          # Негативные проверки
                          ("Крем", False),
                          ("123", False)])

def test_is_empty(string, result):
    res = StringUtils()
    assert res.is_empty(string) == result


# list_to_string
@pytest.mark.parametrize("list, joiner, result",
                         # Позитивные проверки
                         [([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
                          (["а", "б", "в"], ": ", "а: б: в"),
                          (["Анна-Мария, Иванова"], ":",
                           "Анна-Мария, Иванова"),
                          # Негативные проверки
                          ([""], ",", ""),
                          (["  ,  "], ",", "  ,  "),])

def test_list_to_string(list, joiner, result):
    res = StringUtils()
    if joiner is None:
        res = res.list_to_string(list)
    else:
        res = res.list_to_string(list, joiner)
    assert res == result
