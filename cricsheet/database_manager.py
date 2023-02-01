import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, Engine


class DatabaseManager:
    def __init__(
            self,
            db_host: str,
            db_port: str,
            db_username: str,
            db_password: str,
            db_name: str
    ):
        self.db_engine: Engine = create_engine(
            f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
        )

    def update_table(
            self,
            db_table_name: str,
            table: pd.DataFrame
    ):
        if not self.table_exists(db_table_name):
            self.create_table(db_table_name, table)

        table.to_sql(
            db_table_name,
            con=self.db_engine,
            if_exists="append"
        )

    def update_player_id_table(self):
        raise NotImplementedError()

    def update_player_match_table(self):
        raise NotImplementedError()

    def table_exists(
            self,
            db_table_name: str
    ):
        return sqlalchemy.inspect(self.db_engine).has_table(db_table_name)

    def create_table(
            self,
            db_table_name: str,
            table: pd.DataFrame
    ):
        table.head(n=0).to_sql(
            name=db_table_name,
            con=self.db_engine,
            if_exists="replace"
        )

    def delete_table(
            self,
            db_table_name: str
    ):
        raise NotImplementedError()

    def get_existing_match_ids(self):
        raise NotImplementedError()
