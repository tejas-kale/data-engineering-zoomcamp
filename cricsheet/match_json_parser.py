from pathlib import Path
import json

import pandas as pd
from geopy import Nominatim


class MatchJSONParser:
    def __init__(self, match_fp: str):
        """
        Class to parse and return specific data from a Cricsheet JSON file.

        :param match_fp: Path to JSON file that contains all data about
        a match.
        """
        self.match_file = match_fp
        with open(self.match_file, "r") as f:
            self.data = json.load(f)
        self.geolocator = Nominatim(user_agent="de_cricsheet")

        self.match_id = None

    @property
    def match_id(self) -> str:
        return self._match_id

    @match_id.setter
    def match_id(self, value: str = None):
        """
        Set match ID. If a value is provided, which will only be during unit tests,
        the specified value is set to be the match ID. Else, the name of the JSON
        file becomes the match ID.

        :param value: String value specifying match ID.
        :return: String denoting match ID.
        """
        if value:
            self._match_id = value
        else:
            self._match_id = Path(self.match_file).stem

    @property
    def balls_per_over(self):
        return self.data["info"]["balls_per_over"]

    @property
    def dates(self) -> list:
        return self.data["info"]["dates"]

    @property
    def venue(self) -> str:
        return self.data["info"]["venue"]

    @property
    def city(self) -> str:
        return self.data["info"]["city"]

    @property
    def country(self) -> str:
        return self.geolocator.geocode(
            self.city,
            language="en",
            addressdetails=True
        ).raw["address"]["country"]

    @property
    def team_1(self) -> str:
        return self.data["info"]["teams"][0]

    @property
    def team_2(self) -> str:
        return self.data["info"]["teams"][1]

    @property
    def home_team(self) -> str:
        if self.country in self.data["info"]["teams"]:
            return self.country

    @property
    def team_1_players(self) -> list:
        team_1_player_names: list = self.data["info"]["players"][self.team_1]
        s: str
        return [self.data["info"]["registry"]["people"][s]
                for s in team_1_player_names]

    @property
    def team_2_players(self) -> list:
        team_2_player_names: list = self.data["info"]["players"][self.team_2]
        s: str
        return [self.data["info"]["registry"]["people"][s]
                for s in team_2_player_names]

    @property
    def player_id_table(self) -> pd.DataFrame:
        match_players: list = (self.data["info"]["players"][self.team_1] +
                               self.data["info"]["players"][self.team_2])
        people_registry: dict = self.data["info"]["registry"]["people"]
        return pd.DataFrame({
            "player": match_players,
            "player_id": [people_registry[player]
                          for player in match_players],
            "match_id": self.match_id
        })

    @property
    def gender(self) -> str:
        return self.data["info"]["gender"]

    @property
    def season(self) -> str:
        return self.data["info"]["season"]

    @property
    def match_type(self) -> str:
        return self.data["info"]["match_type"]

    @property
    def team_type(self) -> str:
        return self.data["info"]["team_type"]

    @property
    def toss_winner(self) -> str:
        return self.data["info"]["toss"]["winner"]

    @property
    def toss_winner_decision(self) -> str:
        return self.data["info"]["toss"]["decision"]

    @property
    def winner(self) -> str:
        return self.data["info"]["outcome"]["winner"]

    @property
    def won_by_runs(self) -> int:
        return self.data["info"]["outcome"]["by"].get("runs", None)

    @property
    def won_by_wickets(self) -> int:
        return self.data["info"]["outcome"]["by"].get("wickets", None)

    @property
    def umpire_1(self) -> str:
        return self.data["info"]["officials"]["umpires"][0]

    @property
    def umpire_2(self) -> str:
        return self.data["info"]["officials"]["umpires"][1]

    @property
    def third_umpire(self) -> str:
        # TODO: Understand why reserve umpires are specified in a list.
        return self.data["info"]["officials"]["reserve_umpires"][0]

    @property
    def match_referee(self) -> str:
        # TODO: Understand why match referees are specified in a list.
        return self.data["info"]["officials"]["match_referees"][0]

    @property
    def first_innings_data(self) -> pd.DataFrame:
        """
        Ball-by-ball data of the first innings of a match. In a test match,
        it is the first innings of the team batting first.

        :return: Pandas dataframe holding ball-by-ball information about
        the innings
        """
        innings_idx: int = 0
        innings_raw_data: dict = self.data["innings"][innings_idx]
        batting_team: str = innings_raw_data["team"]

        return self._get_parsed_innings_data(
            innings_raw_data["overs"],
            batting_team,
            innings_idx
        )

    @property
    def second_innings_data(self) -> pd.DataFrame:
        """
        Ball-by-ball data of the second innings of a match. In a test match,
        it is the first innings of the team batting second.

        :return: Pandas dataframe holding ball-by-ball information about
        the innings
        """
        innings_idx: int = 1
        innings_raw_data: dict = self.data["innings"][innings_idx]
        batting_team: str = innings_raw_data["team"]

        return self._get_parsed_innings_data(
            innings_raw_data["overs"],
            batting_team,
            innings_idx
        )

    @property
    def third_innings_data(self) -> pd.DataFrame:
        """
        Ball-by-ball data of the third innings of a match. In a test match,
        it is the second innings of the team batting first.

        :return: Pandas dataframe holding ball-by-ball information about
        the innings
        """
        innings_idx: int = 2
        try:
            innings_raw_data: dict = self.data["innings"][2]
            batting_team: str = innings_raw_data["team"]

            return self._get_parsed_innings_data(
                innings_raw_data["overs"],
                batting_team,
                innings_idx
            )
        except IndexError:
            return pd.DataFrame({})

    @property
    def fourth_innings_data(self) -> pd.DataFrame:
        """
        Ball-by-ball data of the fourth innings of a match. In a test match,
        it is the second innings of the team batting second.

        :return: Pandas dataframe holding ball-by-ball information about
        the innings
        """
        innings_idx: int = 3

        try:
            innings_raw_data: dict = self.data["innings"][innings_idx]
            batting_team: str = innings_raw_data["team"]

            return self._get_parsed_innings_data(
                innings_raw_data["overs"],
                batting_team,
                innings_idx
            )
        except IndexError:
            return pd.DataFrame({})

    def _get_parsed_innings_data(self,
                                 innings_ball_by_ball_data: list,
                                 batting_team: str,
                                 innings_idx: int
                                 ) -> pd.DataFrame:
        innings_data: list = []
        overs_data: dict
        for overs_data in innings_ball_by_ball_data:
            dd: dict
            for dd in overs_data["deliveries"]:
                delivery_data: dict = {
                    "match_id": self.match_id,
                    # In cricket parlance, innings and overs are 1-indexed
                    "innings": innings_idx + 1,
                    "over": overs_data["over"] + 1,
                    "batting_team": batting_team
                }
                delivery_data.update(
                    self._get_parsed_delivery_data(dd)
                )
                innings_data.append(delivery_data.copy())

        return pd.DataFrame(innings_data)

    @staticmethod
    def _get_parsed_delivery_data(delivery_data: dict) -> dict:
        parsed_delivery_data: dict = {
            "batsman": delivery_data["batter"],
            "bowler": delivery_data["bowler"],
            "non_striker": delivery_data["non_striker"],
            "runs_by_batsman": delivery_data["runs"]["batter"],
            "extras_type": None,
            "runs_from_extras": delivery_data["runs"]["extras"],
            "dismissed_batsman": None,
            "dismissal_type": None,
            "fielders_in_dismissal": None
        }

        if "extras" in delivery_data:
            parsed_delivery_data["extras_type"] = list(delivery_data["extras"].keys())[0]

        if "wickets" in delivery_data:
            parsed_delivery_data["dismissed_batsman"] = delivery_data["wickets"][0]["player_out"]
            parsed_delivery_data["dismissal_type"] = delivery_data["wickets"][0]["kind"]
            parsed_delivery_data["fielders_in_dismissal"] = [fl["name"]
                                                             for fl in delivery_data["wickets"][0]["fielders"]]

        return parsed_delivery_data
