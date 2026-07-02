from email import message

import anthropic
from requests import request

client = anthropic.Anthropic()

# Program 1 :  Count tokens BEFORE sending — so you can estimate cost
response = client.messages.count_tokens(
    model="claude-sonnet-4-6",
    system="You are a helpful assistant.",
    messages=[
        {
            "role": "user",
            "content": "What is the refund policy for orders above 500 rupees?",
        }
    ],
)

print(f"Input tokens: {response.input_tokens}")
# → Input tokens: 24

# Now calculate cost
input_cost = (response.input_tokens / 1_000_000) * 3.00  # $3 per 1M input tokens
print(f"Cost for this call: ${input_cost:.6f}")
# → Cost for this call: $0.000072


# Program 2:  Input and OutPut Token Count and Execution Time

import anthropic
import time

client = anthropic.Anthropic()

# Get user input
user_query = "What is python? Answer in very short sentence: "

# Keywords indicating a complex question
complex_keywords = [
    "design",
    "architecture",
    "compare",
    "analyze",
    "implement",
    "debug",
    "optimize",
    "strategy",
    "explain in detail",
]

# Model routing
if any(keyword in user_query.lower() for keyword in complex_keywords):
    model = "claude-sonnet-4-6"
else:
    model = "claude-haiku-4-5"

print(f"\nSelected Model: {model}")

# Measure execution time
start_time = time.time()

response = client.messages.create(
    model=model, max_tokens=100, messages=[{"role": "user", "content": user_query}]
)

end_time = time.time()

# Print response
print("\n=== Response ===")

# Print token usage
print("\n=== Token Usage ===")
input_tokens = response.usage.input_tokens
output_tokens = response.usage.output_tokens
print(f"Input Tokens  : {input_tokens}")
print(f"Output Tokens : {output_tokens}")
print(
    f"Total Tokens  : " f"{response.usage.input_tokens + response.usage.output_tokens}"
)

# Print execution time
print(f"\nExecution Time: {end_time - start_time:.2f} seconds")

# Program 3 . Total Cost
inputcost = (input_tokens / 1_000_00) * 3
outputcost = (output_tokens / 1_000_00) * 3
total_cost = input_cost + outputcost
print(f"Total cost : {total_cost:.6f}")

# Program 4 : Latency

import time

start = time.time()

response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=50,
    messages=[{"role": "user", "content": "What is Python? Anser in simple sentence"}],
)

end = time.time()

print(f"Latency/Execution Time: {end-start:.2f} seconds")

# Program 5. Throughput

total_requests = 100
total_time = 20

throughput = total_requests / total_time

print(f"Throughput: {throughput} requests/sec")

# However, there are some trade-offs:

# | Prompt                                                     | Clarity | Tokens |
# |-------------------------------------------------------------|---------|--------|
# | Python                                                       | Low     | Fewest |
# | What is Python?                                              | Medium  | More   |
# | Explain the Python programming language in one sentence.    | High    | Most   |

# Instead of:
# Apple
# use:
# What is Apple Inc.?

# In enterprise AI applications, clear prompts help:

# * Improve accuracy ✅
# * Reduce hallucinations ✅
# * Produce consistent responses ✅
# * Improve user trust ✅

# Ex : What is the Python programming language?
# is the preferred prompt. 👍


# Summary this code covers:
# ✅ Input Tokens
# ✅ Output Tokens
# ✅ Total Tokens
# ✅Cost Calculation
# ✅ Execution Time (Latency)
# ✅Throughput
# ✅ Context Utilization
# ✅ Model Routing
# ✅Token Optimization
