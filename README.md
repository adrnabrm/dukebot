# Computah

Voice assistant. Wake word → listen → reply → remember. Can web search and save long-term facts when needed.

## Stack

- **Wake word:** livekit-wakeword (`computah.onnx`)
- **STT:** faster-whisper (`tiny`)
- **LLM:** Gemini via smolagents / LiteLLM (`gemini-3.1-flash-lite`)
- **Tools:** DuckDuckGo web search; long-term `remember` / `recall` (Chroma)
- **TTS:** Piper (`en_US-lessac-medium`)
- **Memory:** short-term chat history + persistent Chroma store (`data/chroma/`)

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

```env
GEMINI_API_KEY=your_key_here
WAKEWORD_MODEL_PATH=models/wakeword/computah.onnx
PIPER_VOICE_PATH=models/tts/en_US-lessac-medium.onnx
LONG_TERM_MEMORY_PATH=data/chroma
```

Get a key from [Google AI Studio](https://aistudio.google.com/apikey). Same key is used for the LLM and memory embeddings. Load env before running (`export $(grep -v '^#' .env | xargs)` or similar).

## Run

```bash
python main.py
```

Ctrl+C to quit.

Loop: wake word → record → Whisper → Gemini (short-term memory + optional web search / remember / recall) → Piper → repeat.

## Wake word training

Optional. Config: `scripts/wakeword/configs/prod.yaml`.

```bash
cd scripts/wakeword
python train.py
```

Exports ONNX under `models/wakeword/`. Point `WAKEWORD_MODEL_PATH` at it.
