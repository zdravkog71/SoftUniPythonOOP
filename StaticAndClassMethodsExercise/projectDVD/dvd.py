import datetime

class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year =creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        day, month, year = date.split(".")
        year = int(year)
        month = int(month)
        day = int(day)
        creation_month = datetime.datetime(year, month, day).strftime("%B")
        return cls(name, id, year, creation_month, age_restriction)

    def __repr__(self):
        rented = None
        if self.is_rented:
            rented = "rented"
        else:
            rented = "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {rented}"