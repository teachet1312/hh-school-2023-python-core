from datetime import datetime


class Beer:
    def __init__(self, title=None, production_date=None) -> None:
        self.title = title
        self.production_date = production_date

    def __str__(self):
        return f'{self.title}'
