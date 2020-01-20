from typing import NamedTuple

from utils.classes import Ingredient


# -----------------------------------------------------------------------------------------------------------------
# By weight

food = {
    "asparagus": Ingredient(
        group="Green veggies",
        carbs=4 / 180,
        fiber=0
    ),
    "beetroot": Ingredient(
        group="Root veggies",
        carbs=7.2 / 100,
        fiber=0
    ),
    "eggplant": Ingredient(
        group="Veggies",
        carbs=6 / 99,
        fiber=0
    ),
    "spinach": Ingredient(
        group="Leaf veggies",
        carbs=3 / 180,
        fiber=0
    ),
    "milk": Ingredient(
        group="Dairy",
        carbs=12 / 250,
        fiber=0
    ),
    "almond_milk": Ingredient(
        group="Nuts & legumes",
        carbs=8 / 250,
        fiber=0
    ),
    "potato": Ingredient(
        group="Root veggies",
        carbs=17 / 100,
        fiber=3 / 100
    )
}


# -----------------------------------------------------------------------------------------------------------------
# By volume


class ByWeight(NamedTuple):
    """
    Amount of grams of carbs per gram of weight.
    """

    artichoke = 4 / 120
    avocado = 3 / 150
    bell_pepper = 6 / 149
    broccoli = 4.5 / 100
    brussel_sprout = 4 / 78
    cabbage = 2 / 89
    carrot = 4.5 / 61
    cauliflower = 3 / 100
    celery = 1 / 101
    celeri_root = 5.9 / 100
    cucumber = 3 / 104
    garlic = 1 / 3
    green_bell_pepper = 5 / 149
    mushroom = 1 / 70
    onion = 7.3 / 100
    radish = 2 / 116
    tomato = 4 / 149
    sweet_potato = (20 - 3) / 100
    zucchini = 3 / 124

# maybe use collections.Counter
# https://docs.python.org/3/library/typing.html
