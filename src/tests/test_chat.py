import pytest
from src.chat import Chat

class FakeLLM:
    def __init__(self):
        self.last_messages = None

    def chat(self, messages):
        self.last_messages = messages
        return "O que você entende por felicidade?"

def test_chat_returns_answer():
    llm = FakeLLM()
    chat = Chat(llm, "Você é um filósofo.")
    answer = chat.ask("O que é felicidade?")

    assert answer == "O que você entende por felicidade?"

def test_chat_preserves_history():
    llm = FakeLLM()
    chat = Chat(llm, "Você é um filósofo.")
    chat.ask("O que é liberdade?")
    chat.ask("E o que é responsabilidade?")

    assert len(chat.history) == 4

def test_chat_rejects_empty_question():
    llm = FakeLLM()
    chat = Chat(llm, "Você é um filósofo.")

    with pytest.raises(ValueError):
        chat.ask("   ")

def test_chat_does_not_update_history_on_error():
    class FailingLLM:
        def chat(self, messages):
            raise RuntimeError("Falha simulada")

    chat = Chat(FailingLLM(), "Você é um filósofo.")

    with pytest.raises(RuntimeError):
        chat.ask("O que é justiça?")

    assert chat.history == []