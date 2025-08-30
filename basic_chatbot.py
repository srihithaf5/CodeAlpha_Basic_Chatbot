# basic_chatbot.py
import re

# sets / lists of phrases
GREETINGS = {"hello", "hi", "hey", "hiya"}
HOW_ARE_PHRASES = {
    "how are you", "how r u", "how are u", "how're you", "how's it going", "how is it going"
}
FAREWELLS = {"bye", "goodbye", "see you", "exit", "quit"}

def normalize(text: str) -> str:
    """Lowercase and collapse whitespace."""
    return re.sub(r"\s+", " ", text.strip().lower())

def contains_word(text: str, word: str) -> bool:
    """Return True if `word` appears as a whole word inside text."""
    return re.search(rf"\b{re.escape(word)}\b", text) is not None

def get_response(user_input: str) -> str:
    """Return a rule-based reply for the given user_input."""
    text = normalize(user_input)

    # Check multi-word phrases (prioritize these to avoid partial matches)
    for phrase in HOW_ARE_PHRASES:
        if phrase in text:
            return "I'm fine, thanks!"

    # Check greetings (single-word)
    for g in GREETINGS:
        if contains_word(text, g):
            return "Hi!"

    # Check farewells
    for f in FAREWELLS:
        if f in text:
            return "Goodbye!"

    # Default fallback
    return "Sorry, I don't understand. Try 'hello', 'how are you', or 'bye'."

def main():
    print("Simple rule-based chatbot (type 'bye', 'exit' or 'quit' to stop).")
    while True:
        user = input("You: ").strip()
        if not user:
            # optional: ignore empty input and continue
            continue

        reply = get_response(user)
        print("Bot:", reply)

        # stop if the bot just said goodbye
        if reply == "Goodbye!":
            break

if __name__ == "__main__":
    main()
