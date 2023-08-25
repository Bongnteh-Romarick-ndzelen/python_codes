import responses

def get_response(user_input):
    user_input = user_input.lower()
    
    # Check for specific keywords in user input
    if 'hello' in user_input:
        return responses.greet()
    elif 'bye' in user_input:
        return responses.goodbye()
    elif 'what is your name' in user_input:
        return responses.name()
    elif 'what can you do' in user_input:
        return responses.work()

    elif 'how can we solve quadratic equations' in user_input:
        return responses.quadratic()
    else:
        return responses.default()

def chat():
    print("Chatbot: Hello! How can I assist you today?\nEnter your question?")
    
    while True:
        user_input = input("User: ")
        response = get_response(user_input)
        print("Chatbot:", response)
        
        if 'bye' in user_input:
            break

if __name__ == '__main__':
    chat()