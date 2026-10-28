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
    assert parse_time("1:5") == 65

def test_parse_time_wrong_time():
    with pytest.raises(ValueError):
        assert parse_time("25:78")
    
    with pytest.raises(ValueError):
            assert parse_time("22:78")

    with pytest.raises(ValueError):
                assert parse_time("30:59")

    with pytest.raises(ValueError):
                    assert parse_time("a:20")

    with pytest.raises(ValueError):
                        assert parse_time("20:a")
    

def test_parse_time_wrong_format():
    with pytest.raises(ValueError):
        assert parse_time("2314")
        assert parse_time(2312)
        assert parse_time("23;14")
        


def test_parse_measurement_regular_line():
    assert parse_measurement("Köln;14:21;21.7") == ("Köln", 861, 21.7)

def test_parse_measurement_empty_line():
    with pytest.raises(TypeError):
        assert parse_measurement()
        assert parse_measurement('')
        assert parse_measurement(';;')
        assert parse_measurement('None; None; None')

def test_parse_measurement_wrong_format():
     with pytest.raises(ValueError):
                 assert parse_measurement("Köln, 17:23, 17.6")
     
            

def test_parse_measurement_missing_values():
    with pytest.raises(ValueError):
        assert parse_measurement("Köln; 14:21")
        assert parse_measurement("14:21; 17.6")

def test_parse_measurement_delete_whitespaces():
    assert parse_measurement("   Köln     ;14:21;21.7") == ("Köln", 861, 21.7)

def test_parse_measurement_missing_place():
     with pytest.raises(ValueError):
        assert parse_measurement("  ; 14:21; 17.6")

def test_parse_measurement_temp_to_float():
     with pytest.raises(ValueError):
             assert parse_measurement("Berlin; 14:21; String")


measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
        ("Köln", 600, 10.0),
        ("Köln", 500, 10.0),
]

def test_filter_by_temperature_regular_values():

    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
        ("Köln", 600, 10.0),
        ("Köln", 500, 10.0),
    ]

    assert filter_by_temperature(measurements, 15.0, 20.0) == [
        ("Düsseldorf", 720, 18.5)
    ]
def test_filter_by_temperature_duplicate_values():

    measurements = [
            ("Köln", 600, 10.0),
            ("Düsseldorf", 720, 18.5),
            ("Bonn", 900, 25.0),
            ("Köln", 600, 10.0),
            ("Köln", 500, 10.0),
        ]
    
    assert filter_by_temperature(measurements, 10.0, 20.0) == [
            ("Köln", 600, 10.0),
            ("Düsseldorf", 720, 18.5),
            ("Köln", 600, 10.0),
            ("Köln", 500, 10.0),
    ]

def test_filter_by_temperature_lower_bigger_than_upper():
    with pytest.raises(ValueError):
        assert filter_by_temperature(measurements, 20.0, 10.0) 

def test_filter_by_temperature_no_entries():
    assert filter_by_temperature(measurements, 100.0, 200.0) == []



def test_average_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Köln", 720, 20.0),
    ]

    assert average_temperature(measurements, "Köln") == 15.0

def test_average_temperature_no_values():
     with pytest.raises(ValueError):
          assert average_temperature(measurements, "Berlin")



def test_average_temperature_case_sensitive():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
        ("Köln", 600, 10.0),
        ("Köln", 500, 10.0),
        ("Berlin", 500, 10.0),
        ("Berlin", 500, 20.0),
        ("berlin", 500, 20.0),
]
    assert average_temperature(measurements, "Berlin") == 15.0

def test_hottest_measurement_with_unique_maximum():
    
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 25.0),
        ("Bonn", 900, 20.0),
    ]

    assert hottest_measurement(measurements) == ("Düsseldorf", 720, 25.0)



def test_hottest_measurement_several_maxima():

    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 100, 25.0),
        ("Köln", 600, 10.0),
        ("Köln", 500, 10.0),
        ("Berlin", 500, 10.0),
        ("Berlin", 200, 25.0),
        ("berlin", 500, 25.0),
]
    
    assert hottest_measurement(measurements) ==  ("Bonn", 100, 25.0)
     


def test_hottest_measurement_same_max_same_time():

    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 100, 25.0),
        ("Köln", 600, 10.0),
        ("Köln", 500, 10.0),
        ("Berlin", 500, 10.0),
        ("Berlin", 200, 25.0),
        ("berlin", 500, 25.0),
        ("Berlin", 200, 100.0),
        ("Ohio", 200, 100.0),
]
    
    assert hottest_measurement(measurements) ==  ("Berlin", 200, 100.0)



def test_hottest_measurement_no_entries():

    measurements = []
    
    with pytest.raises(ValueError):
        assert hottest_measurement(measurements)

