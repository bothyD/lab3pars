import sqlite3
from news import News

class NewsMethods():
    newsList: list = []

    def add_new_in_list(self, newObj):
        self.newsList.append(newObj)

    def createDB(self):
        conn = sqlite3.connect('pars_news.db')
        conn.execute("""CREATE TABLE IF NOT EXISTS news(
            name_new TEXT,
            name_rubric TEXT,
            ref_new TEXT,
            date_created TEXT,
            ref_site TEXT
                        );
        """)    
        conn.close()

    def insertDB(self):
        conn = sqlite3.connect('pars_news.db')

        for el in self.newsList:   
            conn.execute(f"INSERT INTO news(name_new, name_rubric, ref_new, date_created, ref_site) VALUES(?, ?, ?, ?, ?);", 
                        (el.nameNew, el.rubric, el.refNew, el.date, el.refSite))
        conn.commit()
        conn.close()

    def readDB(self):
        print("data in DB\n")
        conn = sqlite3.connect('pars_news.db')
        cursor = conn.execute("""SELECT * FROM news""")
        records = cursor.fetchall()
        for row in records:
            print(f"name new: {row[0]}, \nrubric: {row[1]}, \nref new: {row[2]}, \ndate created: {row[3]}\n")
        conn.close()
        print("\ndata in DB")
    
    def clearDB(self):
        conn = sqlite3.connect('pars_news.db')
        conn.execute("""DELETE FROM news""")
        conn.commit()
        conn.close()