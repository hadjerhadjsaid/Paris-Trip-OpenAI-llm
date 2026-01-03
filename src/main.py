from llm_travel import conversation, questions, client, model

# -----------------------------
# Loop through questions and get LLM answers
# -----------------------------
for question in questions:
    # Add user question to conversation
    conversation.append({"role": "user", "content": question})

    # Call the LLM
    response = client.chat.completions.create(
        model=model,
        messages=conversation,
        max_tokens=100
    )

    # Extract assistant's reply
    answer = response.choices[0].message.content

    # Print the answer
    print("Q:", question)
    print("A:", answer, "\n")

    # Append reply to conversation
    conversation.append({"role": "assistant", "content": answer})
