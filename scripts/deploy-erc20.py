from brownie import ERC20Basic, config, accounts
 
def deployContract():
    account = accounts.add(config["wallets"]["from_key"])
    ERC20Basic.deploy(1000000000000000000,{'from': account}) # Supply of 1 TST
 
def main():
    deployContract()
