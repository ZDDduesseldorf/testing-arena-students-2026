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
    assert parse_time("00:05") == 5

def test_parse_time_invalid_time(): 
    with pytest.raises(ValueError): 
        parse_time("05:")
        parse_time("05::")
        parse_time("28:05")
        parse_time("22:95")

def test_parse_measurement_regular_line():
    assert parse_measurement("Köln;14:21;21.7") == ("Köln", 861, 21.7)
    assert parse_measurement("Köln  ;  14:21;21.7 ") == ("Köln", 861, 21.7)

def test_prase_measurement_invalid_measurement(): 
    with pytest.raises(ValueError, match = "Measurement must be a string."): 
        parse_measurement([1,2,3])
    with pytest.raises(ValueError, match = "Expected exactly three fields."):
        parse_measurement("Düren; 21:31")
    with pytest.raises(ValueError, match = "City must not be empty."):
        parse_measurement("; 21:30; 20.7")
    with pytest.raises(ValueError):
        parse_measurement("Köln; 21:30; q ")

def test_filter_by_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
        ("Bonn", 900, 25.0)
    ]
    assert filter_by_temperature(measurements, 15.0, 20.0) == [
        ("Düsseldorf", 720, 18.5)
    ]
    assert filter_by_temperature(measurements, 18.5, 20.0) == [
        ("Düsseldorf", 720, 18.5)
    ]
    assert filter_by_temperature(measurements, 16.5, 18.5) == [
        ("Düsseldorf", 720, 18.5)
    ]
    with pytest.raises(ValueError):
        filter_by_temperature(measurements, 25.0, 20.0)
    assert filter_by_temperature(measurements, 15.0, 20.0) != measurements

def test_average_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("köln", 600, 30.0),
        ("Köln", 720, 20.0),
        ("Bonn", 900, 25.0),
        ("Bonn", 900, 27.0),
    ]

    assert average_temperature(measurements, "Köln") == 15.0
    assert average_temperature(measurements, "Bonn") == 26.0
    with pytest.raises(ValueError, match= "No measurements found for city."):
        average_temperature(measurements, "Paris")


def test_hottest_measurement_with_unique_maximum():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 500, 25.0),
        ("Bonn", 900, 20.0),
        ("Düren", 500, 25.0)
    ]

    measurements1 = []

    assert hottest_measurement(measurements) == ("Düsseldorf", 500, 25.0)
    with pytest.raises(TypeError):
        average_temperature(measurements1)


