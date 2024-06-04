import random

# Define a list of facts
facts = [
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
    "A day on Venus is longer than a year on Venus. It takes 243 Earth days for Venus to rotate once on its axis, but only 225 Earth days to orbit the Sun.",
    "Bananas are berries, but strawberries aren't. Botanically, a berry is a fruit produced from the ovary of a single flower with seeds embedded in the flesh.",
    "The Eiffel Tower can be 15 cm taller during the summer, due to the expansion of iron in the heat.",
    "Octopuses have three hearts: two pump blood through the gills, while the third pumps it through the rest of the body.",
    "A group of flamingos is called a 'flamboyance'.",
    "There are more possible iterations of a game of chess than there are atoms in the known universe.",
    "Wombat poop is cube-shaped. This helps it stay in place, marking the wombat's territory."
]

def get_fact():
    return random.choice(facts)

def chat():
    print("Hi! I'm a fact AI. Ask me for a fact or type 'bye' to exit.")
    
    while True:  
        user_input = input("You: ").strip().lower()
        
        if user_input in ["bye", "exit", "quit"]:
            print("Fact AI: Goodbye!")
            break
        elif "fact" in user_input or "tell me" in user_input:
            fact = get_fact()
            print(f"Fact AI: {fact}")
        else:
            print("Fact AI: I'm here to share facts. Ask me for a fact or type 'bye' to exit.")

if __name__ == "__main__":
    chat()
  
