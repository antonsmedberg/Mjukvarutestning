from unittest.mock import MagicMock

def get_user_data(user_id):
    """
    Simulerar ett API-anrop för att hämta användardata.
    """
    # Simulera logik för att hämta användardata från en databas eller annan källa
    # I det här fallet returneras mockad data för teständamål
    if user_id == 1:
        return {"id": 1, "username": "mockuser1", "email": "mockuser1@example.com"}
    elif user_id == 2:
        return {"id": 2, "username": "mockuser2", "email": "mockuser2@example.com"}
    else:
        return None

def perform_api_call(endpoint, data):
    """
    Simulerar ett API-anrop till en viss endpoint med angiven data.
    """
    # Simulera logik för att göra ett API-anrop och returnera ett svar
    # Här returneras bara en tom sträng för teständamål
    return ""

def timeout_mock():
    """
    Skapar ett mockobjekt som utlöser ett TimeoutError vid anrop.
    """
    return MagicMock(side_effect=TimeoutError("Anslutningstimmar"))

def server_error_mock():
    """
    Skapar ett mockobjekt som utlöser ett ConnectionError vid anrop.
    """
    return MagicMock(side_effect=ConnectionError("Serverfel"))

# Lägg till fler funktioner för att skapa olika mockobjekt efter behov

