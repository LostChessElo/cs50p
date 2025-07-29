def fruit():

    fruits={
        'apple': 130,
        'avocado' : 50,
        'banana' : 110,
        'cantaloup' : 50,
        'grapefruit' : 60,
        'grapes' : 90,
        'honeydew melon' : 50,
        'kiwifruit' : 90,
        'lemon' : 15,
        'nectarine' : 20,
        'orange' : 80,
        'peach' : 60,
        'pear' : 100,
        'pineapple' : 50,
        'plums' : 70,
        'strawberries' : 50,
        'sweet cherries' : 100,
        'tangerine' : 50,
        'watermelom' : 80,
    }

    user_fruit=input('Item: ').lower().strip()

    if user_fruit in fruits:
        calories= fruits[user_fruit]
    else:
        return ''
    
    return f'Calories: {calories}'

print(fruit())
