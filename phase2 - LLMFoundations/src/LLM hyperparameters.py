# Topic Context Window — How much the model can “see”

# A RAG call's context budget
system_prompt = 300
retrieved_chunks = 1500
retrieved_chunks = 500
user_query = 50

total_input = system_prompt + retrieved_chunks + retrieved_chunks + user_query
print(total_input)
print(f"Using {total_input} of 200,000 tokens available")


# Progam llm_temperature
import anthropic

prompt = "Write one sentence describing what a refund policy is."
client = anthropic.Anthropic()

for temp in [0, 0.7, 1.0]:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=20,
        temperature=temp,
        messages=[{"role": "user", "content": prompt}],
    )
    print(f"\ntemperature={temp}:")
    # But to satisfy the type checker:
    print(getattr(response.content[0], "text", ""))
