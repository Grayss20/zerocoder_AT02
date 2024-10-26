import pytest
from m3 import init_db, get_user, add_user


@pytest.fixture
def db_conn():
    conn = init_db()
    yield conn
    conn.close()


def test_add_and_get_users(db_conn):
    add_user(db_conn, "Sasha", 30)
    user = get_user(db_conn, "Sasha")
    assert user == (1, "Sasha", 30)