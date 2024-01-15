from datetime import datetime
from logger import logger


class Market:
    def __init__(self, wines: set = None, beers: set = None) -> None:
        self.wines = {wine.title: wine for wine in wines} if wines is not None else {}
        self.beers = {beer.title: beer for beer in beers} if beers is not None else {}

    @logger
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """

        return (title in self.wines) or (title in self.beers)

    @logger
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        drinks = list(self.wines.values()) + list(self.beers.values())
        drinks = sorted(drinks, key=lambda drink: drink.title)
        return drinks

    @logger
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        if from_date is None:
            from_date = datetime(1900, 1, 1)
        if to_date is None:
            to_date = datetime.now()
        drinks = []
        for drink in self.beers.values():
            if (drink.production_date > from_date) and (drink.production_date < to_date):
                drinks.append(drink)

        for drink in self.wines.values():
            if (drink.production_date > from_date) and (drink.production_date < to_date):
                drinks.append(drink)
        return drinks
