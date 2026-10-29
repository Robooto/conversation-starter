"""Exercise the upgraded API against a disposable pre-existing SQLite schema."""
import os
from contextlib import closing
from pathlib import Path
import sqlite3
import tempfile
import unittest


class ApiCompatibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.directory = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1])
        cls.database = Path(cls.directory.name) / "conversations.db"
        os.environ["DATABASE_URL"] = "sqlite:///" + cls.database.as_posix()
        from app.questions import conversation_list_db

        first_topic = next(iter(conversation_list_db))
        with closing(sqlite3.connect(cls.database)) as db:
            db.executescript('''
                CREATE TABLE topics (id INTEGER PRIMARY KEY, topic VARCHAR UNIQUE);
                CREATE TABLE questions (id INTEGER PRIMARY KEY, question VARCHAR,
                    topic_id INTEGER REFERENCES topics(id));
            ''')
            db.execute("INSERT INTO topics VALUES (?, ?)", (17, first_topic))
            db.execute("INSERT INTO questions VALUES (?, ?, ?)", (23, "Preserved legacy question", 17))
            db.commit()
        from fastapi.testclient import TestClient
        from app.main import app

        cls.client_context = TestClient(app)
        cls.client = cls.client_context.__enter__()

    @classmethod
    def tearDownClass(cls):
        cls.client_context.__exit__(None, None, None)
        from app.database import engine
        engine.dispose()
        cls.directory.cleanup()

    def test_existing_schema_and_rows_survive_startup(self):
        with closing(sqlite3.connect(self.database)) as db:
            self.assertEqual(db.execute("SELECT question, topic_id FROM questions WHERE id=23").fetchone(),
                             ("Preserved legacy question", 17))

    def test_topics_and_roulette_remain_readable(self):
        topics = self.client.get("/api/v1/topics/")
        self.assertEqual(topics.status_code, 200)
        self.assertTrue(any(item["id"] == 17 for item in topics.json()))
        question = self.client.get("/api/v1/questions/roulette")
        self.assertEqual(question.status_code, 200)
        self.assertIn("question", question.json())

    def test_topic_and_question_creation_serializes_orm_models(self):
        response = self.client.post("/api/v1/topics/", json={"topic": "Upgrade compatibility"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"topic": "Upgrade compatibility", "questions": []})
        topics = self.client.get("/api/v1/topics/").json()
        topic_id = next(item["id"] for item in topics if item["topic"] == "Upgrade compatibility")
        question = {"question": "Can the upgraded API persist this?", "topic_id": topic_id}
        self.assertEqual(self.client.post("/api/v1/questions/", json=question).json(), question)
        self.assertEqual(self.client.post("/api/v1/topics/", json={"topic": "Upgrade compatibility"}).status_code, 400)

    def test_unknown_topic_is_still_rejected(self):
        self.assertEqual(self.client.get("/api/v1/questions/missing-topic").status_code, 400)
        response = self.client.post("/api/v1/questions/", json={"question": "Missing", "topic_id": 999999})
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
