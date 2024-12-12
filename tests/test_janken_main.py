#以下生成AI
from source.janken_main import main
import source.player
import source.computer
import source.janken_judge

# テストで必要な関数をモックするための簡易的な関数を定義
class MockInput:
    def __init__(self, inputs):
        self.inputs = iter(inputs)

    def __call__(self, prompt):
        return next(self.inputs)


def test_janken_main():
    # プレイヤーの入力をモック
    player_inputs = MockInput(["1", "2", "3"])  # "グー", "チョキ", "パー"を順番に入力
    source.player.input = player_inputs  # player.pyのinputを置き換え

    # コンピュータの手を固定
    def mock_computer_pon():
        return "チョキ"  # 固定で "チョキ" を返す
    source.computer.computer_pon = mock_computer_pon

    # 判定を固定
    def mock_judge(computer_hand, player_hand):
        if player_hand == "グー" and computer_hand == "チョキ":
            return "player_win"
        elif player_hand == "チョキ" and computer_hand == "チョキ":
            return "draw"
        else:
            return "computer_win"
    source.janken_judge.judge = mock_judge

    # 標準出力をキャプチャ
    import sys
    from io import StringIO

    output = StringIO()
    sys.stdout = output  # 標準出力をリダイレクト

    # main関数を実行
    main()

    # 標準出力を元に戻す
    sys.stdout = sys.__stdout__

    # 出力内容を検証
    output_lines = output.getvalue().splitlines()
    assert "-----ラウンド 1 -----" in output_lines
    assert "あなたの勝ちです！" in output_lines
    assert "コンピュータの勝ちです！" in output_lines
    assert "あなたの総合勝利です！" in output_lines
