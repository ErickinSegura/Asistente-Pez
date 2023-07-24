from modules.listen import Listener
from modules.keywords import keywords
from utilities.chat import chat

def main():
    listener = Listener()

    try:
        user_prompt = Listener.listen()
        command = list(filter(lambda x: x in user_prompt, keywords))
        if command:
            keywords[command[0]](user_prompt)
        else:
            chat(user_prompt)
        
    except Exception as e:
        print(f"Lo siento, no entendi {e}")
        print(e)

if __name__ == '__main__':
    main()

