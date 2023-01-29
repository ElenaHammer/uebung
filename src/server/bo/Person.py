from server.bo.BusinessObject import BusinessObject


class Person(BusinessObject):

    def __init__(self):
        super().__init__()
        self._vorname = ""  # Vorname einer Person

    def get_vorname(self):
        return self._vorname    # Auslesen des Vornamens

    def set_vorname(self, value):
        self._vorname = value   # Setzen des Vornamens

    # staticmethod, statische Methode, die aufgerufen werden kann, ohne das eine Instanz der Klasse erstellt wurde.
    @staticmethod
    def from_dict(object_dict=dict()):
        """Umwandeln eines Python dict() in eine Person()."""
        obj = Person()
        obj.set_name(object_dict["name"])
        obj.set_vorname(object_dict["vorname"])
        return obj
