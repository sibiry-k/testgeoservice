import sys
import os

import pytest
from fastapi.testclient import TestClient
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src')
))

from src.main import app # noqa
from .database import Base, get_db, engine, SessionLocal # noqa

TestingSessionLocal = SessionLocal

Base.metadata.create_all(bind=engine)


@pytest.fixture()
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture()
def test_client(db_session):
    def ovveride_get_db():
        try:
            yield db_session
        finally:
            db_session.close()
    app.dependency_overrides[get_db] = ovveride_get_db
    with TestClient(app) as test_client:
        yield test_client
