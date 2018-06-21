def player_health():
    health = 40
    return health

def player_score():
    score = 55
    return score

def main():
    health = player_health()
    score = player_score()

    if health < 50:
        print("Health getting Low")

    if score > 50:
        print("New Highest Score")

main()