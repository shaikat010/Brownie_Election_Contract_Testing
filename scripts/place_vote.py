import os
from brownie import accounts, config
from brownie import Election
from brownie import network

def place_your_vote():
    account = accounts[0]
    # print(account)
    election = Election.deploy({"from": account})
    transaction = election.placeVote(1,{"from": account})
    print("This is the transaction info: ")
    print(transaction.info())
    print("------------------------------------")
    print("These are the transaction events: ")
    print(transaction.events)
    print("------------------------------------")
    return transaction

def main():
    print(place_your_vote())