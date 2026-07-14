# LLM Foundations

This folder contains experiments and notes for large language model foundations.

## Contents

- `src/LLM hyperparameters.py` — Example code showing prompt context window, token budgets, and model routing.
- `src/token_metrics.py` — Scripts to calculate token usage, cost, latency, and throughput for Anthropic models.

## Purpose

- Learn how to estimate LLM token costs.
- Practice model selection and prompt engineering.
- Measure latency, throughput, and token efficiency.

## Running examples

1. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install anthropic requests
```

3. Run the sample scripts:

```bash
python src/LLM\ hyperparameters.py
python src/token_metrics.py
```

## Notes

- Update the code with your own Anthropic API key and environment variables.
- This folder is focused on LLM measurement and foundational concepts, not production deployment.
