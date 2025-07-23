import sqlite3

from app.models import Actor
ALLOWED_TABLES = {"actors"}


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        if table_name not in ALLOWED_TABLES:
            raise ValueError(f"Table name '{table_name}' is not allowed")
        self._connection = sqlite3.connect(db_name)
        self._table_name = table_name

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name} (first_name, "
            f" last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        actors_cursor = self._connection.execute(
            f"SELECT * FROM {self._table_name}"
        )
        return [
            Actor(*row) for row in actors_cursor
        ]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self._table_name} "
            f" SET first_name = ?, last_name = ? "
            f" WHERE id = ? ",
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self._table_name}  WHERE id = ?",
            (pk,)
        )
        self._connection.commit()

# if __name__ == "__main__":
#     manager = ActorManager("actors_DB.sqlite", "actors")
#     print(manager.all())
