def player_details():
    health = 40
    score = 45
    return health,score

def main():
    health,score = player_details()

    if health < 50:
        print("Health getting Low")

    if score > 50:
        print("New Highest Score")

main()