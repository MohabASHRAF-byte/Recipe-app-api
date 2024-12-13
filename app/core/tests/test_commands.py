"""
Test custom django management commands
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

@patch("core.management.commands.wait_for_db.Command.check")
class CommandTests(SimpleTestCase):
    """Test commands"""

    def test_wait_for_db_ready(self, patched_check):
        """ Test db if db is ready"""
        patched_check.return_value = True

        call_command("wait_for_db")

        patched_check.assert_called_once_with(database=['default'])

    @patch("time.sleep")
    def test_wait_for_db_not_ready(self, patched_sleep, patched_check):
        """Test db when not ready"""
        patched_check.side_effect = [Psycopg2Error] * 3 + \
                                    [OperationalError] * 2 + \
                                    [True]

        call_command("wait_for_db")

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(database=['default'])
