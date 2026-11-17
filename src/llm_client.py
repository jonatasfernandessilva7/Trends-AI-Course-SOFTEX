import requests

class OllamaError(Exception):
    """Erro geral de comunicação com Ollama."""

class OllamaConnectionError(OllamaError):
    pass

class OllamaTimeoutError(OllamaError):
    pass

class OllamaModelNotFoundError(OllamaError):
    pass

class OllamaRateLimitError(OllamaError):
    pass

class OllamaResponseError(OllamaError):
    pass

class OllamaClient:
    def __init__(self, base_url, model, timeout=120, temperature=0.7, num_predict=400):
        self.url = f"{base_url.rstrip('/')}/api/chat"
        self.model = model
        self.timeout = timeout
        self.temperature = temperature
        self.num_predict = num_predict

    def chat(self, messages):
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "options": {
                "temperature": self.temperature,
                "num_predict": self.num_predict
            }
        }

        try:
            response = requests.post(
                self.url,
                json=payload,
                timeout=self.timeout
            )

            response.raise_for_status()
            data = response.json()
            content = data.get("message", {}).get("content", "")

            if not isinstance(content, str) or not content.strip():
                raise OllamaResponseError(
                    "O modelo retornou uma resposta vazia."
                )

            return content.strip()

        except requests.exceptions.Timeout as error:
            raise OllamaTimeoutError(
                "O tempo de resposta do Ollama foi excedido."
            ) from error

        except requests.exceptions.ConnectionError as error:
            raise OllamaConnectionError(
                "Não foi possível conectar ao Ollama. "
                "Verifique se o serviço está em execução."
            ) from error

        except requests.exceptions.HTTPError as error:
            status = error.response.status_code

            if status == 404:
                raise OllamaModelNotFoundError(
                    f"Modelo '{self.model}' não encontrado."
                ) from error

            if status == 429:
                raise OllamaRateLimitError(
                    "O serviço recusou a requisição por limite de uso."
                ) from error

            raise OllamaError(
                f"Erro HTTP na comunicação com Ollama: {status}"
            ) from error

        except ValueError as error:
            raise OllamaResponseError(
                "Não foi possível interpretar a resposta do Ollama."
            ) from error
