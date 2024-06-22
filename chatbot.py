def chatbot_response(user_input):
    # Convert the input to lowercase for easier matching
    user_input = user_input.lower()
    
    # Define responses for specific inputs
    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I assist you today?"
    elif 'how are you' in user_input:
        return "I'm just a program, but I'm here to help you!"
    elif 'name' in user_input:
        return "I am a simple chatbot created to assist you."
    elif 'bye' in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

def main():
    print("Hello! How can I help you today?")
    while True:
        user_input = input("> ")
        response = chatbot_response(user_input)
        print(response)
        
        # Exit the chat loop if the user says goodbye
        if 'bye' in user_input.lower():
            break

if __name__ == "__main__":
    main()
