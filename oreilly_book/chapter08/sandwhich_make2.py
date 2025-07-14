import pyinputplus as pyip

def order_sandwich():
    # 価格設定
    bread_prices = {'小麦パン': 100, '白パン': 120, 'サワー種': 150}
    protein_prices = {'ハム': 150, 'チーズ': 130, '卵': 100}
    cheese_prices = {'チェダーチーズ': 80, 'モッツァレラチーズ': 90, 'ブルーチーズ': 100}
    option_prices = {'マヨネーズ': 20, 'レタス': 30, 'トマト': 40}

    # パン
    bread = pyip.inputMenu(list(bread_prices.keys()), prompt='どのパンを選びますか？\n', numbered=True)
    # タンパク質
    protein = pyip.inputMenu(list(protein_prices.keys()), prompt='どの具材を選びますか？\n', numbered=True)
    # チーズ
    cheese_want = pyip.inputYesNo(prompt='チーズを入れますか？(yes/no): ')
    if cheese_want == 'yes':
        cheese = pyip.inputMenu(list(cheese_prices.keys()), prompt='どのチーズを選びますか？\n', numbered=True)
        cheese_price = cheese_prices[cheese]
    else:
        cheese = None
        cheese_price = 0
    # オプション
    mayonnaise = pyip.inputYesNo(prompt='マヨネーズを入れますか？(yes/no): ')
    lettuce = pyip.inputYesNo(prompt='レタスを入れますか？(yes/no): ')
    tomato = pyip.inputYesNo(prompt='トマトを入れますか？(yes/no): ')

    # サンドイッチの数
    num_sandwiches = pyip.inputInt(prompt='サンドイッチの数を入力してください: ', min=1, max=10)

    # 合計金額計算
    total = (
        bread_prices[bread] +
        protein_prices[protein] +
        cheese_price +
        (option_prices['マヨネーズ'] if mayonnaise == 'yes' else 0) +
        (option_prices['レタス'] if lettuce == 'yes' else 0) +
        (option_prices['トマト'] if tomato == 'yes' else 0)
    ) * num_sandwiches

    print(f"\n注文内容:")
    print(f"パン: {bread} ({bread_prices[bread]}円)")
    print(f"具材: {protein} ({protein_prices[protein]}円)")
    if cheese:
        print(f"チーズ: {cheese} ({cheese_price}円)")
    if mayonnaise == 'yes':
        print(f"マヨネーズ ({option_prices['マヨネーズ']}円)")
    if lettuce == 'yes':
        print(f"レタス ({option_prices['レタス']}円)")
    if tomato == 'yes':
        print(f"トマト ({option_prices['トマト']}円)")
    print(f"サンドイッチの数: {num_sandwiches}")
    print(f"合計金額: {total}円")

order_sandwich()