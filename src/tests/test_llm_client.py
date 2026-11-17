import pytest
import requests
from src.llm_client import (
    OllamaClient,
    OllamaConnectionError,
    OllamaModelNotFoundError
)

def test_client_returns_response(monkeypatch):
    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {
                "message": {
                    "content": "A felicidade pode ter vários significados."
                }
            }

    def fake_post(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(requests, "post", fake_post)
    client = OllamaClient(
        base_url="http://localhost:11434",
        model="llama3.2:3b"
    )
    result = client.chat([
        {"role": "user", "content": "O que é felicidade?"}
    ])

    assert "felicidade" in result

def test_client_handles_connection_error(monkeypatch):
    def fake_post(*args, **kwargs):
        raise requests.exceptions.ConnectionError()

    monkeypatch.setattr(requests, "post", fake_post)
    client = OllamaClient(
        "http://localhost:11434",
        "llama3.2:3b"
    )

    with pytest.raises(OllamaConnectionError):
        client.chat([])

def test_client_handles_missing_model(monkeypatch):
    class FakeResponse:
        status_code = 404

        def raise_for_status(self):
            raise requests.exceptions.HTTPError(
                response=self
            )

    def fake_post(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(requests, "post", fake_post)
    client = OllamaClient(
        "http://localhost:11434",
        "modelo-inexistente"
    )

    with pytest.raises(OllamaModelNotFoundError):
        client.chat([])