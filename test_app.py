
import pytest

from app import calculate_total, is_palindrome, get_delivery_status


def test_calculate_total():
    assert calculate_total(100, 3) == 300


def test_calculate_total_with_zero_quantity():
    assert calculate_total(100, 0) == 0


def test_calculate_total_rejects_negative_values():
    with pytest.raises(ValueError):
        calculate_total(-100, 2)


def test_palindrome():
    assert is_palindrome("madam") is True


def test_palindrome_ignores_spaces_and_case():
    assert is_palindrome("Never Odd Or Even") is True


def test_non_palindrome():
    assert is_palindrome("hello") is False


def test_delivery_status_on_time():
    assert get_delivery_status(0) == "On Time"


def test_delivery_status_at_risk():
    assert get_delivery_status(2) == "At Risk"


def test_delivery_status_delayed():
    assert get_delivery_status(5) == "Delayed"


def test_delivery_status_rejects_negative_days():
    with pytest.raises(ValueError):
        get_delivery_status(-1)
