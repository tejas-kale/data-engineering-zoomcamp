from typing import Optional

LAST_MONTH_DATA_URL: str = "https://cricsheet.org/downloads/recently_played_30_csv2.zip"


class DataIngestionManager:
    def __init__(self, data_dir: Optional[str] = None):
        if data_dir:
            self.data_dir = data_dir

    def download_data(self):
        raise NotImplementedError()

    def match_ids(self):
        raise NotImplementedError()

    def ingest_data(self):
        """
        1. List match IDs in the new data.
        2. Fetch existing match IDs in the database.
        3. Get tables for each match from `MatchDataProcessor`.
        4. Update tables in the database.
        :return:
        """
        raise NotImplementedError()