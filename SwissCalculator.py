class Player(object):
    def __init__(self, playerNum) -> None:
        super().__init__()
        self.playerNum = playerNum
        self.games = 0
        self.wins = 0

class Tournament(object):
    def __init__(self, rounds) -> None:
        super().__init__()
        self.players = []
        self.maxRounds = rounds

    def GeneratePlayers(self, count):
        for i in range(count):
            self.players.append(Player(i))

    def PlayerCount(self):
        return len(self.players)

    def FindPlayerCountWithWins(self, winCount):
        playerCount = 0
        for player in self.players:
            if player.wins == winCount:
                playerCount += 1

        return playerCount

    def FindPlayerCountWithMinimumWins(self, winCount):
        playerCount = 0
        for player in self.players:
            if player.wins >= winCount:
                playerCount += 1

        return playerCount

    def AssignXWinsToPlayersWithWinCount(self, winCount, playerCount):
        for player in self.players:
            if player.wins == winCount:
                if playerCount > 0:
                    player.wins += 1
                    playerCount -= 1

        return playerCount

    def RunTournament(self):
        for round in range(self.maxRounds):
            # print(f"Round {round + 1}")
            pairDownActive = False
            pairDownWin = True
            for winCount in range(round, -1, -1):
                count = self.FindPlayerCountWithWins(winCount)
                winnerCount = 0
                # print(f"Round {round + 1} - Wins {winCount} - Players {count}")
                
                if pairDownActive:
                    count -= 1
                    if not pairDownWin:
                        winnerCount += 1
                    pairDownActive = False

                winnerCount += count // 2

                if (count % 2):
                    pairDownActive = True
                    if pairDownWin or winCount == 0:
                        winnerCount += 1

                self.AssignXWinsToPlayersWithWinCount(winCount, winnerCount)
                # print(f"Round {round + 1} - Wins {winCount} - Players {count} - Assigned {winnerCount}")

    def ReportTournamentStats(self, maxLosses):
        winRecord = ""
        for winCount in range(self.maxRounds - maxLosses, self.maxRounds):
            winnerCount = self.FindPlayerCountWithWins(winCount)
            minWinnerCount = self.FindPlayerCountWithMinimumWins(winCount)
            minWinnerPercentage = (minWinnerCount / self.PlayerCount())
            # print(f"Checking {winCount} {winnerCount} {minWinnerCount} {minWinnerPercentage}")
            # if 0.1 <= minWinnerPercentage <= 0.2 and winnerCount > 0:
            winRecord = f"{winRecord} {winCount} Wins, - {minWinnerCount}/{self.PlayerCount()} {minWinnerPercentage * 100}%"

        if len(winRecord):
            winRecord = f"{self.maxRounds} round tournament with {len(self.players)} players: {winRecord}"
            print(winRecord)

for roundCount in range(6,7):
    for playerCount in range(9,300):
        tournament = Tournament(roundCount)
        tournament.GeneratePlayers(playerCount)
        tournament.RunTournament()
        tournament.ReportTournamentStats(2)