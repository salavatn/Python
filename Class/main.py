class Building():
    """Comments"""
    def __init__(self, street, city):
        self.s = street
        self.c = city

    def create(self):
        __tablename__ = "HELLO"
        print(__tablename__)
        print(f"The building is created in {self.c} on {self.s}")


house_x = Building("Молодежная", "Ишимбай")

house_x.create()
