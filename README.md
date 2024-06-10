This repository contains a set of scripts to perform targeted vulnerability testing for blockchain, ZkLogin circuits, and DeepBook systems. The scripts are designed to comply with specific bug bounty program rules, avoiding massive traffic generation and focusing on critical, high, medium, and low impact vulnerabilities.
Table of Contents

    Introduction
    Configuration
    Modules
        Blockchain Module
        ZkLogin Module
        DeepBook Module
    Main Script
    Running the Script
    Logging and Reporting
    Customization and Expansion

Introduction

These scripts are designed to test a variety of vulnerabilities within the specified scope of a bug bounty program. The main focus areas include blockchain/DLT, ZkLogin circuits, and DeepBook systems. The scripts are modular, allowing for targeted testing of specific vulnerabilities while minimizing the risk of generating excessive traffic.
Configuration

Before running the scripts, ensure you have configured the necessary settings in the config.py file. This includes specifying the in-scope endpoints and custom headers for identification.

python

# config.py
IN_SCOPE_ENDPOINTS = {
    'blockchain': 'https://example.com/blockchain',
    'zklogin': 'https://example.com/zklogin',
    'deepbook': 'https://example.com/deepbook'
}

CUSTOM_HEADER = {'X-Custom-Header': 'your-username'}

LOG_FILE = 'vulnerability_test_log.txt'
REPORT_FILE = 'vulnerability_report.txt'

Modules
Blockchain Module

The blockchain.py script contains functions to test the following vulnerabilities:

    Exceeding the maximum supply of 10 billion SUI and claiming excess funds
    Loss of funds
    Violating BFT assumptions
    Network shutdown requiring a hard fork to resolve
    Arbitrary, non-Move remote code execution
    Temporary network shutdown or unintended chain split
    Unintended smart contract behavior
    Permanent burning of SUI
    Shutdown of network processing nodes
    Invariant violation error code
    Crashing a Sui fullnode

ZkLogin Module

The zklogin.py script contains functions to test vulnerabilities in circuit construction that can lead to loss of funds.
DeepBook Module

The deepbook.py script contains functions to test the following vulnerabilities:

    Significant loss of funds
    Permanent freezing of funds or DoS requiring a protocol upgrade
    Temporary DoS and temporary freezing of funds
    Minor loss of funds and temporary DoS

Main Script

The main.py script orchestrates the execution of all the tests defined in the modules. It logs the results and any errors encountered during the testing process.
Running the Script

    Ensure your virtual environment is activated:



source bugbounty_env/bin/activate  # On Windows use `bugbounty_env\Scripts\activate`

Run the main script:



    python main.py

Logging and Reporting

    Logging: The script logs results and errors in the file specified in LOG_FILE (vulnerability_test_log.txt).
    Reporting: You can enhance the script to generate a detailed report in REPORT_FILE (vulnerability_report.txt) by writing the test results to this file.

Customization and Expansion

You can customize the payloads and add more tests based on the in-scope vulnerabilities. Additionally, you can refine the logging and reporting mechanisms to suit your needs.
   
