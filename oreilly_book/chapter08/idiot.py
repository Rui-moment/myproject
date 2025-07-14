import pyinputplus as pyip  # ユーザー入力を制御するためのライブラリをインポート    

while True:  # 無限ループを開始
    prompt = 'バカを何時間も忙しくする方法を知りたい？\n'
    response = pyip.inputYesNo(prompt)

    if response == 'no':
        break  # ユーザーが「no」を入力した場合、ループを終了

print('ありがとう、良い1日を！')  # ユーザーが「no」を入力した後のメッセージを表示
    