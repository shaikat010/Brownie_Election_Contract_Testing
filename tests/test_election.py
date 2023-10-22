from brownie import Election, accounts

# creating the first test
def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    election = Election.deploy({"from": account})
    vote_status = election.viewVoteStatus()
    expected = (0,0,0,0)
    # Assert
    assert vote_status == expected

# creating a new test
# this test will fail due to a bug inside the code
def test_place_vote():
    # Arrange
    account = accounts[0]
    election = Election.deploy({"from": account})
    # Act
    expected = (1,0,0,1)
    election.placeVote(1,{"from":account})
    vote_status = election.viewVoteStatus()
    # Assert
    assert vote_status == expected





