# -*- coding: utf-8 -*-
# White-box unit tests - Alan Varela

"""
White-box unit testing examples.
"""

import unittest

from white_box.class_exercises import (
    DocumentEditingSystem,
    ElevatorSystem,
    TrafficLight,
    UserAuthentication,
    VendingMachine,
    authenticate_user,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_quantity_discount,
    calculate_shipping_cost,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    check_number_status,
    divide,
    get_grade,
    get_weather_advisory,
    grade_quiz,
    is_even,
    is_triangle,
    validate_credit_card,
    validate_date,
    validate_email,
    validate_login,
    validate_password,
    validate_url,
    verify_age,
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is >= A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is >= A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is >= B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")


class TestCheckNumberStatus(unittest.TestCase):
    """Tests exercise 1."""

    def test_positive(self):
        """Tests if a positive number is correctly identified."""
        self.assertEqual(check_number_status(1), "Positive")

    def test_negative(self):
        """Tests if a negative number is correctly identified."""
        self.assertEqual(check_number_status(-1), "Negative")

    def test_zero(self):
        """Tests if zero is correctly identified."""
        self.assertEqual(check_number_status(0), "Zero")


class TestValidatePassword(unittest.TestCase):
    """Tests exercise 2."""

    def test_valid(self):
        """Tests a valid password."""
        self.assertTrue(validate_password("Contr@sena1"))

    def test_too_short(self):
        """Tests a password that is too short."""
        self.assertFalse(validate_password("Co1@"))

    def test_no_uppercase(self):
        """Tests a password missing an uppercase letter."""
        self.assertFalse(validate_password("contr@sena1"))

    def test_no_lowercase(self):
        """Tests a password missing a lowercase letter."""
        self.assertFalse(validate_password("CONTR@SENA1"))

    def test_no_digit(self):
        """Tests a password missing a digit."""
        self.assertFalse(validate_password("Contr@sena"))

    def test_no_special(self):
        """Tests a password missing a special character."""
        self.assertFalse(validate_password("Contrasena1"))


class TestCalculateTotalDiscount(unittest.TestCase):
    """Tests exercise 3."""

    def test_none(self):
        """Tests the case where no discount is applied."""
        self.assertEqual(calculate_total_discount(99), 0)

    def test_10_percent(self):
        """Tests the 10 percent discount tier."""
        self.assertEqual(calculate_total_discount(200), 20)

    def test_20_percent(self):
        """Tests the 20 percent discount tier."""
        self.assertEqual(calculate_total_discount(600), 120)


class TestCalculateOrderTotal(unittest.TestCase):
    """Tests exercise 4."""

    def test_no_discount(self):
        """Tests order total calculation without quantity discount."""
        items = [{"quantity": 3, "price": 10}]
        self.assertEqual(calculate_order_total(items), 30)

    def test_5_percent_discount(self):
        """Tests order total calculation with a 5 percent discount."""
        items = [{"quantity": 8, "price": 10}]
        self.assertEqual(calculate_order_total(items), 76.0)

    def test_10_percent_discount(self):
        """Tests order total calculation with a 10 percent discount."""
        items = [{"quantity": 15, "price": 10}]
        self.assertEqual(calculate_order_total(items), 135.0)


class TestCalculateItemsShippingCost(unittest.TestCase):
    """Tests exercise 5."""

    def test_standard_light(self):
        """Tests standard shipping for a light package."""
        self.assertEqual(calculate_items_shipping_cost([{"weight": 3}], "standard"), 10)

    def test_standard_medium(self):
        """Tests standard shipping for a medium package."""
        self.assertEqual(calculate_items_shipping_cost([{"weight": 8}], "standard"), 15)

    def test_standard_heavy(self):
        """Tests standard shipping for a heavy package."""
        self.assertEqual(
            calculate_items_shipping_cost([{"weight": 12}], "standard"), 20
        )

    def test_express_light(self):
        """Tests express shipping for a light package."""
        self.assertEqual(calculate_items_shipping_cost([{"weight": 4}], "express"), 20)

    def test_express_medium(self):
        """Tests express shipping for a medium package."""
        self.assertEqual(calculate_items_shipping_cost([{"weight": 7}], "express"), 30)

    def test_express_heavy(self):
        """Tests express shipping for a heavy package."""
        self.assertEqual(calculate_items_shipping_cost([{"weight": 15}], "express"), 40)

    def test_invalid_method(self):
        """Tests that an invalid shipping method raises a ValueError."""
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost([{"weight": 5}], "VIP")


class TestValidateLogin(unittest.TestCase):
    """Tests exercise 6."""

    def test_success(self):
        """Tests successful login validation."""
        self.assertEqual(validate_login("user123", "password12"), "Login Successful")

    def test_failed_username_short(self):
        """Tests login failure due to a short username."""
        self.assertEqual(validate_login("usr", "password12"), "Login Failed")

    def test_failed_password_long(self):
        """Tests login failure due to a long password."""
        self.assertEqual(validate_login("user123", "password123456789"), "Login Failed")


class TestVerifyAge(unittest.TestCase):
    """Tests exercise 7."""

    def test_eligible(self):
        """Tests eligible age."""
        self.assertEqual(verify_age(23), "Eligible")

    def test_too_young(self):
        """Tests an age that is too young."""
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_too_old(self):
        """Tests an age that is too old."""
        self.assertEqual(verify_age(66), "Not Eligible")


class TestCategorizeProduct(unittest.TestCase):
    """Tests exercise 8."""

    def test_a(self):
        """Tests category A pricing."""
        self.assertEqual(categorize_product(30), "Category A")

    def test_b(self):
        """Tests category B pricing."""
        self.assertEqual(categorize_product(75), "Category B")

    def test_c(self):
        """Tests category C pricing."""
        self.assertEqual(categorize_product(150), "Category C")

    def test_d_upper(self):
        """Tests category D pricing (upper bound)."""
        self.assertEqual(categorize_product(250), "Category D")

    def test_d_low(self):
        """Tests category D pricing (lower bound/default)."""
        self.assertEqual(categorize_product(5), "Category D")


class TestValidateEmail(unittest.TestCase):
    """Tests exercise 9."""

    def test_valid(self):
        """Tests a valid email format."""
        self.assertEqual(validate_email("test@example.com"), "Valid Email")

    def test_invalid_missing_at(self):
        """Tests an email missing the @ symbol."""
        self.assertEqual(validate_email("testexample.com"), "Invalid Email")

    def test_invalid_missing_dot(self):
        """Tests an email missing the domain dot."""
        self.assertEqual(validate_email("test@examplecom"), "Invalid Email")

    def test_invalid_too_short(self):
        """Tests an email that is too short."""
        self.assertEqual(validate_email("a@.h"), "Invalid Email")


class TestCelsiusToFahrenheit(unittest.TestCase):
    """Tests exercise 10."""

    def test_valid(self):
        """Tests a valid temperature conversion."""
        self.assertEqual(celsius_to_fahrenheit(-9), 15.8)

    def test_invalid_low(self):
        """Tests a temperature below the valid range."""
        self.assertEqual(celsius_to_fahrenheit(-110), "Invalid Temperature")

    def test_invalid_high(self):
        """Tests a temperature above the valid range."""
        self.assertEqual(celsius_to_fahrenheit(110), "Invalid Temperature")


class TestValidateCreditCard(unittest.TestCase):
    """Tests exercise 11."""

    def test_valid(self):
        """Tests a valid credit card number."""
        self.assertEqual(validate_credit_card("12345678901234"), "Valid Card")

    def test_invalid_length(self):
        """Tests a credit card number with invalid length."""
        self.assertEqual(validate_credit_card("12345"), "Invalid Card")

    def test_invalid_characters(self):
        """Tests a credit card number containing non-digits."""
        self.assertEqual(validate_credit_card("1234567890abcd"), "Invalid Card")


class TestValidateDate(unittest.TestCase):
    """Tests exercise 12."""

    def test_valid(self):
        """Tests a valid date."""
        self.assertEqual(validate_date(2026, 2, 23), "Valid Date")

    def test_invalid_year_low(self):
        """Tests a year below the valid range."""
        self.assertEqual(validate_date(1899, 2, 23), "Invalid Date")

    def test_invalid_year_high(self):
        """Tests a year above the valid range."""
        self.assertEqual(validate_date(2101, 2, 23), "Invalid Date")

    def test_invalid_month_low(self):
        """Tests a month below the valid range."""
        self.assertEqual(validate_date(2026, 0, 23), "Invalid Date")

    def test_invalid_month_high(self):
        """Tests a month above the valid range."""
        self.assertEqual(validate_date(2026, 13, 23), "Invalid Date")

    def test_invalid_day_low(self):
        """Tests a day below the valid range."""
        self.assertEqual(validate_date(2026, 2, 0), "Invalid Date")

    def test_invalid_day_high(self):
        """Tests a day above the valid range."""
        self.assertEqual(validate_date(2026, 2, 32), "Invalid Date")


class TestCheckFlightEligibility(unittest.TestCase):
    """Tests exercise 13."""

    def test_by_age(self):
        """Tests flight eligibility based on age."""
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")

    def test_by_frequent_flyer(self):
        """Tests flight eligibility for a frequent flyer."""
        self.assertEqual(check_flight_eligibility(66, True), "Eligible to Book")

    def test_not_eligible(self):
        """Tests ineligibility for flight booking."""
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")


class TestValidateUrl(unittest.TestCase):
    """Tests exercise 14."""

    def test_http(self):
        """Tests a valid HTTP URL."""
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_https(self):
        """Tests a valid HTTPS URL."""
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_invalid_prefix(self):
        """Tests a URL with an invalid prefix."""
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")

    def test_too_long(self):
        """Tests a URL that exceeds the maximum length."""
        long_url = "http://" + "a" * 250 + ".com"
        self.assertEqual(validate_url(long_url), "Invalid URL")


class TestCalculateQuantityDiscount(unittest.TestCase):
    """Tests exercise 15."""

    def test_none(self):
        """Tests the no discount tier based on quantity."""
        self.assertEqual(calculate_quantity_discount(3), "No Discount")

    def test_5_percent(self):
        """Tests the 5 percent discount tier based on quantity."""
        self.assertEqual(calculate_quantity_discount(8), "5% Discount")

    def test_10_percent(self):
        """Tests the 10 percent discount tier based on quantity."""
        self.assertEqual(calculate_quantity_discount(15), "10% Discount")


class TestCheckFileSize(unittest.TestCase):
    """Tests exercise 16."""

    def test_valid(self):
        """Tests a valid file size."""
        self.assertEqual(check_file_size(500000), "Valid File Size")

    def test_invalid_large(self):
        """Tests a file size that is too large."""
        self.assertEqual(check_file_size(2000000), "Invalid File Size")

    def test_invalid_negative(self):
        """Tests a negative file size."""
        self.assertEqual(check_file_size(-10), "Invalid File Size")


class TestCheckLoanEligibility(unittest.TestCase):
    """Tests exercise 17."""

    def test_not_eligible(self):
        """Tests loan ineligibility due to low income."""
        self.assertEqual(check_loan_eligibility(20000, 800), "Not Eligible")

    def test_mid_income_high_score(self):
        """Tests standard loan eligibility for mid income and high score."""
        self.assertEqual(check_loan_eligibility(40000, 750), "Standard Loan")

    def test_mid_income_low_score(self):
        """Tests secured loan eligibility for mid income and low score."""
        self.assertEqual(check_loan_eligibility(40000, 650), "Secured Loan")

    def test_high_income_high_score(self):
        """Tests premium loan eligibility for high income and high score."""
        self.assertEqual(check_loan_eligibility(80000, 800), "Premium Loan")

    def test_high_income_low_score(self):
        """Tests standard loan fallback for high income and low score."""
        self.assertEqual(check_loan_eligibility(80000, 600), "Standard Loan")


class TestCalculateShippingCost(unittest.TestCase):
    """Tests exercise 18."""

    def test_cost5(self):
        """Tests the tier 1 shipping cost ($5)."""
        # weight length width height
        self.assertEqual(calculate_shipping_cost(0.5, 5, 5, 5), 5)

    def test_cost10(self):
        """Tests the tier 2 shipping cost ($10)."""
        self.assertEqual(calculate_shipping_cost(3, 20, 20, 20), 10)

    def test_fallback(self):
        """Tests the fallback shipping cost ($20)."""
        self.assertEqual(calculate_shipping_cost(10, 40, 40, 40), 20)


class TestGradeQuiz(unittest.TestCase):
    """Tests exercise 19."""

    def test_pass(self):
        """Tests quiz grading for a clear pass."""
        self.assertEqual(grade_quiz(8, 1), "Pass")

    def test_conditional_pass(self):
        """Tests quiz grading for a conditional pass."""
        self.assertEqual(grade_quiz(5, 2), "Conditional Pass")

    def test_fail(self):
        """Tests quiz grading for a fail."""
        self.assertEqual(grade_quiz(4, 5), "Fail")


class TestAuthenticateUser(unittest.TestCase):
    """Tests exercise 20."""

    def test_admin(self):
        """Tests authentication for the admin user."""
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_standard(self):
        """Tests authentication for a standard user."""
        self.assertEqual(authenticate_user("alanv", "password"), "User")

    def test_invalid(self):
        """Tests invalid authentication credentials."""
        self.assertEqual(authenticate_user("ala", "pass"), "Invalid")


class TestGetWeatherAdvisory(unittest.TestCase):
    """Tests exercise 21."""

    def test_hot(self):
        """Tests weather advisory for high temperature and humidity."""
        self.assertEqual(
            get_weather_advisory(35, 80),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_cold(self):
        """Tests weather advisory for low temperature."""
        self.assertEqual(get_weather_advisory(-5, 40), "Low Temperature. Bundle Up!")

    def test_normal(self):
        """Tests case where no specific weather advisory applies."""
        self.assertEqual(get_weather_advisory(20, 50), "No Specific Advisory")


class TestVendingMachine(unittest.TestCase):
    """Tests exercise 22"""

    def setUp(self):
        """Initializes the instance and asserts the initial state."""
        self.vending_machine = VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    def test_insert_coin_valid(self):
        """Tests inserting a coin when the machine is Ready."""
        result = self.vending_machine.insert_coin()
        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(result, "Coin Inserted. Select your drink.")

    def test_insert_coin_invalid(self):
        """Tests inserting a coin when the machine is already Dispensing."""
        self.vending_machine.state = "Dispensing"
        result = self.vending_machine.insert_coin()
        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(result, "Invalid operation in current state.")

    def test_select_drink_valid(self):
        """Tests selecting a drink when the machine is Dispensing."""
        self.vending_machine.state = "Dispensing"
        result = self.vending_machine.select_drink()
        self.assertEqual(self.vending_machine.state, "Ready")
        self.assertEqual(result, "Drink Dispensed. Thank you!")

    def test_select_drink_invalid(self):
        """Tests selecting a drink when the machine is just Ready (no coin)."""
        self.vending_machine.state = "Ready"
        result = self.vending_machine.select_drink()
        self.assertEqual(result, "Invalid operation in current state.")


class TestTrafficLight(unittest.TestCase):
    """Tests exercise 23"""

    def setUp(self):
        """Initializes the instance and asserts the initial state."""
        self.traffic_light = TrafficLight()
        self.assertEqual(self.traffic_light.state, "Red")

    def test_state_transitions(self):
        """Tests the correct cycle of state transitions."""
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Green")

        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Yellow")

        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Red")

    def test_get_current_state(self):
        """Tests get current state"""
        self.traffic_light.state = "Red"
        self.assertEqual(self.traffic_light.get_current_state(), "Red")


class TestUserAuthentication(unittest.TestCase):
    """Tests exercise 24"""

    def setUp(self):
        """Initializes the instance and asserts the initial state."""
        self.user_authentication = UserAuthentication()
        self.assertEqual(self.user_authentication.state, "Logged Out")

    def test_login_valid(self):
        """Tests successful login."""
        result = self.user_authentication.login()
        self.assertEqual(self.user_authentication.state, "Logged In")
        self.assertEqual(result, "Login successful")

    def test_login_invalid(self):
        """Tests login when already logged in."""
        self.user_authentication.state = "Logged In"
        result = self.user_authentication.login()
        self.assertEqual(result, "Invalid operation in current state")

    def test_logout_valid(self):
        """Tests successful logout."""
        self.user_authentication.state = "Logged In"
        result = self.user_authentication.logout()
        self.assertEqual(self.user_authentication.state, "Logged Out")
        self.assertEqual(result, "Logout successful")

    def test_logout_invalid(self):
        """Tests logout when already logged out."""
        self.user_authentication.state = "Logged Out"
        result = self.user_authentication.logout()
        self.assertEqual(result, "Invalid operation in current state")


class TestDocumentEditingSystem(unittest.TestCase):
    """Tests exercise 25"""

    def setUp(self):
        """Initializes the instance and asserts the initial state."""
        self.document_editing_system = DocumentEditingSystem()
        self.assertEqual(self.document_editing_system.state, "Editing")

    def test_save_valid(self):
        """Tests saving a document when editing."""
        result = self.document_editing_system.save_document()
        self.assertEqual(self.document_editing_system.state, "Saved")
        self.assertEqual(result, "Document saved successfully")

    def test_save_invalid(self):
        """Tests saving a document when already saved."""
        self.document_editing_system.state = "Saved"
        result = self.document_editing_system.save_document()
        self.assertEqual(result, "Invalid operation in current state")

    def test_edit_valid(self):
        """Tests resuming edit on a saved document."""
        self.document_editing_system.state = "Saved"
        result = self.document_editing_system.edit_document()
        self.assertEqual(result, "Editing resumed")
        self.assertEqual(self.document_editing_system.state, "Editing")

    def test_edit_invalid(self):
        """Tests editing when already editing."""
        self.document_editing_system.state = "Editing"
        result = self.document_editing_system.edit_document()
        self.assertEqual(result, "Invalid operation in current state")


class TestElevatorSystem(unittest.TestCase):
    """Tests exercise 26"""

    def setUp(self):
        """Initializes the instance and asserts the initial state."""
        self.elevator_system = ElevatorSystem()
        self.assertEqual(self.elevator_system.state, "Idle")

    def test_move_up_valid(self):
        """Tests moving up from Idle."""
        result = self.elevator_system.move_up()
        self.assertEqual(self.elevator_system.state, "Moving Up")
        self.assertEqual(result, "Elevator moving up")

    def test_move_down_valid(self):
        """Tests moving down from Idle."""
        result = self.elevator_system.move_down()
        self.assertEqual(self.elevator_system.state, "Moving Down")
        self.assertEqual(result, "Elevator moving down")

    def test_move_invalid(self):
        """Tests trying to move when already moving."""
        self.elevator_system.state = "Moving Up"
        result = self.elevator_system.move_down()
        self.assertEqual(result, "Invalid operation in current state")

    def test_stop_valid_from_up(self):
        """Tests stopping while moving up."""
        self.elevator_system.state = "Moving Up"
        result = self.elevator_system.stop()
        self.assertEqual(self.elevator_system.state, "Idle")
        self.assertEqual(result, "Elevator stopped")

    def test_stop_valid_from_down(self):
        """Tests stopping while moving down."""
        self.elevator_system.state = "Moving Down"
        result = self.elevator_system.stop()
        self.assertEqual(self.elevator_system.state, "Idle")
        self.assertEqual(result, "Elevator stopped")

    def test_stop_invalid(self):
        """Tests stopping when already idle."""
        result = self.elevator_system.stop()
        self.assertEqual(result, "Invalid operation in current state")
