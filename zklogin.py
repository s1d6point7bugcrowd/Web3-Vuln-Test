# zklogin.py
import requests
from config import IN_SCOPE_ENDPOINTS, CUSTOM_HEADER

def test_vulnerabilities_in_circuit():
    payload = {
        'action': 'test_circuit',
        'data': 'sample_data'  # Adjust as needed
    }
    response = requests.post(IN_SCOPE_ENDPOINTS['zklogin'], json=payload, headers=CUSTOM_HEADER)
    return response.json()
