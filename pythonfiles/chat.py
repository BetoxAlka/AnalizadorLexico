import random
import time

class SimpleChatBot:
    def __init__(self):
        self.responses = {
            "hello": ["Hi there!", "Hello!", "Hey!"],
            "how are you": ["I'm doing great, thanks!", "All systems operational!", "Better now that you're here!"],
            "bye": ["Goodbye!", "See you later!", "Take care!"],
            "name": ["I'm ChatPy!", "They call me ChatPy, the simple bot."],
            "default": ["Interesting...", "Tell me more.", "Hmm... I see.", "Can you elaborate?"]
        }

    def get_response(self, message):
        message = message.lower()
        for keyword in self.responses:
            if keyword in message:
                return random.choice(self.responses[keyword])
        return random.choice(self.responses["default"])

    def simulate_typing(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.03)
        print()

    def chat(self):
        self.simulate_typing("Hello! I'm ChatPy. Ask me anything or say 'bye' to end the chat.")
        while True:
            user_input = input("You: ")
            if "bye" in user_input.lower():
                response = self.get_response("bye")
                self.simulate_typing("ChatPy: " + response)
                break
            response = self.get_response(user_input)
            self.simulate_typing("ChatPy: " + response)

def main():
    bot = SimpleChatBot()
    bot.chat()

if __name__ == "__main__":
    main()
