# Computah

Computah, make this repo supa cool and awesome.

## Stack

- **Wake word:** [livekit-wakeword](https://github.com/livekit/agents) (`computah.onnx`)
- **STT:** faster-whisper (`tiny`)
- **LLM:** Ollama via smolagents / LiteLLM (default `qwen3.5:4b`)
- **TTS:** Piper (`en_US-lessac-medium`)

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Install and run [Ollama](https://ollama.com/), then pull the model:

```bash
ollama pull qwen3.5:4b
```

Copy env and fill in paths:

```bash
cp .env.example .env
```

```env
COMPUTAH_MODEL=qwen3.5:4b
OLLAMA_BASE=http://localhost:11434
WAKEWORD_MODEL_PATH=models/wakeword/computah.onnx
PIPER_VOICE_PATH=models/tts/en_US-lessac-medium.onnx
```

Load env before running (e.g. `export $(grep -v '^#' .env | xargs)` or your preferred method).

## Run

```bash
python main.py
```

Flow:

1. Listens for the wake word
2. Records until silence
3. Transcribes with Whisper
4. Queries the Ollama model
5. Speaks the reply with Piper

## Wake word training

Optional. Config lives in `scripts/wakeword/configs/prod.yaml`.

```bash
cd scripts/wakeword
python train.py
```

Exports ONNX under `models/wakeword/`. Point `WAKEWORD_MODEL_PATH` at the new file.
