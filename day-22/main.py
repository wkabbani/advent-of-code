import os
import sys
import time
import collections


def get_data():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        data = f.read()
        data = data.split('\n\n')
        player1 = [line for line in data[0].split('\n')]
        player2 = [line for line in data[1].split('\n')]

        player1 = [int(card) for card in player1[1:]]
        player2 = [int(card) for card in player2[1:]]

        return player1, player2


def part_1(player1_deck, player2_deck):
    total_cards_count = len(player1_deck) + len(player2_deck)
    while len(player1_deck) != total_cards_count and len(player2_deck) != total_cards_count:
        player1_play = player1_deck.pop(0)
        player2_play = player2_deck.pop(0)
        if player1_play > player2_play:
            player1_deck.append(player1_play)
            player1_deck.append(player2_play)
        elif player2_play > player1_play:
            player2_deck.append(player2_play)
            player2_deck.append(player1_play)
        else:
            raise Exception('This should not happen!')

    winner_score = 0
    winner_deck = player1_deck if len(
        player1_deck) == total_cards_count else player2_deck
    for i in range(1, len(winner_deck)+1):
        winner_score += i * winner_deck[-1*i]
    return winner_score


def play_game(player1_deck, player2_deck):
    total_cards_count = len(player1_deck) + len(player2_deck)
    rounds = []
    while len(player1_deck) != total_cards_count and len(player2_deck) != total_cards_count:

        # check previous rounds
        for round in rounds:
            if collections.Counter(round[0]) == collections.Counter(player1_deck):
                if collections.Counter(round[1]) == collections.Counter(player2_deck):
                    return 1
        rounds.append((player1_deck.copy(), player2_deck.copy()))

        player1_play = player1_deck.pop(0)
        player2_play = player2_deck.pop(0)
        if player1_play <= len(player1_deck) and player2_play <= len(player2_deck):

            # need a recursive game
            rec_game_winner = play_game(
                player1_deck[:player1_play], player2_deck[:player2_play])
            if rec_game_winner == 1:
                player1_deck.append(player1_play)
                player1_deck.append(player2_play)
            elif rec_game_winner == 2:
                player2_deck.append(player2_play)
                player2_deck.append(player1_play)
            else:
                raise Exception('This should not happen!')

        # play the normal way
        elif player1_play > player2_play:
            player1_deck.append(player1_play)
            player1_deck.append(player2_play)
        elif player2_play > player1_play:
            player2_deck.append(player2_play)
            player2_deck.append(player1_play)
        else:
            raise Exception('This should not happen!')

    if len(player1_deck) == total_cards_count:
        return 1
    elif len(player2_deck) == total_cards_count:
        return 2
    else:
        raise Exception('This should not happen!')


def part_2(p1_deck, p2_deck):
    winner_deck = []
    winner = play_game(p1_deck, p2_deck)
    if winner == 1:
        print('Player 1')
        winner_deck = p1_deck
    elif winner == 2:
        print('Player 2')
        winner_deck = p2_deck

    winner_score = 0
    for i in range(1, len(winner_deck)+1):
        winner_score += i * winner_deck[-1*i]
    return winner_score


def get_result():
    p1_deck, p2_deck = get_data()

    # part 1
    tic = time.perf_counter()
    res1 = part_1(p1_deck.copy(), p2_deck.copy())
    toc = time.perf_counter()
    print(f"Part-1: {res1}, took {toc - tic:0.4f} seconds")

    # # part 2
    tic = time.perf_counter()
    res2 = part_2(p1_deck.copy(), p2_deck.copy())
    toc = time.perf_counter()
    print(f"Part-2: {res2}, took {toc - tic:0.4f} seconds")


# 34664
# 32018
get_result()
