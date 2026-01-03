# conversation_engine/conversation_memory.py

class ConversationMemory:
    """
    Stores conversation context for the session.
    """

    def __init__(self):
        self.history = []
        self.last_entities = {}
        self.last_analysis_type = None

    def add_turn(self, user_query: str, intent: dict, entities: dict):
        self.history.append({
            "query": user_query,
            "intent": intent,
            "entities": entities
        })
        self.last_entities = entities
        self.last_analysis_type = intent.get("intent")

    def get_last_entities(self):
        return self.last_entities

    def get_last_analysis_type(self):
        return self.last_analysis_type

    def get_history(self):
        return self.history
