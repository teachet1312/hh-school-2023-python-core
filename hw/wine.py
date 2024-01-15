from datetime import datetime


class Wine:
    def __init__(self, title=None, production_date=None) -> None:
        self.title = title
        production_date = [int(d) for d in production_date.split("-")] if production_date is not None else "1900-1-1"
        self.production_date = datetime(production_date[0], production_date[1], production_date[2])

    def __str__(self):
        return f'{self.title}'
