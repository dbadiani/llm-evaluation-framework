import csv
import json
import datetime
from collections import Counter
from openai import OpenAI

from evaluator import score_response
from rubric import evaluate_quality

client = OpenAI()

# -----------------------------
# Create timestamped output file
# -----------------------------
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"results/results_{timestamp}.json"

results = []

# -----------------------------
# Run evaluations
# -----------------------------
with open("prompts.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        prompt = row["prompt"]
        expected = row["expected_keywords"]

        print(f"Running prompt: {prompt}")

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        response = completion.choices[0].message.content

        score_result = score_response(row["id"], response, expected)
        quality_issues = evaluate_quality(response)

        results.append({
            "prompt_id": row["id"],
            "prompt": prompt,
            "response": response,
            "score": score_result,
            "quality_issues": quality_issues,
        })

# -----------------------------
# Save results to file
# -----------------------------
with open(output_file, "w") as f:
    json.dump(results, f, indent=2)

print(f"\nResults saved to {output_file}")

# -----------------------------
# Compute evaluation metrics
# -----------------------------
total_scores = []
issue_counter = Counter()

for r in results:
    total_scores.append(r["score"]["score"])

    for issue in r["quality_issues"]:
        issue_counter[issue] += 1

avg_score = sum(total_scores) / len(total_scores) if total_scores else 0
total_issues = sum(issue_counter.values())

# -----------------------------
# Print evaluation dashboard
# -----------------------------
print("\n========== LLM EVALUATION SUMMARY ==========")
print(f"Run file: {output_file}")
print(f"Total prompts tested: {len(results)}")
print(f"Average score: {avg_score:.2f}")
print(f"Total quality issues: {total_issues}")

print("\nIssue breakdown:")
for issue, count in issue_counter.items():
    print(f"- {issue}: {count}")

print("===========================================\n")