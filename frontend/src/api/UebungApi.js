// Routen verweisen auf das Backend (main.py - Service Layer)
import PersonBO from "./PersonBO";

export default class UebungApi {

    // Singelton
    // Die Klasse verwendet das Singleton-Muster, um sicherzustellen, dass es immer nur eine Instanz von ihr gibt,
    // die wiederverwendet werden kann.
    static #api = null;

    // Python-Backend
    // Die Klasse enthält eine URL-Eigenschaft "uebungServerURL", die auf den Server für die Uebung-Anwendung zeigt.
    #uebungServerURL = '/uebung';

    // Person
    // Eine weitere Eigenschaft "getPersonenURL" erzeugt eine vollständige URL für den Zugriff auf die Person-Ressource.
    #getPersonenURL = () => `${this.#uebungServerURL}/person`;

    // Get die Singleton Instanz
    // Diese Methode "getAPI()" stellt eine Singleton-Instanz der Klasse "UebungApi" bereit. Der Code überprüft,
    // ob es bereits eine Instanz gibt, indem er die private Klasseneigenschaft "#api" auf "null" überprüft.
    // Falls die Eigenschaft "null" ist, wird eine neue Instanz der Klasse erstellt und in "#api" gespeichert.
    // Anschließend wird die Instanz zurückgegeben.
    static getAPI() {
        if (this.#api == null) {
            this.#api = new UebungApi();
        }
        return this.#api;
    }

    // Die Methode "fetchAdvanced" ist eine generische Methode, die auf eine URL (url) zugreift und
    // ein Promise zurückgibt, das bei erfolgreicher Abfrage den Inhalt der Antwort im JSON-Format enthält.
    #fetchAdvanced = (url, init) => fetch(url, init)
    .then(res => {
        if (!res.ok) {
            throw Error(`${res.status} ${res.statusText}`);
        }
        return res.json();
    }
    )

    // Person
    // Die Methode "getPersonen" ruft die Personen-Ressource über die URL von "getPersonenURL" auf und verarbeitet
    // die Antwort mit "fetchAdvanced". Die Antwort wird in ein JSON-Format umgewandelt und an die Klasse "PersonBO"
    // übergeben, um ein Business Object (BO) zu erzeugen. Am Ende wird das erzeugte BO als Promise zurückgegeben.
    getPersonen() {
        return this.#fetchAdvanced(this.#getPersonenURL()).then((responseJSON) => {
            let personenBO = PersonBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(personenBO);
            }
            )
        })
    }

}