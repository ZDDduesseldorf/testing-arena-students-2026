# Plan für mögliche Fehler --> Tests schreiben

## Zu den Fällen gehören u.a.
- gewöhnliche Beispiele:

- leere Tupel:
 (,,), (), (None, None, None), (,)

- nicht vollständige Tupel/ zu viele Tupel:
('Berlin', 14:06), ('Berlin', 14:06, 17.6, HierDürfteNichtsStehen)

- falsche Reihenfolge:
(14:06, 'Berlin', 17.06)

### parse_time(time_text):

- fehlender Doppelpunkt
("1454') --> 14:45

- falsche Uhrzeiten
("25:99") --> falsche zeitangaben --> ValueError

### parse_measurement(line)

- kein String --> ValueError
- ("Köln,14:21,21.7") --> ("Köln;14:21;21.7")
- ("14:21;21.7") --> fehlender Ort
- ("Köln;14:21;21.Ü7") --> float kann nicht gebildet werden --> ValueError

### filter_by_temperature(measurements, lower, upper)

- Grenzen inklusive
- Reihenfolge bleibt nicht erhalten
- upper > lower
- neue Liste
- wenn kein Eintrage gefunden wird leere Liste wiedergeben

### average_temperature(measurements, city)

- städtenamen werden case sensitiv behandelt
- bei keinen Einträgen wird ValueError ausgelöst

### hottest_measurement(measurements)

- Haben mehrere Messungen dieselbe höchste Temperatur, wird die Messung mit der frühesten Uhrzeit zurückgegeben.
- wenn Uhrzeit und temperatur gleich, dann die erste vorkommende
- für leere Sequenz ValueError
- daten werden nicht verändert