# -*- coding: utf-8 -*-
# White-box integration tests - Alan Varela
# 2 Marzo

"""
White-box integration tests examples.
"""

import unittest
from unittest.mock import patch

from white_box.book_store import Book, BookStore, main
from white_box.class_exercises import BankAccount, BankingSystem, Product, ShoppingCart


# Ejercicio 27
class TestBankAccount(unittest.TestCase):
    """Tests exercise 27 - BankAccount"""

    def test_bank_account_creation_and_view(self):
        """Tests the initialization and view_account method."""
        account = BankAccount("user123", 1000)
        self.assertEqual(account.account_number, "user123")
        self.assertEqual(account.balance, 1000)

    @patch("builtins.print")
    def test_view_account_print_mock(self, mock_print):
        """Tests the view account print method."""
        account = BankAccount("user123", 1000)
        account.view_account()

        mock_print.assert_any_call("The account user123 has a balance of 1000")


class TestBankingSystem(unittest.TestCase):
    """Tests exercise 27 - BankingSystem"""

    def setUp(self):
        """Initializes the instance and asserts the initial state."""
        self.banking_system = BankingSystem()
        self.assertEqual(len(self.banking_system.logged_in_users), 0)

    # Authentication

    @patch("builtins.print")
    def test_authenticate_success(self, mock_print):
        """Tests a successful initial authentication."""
        result = self.banking_system.authenticate("user123", "pass123")

        self.assertTrue(result)
        self.assertIn("user123", self.banking_system.logged_in_users)
        mock_print.assert_any_call("User user123 authenticated successfully.")

    @patch("builtins.print")
    def test_authenticate_already_logged_in(self, mock_print):
        """Tests authenticating a user that is already logged in."""
        self.banking_system.authenticate("user123", "pass123")
        result = self.banking_system.authenticate("user123", "pass123")

        self.assertFalse(result)
        mock_print.assert_any_call("User already logged in.")

    @patch("builtins.print")
    def test_authenticate_invalid_credentials(self, mock_print):
        """Tests authentication failure with wrong password."""
        result = self.banking_system.authenticate("user123", "pass")

        self.assertFalse(result)
        self.assertNotIn("user123", self.banking_system.logged_in_users)
        mock_print.assert_any_call("Authentication failed.")

    # Transfers

    @patch("builtins.print")
    def test_transfer_without_authentication(self, mock_print):
        """Tests that a transfer fails if the sender is not logged in."""
        result = self.banking_system.transfer_money(
            "user123", "user456", 100, "regular"
        )

        self.assertFalse(result)
        mock_print.assert_any_call("Sender not authenticated.")

    @patch("builtins.print")
    def test_transfer_regular_success(self, mock_print):
        """Tests a successful regular transfer after authenticating."""
        self.banking_system.authenticate("user123", "pass123")
        # 510
        result = self.banking_system.transfer_money(
            "user123", "user456", 500, "regular"
        )

        self.assertTrue(result)
        mock_print.assert_any_call(
            "Money transfer of $500 (regular transfer) from "
            "user123 to user456 processed successfully."
        )

    @patch("builtins.print")
    def test_transfer_express_success(self, mock_print):
        """Tests a successful express transfer after authenticating."""
        self.banking_system.authenticate("user123", "pass123")
        # 525
        result = self.banking_system.transfer_money(
            "user123", "user456", 500, "express"
        )

        self.assertTrue(result)
        mock_print.assert_any_call(
            "Money transfer of $500 (express transfer) from user123 "
            "to user456 processed successfully."
        )

    @patch("builtins.print")
    def test_transfer_scheduled_success(self, mock_print):
        """Tests a successful scheduled transfer after authenticating."""
        self.banking_system.authenticate("user123", "pass123")
        # 505
        result = self.banking_system.transfer_money(
            "user123", "user456", 500, "scheduled"
        )

        self.assertTrue(result)
        mock_print.assert_any_call(
            "Money transfer of $500 (scheduled transfer) from"
            " user123 to user456 processed successfully."
        )

    @patch("builtins.print")
    def test_transfer_invalid_transaction_type(self, mock_print):
        """Tests a transfer failure due to an unrecognized transaction type."""
        self.banking_system.authenticate("user123", "pass123")
        result = self.banking_system.transfer_money("user123", "user456", 100, "crypto")

        self.assertFalse(result)
        mock_print.assert_any_call("Invalid transaction type.")

    @patch("builtins.print")
    def test_transfer_insufficient_funds(self, mock_print):
        """Tests a transfer failure due to insufficient funds (amount + fee > balance)."""
        self.banking_system.authenticate("user123", "pass123")
        # 1020
        result = self.banking_system.transfer_money(
            "user123", "user456", 1000, "regular"
        )

        self.assertFalse(result)
        mock_print.assert_any_call("Insufficient funds.")


# Ejercicio 28


class TestProduct(unittest.TestCase):
    """Tests exercise 28 - Product class"""

    def test_product_creation(self):
        """Tests the initialization of a product."""
        product = Product("Shirt", 1500)
        self.assertEqual(product.name, "Shirt")
        self.assertEqual(product.price, 1500)

    @patch("builtins.print")
    def test_view_product(self, mock_print):
        """Tests viewing a product and its printed output."""
        product = Product("Apple", 25)
        result = product.view_product()

        expected_msg = "The product Apple has a price of 25"
        mock_print.assert_called_with(expected_msg)  # print
        self.assertEqual(result, expected_msg)  # return


class TestShoppingCart(unittest.TestCase):
    """Tests exercise 28 - ShoppingCart"""

    def setUp(self):
        """Initializes the cart and some mock products for testing."""
        self.cart = ShoppingCart()
        self.apple = Product("Apple", 2)
        self.banana = Product("Banana", 3)

    def test_add_new_product(self):
        """Tests adding a new product to an empty cart."""
        self.cart.add_product(self.apple, 5)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["product"], self.apple)
        self.assertEqual(self.cart.items[0]["quantity"], 5)

    def test_add_existing_product(self):
        """Tests adding a product that is already in the cart (should update quantity)."""
        self.cart.add_product(self.apple, 2)
        self.cart.add_product(self.apple, 3)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 5)

    def test_remove_product_partial(self):
        """Tests removing a portion of a product's quantity."""
        self.cart.add_product(self.apple, 5)
        self.cart.remove_product(self.apple, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 3)

    def test_remove_product_full(self):
        """Tests removing the exact amount of a product's quantity (should remove the item)."""
        self.cart.add_product(self.apple, 2)
        self.cart.remove_product(self.apple, 2)
        self.assertEqual(len(self.cart.items), 0)

    def test_remove_product_more_than_exists(self):
        """Tests removing more quantity than what exists in the cart (should remove the item)."""
        self.cart.add_product(self.apple, 2)
        self.cart.remove_product(self.apple, 5)
        self.assertEqual(len(self.cart.items), 0)

    def test_remove_non_existent_product(self):
        """Tests trying to remove a product that is not in the cart."""
        self.cart.add_product(self.apple, 2)
        self.cart.remove_product(self.banana, 1)
        self.assertEqual(len(self.cart.items), 1)

    @patch("builtins.print")
    def test_view_cart(self, mock_print):
        """Tests viewing the cart contents prints correctly."""
        self.cart.add_product(self.apple, 2)  # 4
        self.cart.add_product(self.banana, 1)  # 3
        self.cart.view_cart()

        mock_print.assert_any_call("2 x Apple - $4")
        mock_print.assert_any_call("1 x Banana - $3")

    @patch("builtins.print")
    def test_checkout(self, mock_print):
        """Tests the checkout calculation and print outputs."""
        self.cart.add_product(self.apple, 2)  # 4
        self.cart.add_product(self.banana, 3)  # 9
        self.cart.checkout()

        mock_print.assert_any_call("Total: $13")
        mock_print.assert_any_call("Checkout completed. Thank you for shopping!")


# Book store


class TestBook(unittest.TestCase):
    """Tests exercise Book class."""

    def test_book_initialization(self):
        """Tests the initialization of a Book."""
        book = Book("1984", "George", 500, 2)
        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "George")
        self.assertEqual(book.price, 500)
        self.assertEqual(book.quantity, 2)

    @patch("builtins.print")
    def test_display(self, mock_print):
        """Tests the display method prints the correct format."""
        book = Book("Flash", "Alan", 20.50, 5)
        book.display()

        mock_print.assert_any_call("Title: Flash")
        mock_print.assert_any_call("Author: Alan")
        mock_print.assert_any_call("Price: $20.5")
        mock_print.assert_any_call("Quantity: 5")


class TestBookStore(unittest.TestCase):
    """Tests exercise BookStore class."""

    def setUp(self):
        """Initializes a BookStore and mock books for testing."""
        self.store = BookStore()
        self.book1 = Book("El Hobbit", "J.R.R. Tolkien", 300, 3)
        self.book2 = Book("Fundacion", "Isaac Asimov", 250, 2)

    @patch("builtins.print")
    def test_add_book(self, mock_print):
        """Tests adding a book to the store."""
        self.store.add_book(self.book1)

        self.assertEqual(len(self.store.books), 1)
        self.assertEqual(self.store.books[0], self.book1)
        mock_print.assert_any_call("Book 'El Hobbit' added to the store.")

    @patch("builtins.print")
    def test_display_books_empty(self, mock_print):
        """Tests displaying books when the store is empty."""
        self.store.display_books()
        mock_print.assert_any_call("No books in the store.")

    @patch("builtins.print")
    def test_display_books_with_inventory(self, mock_print):
        """Tests displaying books when there is inventory."""
        self.store.add_book(self.book1)
        self.store.add_book(self.book2)
        self.store.display_books()

        mock_print.assert_any_call("Books available in the store:")
        mock_print.assert_any_call("Title: El Hobbit")
        mock_print.assert_any_call("Title: Fundacion")

    @patch("builtins.print")
    def test_search_book_found(self, mock_print):
        """Tests searching for a book that exists (case-insensitive)."""
        self.store.add_book(self.book1)
        self.store.search_book("el hobbit")  # Testing lowercase

        mock_print.assert_any_call("Found 1 book(s) with title 'el hobbit':")
        mock_print.assert_any_call("Title: El Hobbit")

    @patch("builtins.print")
    def test_search_book_not_found(self, mock_print):
        """Tests searching for a book that does not exist."""
        self.store.add_book(self.book1)
        self.store.search_book("Harry Potter")

        mock_print.assert_any_call("No book found with title 'Harry Potter'.")


class TestBookStoreMain(unittest.TestCase):
    """Tests the interactive main loop."""

    @patch("builtins.print")
    @patch("builtins.input")
    def test_main_exit_immediately(self, mock_input, mock_print):
        """Tests selecting option 4 directly exits the loop."""
        mock_input.side_effect = ["4"]

        main()

        mock_print.assert_any_call("Exiting...")

    @patch("builtins.print")
    @patch("builtins.input")
    def test_main_invalid_choice_then_exit(self, mock_input, mock_print):
        """Tests entering an invalid choice, then exiting."""
        mock_input.side_effect = ["9", "4"]

        main()

        mock_print.assert_any_call("Invalid choice. Please try again.")
        mock_print.assert_any_call("Exiting...")

    @patch("builtins.print")
    @patch("builtins.input")
    def test_main_full_flow(self, mock_input, mock_print):
        """Tests adding, displaying, searching, and exiting."""
        # This list simulates typing values into the terminal one by one
        mock_input.side_effect = [
            "3",
            "Dracula",
            "Bram Stoker",
            "250",
            "5",  # 3 4 inputs
            "1",  # 1 ver libros
            "2",
            "Dracula",  # 2 buscar libro
            "4",  # 4 salir
        ]

        main()

        mock_print.assert_any_call("Book 'Dracula' added to the store.")
        mock_print.assert_any_call("Books available in the store:")
        mock_print.assert_any_call("Found 1 book(s) with title 'Dracula':")
        mock_print.assert_any_call("Exiting...")
