import os

import pymysql
from qqbot.core.util.yaml_util import YamlUtil


class MedalCabinet:
    db = None
    medal_dict = {}

    def __init__(self):
        config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "../config.yaml"))
        database_info = config["mysql"]["medal"]
        self.db = pymysql.connect(host=database_info["host"],
                                  user=database_info["user"],
                                  password=database_info["password"],
                                  database=database_info["database"])
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM medal")
        results = cursor.fetchall()
        for row in results:
            self.medal_dict[row[0]] = f"[{row[1][2:]}]"
        # generate medal_id and medal_name dict, remove color code ([:2])

    async def get_user_medals(self, player_name)->list:
        cursor = self.db.cursor()
        cursor.execute(f"SELECT * FROM player_medal WHERE player_id = '{player_name}'")
        results = cursor.fetchall()
        medals = []
        for row in results:
            medals.append(self.medal_dict[row[2]])
        return medals
