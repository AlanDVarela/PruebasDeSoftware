# -*- coding: utf-8 -*-
# White-box mocks tests - Alan Varela
# 12 Marzo

"""
White-box integration tests examples.
"""

import subprocess
import unittest
from unittest.mock import MagicMock, patch

from white_box.mockup_exercises import (
    execute_command,
    fetch_data_from_api,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestWhiteBox(unittest.TestCase):
    """Unit tests using mocks for the white_box exercises."""

    # Fetch data API
    @patch("requests.get")
    def test_fetch_success(self, mock_get):
        """Test that API data is returned correctly when request succeeds."""
        mock_get.return_value.json.return_value = {"id": 1, "name": "Alan"}
        mock_get.return_value.status_code = 200

        result = fetch_data_from_api("https://hola.com")

        self.assertEqual(result, {"id": 1, "name": "Alan"})
        mock_get.assert_called_once_with("https://hola.com", timeout=10)

    # Read data from file
    @patch("builtins.open")
    def test_read_data_from_file_valid(self, mock_open):
        """Test reading a file successfully returns its contents."""
        mock_file = MagicMock()
        mock_file.__enter__.return_value.read.return_value = "hola"
        mock_open.return_value = mock_file

        result = read_data_from_file("hola.txt")

        self.assertEqual(result, "hola")
        mock_open.assert_called_once_with("hola.txt", encoding="utf-8")

    @patch("builtins.open")
    def test_read_data_from_file_invalid(self, mock_open):
        """Test that FileNotFoundError is raised when the file does not exist."""
        mock_open.side_effect = FileNotFoundError

        with self.assertRaises(FileNotFoundError):
            read_data_from_file("archivo.txt")

    # Execute command
    @patch("subprocess.run")
    def test_execute_command_success(self, mock_run):
        """Test that execute_command returns stdout when command succeeds."""
        mock_process = MagicMock()
        mock_process.stdout = "hello world"
        mock_run.return_value = mock_process

        result = execute_command(["echo", "hello world"])

        self.assertEqual(result, "hello world")
        mock_run.assert_called_once_with(
            ["echo", "hello world"], capture_output=True, check=False, text=True
        )

    @patch("subprocess.run")
    def test_execute_command_error(self, mock_run):
        """Test that execute_command raises CalledProcessError on failure."""
        mock_run.side_effect = subprocess.CalledProcessError(
            returncode=1, cmd="bad command"
        )

        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(["bad command"])

    # Perform action based on time
    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_on_time_a(self, mock_time):
        """Test that Action A is returned when time condition is met."""
        mock_time.return_value = 5

        result = perform_action_based_on_time()

        self.assertEqual(result, "Action A")

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_on_time_b(self, mock_time):
        """Test that Action B is returned when time condition is met."""
        mock_time.return_value = 11

        result = perform_action_based_on_time()

        self.assertEqual(result, "Action B")
