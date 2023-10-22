import os
from brownie import accounts, config
from brownie import Election
from brownie import network

def get_vote_status():
    account = accounts[0]
    # print(account)
    election = Election.deploy({"from": account})
    current_vote_status = election.viewVoteStatus()
    return current_vote_status

def main():
    print(get_vote_status())

if __name__ == "__main__":
    main()