class Chat:
    def __init__(self, llm_client, system_prompt, max_history=6):
        self.llm_client = llm_client
        self.system_prompt = system_prompt
        self.max_history = max_history
        self.history = []

    def ask(self, question):
        if not question or not question.strip():
            raise ValueError("A pergunta não pode estar vazia.")

        messages = [
            {
                "role": "system",
                "content": self.system_prompt
            }
        ]
        messages.extend(self.history[-self.max_history:])
        messages.append({
            "role": "user",
            "content": question.strip()
        })

        # A conversa só é atualizada após uma resposta válida
        answer = self.llm_client.chat(messages)

        self.history.extend([
            {
                "role": "user",
                "content": question.strip()
            },
            {
                "role": "assistant",
                "content": answer
            }
        ])

        # Mantém somente as últimas mensagens.
        self.history = self.history[-self.max_history:]

        return answer
