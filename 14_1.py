import little_helper


def answer(input):
    input = int(input)

    recipes = [3,7]
    one = 0
    two = 1
    one_recipe = recipes[one]
    two_recipe = recipes[two]

    while True:
        sum_recipes = one_recipe + two_recipe

        new_recipe = sum_recipes // 10 % 10
        if new_recipe > 0:
            recipes.append(new_recipe)
            
        new_recipe = sum_recipes % 10
        recipes.append(new_recipe)

        num_recipes = len(recipes)

        if num_recipes >= input + 10:
            break

        one = (one + 1 + one_recipe) % num_recipes
        one_recipe = recipes[one]

        two = (two + 1 + two_recipe) % num_recipes
        two_recipe = recipes[two]

    return ''.join(str(n) for n in recipes[-10:])


if __name__ == '__main__':
    input = little_helper.get_input(14)
    print(answer(input))
