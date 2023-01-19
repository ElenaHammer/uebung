import PersonBO from "./PersonBO";

export default class UebungApi {

    // Singelton
    static #api = null;

    // Python-Backend
    #uebungServerURL = '/uebung';

    // Person
    #getPersonenURL = () => `${this.#uebungServerURL}/person`;

    static getAPI() {
        if (this.#api == null) {
            this.#api = new UebungApi();
        }
        return this.#api;
    }

    #fetchAdvanced = (url, init) => fetch(url, init)
    .then(res => {
        if (!res.ok) {
            throw Error(`${res.status} ${res.statusText}`);
        }
        return res.json();
    }
    )

    // Person
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