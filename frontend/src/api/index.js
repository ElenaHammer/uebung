//fasst alle exports aus dem api Module zusammen

export { default as UebungApi } from "./UebungApi";
export { default as PersonBO } from './PersonBO';

// Die api index.js dient als barrel-Datei (Zusammenfassungsdatei) für das Backend-API. Es exportiert die Klassen
// UebungApi und PersonBO, die Teil des Backend-Services sind, damit sie von anderen Teilen der Anwendung
// importiert werden können.

// Dies vereinfacht den Code und macht es einfacher, das Backend-API zu verwalten und zu verändern,
// da es an einer einzigen Stelle exportiert wird, anstatt an mehreren Stellen.
// Es kann auch den Überblick über die verschiedenen Klassen erleichtern, die Teil des Backend-API sind.