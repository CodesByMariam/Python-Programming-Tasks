def chatbot():
    print("🤖 Bot: Assalam o Alaikum! Main tumhara Chatbot hun")
    print("🤖 Bot: 'bye' likho to main chala jaun ga\n")

    while True:
        user = input("Tum: ").lower()

        if user == "hello" or user == "hi" or user == "salam":
            print("Bot: Walaikum Salam! Kesi ho Mariam? 😊")

        elif user == "how are you" or user == "kesi ho":
            print("Bot: Main to bilkul fit hun! Tum sunao?")

        elif "name" in user:
            print("Bot: Mera naam AI Bot hai. Tumhara naam Mariam hai na?")

        elif "help" in user:
            print("Bot: Main 'hello', 'how are you', 'name', 'bye' samajhta hun")

        elif user == "bye" or user == "khuda hafiz":
            print("Bot: Allah Hafiz Mariam! Phir milte hain ❤️")
            break

        else:
            print("Bot: Sorry, ye baat samajh nahi aayi. 'help' likh ke dekho")

chatbot()