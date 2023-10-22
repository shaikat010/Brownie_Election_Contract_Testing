import os
from brownie import accounts, config
from brownie import Election
from brownie import network

election = None

def deploy_election():
    account = accounts[0]
    account = get_account()
    # print(account)
    election = Election.deploy({"from": account})
    print(election)
    # transact or call
    # doing the call here
    Vote_Status = election.viewVoteStatus()
    print(Vote_Status)
    # making a transaction
    transaction = election.placeVote(1,{"from":account})
    transaction.wait(1)
    # checking the vote status after the transaction
    Vote_Status = election.viewVoteStatus()
    print(Vote_Status)

    # other methods to add accounts
    # to work with the other method via using the brownie command line
    # it will be asking us for the password using this method
    # account = accounts.load("ShaikatAccount")
    # print(account)
    # this is the .env method
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # print(account)
    # we could do this too
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)

    return election


# show this when showing how to deploy in the test network
def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    global election
    election = deploy_election()
