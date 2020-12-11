class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        status = ""
        if self.is_rented:
            status = "rented"
        else:
            status = "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {status}"

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        year = date.split('.')[2]
        month = cls.get_month(str(date.split('.')[1]))
        return cls(name, id, year, month, age_restriction)

    @classmethod
    def get_month(cls, month):
        months = {
            '01': 'January', '02': 'February', '03': 'March',
            '04': 'April', '05': 'May', '06': 'June', '07': 'July',
            '08': 'August', '09': 'September', '10': 'October',
            '11': 'November', '12': 'December'
        }
        for k, v in months.items():
            if month == k:
                return v
#
#
# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
# print(d2)
