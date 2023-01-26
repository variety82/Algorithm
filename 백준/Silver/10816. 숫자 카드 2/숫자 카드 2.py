def count_card(cards):
    card_set = {}
    for card in cards:
        if card not in card_set:
            card_set[card] = 1
        else:
            card_set[card] += 1
    return card_set

def search_card(goal):
    answer = []
    for card in goal:
        start = 0
        end = len(cards) - 1

        while(start <= end):
            mid = (start + end) // 2
            if(cards[mid] == card):
                break
            elif(cards[mid] > card):
                end = mid - 1
            else:
                start = mid + 1
        if(cards[mid] == card):
            answer.append(card_set[card])
        else:
            answer.append(0)
    return answer




N = int(input())
cards = sorted([int(x) for x in input().split()])
card_set = count_card(cards)
M = int(input())
goal = [int(x) for x in input().split()]

print(*search_card(goal))