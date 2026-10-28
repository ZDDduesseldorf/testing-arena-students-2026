"""Starter tests for the weather module.

These tests deliberately cover only ordinary examples. They show how pytest works,
but they are not a sufficient test suite for the specification in SPECIFICATION.md.
"""

import pytest
from weather import (
    average_temperature,
    filter_by_temperature,
    hottest_measurement,
    parse_measurement,
    parse_time,
)


def test_parse_time_regular_time():
    assert parse_time("14:21") == 861
    assert parse_time("00:00") == 0
    assert parse_time ("012:00") == 720
    assert parse_time ("01:1") == 61

def test_parse_time_Errors():
    # len(parts) != 2
    with pytest.raises(ValueError, match="Time must have HH:MM format."):
        parse_time("23:45:94")

    # not hour_text.isdigit() or not minute_text.isdigit()
    with pytest.raises(ValueError, match="Hour and minute must be numeric."):
        parse_time("Five:7")
        parse_time("2:Six")
        parse_time("Five:Six")

    # hour < 0 or hour > 23
    with pytest.raises(ValueError, match="Hour must be between 0 and 23."):
            # parse_time("-5:7") --> isdigit() = False
            parse_time("24:9")

    # minute < 0 or minute > 59
    with pytest.raises(ValueError, match="Minute must be between 0 and 59."):
            # parse_time("15:-7") --> isdigit() = False
            parse_time("16:69")



def test_parse_measurement_regular_line():
    assert parse_measurement("Köln;14:21;21.7") == ("Köln", 861, 21.7)
    assert parse_measurement("Köln;14:21;-21.7") == ("Köln", 861, -21.7)

def test_parse_measurement_Errors():
     # not isinstance(line, str)
    with pytest.raises(ValueError, match="Measurement must be a string."):
        parse_measurement(5)
        parse_measurement(["Helloo"])

    # len(parts) != 3
    with pytest.raises(ValueError, match="Expected exactly three fields."):
        parse_measurement("5; 6; 7; 6")
        parse_measurement("Helloo")

    # city == ""
    with pytest.raises(ValueError, match="City must not be empty."):
        parse_measurement("; 6; 7")

    # temperature = float(temperature_text)
    with pytest.raises(ValueError, match="Temperature must be numeric."):
        parse_measurement("Fünf; 6:9; zwei")


def test_filter_by_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]

    assert filter_by_temperature(measurements, 15.0, 20.0) == [
        ("Düsseldorf", 720, 18.5)
    ]

    assert len(filter_by_temperature(measurements, 0.0, 100.0)) == len(measurements)

def test_filter_by_temperature_Errors():
     # lower > upper
    with pytest.raises(ValueError, match="lower must not be greater than upper."):
        filter_by_temperature(5, 7, 0)
        filter_by_temperature(5, 0, 0)


def test_average_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Köln", 720, 20.0),
        ("köln", 720, 30.0),
    ]

    assert average_temperature(measurements, "Köln") == 15.0
    assert average_temperature(measurements, "Köln") != average_temperature(measurements, "köln")

def test_average_temperature_Errors():
    with pytest.raises(ValueError, match="No measurements found for city."):
        average_temperature(
            [
                ("Köln", 600, 10.0),
                ("Düsseldorf", 720, 25.0),
                ("Bonn", 900, 20.0),
            ],
            "Hallo",
        )



def test_hottest_measurement_with_unique_maximum():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 25.0),
        ("Bonn", 900, 20.0),
    ]

    assert hottest_measurement(measurements) == ("Düsseldorf", 720, 25.0)

def test_hottest_measurement_Errors():
    # len(measurements) == 0
    with pytest.raises(ValueError, match="No measurements available."):
        hottest_measurement([])
