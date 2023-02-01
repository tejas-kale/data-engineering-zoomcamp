import json

import pytest


@pytest.fixture()
def sample_test_data() -> str:
    return json.dumps(
        {
            "meta": {
                "data_version": "1.0.0",
                "created": "2023-01-01",
                "revision": 1
            },
            "info": {
                "balls_per_over": 6,
                "city": "Nairobi",
                "dates": [
                    "2022-01-01",
                    "2022-01-02",
                    "2022-01-03",
                    "2022-01-04",
                    "2022-01-05"
                ],
                "gender": "male",
                "match_type": "MDM",
                "officials": {
                    "match_referees": ["D Govindjee"],
                    "reserve_umpires": ["D Angara"],
                    "umpires": ["Zameer Haider", "SR Modi"]
                },
                "outcome": {"winner": "Kenya", "by": {"wickets": 5}},
                "players": {
                    "Netherlands": [
                        "AN Kervezee",
                        "NA Statham"
                    ],
                    "Kenya": [
                        "RR Patel",
                        "MA Ouma"
                    ]
                },
                "registry": {
                    "people": {
                        "AN Kervezee": "id1",
                        "NA Statham": "id2",
                        "RR Patel": "id3",
                        "MA Ouma": "id4"
                    }
                },
                "season": "2009/10",
                "team_type": "international",
                "teams": ["Netherlands", "Kenya"],
                "toss": {"decision": "bat", "winner": "Netherlands"},
                "venue": "Gymkhana Club Ground",
            },
            "innings": [
                {
                    "team": "Netherlands",
                    "overs": [
                        {
                            "over": 0,
                            "deliveries": [
                                {
                                    "batter": "AN Kervezee",
                                    "bowler": "NN Odhiambo",
                                    "non_striker": "ES Szwarczynski",
                                    "runs": {
                                        "batter": 0,
                                        "extras": 0,
                                        "total": 0
                                    }
                                },
                                {
                                    "batter": "AN Kervezee",
                                    "bowler": "NN Odhiambo",
                                    "non_striker": "ES Szwarczynski",
                                    "extras": {"wides": 1},
                                    "runs": {
                                        "batter": 1,
                                        "extras": 1,
                                        "total": 2
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "team": "Kenya",
                    "overs": [
                        {
                            "over": 0,
                            "deliveries": [
                                {
                                    "batter": "E Otieno",
                                    "bowler": "B Zuiderent",
                                    "non_striker": "NN Odhiambo",
                                    "runs": {
                                        "batter": 0,
                                        "extras": 0,
                                        "total": 0
                                    }
                                },
                                {
                                    "batter": "E Otieno",
                                    "bowler": "B Zuiderent",
                                    "non_striker": "NN Odhiambo",
                                    "wickets": [
                                        {
                                            "player_out": "E Otieno",
                                            "fielders": [{
                                                "name": "AN Kervezee"
                                            }],
                                            "kind": "caught"
                                        }
                                    ],
                                    "runs": {
                                        "batter": 0,
                                        "extras": 0,
                                        "total": 0
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "team": "Netherlands",
                    "overs": [
                        {
                            "over": 0,
                            "deliveries": [
                                {
                                    "batter": "AN Kervezee",
                                    "bowler": "NN Odhiambo",
                                    "non_striker": "ES Szwarczynski",
                                    "runs": {
                                        "batter": 6,
                                        "extras": 0,
                                        "total": 0
                                    }
                                },
                                {
                                    "batter": "AN Kervezee",
                                    "bowler": "NN Odhiambo",
                                    "non_striker": "ES Szwarczynski",
                                    "runs": {
                                        "batter": 0,
                                        "extras": 0,
                                        "total": 0
                                    }
                                }
                            ]
                        }
                    ]
                },
                {
                    "team": "Kenya",
                    "overs": [
                        {
                            "over": 0,
                            "deliveries": [
                                {
                                    "batter": "E Otieno",
                                    "bowler": "B Zuiderent",
                                    "non_striker": "NN Odhiambo",
                                    "runs": {
                                        "batter": 1,
                                        "extras": 0,
                                        "total": 1
                                    }
                                },
                                {
                                    "batter": "NN Odhiambo",
                                    "bowler": "B Zuiderent",
                                    "non_striker": "E Otieno",
                                    "runs": {
                                        "batter": 0,
                                        "extras": 0,
                                        "total": 0
                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    )
