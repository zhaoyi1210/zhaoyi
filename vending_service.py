

balance=0 #使用者餘額
drinks=[
    {'name': '可樂', 'price': 20},
    {'name': '雪碧', 'price': 30},
    {'name': '茶裏王', 'price': 40},
    {'name': '原翠', 'price': 30},
    {'name': '純粹喝', 'price': 40},
    {'name': '水', 'price': 3000}]

def deposit():
    """"儲值功能
    數字相加
    :param:數字1
    :paramy:數字2
    :return:相加結果
    """
    global balance
    value = eval(input('儲值金額:'))
    while value < 1:
        print('====儲值金額需大於零====')
        value = eval(input('儲值金額:'))
    balance += value
    print(f"儲值後金額{balance}元")
def buy():
    global balance,drinks
    print('\n請選擇商品')
    for i in range(0, len(drinks)):
        print(f'({i + 1})\t{drinks[i]["name"]} \t {drinks[i]["price"]}元')
    choose = eval(input('請選擇:'))
    while choose < 1 or choose > 6:
        print('====請輸入1-6之間====')
        choose = eval(input("請選擇:"))
    buy_drink = drinks[choose - 1]
    while balance<buy_drink['price']:
        print('====餘額不足，需要儲值嘛====')
        want_deposit=input('y/n?')
        if balance < buy_drink['price']:
            deposit()
        if want_deposit=='y':
            deposit()
        elif want_deposit=='n':
            break
        else:
            print('====餘額不足====')
        deposit()
    else:
        print(f'以購買{buy_drink["name"]}{buy_drink["price"]}元')
        balance -= buy_drink["price"]
        print(f'購買後餘額為{balance}元')


