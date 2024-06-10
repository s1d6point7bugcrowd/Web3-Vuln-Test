# main.py
import logging
from config import LOG_FILE, REPORT_FILE
from blockchain import (
    test_exceed_max_supply, test_loss_of_funds,
    test_bft_violation, test_network_shutdown,
    test_remote_code_execution, test_temporary_network_shutdown,
    test_unintended_smart_contract_behavior, test_permanent_burning_of_sui,
    test_node_shutdown, test_invariant_violation_error, test_fullnode_crash
)
from zklogin import test_vulnerabilities_in_circuit
from deepbook import (
    test_significant_loss_of_funds, test_permanent_dos,
    test_temporary_dos
)

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

def run_tests():
    logging.info("Starting vulnerability tests")
    
    # Blockchain/DLT Tests
    try:
        exceed_supply_result = test_exceed_max_supply()
        logging.info(f"Exceed Max Supply Result: {exceed_supply_result}")
    except Exception as e:
        logging.error(f"Error in Exceed Max Supply Test: {e}")
    
    try:
        loss_of_funds_result = test_loss_of_funds()
        logging.info(f"Loss of Funds Result: {loss_of_funds_result}")
    except Exception as e:
        logging.error(f"Error in Loss of Funds Test: {e}")
    
    try:
        bft_violation_result = test_bft_violation()
        logging.info(f"BFT Violation Result: {bft_violation_result}")
    except Exception as e:
        logging.error(f"Error in BFT Violation Test: {e}")

    try:
        network_shutdown_result = test_network_shutdown()
        logging.info(f"Network Shutdown Result: {network_shutdown_result}")
    except Exception as e:
        logging.error(f"Error in Network Shutdown Test: {e}")

    try:
        rce_result = test_remote_code_execution()
        logging.info(f"Remote Code Execution Result: {rce_result}")
    except Exception as e:
        logging.error(f"Error in Remote Code Execution Test: {e}")

    try:
        temp_network_shutdown_result = test_temporary_network_shutdown()
        logging.info(f"Temporary Network Shutdown Result: {temp_network_shutdown_result}")
    except Exception as e:
        logging.error(f"Error in Temporary Network Shutdown Test: {e}")

    try:
        smart_contract_behavior_result = test_unintended_smart_contract_behavior()
        logging.info(f"Unintended Smart Contract Behavior Result: {smart_contract_behavior_result}")
    except Exception as e:
        logging.error(f"Error in Unintended Smart Contract Behavior Test: {e}")

    try:
        burning_sui_result = test_permanent_burning_of_sui()
        logging.info(f"Permanent Burning of SUI Result: {burning_sui_result}")
    except Exception as e:
        logging.error(f"Error in Permanent Burning of SUI Test: {e}")

    try:
        node_shutdown_result = test_node_shutdown()
        logging.info(f"Node Shutdown Result: {node_shutdown_result}")
    except Exception as e:
        logging.error(f"Error in Node Shutdown Test: {e}")

    try:
        invariant_violation_result = test_invariant_violation_error()
        logging.info(f"Invariant Violation Error Result: {invariant_violation_result}")
    except Exception as e:
        logging.error(f"Error in Invariant Violation Test: {e}")

    try:
        fullnode_crash_result = test_fullnode_crash()
        logging.info(f"Fullnode Crash Result: {fullnode_crash_result}")
    except Exception as e:
        logging.error(f"Error in Fullnode Crash Test: {e}")

    # ZkLogin Circuit Tests
    try:
        zklogin_result = test_vulnerabilities_in_circuit()
        logging.info(f"ZkLogin Circuit Result: {zklogin_result}")
    except Exception as e:
        logging.error(f"Error in ZkLogin Circuit Test: {e}")
    
    # DeepBook Tests
    try:
        deepbook_loss_funds_result = test_significant_loss_of_funds()
        logging.info(f"DeepBook Significant Loss of Funds Result: {deepbook_loss_funds_result}")
    except Exception as e:
        logging.error(f"Error in DeepBook Significant Loss of Funds Test: {e}")
    
    try:
        deepbook_perm_dos_result = test_permanent_dos()
        logging.info(f"DeepBook Permanent DoS Result: {deepbook_perm_dos_result}")
    except Exception as e:
        logging.error(f"Error in DeepBook Permanent DoS Test: {e}")

    try:
        deepbook_temp_dos_result = test_temporary_dos()
        logging.info(f"DeepBook Temporary DoS Result: {deepbook_temp_dos_result}")
    except Exception as e:
        logging.error(f"Error in DeepBook Temporary DoS Test: {e}")

    logging.info("Completed vulnerability tests")

if __name__ == "__main__":
    run_tests()
