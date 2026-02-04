# jankenapp.py
# Streamlitを使った3本先取じゃんけんゲーム
# 必要なライブラリのインポート
import streamlit as st
import random
# プレイヤーとCPUのスコアをセッションで管理
player = None
if "player_score" not in st.session_state:
    st.session_state.player_score = 0
    st.session_state.cpu_score = 0
# inputされた数字に対応する手を辞書で定義
hands = {
    "0": "グー ✊",
    "1": "チョキ ✌️",
    "2": "パー 🖐️"
}
# ゲームタイトル表示
st.title("3本先取じゃんけん！")
# ゲームループSTART
if st.session_state.player_score < 3 and st.session_state.cpu_score < 3:
    st.write("ボタンを押して手を選んでね。")
    # ボタンで手を選択(カラムを使って横並びに配置)
    col1, col2, col3 = st.columns(3)
    if col1.button("グー ✊"):
        player = "0"
    if col2.button("チョキ ✌️"):
        player = "1"
    if col3.button("パー 🖐️"):
        player = "2"
    # 勝敗判定
    if player is not None:
        cpu = str(random.randint(0, 2))
        st.write(hands[player] + "を選んだ！")
        st.write("CPUの手は: " + hands[cpu])
        result = (int(player) - int(cpu) + 3) % 3
        # 結果表示とスコア更新
        if result == 0:
            st.write("引き分け！")
        elif result == 2:
            st.write("君の勝ち！🎉")
            st.session_state.player_score += 1
        else:
            st.write("君の負け...😢")
            st.session_state.cpu_score += 1
        # スコア表示
        st.write(f"スコア - 君: {st.session_state.player_score} | CPU: {st.session_state.cpu_score}")
        st.write("-------------------------")
        # ゲーム終了判定
        if st.session_state.player_score == 3 or st.session_state.cpu_score == 3:
            st.rerun()
        #ゲームループEND
# 最終結果表示
else:
    st.write("ゲーム終了！")
    st.write(f"最終スコア - 君: {st.session_state.player_score} | CPU: {st.session_state.cpu_score}")
    # 勝敗表示
    if st.session_state.player_score == 3:
        st.write("おめでとう！君の勝ち！🏆")
    else:
        st.write("残念！負けちゃった！💻")
    # リセットボタン
    if st.button("もう一回！🔄"):
        st.session_state.player_score = 0
        st.session_state.cpu_score = 0
        st.rerun()