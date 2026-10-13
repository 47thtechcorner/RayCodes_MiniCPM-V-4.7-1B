"""
Offline Visual Intelligence Workstation powered by MiniCPM-V 4.7 (1B).
Analyzes receipts, scientific diagrams, benchmark charts, and multi-image scenes locally,
measuring response times and writing comprehensive outputs to outputs/outputs.md.
"""

import time
from pathlib import Path
import ollama

MODEL_NAME = "minicpm-v4.7"

PIPELINE_TASKS = [
    {
        "id": "receipt_ocr",
        "title": "Store Receipt OCR & Structured Itemization",
        "images": ["inputs/store_receipt.jpg"],
        "prompt": "Extract the merchant name, date, itemized receipt table with prices, and final total amount.",
    },
    {
        "id": "diagram_reasoning",
        "title": "Scientific Diagram Analysis & Physics Reasoning",
        "images": ["inputs/diagram_refraction.png"],
        "prompt": "Explain the physical optical principles depicted here, describing the ray behavior across media interfaces.",
    },
    {
        "id": "chart_interpretation",
        "title": "Multimodal Frontier Benchmark Curve Analysis",
        "images": ["inputs/chart_frontier.png"],
        "prompt": "Analyze this benchmark chart: which model leads the Pareto efficiency curve at the 1B scale and why?",
    },
    {
        "id": "multi_image_comparison",
        "title": "Multi-Image Cross-Scene Reasoning & Grounding",
        "images": ["inputs/urban_street.jpg", "inputs/diagram_refraction.png"],
        "prompt": "Compare these two images: identify the key objects in the scene and explain how the optical principle in the diagram applies to the cameras in the real-world scene.",
    },
]


def run_pipeline():
    outputs_dir = Path("outputs")
    outputs_dir.mkdir(parents=True, exist_ok=True)
    report_file = outputs_dir / "outputs.md"

    results = []
    total_start_time = time.time()

    for task in PIPELINE_TASKS:
        # Validate input image paths
        valid_images = [str(Path(p)) for p in task["images"] if Path(p).exists()]

        start_time = time.time()

        # Ollama multimodal inference call
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": task["prompt"],
                    "images": valid_images,
                }
            ],
            options={"temperature": 0.2},
        )

        elapsed_sec = round(time.time() - start_time, 2)
        answer_text = response.get("message", {}).get("content", "").strip()

        results.append({
            "task": task["title"],
            "images": ", ".join(task["images"]),
            "elapsed": elapsed_sec,
            "answer": answer_text,
        })

    total_duration = round(time.time() - total_start_time, 2)

    # Write outputs.md
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("# Visual Intelligence Studio Inference Report\n\n")
        f.write("Comprehensive multimodal analysis results powered by **MiniCPM-V 4.7 (1B)**.\n\n")
        f.write("## Performance Latency Overview\n\n")
        f.write("| Task | Target Domain | Image Assets | Latency |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for res in results:
            f.write(f"| {res['task']} | Multimodal Analysis | `{res['images']}` | **{res['elapsed']}s** |\n")
        f.write(f"\n**Total Pipeline Execution Time:** {total_duration}s\n\n")
        f.write("---\n\n")
        f.write("## Detailed Task Outputs\n\n")
        for res in results:
            f.write(f"### {res['task']}\n\n")
            f.write(f"- **Input Image:** `{res['images']}`\n")
            f.write(f"- **Response Latency:** `{res['elapsed']}s`\n\n")
            f.write(f"#### Extracted Visual Intelligence:\n\n{res['answer']}\n\n")
            f.write("---\n\n")


if __name__ == "__main__":
    run_pipeline()
