from utils.chef import parse_meal


def run_main():

    meal = {
        "potato": 330,
        "milk": 150,
    }

    insulin_ratio = 2.5

    parse_meal(meal, insulin_ratio)


if __name__ == "__main__":
    run_main()
