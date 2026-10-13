<div align="center">
  <a href="https://youtu.be/SQg5L6f50Bs">
    <img src="https://img.youtube.com/vi/SQg5L6f50Bs/0.jpg" alt="MiniCPM-V 4.7: The 1GB Vision AI That Destroys Qwen Vision!">
  </a>
  <h3>📺 <a href="https://youtu.be/SQg5L6f50Bs">Watch the full tutorial on YouTube</a></h3>
</div>

# 👁️ MiniCPM Visual Intelligence Studio

High-speed offline multimodal visual analysis workstation powered by the ultra-compact MiniCPM-V 4.7 1B on-device vision model.

| Step 1: Input | Step 2: AI Action | Step 3: Result |
| :--- | :--- | :--- |
| Select local receipt, chart, or multiple photos | MiniCPM-V extracts visual tokens and runs local reasoning | Generates structured markdown tables, OCR fields, and latency benchmarks |

## 🌟 Superpowers

- **Receipt OCR & Itemization:** Parses store receipts into structured JSON and clean Markdown tables with totals and tax rates.
- **Scientific Diagram Reasoning:** Explains optical and physics charts, calculating incident angles and light path deviations.
- **Benchmark Graph Interpretation:** Compares multi-model frontier curves and determines Pareto efficiency leaders.
- **Multi-Image Scene Comparison:** Analyzes sequential imagery side-by-side to detect object changes and spatial transitions.
- **Latency Benchmarking:** Accurately measures time-to-first-token and throughput speeds directly on consumer CPUs.

## 📦 Tech Stack

- **Model:** OpenBMB MiniCPM-V 4.7 (1B Q8_0 GGUF / Ollama Model)
- **Runtime:** Python 3.10+, Ollama Local Server / Llama.cpp Engine
- **Libraries:** `ollama`, `Pillow`, `rich`
- **Architecture:** SigLIP2 Vision Encoder + Qwen3.6 Language Backbone + Intra-ViT Compression

## 📋 File Layout

```
.
├── Modelfile             # Ollama registration template for MiniCPM-V 4.7 GGUF
├── README.md             # Complete setup and execution guide
├── main.py               # Multimodal analysis pipeline and latency benchmarks
├── inputs/               # High-resolution offline test images and charts
└── models/               # Local GGUF checkpoints directory
```

## 🚀 Quick Setup & Installation

Follow these steps in your PowerShell terminal to set up the offline visual studio:

### 1. Install Python Dependencies

```powershell
pip install ollama pillow rich
```

### 2. Download Model Checkpoint

Download the official 8-bit quantized GGUF weights directly into the `models/` directory using modern `hf download`:

```powershell
hf download openbmb/MiniCPM-V-4.7-1B-gguf MiniCPM-V-4_7-1B-Q8_0.gguf --local-dir models
```

### 3. Register Model in Ollama

Register the local model in Ollama using the included `Modelfile`:

```powershell
ollama create minicpm-v4.7 -f Modelfile
```

### 4. Run Offline Visual Studio

Execute the main visual analysis pipeline:

```powershell
python main.py
```

## 💡 Practical Workflows

1. **Automated Expense Accounting:** Point the tool at captured paper receipts to export line items directly into accounting software.
2. **Chart-to-Report Generation:** Feed financial and performance charts to auto-generate executive summary bullet points.
3. **Hardware Defect Inspection:** Compare side-by-side assembly line photos to spot anomalies and misalignment.
4. **Offline Mobile Diagnostics:** Embed the 1.06 GB model on field inspection laptops without internet access.
5. **Medical & Scientific Diagramming:** Decode textbook anatomy and optical refraction graphics for interactive tutorials.

## 🔮 Roadmap & Upcoming Features

1. **Real-time Webcam Stream Parsing:** Process continuous live camera frames directly via OpenCV feed.
2. **Structured JSON Schema Enforcement:** Guarantee strict Pydantic JSON schemas across all OCR extractions.
3. **Bounding Box Visualizer Overlay:** Auto-draw visual grounding bounding boxes on input images and save annotated PNGs.
4. **Audio Narration Output:** Voice generation pipeline synthesizing model answers into natural speech.
5. **Batch Folder Watcher:** Background daemon watching hot folders for new incoming scans and auto-processing them.

---

## 🏷️ Keywords

`minicpm-v-4.7` · `minicpm-v` · `openbmb` · `multimodal-ai` · `vision-language-model` · `on-device-ai` · `gguf` · `ollama` · `edge-ai` · `qwen-vision` · `siglip2` · `ocr` · `document-parsing` · `local-ai` · `offline-vision`

