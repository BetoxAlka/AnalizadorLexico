import random

class SimpleChatBot:
    def __init__(self, name="ChatBot"):
        self.name = name
        self.responses = {
            "hello": ["Hi!", "Hello!", "Hey there!", "Greetings!"],
            "how are you": ["I'm doing great, thank you!", "All good!", "Happy to chat!"],
            "bye": ["Goodbye!", "See you later!", "Have a nice day!"],
            "default": ["Sorry, I didn't understand that.", "Could you rephrase?"]
        }

    def greet(self):
        print(f"{self.name}: Hello! I'm {self.name}. How can I help you today?")

    def get_response(self, message):
        message = message.lower()
        for key in self.responses:
            if key in message:
                return random.choice(self.responses[key])
        return random.choice(self.responses["default"])

    def chat(self):
        self.greet()
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print(f"{self.name}: It was nice talking to you. Goodbye!")
                break
            response = self.get_response(user_input)
            print(f"{self.name}: {response}")

def test_bot():
    bot = SimpleChatBot("TestBot")
    print("Running chatbot test...")
    test_messages = ["hello", "how are you", "what's up", "bye"]
    for msg in test_messages:
        print(f"User: {msg}")
        print(f"Bot: {bot.get_response(msg)}")

def main():
    mode = input("Type 'test' to run test, or anything else to chat: ").strip()
    if mode == "test":
        test_bot()
    else:
        bot = SimpleChatBot("Milo")
        bot.chat()

if __name__ == "__main__":
    main()
