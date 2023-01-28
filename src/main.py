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
"""
CORS(app, resources=r'/uebung/*')


# @app.route('/')
# def index():
#     return app.send_static_file('index.html')
#
#
# @app.errorhandler(404)
# def handle_exeption(err):
#     return redirect(url_for("index"))


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
    @api.marshal_list_with(person, code=200)
    @api.expect(person)
    def __pos__(self):
        adm = Administraion()
        proposal = Person.from_dict(api.payload)
        if proposal is not None:
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
