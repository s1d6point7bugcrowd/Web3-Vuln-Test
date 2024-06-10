# deepbook.py
import requests
from config import IN_SCOPE_ENDPOINTS, CUSTOM_HEADER

def test_significant_loss_of_funds():
    payload = {
        'action': 'test_loss_of_funds',
        'amount': 1000  # Adjust as needed
    }
    response = requests.post(IN_SCOPE_ENDPOINTS['deepbook'], json=payload, headers=CUSTOM_HEADER)
    return response.json()

def test_permanent_dos():
    payload = {
        'action': 'test_permanent_dos'
    }
    response = requests.post(IN_SCOPE_ENDPOINTS['deepbook'], json=payload, headers=CUSTOM_HEADER)
    return response.json()

def test_temporary_dos():
    payload = {
        'action': 'test_temporary_dos'
    }
    response = requests.post(IN_SCOPE_ENDPOINTS['deepbook'], json=payload, headers=CUSTOM_HEADER)
    return response.json()
