from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    """Test API root response"""

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}

def test_words_count():
    """Test autocomplete suggestions"""

    response = client.get("/words/school")
    assert response.status_code == 200
    assert len(response.json()["words"]) == 13 #["schoolmate","schoolboy","schoolgirlish","schoolhouse","schoolyard","schoolmaster","schoolbook","school","schoolroom","schoolwork","schoolmarm","schoolgirl","schoolteacher"]

def test_words_single_match():
    """Test autocomplete suggestions with single result"""

    response = client.get("/words/schoolw")
    assert response.status_code == 200
    assert response.json() == {"words":["schoolwork"]}
    
