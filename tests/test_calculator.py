"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException

@pytest.fixture
def calc():
    return Calculator()

class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self, calc):
        """Test adding two positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self, calc):
        """Test adding two negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self, calc):
        """Test adding positive and negative numbers."""
        # Arrange
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self, calc):
        """Test adding negative and positive numbers."""
        # Arrange
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self, calc):
        """Test adding positive number with zero."""
        # Arrange
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self, calc):
        """Test adding zero with positive number."""
        # Arrange
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self, calc):
        """Test adding floating point numbers."""
        # Arrange
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)
        


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self, calc):
        """Test subtracting positive numbers."""
        # Arrange
        a = 10
        b = 4
        expected = 6

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self, calc):
        """Test multiplying positive numbers."""
        # Arrange
        a = 4
        b = 5
        expected = 20

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self, calc):
        """Test dividing positive numbers."""
        # Arrange
        a = 20
        b = 5
        expected = 4

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected


class TestInvalid:
    """Tests for invalid inputs."""

    def test_add_invalid_input(self, calc):
        """Test adding with invalid input."""
        # Arrange
        a = "five"
        b = 3

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_add_value_exceeds_max(self, calc):
        """Test adding with value exceeding MAX_VALUE."""
        # Arrange
        a = 2e6  # Greater than MAX_VALUE (1e6)
        b = 1

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_add_value_below_min(self, calc):
        """Test adding with value below MIN_VALUE."""
        # Arrange
        a = -2e6  # Less than MIN_VALUE (-1e6)
        b = 1

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_divide_by_zero(self, calc):
        """Test dividing by zero raises ValueError."""
        # Arrange
        a = 10
        b = 0

        # Act & Assert
        with pytest.raises(ValueError):
            calc.divide(a, b)


class TestBoundaryValues:
    """Tests for boundary values."""

    def test_add_at_max_value(self, calc):
        """Test adding with value exactly at MAX_VALUE."""
        # Arrange - MAX_VALUE (1e6) should be valid
        a = 1e6
        b = 0
        expected = 1e6

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_at_min_value(self, calc):
        """Test adding with value exactly at MIN_VALUE."""
        # Arrange - MIN_VALUE (-1e6) should be valid
        a = -1e6
        b = 0
        expected = -1e6

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_just_over_max_value(self, calc):
        """Test adding with value just over MAX_VALUE."""
        # Arrange - Just over MAX_VALUE should be invalid
        a = 1e6 + 1
        b = 0

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_add_just_under_min_value(self, calc):
        """Test adding with value just under MIN_VALUE."""
        # Arrange - Just under MIN_VALUE should be invalid
        a = -1e6 - 1
        b = 0

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_subtract_result_verification(self, calc):
        """Test subtract returns correct result (not add)."""
        # Arrange
        a = 10
        b = 3
        expected = 7

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_multiply_result_verification(self, calc):
        """Test multiply returns correct result."""
        # Arrange
        a = 7
        b = 8
        expected = 56

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_divide_result_verification(self, calc):
        """Test divide returns correct result."""
        # Arrange
        a = 100
        b = 4
        expected = 25

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected


class TestErrorMessages:
    """Tests for verifying error messages."""

    def test_invalid_input_error_message(self, calc):
        """Test that invalid input error message is correct."""
        # Arrange
        a = "five"
        b = 3

        # Act & Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.add(a, b)
        
        error_msg = str(exc_info.value)
        assert error_msg.startswith("Input")
        assert "not a valid number" in error_msg
        assert not error_msg.endswith("XX")

    def test_out_of_range_error_message(self, calc):
        """Test that out of range error message is correct."""
        # Arrange
        a = 2e6  # Exceeds MAX_VALUE
        b = 0

        # Act & Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.add(a, b)
        
        # Check message format exactly
        error_msg = str(exc_info.value)
        assert error_msg.startswith("Input")
        assert "outside the valid range" in error_msg
        assert error_msg.endswith("]")  # Should end with ]

    def test_divide_by_zero_error_message(self, calc):
        """Test that divide by zero error message is correct."""
        # Arrange
        a = 10
        b = 0

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            calc.divide(a, b)
        
        # Exact message check
        assert str(exc_info.value) == "Cannot divide by zero"