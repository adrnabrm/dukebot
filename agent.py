import os
from smolagents import ChatMessage, LiteLLMModel
from smolagents.models import MessageRole
from utils.audio_handler import AudioHandler

MODEL_ID = os.getenv("COMPUTAH_MODEL", "qwen3.5:4b")
OLLAMA_BASE = os.getenv("OLLAMA_BASE", "http://localhost:11434")

class Computah:

    def __init__(self):
        print("Initializing Computah...")
        # Initialize the model
        self.model = LiteLLMModel(
            model_id=f"ollama_chat/{MODEL_ID}",
            api_base=OLLAMA_BASE,
            num_ctx=8192,
        )
        # Initialize the audio handler
        self.audio_handler = AudioHandler()
        print("Computah initialized!")

    def listen(self) -> str:
        print("Listening for wakeword...")
        if self.audio_handler.listen_for_wakeword():
            print("Wakeword detected!")
        return True

    def run(self, input: str) -> str:
        response = self.model.generate([
            ChatMessage(
                role=MessageRole.USER,
                content=[{"type": "text", "text": input}],
            ),
        ])
        return response.content