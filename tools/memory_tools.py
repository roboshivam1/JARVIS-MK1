from memory_manager import MemoryVault

# initialize the vault so the tool can access it
vault = MemoryVault()

def search_memory(query: str) -> str:
    """
    Searches the user's long-term memory vault for past facts, preferences, or project details.
    """
    print(f"[JARVIS is searching memory for: '{query}']")
    return vault.search_memory(query)

# 1. The actual function mapping for your tool executor
MEMORY_TOOLS_MAP = {
    "search_memory": search_memory
}

# 2. The JSON Schema to pass into the Ollama `tools` array
MEMORY_TOOLS_SCHEMA = [
    {
        "type": "function",
        "function": {
            "name": "search_memory",
            "description": "Searches the user's long-term memory vault for past facts, preferences, or project details. Use this when the user asks you to recall something you previously discussed, or if you need context about their life.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The specific keyword or topic to search for (e.g., 'favorite color', 'PostgreSQL', 'girlfriend')."
                    }
                },
                "required": ["query"]
            }
        }
    }
]