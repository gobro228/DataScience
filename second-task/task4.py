def cars(distance, road, fuel):
    consumption_offroad = 24    # road = 0
    consumption_town = 14.8       # road = 1
    consumption_highway = 10     # road = 2
    cost_92 = 52.7
    cost_95 = 56.92
    cost_98 = 70.84

    match road:
        case 0:
            fuel_consumption = distance / 100 * consumption_offroad
        case 1:
            fuel_consumption = distance / 100 * consumption_town
        case 2:
            fuel_consumption = distance / 100 * consumption_highway

    match fuel:
        case 92:
            money_consumption = fuel_consumption * cost_92
        case 95:
            money_consumption = fuel_consumption * cost_95
        case 98:
            money_consumption = fuel_consumption * cost_98

    return fuel_consumption, money_consumption


distance = int(input("Введите дистанцию: "))
road = int(input("Введите тип дороги (0 - грунтовая, 1 - город, 2 - шоссе): "))
fuel = int(input("Введите тип топлива(92, 95 или 98): "))
answer1, answer2 = cars(distance, road, fuel)
print(f'Расход топлива: {round(answer1, 2)} литров\nЗатраты: {round(answer2, 2)} рублей)')
