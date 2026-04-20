# LLM Evaluation Framework

This project demonstrates how QA principles can be applied to evaluate LLM outputs.

## What it does

- Sends prompts to an LLM
- Scores responses against expected keywords (golden dataset)
- Applies quality rubrics to detect weak or uncertain answers
- Stores structured evaluation results for regression testing

## Why

LLM outputs are non-deterministic. This framework shows how to:
- Detect response drift
- Evaluate correctness signals
- Apply repeatable evaluation criteria

Built using Python and OpenAI API.