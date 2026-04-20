# 🧪 LLM Evaluation Framework

A Python-based framework for evaluating Large Language Model (LLM) outputs using structured prompts, scoring rubrics, and automated test pipelines.

This project demonstrates how **QA engineering principles can be applied to AI systems**, including prompt testing, output scoring, and hallucination detection.

---

## 🚀 What this project does

- Sends prompts to an LLM (via API)
- Captures and stores model responses
- Evaluates outputs using structured scoring rules
- Detects quality issues such as:
  - Hallucinations (missing expected facts)
  - Low-quality or incomplete responses
  - Weak or uncertain answers
- Generates timestamped evaluation reports
- Produces a summary dashboard for each run

---

## 🧠 Why this matters

LLMs are non-deterministic systems — traditional testing methods do not work well.

This framework demonstrates how to:
- Bring **structure to unpredictable AI outputs**
- Build **repeatable evaluation pipelines**
- Apply **QA automation principles to LLM systems**
- Perform **regression testing on model behavior**

---

## 📊 Example Output

Each run generates:

- JSON report of all prompt evaluations
- Summary metrics:
  - Average score
  - Total issues detected
  - Issue breakdown (hallucination, low confidence, etc.)

---

## 🛠 Tech Stack

- Python
- OpenAI API
- CSV-based test datasets
- Custom evaluation rubrics
- Simple scoring engine
- JSON reporting

---

## 📂 Project Structure
llm-evaluation-framework/
│
├── prompts.csv # Test dataset (golden prompts)
├── run_eval.py # Main evaluation runner
├── evaluator.py # Scoring logic
├── rubric.py # Quality rules
├── results/ # Output reports (timestamped)
└── README.md

---

## ▶️ How to run

```bash
pip install openai
python3 run_eval.py