from server.bo.BusinessObject import BusinessObject


class Person(BusinessObject):

    def __init__(self):
        super().__init__()
        self._vorname = ""  # Vorname einer Person

    def get_vorname(self):
        return self._vorname    # Auslesen des Vornamens

    def set_vorname(self, value):
        self._vorname = value   # Setzen des Vornamens
