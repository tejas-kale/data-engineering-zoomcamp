import json
import tempfile
from typing import Optional

import pandas as pd
import pytest

from cricsheet.match_json_parser import MatchJSONParser


def test_json_parser_returns_correct_match_id(sample_test_data: str):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        expected_test_match_id_suffix: str = "_sample"

        json_parser = MatchJSONParser(temp_file)

        assert json_parser.match_id.endswith(expected_test_match_id_suffix)

        json_parser.match_id = "another_id"
        assert json_parser.match_id == "another_id"


def test_json_parser_returns_correct_balls_per_over(sample_test_data: str):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        json_parser = MatchJSONParser(temp_file)

        expected_test_balls_per_over: int = 6

        assert json_parser.balls_per_over == expected_test_balls_per_over


def test_json_parser_returns_correct_dates(sample_test_data: str):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        json_parser = MatchJSONParser(temp_file)

        expected_test_dates: list = [
            "2022-01-01",
            "2022-01-02",
            "2022-01-03",
            "2022-01-04",
            "2022-01-05"
        ]

        assert json_parser.dates == expected_test_dates


def test_json_parser_returns_correct_venue(sample_test_data: str):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        json_parser = MatchJSONParser(temp_file)

        expected_test_venue: str = "Gymkhana Club Ground"

        assert json_parser.venue == expected_test_venue


def test_json_parser_returns_correct_city(sample_test_data: str):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        json_parser = MatchJSONParser(temp_file)

        expected_test_city: str = "Nairobi"

        assert json_parser.city == expected_test_city


def test_json_parser_returns_correct_country(sample_test_data: str):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        json_parser = MatchJSONParser(temp_file)

        expected_test_country: str = "Kenya"

        assert json_parser.country == expected_test_country


def test_json_parser_returns_correct_teams(sample_test_data: str):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        json_parser = MatchJSONParser(temp_file)

        expected_test_team_1: str = "Netherlands"
        expected_test_team_2: str = "Kenya"
        expected_test_home_team: str = "Kenya"

        assert json_parser.team_1 == expected_test_team_1
        assert json_parser.team_2 == expected_test_team_2
        assert json_parser.home_team == expected_test_home_team


def test_json_parser_returns_correct_player_id_table(sample_test_data: str):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        partial_expected_output: pd.DataFrame = pd.DataFrame({
            "player": ["AN Kervezee", "NA Statham", "RR Patel", "MA Ouma"],
            "player_id": ["id1", "id2", "id3", "id4"]
        })

        json_parser = MatchJSONParser(temp_file)
        assert json_parser.player_id_table["player"].equals(partial_expected_output["player"])
        assert json_parser.player_id_table["player_id"].equals(partial_expected_output["player_id"])
        assert json_parser.player_id_table["match_id"].str.endswith("_sample").all()


def test_json_parser_returns_correct_gender(sample_test_data: str):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        json_parser = MatchJSONParser(temp_file)

        expected_test_gender: str = "male"

        assert json_parser.gender == expected_test_gender


def test_json_parser_returns_correct_season(sample_test_data: str):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        json_parser = MatchJSONParser(temp_file)

        expected_test_season: str = "2009/10"

        assert json_parser.season == expected_test_season


def test_json_parser_returns_correct_match_and_team_types(sample_test_data: str):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        json_parser = MatchJSONParser(temp_file)

        expected_test_match_type: str = "MDM"
        expected_test_team_type: str = "international"

        assert json_parser.match_type == expected_test_match_type
        assert json_parser.team_type == expected_test_team_type


def test_json_parser_returns_correct_toss_information(sample_test_data: str):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        json_parser = MatchJSONParser(temp_file)

        expected_test_toss_winner: str = "Netherlands"
        expected_test_toss_winner_decision: str = "bat"

        assert json_parser.toss_winner == expected_test_toss_winner
        assert json_parser.toss_winner_decision == expected_test_toss_winner_decision


def test_json_parser_returns_correct_match_outcome(sample_test_data: str):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        json_parser = MatchJSONParser(temp_file)

        expected_test_winner: str = "Kenya"
        expected_test_won_by_runs: Optional[str] = None
        expected_test_won_by_wickets: Optional[int] = 5

        assert json_parser.winner == expected_test_winner
        assert json_parser.won_by_runs == expected_test_won_by_runs
        assert json_parser.won_by_wickets == expected_test_won_by_wickets


def test_json_parser_returns_correct_information_about_match_officials(sample_test_data: str):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        json_parser = MatchJSONParser(temp_file)

        expected_test_umpire_1: str = "Zameer Haider"
        expected_test_umpire_2: str = "SR Modi"
        expected_test_third_umpire: str = "D Angara"
        expected_test_match_referee: str = "D Govindjee"

        assert json_parser.umpire_1 == expected_test_umpire_1
        assert json_parser.umpire_2 == expected_test_umpire_2
        assert json_parser.third_umpire == expected_test_third_umpire
        assert json_parser.match_referee == expected_test_match_referee


def test_json_parser_returns_correct_team_players(sample_test_data: str):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        json_parser = MatchJSONParser(temp_file)

        expected_test_team_1_players: list = ["id1", "id2"]
        expected_test_team_2_players: list = ["id3", "id4"]

        assert json_parser.team_1_players == expected_test_team_1_players
        assert json_parser.team_2_players == expected_test_team_2_players


@pytest.mark.parametrize(
    "innings_key, expected_output",
    [
        pytest.param(
            "first_innings_data",
            pd.DataFrame({
                "innings": [1] * 2,
                "over": [1] * 2,
                "batting_team": ["Netherlands"] * 2,
                "batsman": ["AN Kervezee"] * 2,
                "bowler": ["NN Odhiambo"] * 2,
                "non_striker": ["ES Szwarczynski"] * 2,
                "runs_by_batsman": [0, 1],
                "extras_type": [None, "wides"],
                "runs_from_extras": [0, 1],
                "dismissed_batsman": [None] * 2,
                "dismissal_type": [None] * 2,
                "fielders_in_dismissal": [None] * 2
            }),
            id="first innings"
        ),
        pytest.param(
            "second_innings_data",
            pd.DataFrame({
                "innings": [2] * 2,
                "over": [1] * 2,
                "batting_team": ["Kenya"] * 2,
                "batsman": ["E Otieno"] * 2,
                "bowler": ["B Zuiderent"] * 2,
                "non_striker": ["NN Odhiambo"] * 2,
                "runs_by_batsman": [0] * 2,
                "extras_type": [None] * 2,
                "runs_from_extras": [0] * 2,
                "dismissed_batsman": [None, "E Otieno"],
                "dismissal_type": [None, "caught"],
                "fielders_in_dismissal": [None, ["AN Kervezee"]]
            }),
            id="second innings"
        ),
        pytest.param(
            "third_innings_data",
            pd.DataFrame({
                "innings": [3] * 2,
                "over": [1] * 2,
                "batting_team": ["Netherlands"] * 2,
                "batsman": ["AN Kervezee"] * 2,
                "bowler": ["NN Odhiambo"] * 2,
                "non_striker": ["ES Szwarczynski"] * 2,
                "runs_by_batsman": [6, 0],
                "extras_type": [None] * 2,
                "runs_from_extras": [0] * 2,
                "dismissed_batsman": [None] * 2,
                "dismissal_type": [None] * 2,
                "fielders_in_dismissal": [None] * 2
            }),
            id="third innings"
        ),
        pytest.param(
            "fourth_innings_data",
            pd.DataFrame({
                "innings": [4] * 2,
                "over": [1] * 2,
                "batting_team": ["Kenya"] * 2,
                "batsman": ["E Otieno", "NN Odhiambo"],
                "bowler": ["B Zuiderent"] * 2,
                "non_striker": ["NN Odhiambo", "E Otieno"],
                "runs_by_batsman": [1, 0],
                "extras_type": [None] * 2,
                "runs_from_extras": [0] * 2,
                "dismissed_batsman": [None] * 2,
                "dismissal_type": [None] * 2,
                "fielders_in_dismissal": [None] * 2
            }),
            id="fourth innings"
        )
    ]
)
def test_json_parser_returns_correct_innings_data(
        sample_test_data: str,
        innings_key: str,
        expected_output: pd.DataFrame
):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file: str = tempfile.mkstemp(suffix="_sample.json", dir=temp_dir)[1]
        with open(temp_file, "w") as f:
            f.write(sample_test_data)

        json_parser = MatchJSONParser(temp_file)
        innings_data: pd.DataFrame = json_parser.__getattribute__(innings_key)

        expected_output.insert(0, "match_id", json_parser.match_id, allow_duplicates=True)

        assert isinstance(innings_data, pd.DataFrame)
        assert innings_data.equals(expected_output)


def test__get_parsed_innings_data_returns_correct_dataframe(sample_test_data: str):
    parsed_sample_test_data: dict = json.loads(sample_test_data)
    innings_idx: int = 0
    innings_1_ball_by_ball_data: list = parsed_sample_test_data["innings"][innings_idx]["overs"]
    batting_team: str = parsed_sample_test_data["innings"][innings_idx]["team"]

    json_parser = object.__new__(MatchJSONParser)
    json_parser.match_id = "sample_match_id"
    innings_data: pd.DataFrame = json_parser._get_parsed_innings_data(
        innings_1_ball_by_ball_data,
        batting_team,
        innings_idx
    )

    assert isinstance(innings_data, pd.DataFrame)
    assert len(innings_data) == 2
    assert all(innings_data["innings"] == 1)
    assert all(innings_data["over"] == 1)
    assert all(innings_data["batting_team"] == "Netherlands")
    assert all(innings_data["batsman"] == "AN Kervezee")
    assert all(innings_data["bowler"] == "NN Odhiambo")
    assert all(innings_data["non_striker"] == "ES Szwarczynski")
    assert innings_data["runs_by_batsman"].iloc[1] == 1
    assert innings_data["extras_type"].iloc[1] == "wides"
    assert innings_data["runs_from_extras"].iloc[1] == 1
    assert innings_data["dismissed_batsman"].isnull().all()
    assert innings_data["dismissal_type"].isnull().all()
    assert innings_data["fielders_in_dismissal"].isnull().all()


@pytest.mark.parametrize(
    "innings_idx, delivery_idx, expected_output",
    [
        pytest.param(
            0,
            0,
            {
                "batsman": "AN Kervezee",
                "bowler": "NN Odhiambo",
                "non_striker": "ES Szwarczynski",
                "runs_by_batsman": 0,
                "extras_type": None,
                "runs_from_extras": 0,
                "dismissed_batsman": None,
                "dismissal_type": None,
                "fielders_in_dismissal": None
            },
            id="default"),
        pytest.param(
            0,
            1,
            {
                "batsman": "AN Kervezee",
                "bowler": "NN Odhiambo",
                "non_striker": "ES Szwarczynski",
                "runs_by_batsman": 1,
                "extras_type": "wides",
                "runs_from_extras": 1,
                "dismissed_batsman": None,
                "dismissal_type": None,
                "fielders_in_dismissal": None
            },
            id="extras"),
        pytest.param(
            1,
            1,
            {
                "batsman": "E Otieno",
                "bowler": "B Zuiderent",
                "non_striker": "NN Odhiambo",
                "runs_by_batsman": 0,
                "extras_type": None,
                "runs_from_extras": 0,
                "dismissed_batsman": "E Otieno",
                "dismissal_type": "caught",
                "fielders_in_dismissal": ["AN Kervezee"]
            },
            id="wickets")
    ]
)
def test__get_parsed_delivery_data(
        sample_test_data: str,
        innings_idx: int,
        delivery_idx: int,
        expected_output: dict
):
    parsed_sample_test_data: dict = json.loads(sample_test_data)

    json_parser = object.__new__(MatchJSONParser)
    json_parser.match_id = "sample_match_id"

    # Currently, the sample test data only has one over per innings.
    delivery_data: dict = parsed_sample_test_data["innings"][innings_idx]["overs"][0]["deliveries"][delivery_idx]
    parsed_delivery_data: dict = json_parser._get_parsed_delivery_data(delivery_data)
    assert parsed_delivery_data == expected_output
