# blockchain.py
import requests
from config import IN_SCOPE_ENDPOINTS, CUSTOM_HEADER

def test_exceed_max_supply():
    payload = {
        'action': 'exceed_supply',
        'amount': 10000000001  # Adjust as needed
    }
    response = requests.post(IN_SCOPE_ENDPOINTS['blockchain'], json=payload, headers=CUSTOM_HEADER)
    return response.json()

def test_loss_of_funds():
    payload = {
        'action': 'transfer_funds',
        'from': '0xExampleFromAddress',
        'to': '0xExampleToAddress',
        'amount': 100000  # Adjust as needed
    }
    response = requests.post(IN_SCOPE_ENDPOINTS['blockchain'], json=payload, headers=CUSTOM_HEADER)
    return response.json()

def test_bft_violation():
    payload = {
        'action': 'bft_violation_test'
    }
    response = requests.post(IN_SCOPE_ENDPOINTS['blockchain'], json=payload, headers=CUSTOM_HEADER)
    return response.json()

def test_network_shutdown():
    payload = {
        'action': 'network_shutdown_test'
    }
    response = requests.post(IN_SCOPE_ENDPOINTS['blockchain'], json=payload, headers=CUSTOM_HEADER)
    return response.json()

def test_remote_code_execution():
    payload = {
        'action': 'rce_test',
        'code': 'some_malicious_code'  # Adjust as needed
    }
    response = requests.post(IN_SCOPE_ENDPOINTS['blockchain'], json=payload, headers=CUSTOM_HEADER)
    return response.json()

def test_temporary_network_shutdown():
    payload = {
        'action': 'temporary_network_shutdown_test'
    }
    response = requests.post(IN_SCOPE_ENDPOINTS['blockchain'], json=payload, headers=CUSTOM_HEADER)
    return response.json()

def test_unintended_smart_contract_behavior():
    payload = {
        'action': 'smart_contract_behavior_test'
    }
    response = requests.post(IN_SCOPE_ENDPOINTS['blockchain'], json=payload, headers=CUSTOM_HEADER)
    return response.json()

def test_permanent_burning_of_sui():
    payload = {
        'action': 'permanent_burning_test',
        'amount': 5000  # Adjust as needed
    }
    response = requests.post(IN_SCOPE_ENDPOINTS['blockchain'], json=payload, headers=CUSTOM_HEADER)
    return response.json()

def test_node_shutdown():
    payload = {
        'action': 'node_shutdown_test'
    }
    response = requests.post(IN_SCOPE_ENDPOINTS['blockchain'], json=payload, headers=CUSTOM_HEADER)
    return response.json()

def test_invariant_violation_error():
    payload = {
        'action': 'invariant_violation_test'
    }
    response = requests.post(IN_SCOPE_ENDPOINTS['blockchain'], json=payload, headers=CUSTOM_HEADER)
    return response.json()

def test_fullnode_crash():
    payload = {
        'action': 'fullnode_crash_test'
    }
    response = requests.post(IN_SCOPE_ENDPOINTS['blockchain'], json=payload, headers=CUSTOM_HEADER)
    return response.json()
