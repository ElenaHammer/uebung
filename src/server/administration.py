from server.bo.Person import Person
from server.mapper.PersonMapper import PersonMapper


class Administraion(object):
    """Diese Klasse aggregiert nahezu sämtliche Applikationslogik (engl. Business Logic).

        Sie ist wie eine Spinne, die sämtliche Zusammenhänge in ihrem Netz (in unserem
        Fall die Daten der Applikation) überblickt und für einen geordneten Ablauf und
        dauerhafte Konsistenz der Daten und Abläufe sorgt.

        Die Applikationslogik findet sich in den Methoden dieser Klasse. Jede dieser
        Methoden kann als *Transaction Script* bezeichnet werden. Dieser Name
        lässt schon vermuten, dass hier analog zu Datenbanktransaktion pro
        Transaktion gleiche mehrere Teilaktionen durchgeführt werden, die das System
        von einem konsistenten Zustand in einen anderen, auch wieder konsistenten
        Zustand überführen. Wenn dies zwischenzeitig scheitern sollte, dann ist das
        jeweilige Transaction Script dafür verwantwortlich, eine Fehlerbehandlung
        durchzuführen.

        Diese Klasse steht mit einer Reihe weiterer Datentypen in Verbindung. Dies
        sind:
        - die Klassen BusinessObject und deren Subklassen,
        - die Mapper-Klassen für den DB-Zugriff.

        BankAdministration bilden nur die Server-seitige Sicht der
        Applikationslogik ab. Diese basiert vollständig auf synchronen
        Funktionsaufrufen.

        **Wichtiger Hinweis:** Diese Klasse bedient sich sogenannter
        Mapper-Klassen. Sie gehören der Datenbank-Schicht an und bilden die
        objektorientierte Sicht der Applikationslogik auf die relationale
        organisierte Datenbank ab. Zuweilen kommen "kreative" Zeitgenossen auf die
        Idee, in diesen Mappern auch Applikationslogik zu realisieren. Siehe dazu
        auch die Hinweise in der Methode zum Löschen von Customer-Objekten.
        Einzig nachvollziehbares Argument für einen solchen Ansatz ist die Steigerung
        der Performance umfangreicher Datenbankoperationen. Doch auch dieses Argument
        zieht nur dann, wenn wirklich große Datenmengen zu handhaben sind. In einem
        solchen Fall würde man jedoch eine entsprechend erweiterte Architektur realisieren,
        die wiederum sämtliche Applikationslogik in der Applikationsschicht isolieren
        würde. Also: keine Applikationslogik in die Mapper-Klassen "stecken" sondern
        dies auf die Applikationsschicht konzentrieren!

        Es gibt sicherlich noch viel mehr über diese Klasse zu schreiben. Weitere
        Infos erhalten Sie in der Lehrveranstaltung.
        """

    def __init__(self):
        pass
    
    # Person spezifische Methoden
    def get_all_personen(self):
        with PersonMapper() as mapper:
            return mapper.find_all()

    # neue Person anlegen
    def create_person(self, name, vorname):
        person = Person()
        person.set_name(name)
        person.set_vorname(vorname)
        with PersonMapper() as mapper:
            return mapper.insert(person)

    # Eine Person anhand der ID auslesen.
    def get_person_by_id(self, number):
        with PersonMapper() as mapper:
            return mapper.find_by_key(number)

    def save_person(self, person):
        with PersonMapper() as mapper:
            return mapper.update(person)

    def delete_person(self, person):
        with PersonMapper() as mapper:
            return mapper.delete(person)
