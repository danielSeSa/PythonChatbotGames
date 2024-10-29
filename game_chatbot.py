import random
import re
import requests
from datetime import datetime

#Github: danielSeSa || CS50P__PROJECT

# Function to get input from the user
def get_user_input():
    return input("You: ")

# Rock-Paper-Scissors game


def rock_paper_scissors():
    rounds = 5
    user_score = 0
    bot_score = 0
    choices = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}

    print("Let's play Rock-Paper-Scissors!")

    for _ in range(rounds):
        user_choice = int(
            input("Choose your move \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n "))
        bot_choice = random.randint(1, 3)

        print(f"\nBot chose: {choices[bot_choice]}")

        if user_choice == bot_choice:
            print("\nIt's a tie!")
        elif (user_choice == 1 and bot_choice == 3) or (user_choice == 2 and bot_choice == 1) or (user_choice == 3 and bot_choice == 2):
            print("\nYou win this round!")
            user_score += 1
        else:
            print("\nBot wins this round!")
            bot_score += 1

    print(f"Final Score - You: {user_score}, Bot: {bot_score}")
    if user_score > bot_score:
        print("Congratulations! You are the overall winner!")
    elif user_score < bot_score:
        print("Sorry, the bot wins this game!")
    else:
        print("It's a tie overall!")

# Number Guessing game


def number_guessing():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    print("Guess the number between 1 and 10.")

    while attempts < 3:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess == number_to_guess:
            print("Congratulations! You've guessed the right number!")
            return
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")

    print(f"Sorry, the number was {number_to_guess}. Better luck next time!")

# Function to check if a message is a math expression


def is_math_expression(message):
    return bool(re.match(r'^[0-9+\-*/(). ]+$', message))

# Function to get the current time


def get_time():
    now = datetime.now()
    return f"The current time is {now.strftime('%H:%M:%S')} ⏰"

# Function to return a random joke from a predefined list


def joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything! 😂",
        "Why did the scarecrow win an award? Because he was outstanding in his field! 😄",
        "Why don't skeletons fight each other? They don't have the guts. 💀",
        "I'm reading a book on anti-gravity. It's impossible to put down! 📚",
        "Why was the math book sad? Because it had too many problems. 📘",
        "Why did the bicycle fall over? Because it was two-tired! 🚲",
        "What do you call fake spaghetti? An impasta! 🍝",
        "Why did the cookie go to the hospital? Because it felt crummy! 🍪",
        "How does a penguin build its house? Igloos it together! 🐧",
        "What do you call cheese that isn't yours? Nacho cheese! 🧀",
        "Why can't you hear a pterodactyl going to the bathroom? Because the 'P' is silent! 🦖",
        "Why did the math teacher break up with the calculator? She felt he was too calculating! 📏",
        "Why was the computer cold? It left its Windows open! 🖥️",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one! ⛳",
        "What did the ocean say to the beach? Nothing, it just waved! 🌊",
        "Why did the stadium get hot after the game? All the fans left! 🏟️",
        "Why do seagulls fly over the ocean? Because if they flew over the bay, they'd be bagels! 🥯",
        "What do you call a bear with no teeth? A gummy bear! 🐻",
        "Why don't eggs tell jokes? They'd crack each other up! 🥚",
        "What did one wall say to the other wall? I'll meet you at the corner! 🧱",
        "Why did the picture go to jail? Because it was framed! 🖼️",
        "Why did the skeleton go to the party alone? Because he had no body to go with him! 🦴",
        "What do you get when you cross a snowman and a vampire? Frostbite! 🧛",
        "Why did the computer go to therapy? Because it had a hard drive! 💻",
        "Why was the math book always worried? Because it had too many problems! 📖",
        "What do you call a fish with no eyes? Fsh! 🐟",
        "Why did the chicken join a band? Because it had the drumsticks! 🐔",
        "Why can't you give Elsa a balloon? Because she will let it go! 🎈",
        "What do you call a factory that makes good products? A satisfactory! 🏭",
        "Why did the golfer bring an extra pair of socks? In case he got a hole in one! 🧦",
        "Why don't programmers like nature? It has too many bugs! 🐞",
        "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
        "What did the left eye say to the right eye? Between you and me, something smells! 👀",
        "What do you call a sleeping bull? A bulldozer! 🐂",
        "What do you call a bear that’s stuck in the rain? A drizzly bear! 🌧️",
        "Why did the tomato turn red? Because it saw the salad dressing! 🍅",
        "Why did the math book look sad? Because it had too many problems! 😢",
        "Why was the broom late? It swept in! 🧹",
        "What do you call a dog that can do magic? A labracadabrador! 🐕‍🦺",
        "What do you call a pile of cats? A meowtain! 🐱",
        "Why was the stadium so cool? Because it was filled with fans! 🥳",
        "Why did the coffee file a police report? It got mugged! ☕",
        "Why do cows have hooves instead of feet? Because they lactose! 🐄",
    ]
    return random.choice(jokes)

# Function to get weather information
# def get_weather(city):
#     api_key = "your_api_key"  # Make sure to replace this with your actual API key
#     base_url = "http://api.openweathermap.org/data/2.5/weather?"
#     complete_url = base_url + "q=" + city + "&appid=" + api_key
#     response = requests.get(complete_url)
#     data = response.json()

#     if "cod" in data and data["cod"] != 200:
#         if data["cod"] == "404":
#             return "City not found."
#         else:
#             return "Error fetching weather data."

#     weather_description = data["weather"][0]["description"]
#     temperature = data["main"]["temp"] - 273.15
#     return f"The weather in {city} is currently {weather_description} with a temperature of {temperature:.2f}°C."

# Function to evaluate a math expression safely


def evaluate_expression(expression):
    try:
        result = eval(expression)
        return f"The result is: {result}"
    except Exception:
        return "Sorry, I couldn't evaluate that. Please make sure your math expression is correct."

# Function to generate a response based on the user's message and their name


def generate_response(message, user_name):
    message = message.lower().strip()

    dont_understandind_messages = [
        "Sorry, I didn't understand. Can you rephrase your question? Or type 'info' for help.",
        "I'm not an advanced chatbot, so sorry, I don't understand what you mean. Try 'info' for more options.",
        "Can you rephrase your question? 🤔 Type 'info' to see what I can do.",
        "I didn't understand 🤔 Try typing 'info' to learn more about what I can do.",
        "Sorry, I didn't understand 🤔 Type 'info' for a list of commands."
    ]

    hi_messages = [
        f"Hello {user_name}! How can I assist you today? 😊",
        f"Hello {user_name}, welcome! How can I help you?",
        f"Hi {user_name}, how can I assist you today?"
    ]

    if message == "info":
        return (
            "\n____________________________________________________________________\n"
            "Here are some things I can assist you with:\n"
            "- **Greetings:** You can say 'hello' or 'hi' to start a conversation!\n"
            "- **Games:** I can play various games with you:\n"
            "  - **Rock-Paper-Scissors:** A simple game where you compete against me!\n"
            "  - **Number Guessing:** Try to guess the number I'm thinking of between 1 and 10.\n"
            "- **Math Operations:** You can ask me to perform basic math operations such as:\n"
            "  - Addition (e.g., '2 + 2')\n"
            "  - Subtraction (e.g., '5 - 3')\n"
            "  - Multiplication (e.g., '3 * 4')\n"
            "  - Division (e.g., '10 / 2')\n"
            # "- **Weather Information:** Ask me about the weather by saying:\n"
            #   "  - 'weather in [city]' (e.g., 'weather in Paris')\n"
            "- **Time Check:** You can ask me, 'what time is it?' to get the current time.\n"
            "- **Jokes:** I can tell you a random joke. Just say, 'tell me a joke'!\n"
            "- **Goodbye:** When you're ready to leave, simply say 'bye' or 'goodbye'.\n"
            "- **Help:** Type 'info' at any time to see this list again!\n"
            "Feel free to try any of these features!"
            "\n____________________________________________________________________\n"
        )
    elif is_math_expression(message):
        return evaluate_expression(message)
    elif "hello" in message or "hi" in message:
        if user_name == "":
            return "Hello! What's your name?"
        else:
            return random.choice(hi_messages)
    elif "bye" in message or "goodbye" in message:
        return None  # We will handle this in the main loop
    elif message in ["how are you", "how are you doing?", "what's up?"]:
        return f"I'm a bot, so I'm always functioning as expected. How about you, {user_name}?"
    elif message in ["good", "fine", "I'm good", "great", "awesome", "I'm fine", "Im good", "Im fine"]:
        return f"Nice! I'm glad to hear that! 😊 As a bot, I'm here to assist you. What can I do for you today, {user_name}?"
    elif message in ["bad", "not good", "I'm not feeling well", "terrible", "sad"]:
        return f"I'm sorry to hear that. 😢 As a bot, I'm here to assist you. What can I do for you today, {user_name}?"
    elif "how are you" in message:
        return f"I'm a bot, so I'm always functioning as expected. How about you, {user_name}?"
    elif "good" in message or "im good" in message:
        return f"nice, {user_name}?"
    elif "what is your name" in message or "what's your name" in message or "whats your name" in message:
        return f"I'm a chat_bot and Daniel Seyed Saadat created me."
    elif "joke" in message or "tell me a joke" in message or "tell me joke" in message:
        return joke()
    elif "weather" in message:
        return "I'm not equipped with weather data yet, but it's always sunny in here! ☀️"
    elif "time" in message or "what time is it" in message:
        return get_time()
    # elif "weather" in message:
    #     city = message.split("weather in")[-1].strip()
    #     if city:
    #         return get_weather(city)
    #     else:
    #         return "Please specify a city to get the weather information."
    else:
        return random.choice(dont_understandind_messages)

# Game selection function


def games():
    while True:
        print("\nWelcome to the game section! Choose a game:")
        print("\n1. Rock-Paper-Scissors")
        print("2. Number Guessing")
        print("\n4. Exit to Main Menu\n")  # New exit option

        choice = input("Enter the game number (1, 2, or 4): \n")

        if choice == '1':
            rock_paper_scissors()
        elif choice == '2':
            number_guessing()
        elif choice == '4':  # Exit option
            print("Exiting to main menu...")
            break  # Exit the game selection loop
        else:
            print("Invalid choice! Please enter 1, 2, or 4.")

# Main function to start the chatbot and handle user interactions


def main():
    print("\nThis is CS50-P Final Project || --> Github:danielSeSa <--")
    print("Welcome to ChatBot! If you need help, type 'info' to see what I can do.")
    print("To exit the chat, simply type 'bye'.\n")
    user_name = ""

    while True:
        user_message = get_user_input()

        if "bye" in user_message.lower():
            goodbye_messages = [
                f"Goodbye {user_name}! Have a nice day! 😊",
                f"See you later {user_name}! Take care! 👋",
                f"Farewell {user_name}! Hope to chat again soon! 😄",
                f"Bye {user_name}! Don't forget to smile today! 😊",
                f"Goodbye {user_name}! It was nice talking to you! 😄"
            ]
            print(f"Bot: {random.choice(goodbye_messages)}")
            break

        if user_name == "" and ("hello" in user_message.lower().strip() or "hi" in user_message.lower().strip()):
            print("Bot: Hello! What's your name?")
            user_name = get_user_input().strip()
            if user_name:
                print(f"Bot: Nice to meet you, {user_name}!")
            else:
                print("Bot: I didn't catch your name, but that's okay!")
        elif "play a game" in user_message.lower() or "game" in user_message.lower():
            games()  # Call the games function when the user wants to play a game
        else:
            response = generate_response(user_message, user_name)
            if response:  # Check if response is not None
                print(f"Bot: {response}")


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
