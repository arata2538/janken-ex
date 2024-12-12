#以下生成AI
def test_player_pon(input_func=None):
    if input_func is None:
        input_func = input  # デフォルトは標準の `input`
    hands_dic = {'1': "グー", '2': "チョキ", '3': "パー"}
    print("1.グー 2.チョキ 3.パー")
    player_hand = input_func("グー、チョキ、パーのいずれかを入力してください：")
    while player_hand not in hands_dic.keys():
        print("不正な入力です。もう一度入力してください。")
        player_hand = input_func("グー、チョキ、パーのいずれかを入力してください：")

    return hands_dic[player_hand]
