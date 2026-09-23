from utils import generate_secret_number, check_user_guess

def player_scoring(s):
    mini = 0
    s = s - 10
    if s < mini:
        s = mini
    return s



def score_rating(fscore):
    if fscore >= 80 and fscore <= 100:
        print("Excellent")
    elif fscore >= 50 and fscore <= 79:
        print("Good")
    elif fscore >= 0 and fscore <= 49:
        print("Keep Practicing")



if __name__ == "__main__":
    number_to_print = generate_secret_number()
    score = 100
    print(f"Secret number: {number_to_print}")

    for _ in range(3):
        print(f"Secret number: {number_to_print}")
        print("Check if the code can identify numbers above, numbers below, and a correct guess.")
        check_user_guess(number_to_print)
        score = player_scoring(score)
        print("Score: ",score)
        score_rating(score)

