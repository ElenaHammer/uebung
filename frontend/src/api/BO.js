/* Superklasse für alle Subklassen mit ID und create Date  */

export default class BO {

    /* erstellt ein BusinessObject mit folgenden Parametern
    @param {Integer} xId 
    @param {String} xName
     */


    constructor(xId = 0, xName= "") {
        this.id = xId;  // Jedes BO wird mit einer eindeutigen ID versehen
        this.name = xName;  // Jedes BO wird mit einem Namen versehen
    }

    // Setzt die ID
    setId(xId) {
        this.id = xId;
    }

    // Gibt die ID aus
    getId() {
        return this.id;
    }

    // setzt den Namen
    setName(xName) {
        this.name = xName;
    }

    // Gibt den Namen aus
    getName() {
        return this.name;
    }

    // Gibt eine String-Darstellung dieses Objekts zurück. 
    // Dies ist für Debugging-Zwecke nützlich.
    toString() {
        let result = '';
        for (let prop in this) {
            result += prop + ': ' + this[prop] + '';
        }
        return result;
    }
}
