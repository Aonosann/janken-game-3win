import random
# スコア初期化　pythonは型宣言をする必要がないが、初期化は必要
player_score = 0
cpu_score = 0
# inputされた数字に対応する手を辞書で定義(inputは文字列として扱われるため、キーも文字列にする)
hands = {
    "0": "グー ✊",
    "1": "チョキ ✌️",
    "2": "パー 🖐️"
}
# ゲーム開始メッセージ
print("三本先取じゃんけんゲーム！")
while player_score < 3 and cpu_score < 3:
    print("0: グー, 1: チョキ, 2: パー") 
    player = input("数字を入力してね: ")# inputは文字列として扱われる
    if player not in hands:
        print("エラー👹")
        continue
    cpu = str(random.randint(0, 2))# CPUの手をランダムに決定 str型に変換しているのはplayerと型を合わせるため
    # 結果表示
    print("君が選んだのは: " + hands[player])
    print("CPUが選んだのは: " + hands[cpu])
    # 勝敗判定
    result=(int(player) - int(cpu)+3)%3 #result変数はInt型なので、playerとcpuをInt型に変換
    if result ==0:
        print("引き分け！")
    elif result ==2:
        print("君の勝ち！🎉")
        player_score+=1
    else:
        print("君の負け...😢")
        cpu_score+=1
    # スコア表示
    print(f"スコア - 君: {player_score} | CPU: {cpu_score}")
    print("-------------------------")
# 最終結果表示
if player_score == 3:
    print("おめでとう！君の勝ち！🏆")
else:
    print("残念！負けちゃった！💻")