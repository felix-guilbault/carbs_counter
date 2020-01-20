from utils.ingredients import food


def parse_meal(meal: dict, insulin):

    carbs = 0
    fiber = 0

    for k in meal.keys():
        quantity = meal[k]
        carbs += food[k].carbs * quantity
        fiber += food[k].fiber * quantity

    print(f"Carbohydrates:  % d" % carbs)
    print(f"Fiber:          % .1f" % fiber)
    print(f"Total carbs:    % d\n" % (carbs - fiber))
    print(f"Nb portions:    % .2f" % ((carbs - fiber) / 15.0))
    print(f"Insulin:        % .1f" % (((carbs - fiber) * insulin) / 15.0))
