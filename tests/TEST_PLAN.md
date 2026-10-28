# Test Plan

- gewöhnliche Beispiele,
- Grenzwerte,
- Spezialfälle,
- ungültige Eingaben,
- Seiteneffekte bzw. Veränderungen von Eingabedaten.

## `test_parse_time_regular_time`
- 0:0 -> 0
- 0 -> 0 oder Fehler
- 24 -> Fehler
- 24:00 -> Fehler
- 23:59 -> 1.440 - 1
- 12:00 -> 720
- string
- float
- -1

## `test_parse_measurement_regular_line`
- parse_measurement("Köln;14:21;") -> ("Köln", 861, 0) 
- parse_measurement("Köln;14:21) -> Fehler
- parse_measurement() -> Fehler


## `test_filter_by_temperature_regular_values`

measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
]

assert filter_by_temperature(measurements, 10.0, 25.0) == [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
]

measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
]

assert filter_by_temperature(measurements, 11.0, 26.0) == [
    ("Düsseldorf", 720, 18.5),
]

assert filter_by_temperature(measurements, 9.0, 24.0) == [
    ("Köln", 600, 10.0),
    ("Düsseldorf", 720, 18.5),
    ("Bonn", 900, 25.0),
]

## `test_hottest_measurement_with_unique_maximum`

measurements = [
        ("Düsseldorf", 720, 25.0),
        ("Düsseldorf", 721, 25.0),
    ]

assert hottest_measurement(measurements) == ("Düsseldorf", 720, 25.0)

measurements = [
        ("Düsseldorf", 720, 25.0),
        ("Aachen", 720, 25.0),
    ]

assert hottest_measurement(measurements) == ("Düsseldorf", 720, 25.0)

