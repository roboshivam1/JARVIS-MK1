import ollama
from memory import ConversationMemory

class JarvisBrain:
    def __init__(self, model_name: str= "llama3.1"):
        """
        Initializes the brain with the specific ollama model
        """
        self.model_name = model_name
    
    def think(self, user_text: str, memory: ConversationMemory) -> str:
        """
        Takes user text, updates memory, and generates a response.
        """
        memory.add_message("user", user_text)

        context = memory.get_context()

        response = ollama.chat(
            model=self.model_name,
            messages=context
        )

        jarvis_reply = response['message']['content']

        memory.add_message("assistant", jarvis_reply)
        
        return jarvis_reply
