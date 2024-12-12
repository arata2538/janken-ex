#以下生成AI
from source.computer import computer_pon

def test_computer_pon():
    valid_hands = ["グー", "チョキ", "パー"]
    for _ in range(10):  # ランダム性を考慮して複数回テスト
        result = computer_pon()
        assert result in valid_hands, f"無効な手が返されました: {result}"
