import pyinputplus as pyip
def order_sandwich():#Take the sandwich order
    # Prompt for the type of bread
    bread = pyip.inputMenu(['小麦パン', '白パン', 'サワー種'], prompt='どのパンを選びますか？\n', numbered=True)
    # Prompt for the type of filling
    protein = pyip.inputMenu(['ハム', 'チーズ', '卵'], prompt='どの具材を選びますか？\n', numbered=True)
    # Prompt for the type of cheese
    cheese_want = pyip.inputYesNo(prompt='チーズを入れますか？(y/n): ')
    if cheese_want == 'yes':
        cheese = pyip.inputMenu(['チェダーチーズ', 'モッツァレラチーズ', 'ブルーチーズ'], prompt='どのチーズを選びますか？\n', numbered=True)
    else:
        cheese = None
    # Prompt for the type of sauce and toppings
    mayonnaise = pyip.inputYesNo(prompt='マヨネーズを入れますか？(y/n): ')
    lettuce = pyip.inputYesNo(prompt='レタスを入れますか？(y/n): ')
    tomato = pyip.inputYesNo(prompt='トマトを入れますか？(y/n): ')
    
    # prompt for the type of how many sandwiches
    num_sandwhiches = pyip.inputInt(prompt='サンドイッチの数を入力してください: ', min=1, max=10)

order_sandwich()


    