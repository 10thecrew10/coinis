from typing import List, Tuple
import random


class Tournament:
    def __init__(self, title: str = '', players: List[Tuple[str, int]] = [], rounds: int = 0):
        self._title = title
        self._players = players
        self._rounds = rounds

    def __str__(self):
        return f'Title: {self.title}, players: {self.players}'

    def add_player(self, name: str):
        self.players.append((name, 0))

    def del_player(self, name: str):
        found = [x for x in self.players if x[0] == name]
        if found:
            self.players.remove(found[0])

    def find_best_player(self):
        found = max(self.players, key=lambda x: x[1])
        if found:
            print(found[0])

    def begin_round(self):
        p1, p2 = random.sample(self.players, 2)
        if p1[1] < p2[1]:
            p1, p2 = p2, p1
        if random.random() < 0.6:
            print(f'Pobjedio je {p1[0]}. Ucestvovali su {p1[0]} i {p2[0]}')
        else:
            print(f'Pobjedio je {p2[0]}. Ucestvovali su {p1[0]} i {p2[0]}')
        self.rounds += 1

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value:
            self._title = value

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value):
        if value:
            self._players = value

    @property
    def rounds(self):
        return self._rounds

    @rounds.setter
    def rounds(self, value):
        if 0 < value < 10:
            self._rounds = value


if __name__ == "__main__":
    t = Tournament('Katowice 2018', [('Bojo', 3), ('Marko', 5), ('Vulan', 7)], 5)
    t.add_player('Vido')
    print(t)
    t.find_best_player()
    t.del_player('Vulan')
    print(t)
    t.begin_round()
    t.begin_round()
    t.begin_round()