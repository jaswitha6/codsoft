import wikipedia
import datetime
import random

# Preload a few jokes
JOKES = [
    "Why don’t scientists trust atoms? Because they make up everything! 😂",
    "I told my computer I needed a break, and it said ‘Error 404: Coffee not found.’ ☕",
    "Why did the scarecrow become a successful neurosurgeon? He was outstanding in his field! 🧠🌾",
]

def get_factual_answer(query):
    """Try to fetch a 2-sentence summary from Wikipedia."""
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.DisambiguationError as e:
        return f"Your question is ambiguous, did you mean one of: {e.options[:5]}?"
    except Exception:
        return None

def chatbot():
    print("🤖 ChatBot: Hello! Ask me anything. (type 'bye' to exit)\n")
    while True:
        user = input("You: ").strip()
        if user.lower() in ("bye", "exit", "quit"):
            print("ChatBot: Goodbye! 👋")
            break

        q = user.lower()

        # 1) Time questions
        if "time" in q:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"ChatBot: The current time is {now}\n")
            continue

        # 2) Joke requests
        if "joke" in q or "laugh" in q:
            print(f"ChatBot: {random.choice(JOKES)}\n")
            continue

        # 3) Try Wikipedia for factual answers
        answer = get_factual_answer(user)
        if answer:
            print(f"ChatBot: {answer}\n")
            continue

        # 4) Fallback
        print("ChatBot: Sorry, I don't know the answer to that. Can you try asking differently?\n")

if __name__ == "__main__":
    chatbot()
