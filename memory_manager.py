import json
import os

class MemoryVault:
    def __init__(self, filepath="memory.json"):
        """
        Initializes the memory vault.
        If the JSON file doesn't exist, it creates a blank slate.
        """

        self.filepath = filepath
        self.vault = self._load_vault()

    def _load_vault(self) -> dict:
        """Secretly loads the JSON file. Creates a default structure if missing or corrupted."""
        if not os.path.exists(self.filepath):
            return self._create_default_vault()
            
        try:
            with open(self.filepath, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("[System Warning] memory.json corrupted. Creating a fresh backup.")
            return self._create_default_vault()
            
    def _create_default_vault(self) -> dict:
        """Creates the foundational memory categories."""
        default_structure = {
            "user_profile": ["The user is a developer building JARVIS."],
            "preferences": ["The user prefers concise and witty responses."],
            "current_projects": [],
            "general_facts": []
        }
        self._save_vault(default_structure)
        return default_structure
        
    def _save_vault(self, data: dict = None):
        """Saves the current dictionary back to the JSON file."""
        if data is None:
            data = self.vault
        with open(self.filepath, 'w') as file:
            json.dump(data, file, indent=4)
        
    def add_memory(self, category: str, fact: str) -> str:
        """
        Adds a new fact to a specific category. 
        If the category doesn't exist, it creates it.
        """

        #cleaning up the inputs. (good boys always do!)
        category = category.lower().strip().replace(" ", "_")
        fact = fact.strip()

        if category not in self.vault:
            self.vault[category] = []
            
        #prevent duplicates. (that shit not good)
        if fact not in self.vault[category]:
            self.vault[category].append(fact)
            self._save_vault()
            return f"Successfully saved to {category}: '{fact}'"
        else:
               return f"I already have that fact stored in {category}."

    def search_memory(self, query: str) -> str:
        """
        Scans every fact in every category for the keyword.
        Returns a formatted string of matches for the AI to read.
        """

        query = query.lower().strip()
        matches = []

        for category, facts in self.vault.items():
            for fact in facts:
                if query in fact.lower():
                    matches.append(f"[{category.upper()}]: {fact}")
        
        if not matches:
            return f"No facts found in memory matching '{query}'."
        
        # join all matches into single block
        result_string = "Found the following memories:\n" + "\n".join(matches)
        return result_string
    #btw this program was written listening to Karan Aujla

    def get_core_profile(self) -> str:
        """
        Grabs the most critical info (profile and preferences) to inject 
        into JARVIS's system prompt on boot.
        """
        profile = "\n".join(self.vault.get("user_profile", []))
        prefs = "\n".join(self.vault.get("preferences", []))

        return f"\nUser Profile:\n{profile}\n\nUser Preferences:\n{prefs}"


