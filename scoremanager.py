import sqlite3 as db


class ScoreManager:
    schools = {}
    drunkest_school = None
    high_scores = {}
    best_schools = {}
    score = 0
    games = {}

    def __init__(self, dbfile):
        self.conn = db.connect(dbfile)
        self._load_games()

    def get_schools(self):
        if len(self.schools) == 0:
            cursor = self.conn.execute("SELECT school_id, school_name FROM school ORDER BY school_name")
            for row in cursor:
                self.schools[row[0]] = row[1]
        return self.schools

    def _load_games(self):
        cursor = self.conn.execute("""SELECT school.school_id, score
                                  FROM game
                                  JOIN school ON game.school_id = school.school_id""")
        for r in cursor.fetchall():
            self._add_game(r[0], r[1])

    def _add_game(self, school, score):
        if not school in self.games:
            self.games[school] = []
        if score:
            self.games[school].append(score)

    def get_school_id(self, name):
        return [i for i, n in self.get_schools().items() if n == name][0]

    def get_drunkest_schools(self):
        game_count = [(self.get_schools()[s], len(g)) for s, g in self.games.items()]
        game_count = sorted(game_count, key=lambda tup: tup[1], reverse=True)
        return game_count[:3]

    def get_total_school_score(self):
        scores = [(self.get_schools()[s], sum(g)) for s, g in self.games.items()]
        scores = sorted(scores, key=lambda tup: tup[1], reverse=True)
        return scores[:3]

    def get_high_scores(self):
        allgames = []
        for school, scores in self.games.items():
            for score in scores:
                allgames.append((school, score))
        allgames = sorted(allgames, key=lambda tup: tup[1], reverse=True)
        return [(self.get_schools()[school], score) for school, score in allgames][:3]

    def get_average_score(self):
        scores = [(self.get_schools()[s], int(sum(g)/(len(g)+0.000001))) for s, g in self.games.items()]
        scores = sorted(scores, key=lambda tup: tup[1], reverse=True)
        return scores[:3]

    def get_score(self):
        return self.score

    def increment_score(self, score):
        self.score += score
        #print self.score

    def save_game(self, school_id):
        self.conn.execute("INSERT INTO game (school_id, score) VALUES (?, ?)", (school_id, self.score))
        self._add_game(school_id, self.score)
        self.conn.commit()
        self.score = 0

