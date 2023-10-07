def get_user_choice(prompt, options):
    print(prompt)
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    choice = int(input("Elije una opción: "))
    return choice - 1



