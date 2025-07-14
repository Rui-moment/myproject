import pyinputplus as pyip
import random, time # ランダムな数値生成と時間操作のためのライブラリをインポート

number_of_questions = 10  # クイズの問題数を設定
correct_answers = 0  # 正解数を初期化
for question_number in range(number_of_questions):    # 1から9までのランダムな整数を2つ生成
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = f'#{question_number + 1}: {num1} * {num2} = '  # 問題のプロンプトを作成
    
    try:
        pyip.inputStr(prompt, allowRegexes=[f'^{num1 * num2}$'],#正解をallowRegexesで指定
                              blockRegexes=[('.*', '不正解！')],#不正解をblockRegexesで指定
                              timeout=8, limit=3)  # ユーザーの入力を待つ
    except pyip.TimeoutException:
        print('時間切れ！')
    except pyip.RetryLimitException:
        print('回数制限に達しました！')
    else:
        print('正解！')
        correct_answers += 1
    time.sleep(1)  # 1秒間の遅延を挿入        

print(f'あなたは{correct_answers}問正解しました。')  # 正解数を表示