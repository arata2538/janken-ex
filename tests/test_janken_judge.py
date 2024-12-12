#以下生成AI
from source.janken_judge import judge

def test_judge():
    # 引き分けのテスト
    assert judge("グー", "グー") == "draw", "引き分けの判定が間違ってる！"
    assert judge("チョキ", "チョキ") == "draw", "引き分けの判定が間違ってる！"
    assert judge("パー", "パー") == "draw", "引き分けの判定が間違ってる！"

    # プレイヤーの勝利
    assert judge("チョキ", "グー") == "player_win", "プレイヤー勝利の判定が間違ってる！"
    assert judge("パー", "チョキ") == "player_win", "プレイヤー勝利の判定が間違ってる！"
    assert judge("グー", "パー") == "player_win", "プレイヤー勝利の判定が間違ってる！"

    # コンピューターの勝利
    assert judge("グー", "チョキ") == "computer_win", "コンピューター勝利の判定が間違ってる！"
    assert judge("チョキ", "パー") == "computer_win", "コンピューター勝利の判定が間違ってる！"
    assert judge("パー", "グー") == "computer_win", "コンピューター勝利の判定が間違ってる！"