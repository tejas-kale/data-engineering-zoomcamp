import tempfile
from pathlib import Path
from typing import Optional

import pandas as pd

from cricsheet.match_data_processor import MatchDataProcessor


def test_get_match_info(sample_test_data: str):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        expected_test_match_id_suffix: str = "_sample"
        expected_test_balls_per_over: int = 6
        expected_test_city: str = "Nairobi"
        expected_test_dates: list = [
            "2022-01-01",
            "2022-01-02",
            "2022-01-03",
            "2022-01-04",
            "2022-01-05"
        ]
        expected_test_gender: str = "male"
        expected_test_match_type: str = "MDM"
        expected_test_umpire_1: str = "Zameer Haider"
        expected_test_umpire_2: str = "SR Modi"
        expected_test_third_umpire: str = "D Angara"
        expected_test_match_referee: str = "D Govindjee"
        expected_test_winner: str = "Kenya"
        expected_test_won_by_runs: Optional[int] = None
        expected_test_won_by_wickets: Optional[int] = 5
        expected_test_team_1: str = "Netherlands"
        expected_test_team_1_players: list = ["id1", "id2"]
        expected_test_team_2: str = "Kenya"
        expected_test_team_2_players: list = ["id3", "id4"]
        expected_test_season: str = "2009/10"
        expected_test_team_type: str = "international"
        expected_test_toss_winner: str = "Netherlands"
        expected_test_toss_winner_decision: str = "bat"
        expected_test_venue: str = "Gymkhana Club Ground"

        match_data_manager = MatchDataProcessor(temp_file)
        match_info_row: dict = match_data_manager.get_match_info()

        assert isinstance(match_info_row, dict)
        assert match_info_row["match_id"].endswith(expected_test_match_id_suffix)
        assert match_info_row["balls_per_over"] == expected_test_balls_per_over
        assert match_info_row["city"] == expected_test_city
        assert match_info_row["dates"] == expected_test_dates
        assert match_info_row["gender"] == expected_test_gender
        assert match_info_row["match_type"] == expected_test_match_type
        assert match_info_row["umpire_1"] == expected_test_umpire_1
        assert match_info_row["umpire_2"] == expected_test_umpire_2
        assert match_info_row["third_umpire"] == expected_test_third_umpire
        assert match_info_row["match_referee"] == expected_test_match_referee
        assert match_info_row["winner"] == expected_test_winner
        assert match_info_row["won_by_runs"] == expected_test_won_by_runs
        assert match_info_row["won_by_wickets"] == expected_test_won_by_wickets
        assert match_info_row["team_1"] == expected_test_team_1
        assert match_info_row["team_1_players"] == expected_test_team_1_players
        assert match_info_row["team_2"] == expected_test_team_2
        assert match_info_row["team_2_players"] == expected_test_team_2_players
        assert match_info_row["season"] == expected_test_season
        assert match_info_row["team_type"] == expected_test_team_type
        assert match_info_row["toss_winner"] == expected_test_toss_winner
        assert match_info_row["toss_winner_decision"] == expected_test_toss_winner_decision
        assert match_info_row["venue"] == expected_test_venue


def test_get_ball_by_ball_data(sample_test_data):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        match_data_manager = MatchDataProcessor(temp_file)
        ball_by_ball_table: pd.DataFrame = match_data_manager.get_ball_by_ball_table()

        expected_output: pd.DataFrame = pd.DataFrame({
            "match_id": [Path(temp_file).stem] * 8,
            "innings": [1, 1, 2, 2, 3, 3, 4, 4],
            "over": [1] * 8,
            "batting_team": ["Netherlands", "Netherlands", "Kenya", "Kenya",
                             "Netherlands", "Netherlands", "Kenya", "Kenya"],
            "batsman": ["AN Kervezee", "AN Kervezee", "E Otieno", "E Otieno",
                        "AN Kervezee", "AN Kervezee", "E Otieno", "NN Odhiambo"],
            "bowler": ["NN Odhiambo", "NN Odhiambo", "B Zuiderent", "B Zuiderent",
                       "NN Odhiambo", "NN Odhiambo", "B Zuiderent", "B Zuiderent"],
            "non_striker": ["ES Szwarczynski", "ES Szwarczynski", "NN Odhiambo", "NN Odhiambo",
                            "ES Szwarczynski", "ES Szwarczynski", "NN Odhiambo", "E Otieno"],
            "runs_by_batsman": [0, 1, 0, 0, 6, 0, 1, 0],
            "extras_type": [None, "wides", None, None, None, None, None, None],
            "runs_from_extras": [0, 1, 0, 0, 0, 0, 0, 0],
            "dismissed_batsman": [None, None, None, "E Otieno", None, None, None, None],
            "dismissal_type": [None, None, None, "caught", None, None, None, None],
            "fielders_in_dismissal": [None, None, None, ["AN Kervezee"], None, None, None, None]
        })

        assert ball_by_ball_table.equals(expected_output)
