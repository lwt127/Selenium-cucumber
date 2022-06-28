# Description
This is a demo Python based automation framework using Cucumber and Selenium

# Installing
1. Python: https://www.python.org/downloads/
2. Allure Framework: https://docs.qameta.io/allure/#_installing_a_commandline

After Python installation, please install Behave and Selenium package for Python 
```bash
pip install behave
pip install selenium
pip install allure-behave
```

# Execution
1. Clone Selenium-cucumber to local
2. To run the tests


Mac:
```
$ source <path to the folder created>/crypto-nft/behave -f allure_behave.formatter:AllureFormatter -o report
```
Windows:
```
C:\ <path to the folder created>/crypto-nft/behave -f allure_behave.formatter:AllureFormatter -o report
```

# Test scope
These test scripts cover 3 webpages: 

1. Homepage
    * The top navigation bar: test the accessibility of the links on the  navigation ba
    * Sort by: Verify the order of NFT cards based by different sorting
2. Marketplace
    * All the cards details: test the details if every NFT cards
    * The curated cards details: test the details if every curated NFT cards

3. Drops
    * Email Subscrptioon: Test the functionality of  email verification and subscription box

# Test design
This test design is based on a BDD (Behavior Driven Development) framework, written in plain language, QA can help stakeholders to easily understand the logic in the test scripts, and combine different plain languages to create complex test steps quickly. 

![alt text](https://github.com/lwt127/crypto-nft-demo/blob/main/image.png?raw=true)

The  BDD setps are in feature folder. 

The definition and assertion are in steps.py

The test reports are in report folder. To review the test reports, please execute
Mac:
```
$ source <path to the folder created>/crypto-nft/allure serve report
```
Windows:
```
C:\ <path to the folder created>/crypto-nft/allure serve report
```
