from server.mapper.Mapper import Mapper
from server.bo.Person import Person


class PersonMapper(Mapper):
    """Mapper-Klasse, die Customer-Objekte auf eine relationale
        Datenbank abbildet. Hierzu wird eine Reihe von Methoden zur Verfügung
        gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und
        gelöscht werden können. Das Mapping ist bidirektional. D.h., Objekte können
        in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
        """
    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Personen. Returned eine Sammlung mit Personen-Objekten,
        die sämtliche Personen repräsentieren. """
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from person")
        tuples = cursor.fetchall()

        for (id, name, vorname) in tuples:
            person = Person()
            person.set_id(id)
            person.set_name(name)
            person.set_vorname(vorname)
            result.append(person)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = ("SELECT id, name, vorname FROM person WHERE id={}".format(key))
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, name, vorname) = tuples[0]

            person = Person()
            person.set_id(id)
            person.set_name(name)
            person.set_vorname(vorname)
            result = person

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def insert(self, object):
        pass

    # gegebene Person aktualisieren
    def update(self, person: Person):
        cursor = self._cnx.cursor()

        command = "UPDATE person " + "SET name=%s, vorname=%s WHERE id=%s "
        data = (person.get_name(),
                person.get_vorname(),
                person.get_id())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, object):
        pass
