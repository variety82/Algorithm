def solution(players, callings):
    palyer_idx_dict = {player:idx for idx, player in enumerate(players)}
    for call in callings:
        idx = palyer_idx_dict[call]
        palyer_idx_dict[call] -= 1
        palyer_idx_dict[players[idx-1]] += 1

        players[idx], players[idx-1] = players[idx-1], players[idx]
    return players