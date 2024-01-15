
from datetime import datetime
from wine import Wine
from beer import Beer
from market import Market

"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""
beers = {
    Beer("Балтика-9", "2023-08-31"),
    Beer("Жигули рязанские", "2023-11-20"),
    Beer("Spaten", "2023-12-1"),
    Beer("Жигули барные", "2023-12-17"),
    Beer("Охота крепкая", "2023-12-18"),
}
wines = {
    Wine("Саперави", "2023-11-08"),
    Wine("Каберне", "2023-12-01"),
    Wine("Брют", "2023-7-11"),
    Wine("Пакетированное", "2023-10-1"),
    Wine("Пиногринж", "2023-9-2")
}
market = Market(wines, beers)
# проверяем наличие напитка
print(market.has_drink_with_title("Балтика-9"))
print(market.has_drink_with_title("Балтика-10"))
print(market.has_drink_with_title("Саперави"))
print(market.has_drink_with_title("Шардоне"))

#получаем список всех напитков
print([str(drink) for drink in market.get_drinks_sorted_by_title()])

# получаем список напитков в диапазоне дат
print(market.get_drinks_by_production_date(datetime(2023, 9, 1),\
                                           datetime(2023, 11, 1)))