from brain import get_response

print("=" * 55)
print("💙 Heard AI")
print("Because everyone deserves to be heard.")
print("=" * 55)
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("\nHeard AI: Take care. I'll be here whenever you need me. 💙")
        break

    response = get_response(user_input)

    print(f"\nHeard AI: {response}\n")