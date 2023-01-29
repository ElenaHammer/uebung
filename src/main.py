# Flask importieren
from flask import Flask, redirect, url_for
# CORS importieren
from flask_cors import CORS
# RestX importieren
from flask_restx import Api, Resource, fields

from server.administration import Administraion
from server.bo.Person import Person

"""Flask instanziieren. Am Ende dieser Datei erfolgt dann erst der 'Start' von Flask."""
app = Flask(__name__)

"""
Alle Ressourcen mit dem Präfix /uebung für **Cross-Origin Resource Sharing** (CORS) freigeben.
Diese eine Zeile setzt die Installation des Package flask-cors voraus.
Im Frontend unter package.json -> "proxy": "http://127.0.0.1:5000" 
"""
CORS(app, resources=r'/uebung/*')

# API aufbauen
api = Api(app, version='1.0', title='Uebung API')

api = api.namespace('uebung')

# Folgende Strukturen werden auch verwendet, um automatisch die JSON-Antworten der API zu generieren, wenn die Daten von
# der Datenbank abgerufen werden. Wenn eine Anfrage an die API gesendet wird, wird die 'marshal_list_with' Methode
# verwendet, um die Daten in das definierte Format zu konvertieren, bevor sie an den Client gesendet werden.

# BusinessObject dient als Basisklasse, auf der die weiteren Strukturen aufsetzen.
bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Der Unique Identifier eines Business Object'),
    'name': fields.String(attribute='_name', description='Name des Objekts')
})

# Klassen die von BO erben
person = api.inherit('Person', bo, {
    'vorname': fields.String(attribute='_vorname', description='Vorname der Person')
})


# Person - Restful API Route die es ermöglicht Personen-Daten aus der Datenbank abzurufen
@api.route('/person')  # URL-Route die an den Server über eine GET-Request gesendet wird
@api.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
# erstellt eine neue Klasse PersonListOperations und erweitert die Flask-Restful "Resource" Klasse
# ermöglicht es, die RESTful-Funktionalitäten für die Personen-Daten bereitzustellen.
class PersonListOperations(Resource):
    # api.marshal_list_with() sagt dem Flask-RESTful-Framework, dass die Ausgabe der Methode eine Liste
    # von Personen-Objekten ist und dass es die Ausgabe automatisch in das JSON-Format umwandeln soll,
    # das von dem "person"-Schema definiert wurde.
    @api.marshal_list_with(person)
    # @secured
    # In der Methode get() wird ein Objekt "Administration" erstellt, welches die Methode "get_all_personen()" aufruft.
    # Diese Methode liest die Personen aus der Datenbank und speichert sie in einer Variable "person".
    def get(self):
        adm = Administraion()
        person = adm.get_all_personen()
        # Die letzte Anweisung in der Methode "get()" ist "return person", dies gibt die Liste der Personen zurück
        # und Flask-RESTful wird die Liste in das JSON-Format umwandeln, das durch das "person"-Schema definiert wurde,
        # und die Daten an den Client zurückgeben.
        return person

    # Person anlegen
    # Dieser Code definiert eine HTTP-Post-Methode für Resource PersonListOperations (von Flask-Rest-Api bereitgestellt)
    # Die @api.marshal_list_with(person, code=200) Annotation sagt der API, dass die Antwort eine Liste
    # von Personen-Objekten im JSON-Format sein soll, und das HTTP-Statuscode 200 (OK) zurückgegeben werden soll.
    @api.marshal_list_with(person, code=200)
    # Die @api.expect(person) Annotation sagt der API, dass die Anforderung ein Personen-Objekt
    # im JSON-Format enthalten soll.
    @api.expect(person)
    def post(self):
        # Die Funktion erstellt eine neue Instanz der Klasse Administration und erstellt dann eine neue Person-Instanz
        # mithilfe der Methode Person.from_dict(api.payload),
        # die aus dem übergebenen api.payload-Dictionary eine Person erstellt.
        adm = Administraion()
        proposal = Person.from_dict(api.payload)
        # RATSCHLAG Thies: Prüfen Sie stets die Referenzen auf valide Werte, bevor Sie diese verwenden!
        if proposal is not None:
            # Danach wird die Methode adm.create_person() aufgerufen, um die Person in der Datenbank zu erstellen.
            # Falls dies erfolgreich ist, wird die erstellte Person und der HTTP-Statuscode 200 zurückgegeben.
            # Falls nicht, wird nur der Statuscode 500 zurückgegeben.
            person = adm.create_person(
                proposal.get_name(),
                proposal.get_vorname())
            return person, 200
        else:
            return '', 500


# Person updaten
@api.route('/person/<int:id>')
@api.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@api.param('id', 'Die ID des Personen-Objektes')
class PersonOperations(Resource):

    # Auslesen einer bestimmten Person via ID
    @api.marshal_with(person)
    def get(self, id):
        adm = Administraion()
        person = adm.get_person_by_id(id)
        return person

"""
Nachdem wir nun sämtliche Resourcen definiert haben, die wir via REST bereitstellen möchten,
müssen nun die App auch tatsächlich zu starten.

Diese Zeile ist leider nicht Teil der Flask-Doku! In jener Doku wird von einem Start via Kommandozeile ausgegangen.
Dies ist jedoch für uns in der Entwicklungsumgebung wenig komfortabel. Deshalb kommt es also schließlich zu den 
folgenden Zeilen. 

**ACHTUNG:** Diese Zeile wird nur in der lokalen Entwicklungsumgebung ausgeführt und hat in der Cloud keine Wirkung!
"""
if __name__ == '__main__':
    app.run(debug=True)
