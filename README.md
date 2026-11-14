
# PensaComigo

Chat filosófico desenvolvido em Python com Ollama.

## Objetivo

O PensaComigo é um assistente filosófico que utiliza
um modelo de linguagem local para estimular o pensamento
crítico, o questionamento e a reflexão.

O sistema utiliza o método socrático para incentivar
o usuário a construir suas próprias conclusões.

## Tecnologias

- Python 3.11+
- Ollama
- Llama 3.2 3B
- Requests
- Pytest
- Git

## Pré-requisitos

- Python instalado
- Ollama instalado
- Modelo llama3.2:3b disponível localmente

## Instalação

1. Clone o repositório:

2. git clone URL_DO_REPOSITORIO

3. Entre na pasta:
```bash
cd PensaComigo
```

4. Crie o ambiente virtual:
```python
python -m venv .venv
```

5. Ative o ambiente virtual e instale as dependências:
```python
pip install -r requirements.txt
```

6. Copie .env.example para .env.

## Executar

1. Certifique-se de que o Ollama está funcionando.

2. Execute:

```python
python -m src.main
```

## Testes

1. Execute:
```python
pytest -v
```

## Escopo

#### O P0 contempla:

- Execução local
- Interface textual
- Um único LLM
- Histórico temporário
- Tratamento básico de erros
- Testes automatizados

## Autor

Jônatas Fernandes Silva
