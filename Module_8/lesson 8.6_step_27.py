from dataclasses import dataclass, field


@dataclass(order=True)
class FootballPlayer:
    name: str=field(compare=False)
    surname: str=field(compare=False)
    value: int=field(repr=False)



@dataclass
class FootballTeam:
    name: str
    players: list= field(default_factory=list, repr=False, compare=False)


    def add_players(self, *args:FootballPlayer):
        # [self.players.append(player) for player in args]
        self.players.extend(args)

# INPUT DATA:

# TEST_1:
player = FootballPlayer('Kylian', 'Mbappe', 180000000)

print(player)
print(player.name)
print(player.surname)
print(player.value)

# TEST_2:
player1 = FootballPlayer('Jude', 'Bellingham', 120000000)
player2 = FootballPlayer('Vinicius', 'Junior', 120000000)
player3 = FootballPlayer('Kylian', 'Mbappe', 180000000)

print(player1 == player2)
print(player1 == player3)
print(player1 > player3)
print(player1 < player3)

# TEST_3:
team = FootballTeam('PSG')

print(team)
print(team.name)
print(team.players)

team.add_players(FootballPlayer('Kylian', 'Mbappe', 180000000))
print(team.players)

# TEST_4:
team1 = FootballTeam('PSG')
team2 = FootballTeam('PSG')
team3 = FootballTeam('Arsenal')

player1 = FootballPlayer('Jude', 'Bellingham', 120000000)
player2 = FootballPlayer('Vinicius', 'Junior', 110000000)
player3 = FootballPlayer('Kylian', 'Mbappe', 180000000)

team1.add_players(player1)
team2.add_players(player2)
team3.add_players(player3)

print(team1 == team2)
print(team1 != team2)
print(team1 == team3)
print(team1 != team3)

# TEST_5:
player1 = FootballPlayer('Ronaldo', '', 20000000)
player2 = FootballPlayer('Lothar', 'Matthaus', 250000000)
player3 = FootballPlayer('Xavi', 'Simons', 54000000)
player4 = FootballPlayer('Paolo', 'Maldini', 28000000)
player5 = FootballPlayer('Лев', 'Яшин', 200000000)
player6 = FootballPlayer('Diego', 'Maradona', 305000000)
player7 = FootballPlayer('Lionel', 'Messi', 180000000)
player8 = FootballPlayer('Kristiano','Ronaldo',10000000)

team = FootballTeam('Best')
print(team.name)

team.add_players(player1, player2, player3, player4, player5, player6, player7, player8)
print(team.players)