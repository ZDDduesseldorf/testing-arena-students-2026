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
    assert parse_time("0:0") == 0

    assert parse_time("23:59") == 1440 - 1
    assert parse_time("12:00") == 720
    assert parse_time("12:00") != 721

    with pytest.raises(ValueError):
        assert parse_time("0")

    with pytest.raises(ValueError):
        assert parse_time("0.1")

    with pytest.raises(ValueError):
        assert parse_time("-0")

    with pytest.raises(ValueError):
        assert parse_time("-1")

    with pytest.raises(ValueError):
        assert parse_time("25:00")

    with pytest.raises(ValueError):
        assert parse_time("24:00")

    with pytest.raises(ValueError):
        assert parse_time("12:61")

    with pytest.raises(ValueError):
        assert parse_time("12:60")

    with pytest.raises(ValueError):
        assert parse_time("12:-1")

    with pytest.raises(ValueError):
        assert parse_time("12:a")

    with pytest.raises(ValueError):
        assert parse_time("a:12")

    with pytest.raises(ValueError):
        assert parse_time("halol")

    with pytest.raises(ValueError, match="Time must have HH:MM format"):
        assert parse_time("13:13:13")

def test_parse_measurement_regular_line():
    assert parse_measurement("Köln;14:21;21.7") == ("Köln", 861, 21.7)

    with pytest.raises(ValueError):
        assert parse_measurement("Köln;14:21;")

    with pytest.raises(ValueError):
        assert parse_measurement(";14:21;")

    with pytest.raises(ValueError):
        parse_measurement(";14:21;")

    assert parse_measurement("Köln;23:59;0") == ("Köln", 1439, 0)

    with pytest.raises(ValueError):
        assert parse_measurement(12)


def test_filter_by_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]

    assert filter_by_temperature(measurements, 15.0, 20.0) == [
        ("Düsseldorf", 720, 18.5)
    ]

def test_filter_by_temperature_regular_values_10_and_25():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]

    with pytest.raises(ValueError):
        assert filter_by_temperature(measurements, 10.0, 25.0) == [
            ("Köln", 600, 10.0),
            ("Düsseldorf", 720, 18.5),
            ("Bonn", 900, 25.0),
        ]

def test_filter_by_temperature_measurement_not_complete():
    measurements = [
        ("Köln", 600),
        ("Düsseldorf", 720),
        ("Bonn", 900),
    ]


    assert filter_by_temperature(measurements, 10.0, 25.0) == [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]


def test_filter_by_temperature_regular_values_9_and_26():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]

    assert filter_by_temperature(measurements, 9.0, 26.0) == [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]


def test_filter_by_temperature_regular_values_11_and_24():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]

    assert filter_by_temperature(measurements, 11.0, 24.0) == [
        ("Düsseldorf", 720, 18.5),
    ]

def test_filter_by_temperature_regular_values_ausgefiltert():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]

    assert filter_by_temperature(measurements, 26.0, 30.0) == [
    ]


def test_filter_by_temperature_regular_values_24_and_11():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]

    with pytest.raises(ValueError):
        assert filter_by_temperature(measurements, 25.0, 11.0) == [
            ("Düsseldorf", 720, 18.5),
        ]

def test_filter_by_temperature_regular_values_error():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]

    with pytest.raises(ValueError):
        assert filter_by_temperature(measurements, 100.0, 20.0) == [
            ("Düsseldorf", 720, 18.5),
        ]




def test_average_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Köln", 720, 20.0),
    ]

    assert average_temperature(measurements, "Köln") == 15.0


def test_average_temperature_one_value():
    measurements = [
        ("Köln", 600, 10.0),
    ]

    assert average_temperature(measurements, "Köln") == 10

def test_average_temperature_no_values():
    measurements = [

    ]

    with pytest.raises(ValueError):
        assert average_temperature(measurements, "Köln") == 600


def test_hottest_measurement_with_unique_maximum():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 25.0),
        ("Bonn", 900, 20.0),
    ]

    assert hottest_measurement(measurements) == ("Düsseldorf", 720, 25.0)


def test_hottest_measurement_with_two_maximum_one_earlier():
    measurements = [
        ("Köln", 600, 10.0),
        ("Bonn", 900, 10.0),
    ]

    assert hottest_measurement(measurements) == ("Köln", 600, 10.0)

def test_hottest_measurement_with_two_maximum_not_one_earlier():
    measurements = [
        ("Köln", 600, 10.0),
        ("Bonn", 900, 10.0),
    ]

    assert not hottest_measurement(measurements) == ("Bonn", 900, 10.0)


def test_hottest_measurement_with_two_maximum():
    measurements = [
        ("Düsseldorf", 720, 25.0),
        ("Aachen", 720, 25.0),
    ]

    assert hottest_measurement(measurements) == ("Düsseldorf", 720, 25.0)

def test_hottest_measurement_no_maximum():
    measurements = [

    ]

    with pytest.raises(ValueError):
        assert hottest_measurement(measurements) == ("Düsseldorf", 720, 25.0)

