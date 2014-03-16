import sqlite3 as db


class ScoreManager:
    schools = {}
    drunkest_school = None
    high_scores = {}
    best_schools = {}
    score = 0

    def __init__(self, dbfile):
        self.conn = db.connect(dbfile)

    def get_schools(self):
        if len(self.schools) == 0:
            cursor = self.conn.execute("SELECT school_id, school_name FROM school ORDER BY school_name")
            for row in cursor:
                self.schools[row[0]] = row[1]
        return self.schools

    def get_school_id(self, name):
        return [i for i, n in self.get_schools().items() if n == name][0]

    def get_drunkest_school(self):
        if self.drunkest_school == None:
            self.update_drunkest_school()
        return self.drunkest_school

    def get_high_scores(self):
        if len(self.high_scores) == 0:
            self.update_high_scores()
        return self.high_scores

    def get_best_schools(self):
        if len(self.best_schools) == 0:
            self.update_best_schools()
        return self.best_schools

    def get_score(self):
        return self.score

    def increment_score(self, score):
        self.score += score
        #print self.score

    def save_game(self, school_id):
        self.conn.execute("INSERT INTO game (school_id, score) VALUES (?, ?)", (school_id, self.score))
        self.conn.commit()
        self.update_drunkest_school()
        self.update_high_scores()
        self.update_best_schools()
        self.score = 0

    def update_drunkest_school(self):
        cursor = self.conn.execute("""SELECT school_name, count(*) games
                                      FROM game
                                      JOIN school ON game.school_id = school.school_id
                                      GROUP BY school.school_id
                                      ORDER BY games DESC
                                      LIMIT 1""")
        self.drunkest_school = cursor.fetchone()[0]

    def update_best_schools(self):
        cursor = self.conn.execute("""SELECT school_name, sum(score) total
                                      FROM game
                                      JOIN school ON game.school_id = school.school_id
                                      GROUP BY school.school_id
                                      ORDER BY total DESC
                                      LIMIT 3""")
        for row in cursor:
            self.best_schools[row[0]] = row[1]

    def update_high_scores(self):
        cursor = self.conn.execute("""SELECT school_name, score
                                      FROM game
                                      JOIN school ON game.school_id = school.school_id
                                      ORDER BY score DESC
                                      LIMIT 3;""")
        for row in cursor:
            self.high_scores[row[0]] = row[1]

