import os
from dotenv import load_dotenv
from src.chat import Chat
from src.llm_client import OllamaClient, OllamaError
from src.prompts import SYSTEM_PROMPT

def main():
    load_dotenv()
    base_url = os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434"
    )
    model = os.getenv(
        "OLLAMA_MODEL",
        "llama3.2:3b"
    )
    timeout = int(os.getenv("OLLAMA_TIMEOUT", "120"))
    temperature = float(os.getenv("OLLAMA_TEMPERATURE", "0.7"))
    num_predict = int(os.getenv("OLLAMA_NUM_PREDICT", "400"))
    client = OllamaClient(
        base_url=base_url,
        model=model,
        timeout=timeout,
        temperature=temperature,
        num_predict=num_predict
    )
    chat = Chat(
        llm_client=client,
        system_prompt=SYSTEM_PROMPT,
        max_history=6
    )

    print("\n" + "=" * 55)
    print("             BEM-VINDO AO PENSACOMIGO")
    print("=" * 55)

    print("\nUm espaço para pensar, questionar e refletir.")
    print("\nDigite 'sair' para encerrar a conversa.")

    while True:
        try:
            question = input("\nVocê: ").strip()

            if question.lower() in ["sair", "exit", "quit"]:
                print("\nPensaComigo: Até nossa próxima reflexão!")
                break

            if not question:
                print("\nPensaComigo: Escreva uma questão para começarmos.")
                continue

            print("\nPensaComigo: Estou refletindo...\n")

            answer = chat.ask(question)

            print(f"PensaComigo: {answer}")

        except OllamaError as error:
            print(f"\nPensaComigo: {error}")

        except KeyboardInterrupt:
            print("\n\nConversa encerrada.")
            break

        except EOFError:
            print("\n\nConversa encerrada.")
            break

        except Exception as error:
            print(f"\nErro inesperado: {error}")

if __name__ == "__main__":
    main()
