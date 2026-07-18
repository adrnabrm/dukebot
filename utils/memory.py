from collections import deque

class Memory:
    def __init__(self, max_size: int = 100):
        self.memory = deque(maxlen=max_size)

    def add(self, message: str, response: str) -> None:
        self.memory.append(f"User: {message}\nAssistant: {response}")

    def get(self) -> str:
        return "\n".join(self.memory)