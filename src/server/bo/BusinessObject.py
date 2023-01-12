from abc import ABC


class BusinessObject(ABC):

    """Gemeinsame Basisklasse aller in diesem Projekt für die Umsetzung des Fachkonzepts relevanten Klassen.

    Zentrales Merkmal ist, dass jedes BusinessObject eine Nummer besitzt, die man in
    einer relationalen Datenbank auch als Primärschlüssel bezeichnen würde.
    """

    def __init__(self):
        self._id = 0    # Die eindeutige Identifikationsnummer einer Instanz dieser Klasse.
        self._name = ""     # Name eines Objekts

    def get_id(self):
        # Auslesen einer ID
        return self._id

    def set_id(self, value):
        # Setzen der ID
        self._id = value

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value
