# Flask importieren
from flask import Flask, redirect, url_for
# CORS importieren
from flask_cors import CORS
# RestX importieren
from flask_restx import Api, Resource, fields


# Flask instanziieren. Am Ende dieser Datei erfolgt dann erst der 'Start' von Flask.
app = Flask(__name__, static_folder='./build', static_url_path='/')

"""
Alle Ressourcen mit dem Präfix /uebung für **Cross-Origin Resource Sharing** (CORS) freigeben.
Diese eine Zeile setzt die Installation des Package flask-cors voraus.
"""
CORS(app, resources=r'/uebung/*')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.errorhandler(404)
def handle_exeption(err):
    return redirect(url_for("index"))

# API aufbauen
api = Api(app, version='1.0', title='Uebung API')

api = api.namespace('uebung')

# BusinessObject dient als Basisklasse, auf der die weiteren Strukturen aufsetzen.
bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Der Unique Identifier eines Business Object'),
    'name': fields.String(attribute='_name', description='Name des Objekts')
})

# Klassen die von BO erben
person = api.inherit('Person', bo, {
    'vorname': fields.String(attribute='_vorname', description='Vorname der Person')
})
