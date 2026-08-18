class LuisAIEngine:
    def __init__(self):
        self.name = "LuisAI"
        self.version = "0.1.0"

    def run(self, user_request: str) -> dict:
        return {
            "request": user_request,
            "status": "received",
            "analyses": [],
            "ai_responses": [],
            "critic_results": [],
            "final_result": None,
            "confidence": None,
        }


if __name__ == "__main__":
    engine = LuisAIEngine()

    result = engine.run("Phân tích cổ phiếu mẫu")

    print(result)
