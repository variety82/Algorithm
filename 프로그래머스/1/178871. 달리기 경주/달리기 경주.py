def solution(players, callings):
    palyer_idx_dict = {player:idx for idx, player in enumerate(players)}
    idx_player_dict = {idx:player for idx, player in enumerate(players)}
    for call in callings:
        cur_idx = palyer_idx_dict[call]
        pre_idx = cur_idx - 1
        pre_player = idx_player_dict[pre_idx]

        palyer_idx_dict[call] = pre_idx
        palyer_idx_dict[pre_player] = cur_idx

        idx_player_dict[cur_idx] = pre_player
        idx_player_dict[pre_idx] = call
    
    return list(idx_player_dict.values())