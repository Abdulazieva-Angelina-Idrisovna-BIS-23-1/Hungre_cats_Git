class Stats():
    """отслеживание статистики"""

    def __init__(self):
        """инициализация статистики"""
        self.reset_stats()
        self.go_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """ статистика, изменяющаяся во время процесса самой игры"""
        self.mcs_left = 2
        self.score = 0