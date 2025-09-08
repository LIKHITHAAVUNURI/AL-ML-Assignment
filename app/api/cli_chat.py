app/chatbot/cli_chat.py
import requests

def chat():
    print("👨‍🍳 RecipeBot: Enter ingredients (comma-separated) or type 'exit'")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        ingredients = [i.strip() for i in user_input.split(",") if i.strip()]
        response = requests.post("http://127.0.0.1:8000/get-recipe", json={"ingredients": ingredients})

        if response.ok:
            data = response.json()
            print(f"\n🤖 RecipeBot Suggestion:\n🍽️ {data['suggested_recipe']} (Match: {data['similarity_score']})\n")
        else:
            print("Error: Couldn't fetch recipe.")

if __name__ == "__main__":
    chat()
