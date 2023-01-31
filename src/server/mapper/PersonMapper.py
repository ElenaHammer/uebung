from server.mapper.Mapper import Mapper
from server.bo.Person import Person


class PersonMapper(Mapper):
    """Mapper-Klasse, die Customer-Objekte auf eine relationale
        Datenbank abbildet. Hierzu wird eine Reihe von Methoden zur Verfügung
        gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und
        gelöscht werden können. Das Mapping ist bidirektional. D.h. Objekte können
        in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
        """
    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Personen. Returned eine Sammlung mit Personen-Objekten,
        die sämtliche Personen repräsentieren. """
        # leere Liste
        result = []
        # Cursor-Objekt wird erstellt, welches mit der Datenbank kommuniziert
        cursor = self._cnx.cursor()
        # SQL-Abfrage an die Datenbank, um alle Datensätze aus der Tabelle "person" zu selektieren.
        cursor.execute("SELECT * from person")
        # cursor.fetchall() ruft alle Datensätze aus der Tabelle "person" in der Form von Tupel ab.
        tuples = cursor.fetchall()

        # Der for-loop iteriert durch die Tupel und erstellt für jeden ein Personen-Objekt.
        for (id, name, vorname) in tuples:
            # In jeder Iteration werden die Werte aus dem Tupel den entsprechenden Attributen
            # des Personen-Objekts zugewiesen.
            person = Person()
            person.set_id(id)
            person.set_name(name)
            person.set_vorname(vorname)
            # Jedes Personen-Objekt wird dann der 'result' Liste hinzugefügt.
            result.append(person)

        # Mit self._cnx.commit() werden die Änderungen an der Datenbank bestätigt.
        self._cnx.commit()
        # cursor.close() schließt den Cursor.
        cursor.close()
        # Die Methode gibt dann die 'result' Liste zurück, die alle Personen-Objekte enthält.
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

    def insert(self, person):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as maxid FROM person")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                person.set_id(maxid[0] + 1)
            else:
                person.set_id(1)

        command = "INSERT INTO person (id, name, vorname) " \
                  "VALUES (%s, %s, %s)"

        data = (person.get_id(),
                person.get_name(),
                person.get_vorname())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return person

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

    def delete(self, person):
        cursor = self._cnx.cursor()
        cursor.execute("DELETE FROM person WHERE id='{}'".format(person.get_id()))

        self._cnx.commit()
