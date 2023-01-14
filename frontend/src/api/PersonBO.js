import BO from './BO'

export default class PersonBO extends BO {

    constructor(xName, xVorname) {
        // liefert die Id und den Namen
        super(xName);
        this.vorname = xVorname;
    }

    // Vornamen setzen
    setVorname(xVorname) {
        this.vorname = xVorname;
    }

    // Vornamen holen
    getVorname() {
        return this.vorname;
    }

    // Gibt ein Array von CustomerBOs aus einer gegebenen JSON-Struktur zurück.
    static fromJSON(person) {
        let result = [];
        //wenn mehrere PersonBOs ausgegeben werden sollen
        if (Array.isArray(person)) {
            person.forEach((c) => {
                Object.setPrototypeOf(c, PersonBO.prototype);
                result.push(c);
            })
            //wenn nur ein PersonBO ausgegeben werden soll
        } else {
            let c = person;
            Object.setPrototypeOf(c, PersonBO.prototype);
            result.push(c);
        }
        return result;
    }
}