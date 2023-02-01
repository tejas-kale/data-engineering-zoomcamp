from typing import Dict, Union, List

import pandas as pd

from cricsheet.match_json_parser import MatchJSONParser


class MatchDataProcessor:
    def __init__(self, match_fp: str):
        """
        Constructor.

        :param match_fp: Path to the JSON file containing match data
        """
        self.match_json_parser = MatchJSONParser(match_fp)

    def get_match_info(self) -> Dict[str, Union[str, int, List[str]]]:
        """
        Construct a table (with one row) of all match info.

        :return:
        """
        return {
            "match_id": self.match_json_parser.match_id,
            "balls_per_over": self.match_json_parser.balls_per_over,
            "dates": self.match_json_parser.dates,
            "venue": self.match_json_parser.venue,
            "city": self.match_json_parser.city,
            "country": self.match_json_parser.country,
            "team_1": self.match_json_parser.team_1,
            "team_1_players": self.match_json_parser.team_1_players,
            "team_2": self.match_json_parser.team_2,
            "team_2_players": self.match_json_parser.team_2_players,
            "home_team": self.match_json_parser.home_team,
            "gender": self.match_json_parser.gender,
            "season": self.match_json_parser.season,
            "team_type": self.match_json_parser.team_type,
            "toss_winner": self.match_json_parser.toss_winner,
            "toss_winner_decision": self.match_json_parser.toss_winner_decision,
            "match_type": self.match_json_parser.match_type,
            "winner": self.match_json_parser.winner,
            "won_by_runs": self.match_json_parser.won_by_runs,
            "won_by_wickets": self.match_json_parser.won_by_wickets,
            "umpire_1": self.match_json_parser.umpire_1,
            "umpire_2": self.match_json_parser.umpire_2,
            "third_umpire": self.match_json_parser.third_umpire,
            "match_referee": self.match_json_parser.match_referee
        }

    def get_ball_by_ball_table(self) -> pd.DataFrame:
        """
        Construct ball-by-ball data of all innings in a match.
        
        :return:
        """
        return pd.concat([
            self.match_json_parser.first_innings_data,
            self.match_json_parser.second_innings_data,
            self.match_json_parser.third_innings_data,
            self.match_json_parser.fourth_innings_data
        ]).reset_index(drop=True)


