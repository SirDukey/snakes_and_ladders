import random


class Player:
    def __init__(self, name: str):
        self.name = name.capitalize()
        self.position = 0
        self.board_size = 0

    def __move(self, move_steps: int):
        self.new_position = self.position + move_steps
        print(f'moving from {self.position} to '
              f'{self.board_size if self.new_position > self.board_size else self.new_position}')
        self.position = self.new_position

    def roll_dice(self):
        roll_result = random.randint(1, 6)
        print(f'{self.name} has rolled a {roll_result}, ', end='')
        self.__move(roll_result)


class SnakesAndLadders:
    """A snakes and ladders board game

    SnakesAndLadders(['mike', 'josh'])
    """
    def __init__(self, players: list, board_size: int = 50):
        self.players = players or []
        self.board_size = board_size
        self.snakes = [(3, 16), (25, 38), (9, 42), (19, 24)]
        self.ladders = [(8, 20), (17, 31), (23, 35), (33, 47)]
        self.finished_player = None

        print('Welcome to Snakes & Ladders')
        print(f'There are {len(self.players)} players today and the board size is {self.board_size}')
        begin = input("Press return to start the game or 'q' at any time during the game to quit... ")
        if begin != 'q':
            if self.players:
                for idx, name in enumerate(self.players):
                    player = Player(name)
                    player.board_size = self.board_size
                    self.players[idx] = player
            self.start()
        else:
            print('Until next time, goodbye')

    def check_for_snake(self, player: Player):
        for snake in self.snakes:
            snake_tail, snake_head = snake
            if player.position == snake_head:
                print(f'Oh no! {player.name} has reached a snake!! moving down to position {snake_tail}')
                player.position = snake_tail

    def check_for_ladder(self, player: Player):
        for ladder in self.ladders:
            ladder_bottom, ladder_top = ladder
            if player.position == ladder_bottom:
                print(f'Hooray! {player.name} has reached a ladder, moving up to position {ladder_top}')
                player.position = ladder_top

    def start(self):
        while self.players:
            for player in self.players:
                player.roll_dice()
                self.check_for_snake(player)
                self.check_for_ladder(player)
                if player.position >= self.board_size:
                    print(f'Congratulations {player.name} has won the game!!!')
                    self.players = None
                    break
                choice = input("press return continue the next player... ")
                if choice == 'q':
                    print('thanks for playing snakes and ladders!')
                    self.players = None
                    break
