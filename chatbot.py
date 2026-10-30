import datetime

def play_chatbot():
    print("=" * 45)
    print("      WELCOME TO THE ENHANCED BASIC CHATBOT      ")
    print("=" * 45)
    
    raw_name = input("Bot: Hello! What is your name? \nYou: ").strip()
    
    # Smart cleanup for common introductory phrases
    cleaned_name = raw_name
    for prefix in ["hi im ", "hi, im ", "hi i\'m ", "i am ", "im ", "i\'m ", "my name is ", "this is "]:
        if cleaned_name.lower().startswith(prefix):
            cleaned_name = cleaned_name[len(prefix):].strip()
            
    # Capitalize nicely or fallback to "Friend" if empty
    user_name = cleaned_name.title() if cleaned_name else "Friend"
        
    print(f"\nBot: Nice to meet you, {user_name}! Type 'bye' to exit anytime.\n")
    
    while True:
        # Now uses the clean name for the prompt
        user_input = input(f"{user_name}: ").strip().lower()
        
        # Rule-based responses
        if user_input in ["hello", "hi", "hey"]:
            print(f"Bot: Hi {user_name}! I\'m fine, thanks!")
        elif user_input in ["how are you", "how are you?"]:
            print("Bot: I\'m doing great, thank you! How can I help you today?")
        elif user_input in ["what is your name", "who are you"]:
            print("Bot: I am a simple rule-based Python chatbot built for my internship task.")
        elif user_input in ["time", "what time is it"]:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Bot: The current time is {current_time}.")
        elif user_input in ["joke", "tell me a joke"]:
            print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")
        elif user_input in ["bye", "goodbye", "exit"]:
            print(f"Bot: Goodbye, {user_name}! Have a wonderful day!")
            break
        else:
            print(f"Bot: That\'s interesting, {user_name}! Tell me more (or type 'bye' to exit).")
            
        print("-" * 40)

if __name__ == "__main__":
    play_chatbot()
