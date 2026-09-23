
from utils import generate_secret_number, check_user_guess
from score import player_scoring, score_rating


secret_number = generate_secret_number()
print("Secret:", secret_number)
score = 100

while True:
    if check_user_guess(secret_number):
        break
    else:
        score = player_scoring(score)
    if score == 0:
        print("You Lose")
        break
score_rating(score)
print("Your score:", score)