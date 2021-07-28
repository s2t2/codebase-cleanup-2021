

from app.game import determine_winner

# TODO: test the code

#u = "rock"
#c = "scissors"
#winner = "USER" # / rock

def test_enlarge():
    assert determine_winner(user_choice="rock", computer_choice="paper") == "paper"
    assert determine_winner(user_choice="rock", computer_choice="rock") == None
    assert determine_winner(user_choice="rock", computer_choice="scissors") == "rock"

    #assert determine_winner(user_choice="rock", computer_choice="paper") == "paper"
    #assert determine_winner(user_choice="rock", computer_choice="paper") == "paper"
    #assert determine_winner(user_choice="rock", computer_choice="paper") == "paper"
    #assert determine_winner(user_choice="rock", computer_choice="paper") == "paper"
