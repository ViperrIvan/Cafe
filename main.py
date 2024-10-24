def check_decorator(func):
    def wrapper(*args, **kwargs):
        buy()
        print("\n" + "="*30)
        func(*args, **kwargs)
        print("="*30 + "\n")
    return wrapper

def menu(user_input):
    global products
    products = {
        1: 'кофе',
        2: 'лапша',
        3: 'бургер',
        4: 'сочные пельмени'
    }
    return products[user_input]
def cost(key):
    cost = {
        'кофе': 50,
        'лапша': 100,
        'бургер':200,
        'сочные пельмени':250
    }
    return cost[key]

buskett=[]
def busket():
    if menu(user_input) in buskett:
        buskett[buskett.index(menu(user_input))+2]+=user_number
    else:
        buskett.append(menu(user_input))
        buskett.append(cost(menu(user_input)))
        buskett.append(user_number)
@check_decorator
def check():
    moreCost = 0
    print('Ваш чек:')
    for i in range(0,len(buskett),3):
        print(f"{buskett[i]}: {buskett[i+1]} x {buskett[i+2]}шт")
        moreCost+=buskett[i+1]*buskett[i+2]
    print(' ')
    print(f'Оплачено: {moreCost}')
    if bought==1:
        print(f'Внесено: {CardOrNal}')
        print(f'Сдача: {CardOrNal-moreCost}')


def zakaz():
    global user_input
    global user_number
    try:
        print('Что вы хотели бы заказать?')
        user_input = int(input('Введите цифру соответствующую ващему выбору: '))
        user_number = int(input('введите количество: '))
        busket()
        if input('Для продолжения заказа введите 1, иначе любой символ: ')=='1':
            zakaz()
        else:
            check()
    except KeyError:
        print('Такого варианта нет!!!')
        zakaz()
    except ValueError:
        print('Введите число а не букву!!!')
        zakaz()

def printMenu():
    print('Меню: ')
    for i in range(1, 5):
        print(f'   {i}){menu(i)}: {cost(menu(i))}')

def buy():
    mostCost = 0
    for i in range(0,len(buskett),3):
        mostCost+=buskett[i+1]*buskett[i+2]
    print(f'Итого к оплате: {mostCost}')
    print('Оплата картой или наличными?')
    print('1)Наличные\n2)Карта')
    global bought
    try:
        bought = int(input('Введите цифру соответствующую ващему выбору: '))
    except ValueError:
        print('Введи числовое значение!!!')
        buy()
    if bought==1:
        global CardOrNal
        try:
            CardOrNal = int(input('Внесите сумму в рублях: '))
            if CardOrNal<mostCost:
                print('Нехватает денежных средств!!!')
            elif CardOrNal<0:
                print('Долги берут в банке а не в кафе!!!')
                buy()
        except ValueError:
            print('Введи числовое значение!!!')
            buy()
    elif bought==2:
        pass
    else:
        print('Такого варианта ответа нет!!!')
        buy()



printMenu()
print('Что вы хотели бы заказать?')
try:
    user_input = int(input('Введите цифру соответствующую ващему выбору: '))
    user_number = int(input('Введите количество: '))
    busket()
    if input('Для продолжения заказа введите 1, иначе любой символ: ') == '1':
        zakaz()
    else:
        check()
except KeyError:
    print('Такого варианта нет!!!')
    zakaz()
except ValueError:
    print('Введите число а не букву!!!')
    zakaz()
