import unittest
from unittest.mock import MagicMock
from Mockobjekt.mock_api import get_user_data, perform_api_call

class TestMockAPI(unittest.TestCase):
    def setUp(self):
        # Förbereder gemensamma resurser för testfallen
        self.valid_user_id = 1
        self.invalid_user_id = 3
        self.api_endpoint = "/example"
        self.api_data = {"key": "value"}

    def test_hamta_giltig_anvandardata(self):
        """
        Testar hämtning av användardata med ett giltigt användar-ID.
        """
        # Utför testfall
        user_data = get_user_data(self.valid_user_id)

        # Validerar resultat
        self.assertIsNotNone(user_data)
        self.assertEqual(user_data["id"], self.valid_user_id)
        self.assertEqual(user_data["username"], "mockuser1")
        self.assertEqual(user_data["email"], "mockuser1@example.com")

    def test_hamta_ogiltig_anvandardata(self):
        """
        Testar hämtning av användardata med ett ogiltigt användar-ID.
        """
        # Utför testfall
        user_data = get_user_data(self.invalid_user_id)

        # Validerar resultat
        self.assertIsNone(user_data)

    def test_utfors_api_anrop(self):
        """
        Testar utförande av ett API-anrop.
        """
        # Utför testfall
        response = perform_api_call(self.api_endpoint, self.api_data)

        # Validerar resultat
        self.assertEqual(response, "")

if __name__ == "__main__":
    unittest.main()



