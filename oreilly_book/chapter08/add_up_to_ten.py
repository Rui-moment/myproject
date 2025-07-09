import pyinputplus as pyip  # ユーザー入力を制御するためのライブラリをインポート

# 入力された数字の各桁を合計し、それが10かどうかをチェックする関数
def add_up_to_ten(numbers):
    number_list = list(str(numbers))  # 数字を文字列に変換して、各桁をリストに分解
    for i, digit in enumerate(number_list):  # 各桁を整数に変換
        number_list[i] = int(digit)
    if sum(number_list) != 10:  # 桁の合計が10でない場合はエラーを出す
        raise Exception('The digits must add up to 10, '
                        f'not {sum(number_list)}.')
    return int(numbers)  # 条件を満たす場合は整数として返す

# ユーザーに入力を求め、add_up_to_ten関数でバリデーションを行う
response = pyip.inputCustom(add_up_to_ten)
print(f'Thanks, the number you entered is {response}.')  # 結果を表示