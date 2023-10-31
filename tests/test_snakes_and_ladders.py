from snakes_and_ladders import random_maker, Player


def test_random_maker():
    snakes = 4
    board_size = 50
    result = [(random_maker([], board_size), random_maker([], board_size)) for _ in range(0, snakes)]
    assert len(result) == snakes
    assert len(result[0]) == 2


def test_player():
    name = 'test_player'
    player = Player(name)
    player.roll_dice()
    assert player.name == name.capitalize()
    assert player.position == player.roll_result
