import json


def menu(file):
    p = file["general"]["properties"]
    text = f'''
    Select counter:
    1. {p["countdown1"]["value"]} | {p["date"]["value"]}
    2. {p["countdown2"]["value"]} | {p["date1"]["value"]}
    3. {p["countdown3"]["value"]} | {p["date2"]["value"]}
    4. {p["countdown4"]["value"]} | {p["date3"]["value"]}
    5. {p["countdown5"]["value"]} | {p["date4"]["value"]}
    '''

    print(text)

    choice: int = 0
    while choice not in range(1, 6):
        try:
            choice = int(input('>>> '))
        except:
            continue

    text1 = '''
    1. Switch ON/OFF
    2. Change name
    3. Change date
    4. Back
    '''

    print(text1)

    option: int = 0
    while option not in range(1, 5):
        try:
            option = int(input('>>> '))
        except:
            continue

    if option == 1:
        p[f"countdown{choice}1"]["value"] = 'true' if not bool(p[f"countdown{choice}1"]["value"]) else 'false'
        print('Switched!')
    elif option == 2:
        print('Input counter name:')
        p[f"countdown{choice}"]["value"] = input('>>> ')
    elif option == 3:
        print('Input counter date (DD/MM/YYYY):')
        p[f"date{choice - 1 if choice - 1 else ''}"]["value"] = input('>>> ')
    elif option == 4:
        print('\n\n')

    return file


def main():
    while True:
        with open('project.json', 'r') as file:
            properties = json.load(file)
            properties_new: str = menu(properties)

        with open('project.json', 'w') as file:
            file.write(json.dumps(properties_new))


if __name__ == '__main__':
    main()
