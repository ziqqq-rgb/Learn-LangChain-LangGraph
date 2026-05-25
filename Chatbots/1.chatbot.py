from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

chat_history = [
    SystemMessage(content="You are a helpful assistant")
]

while True:
    user_input = input("User: ")
    chat_history.append(HumanMessage(content=user_input))

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat...")
        break

    result = model.invoke(chat_history)

    chat_history.append(AIMessage(content=result.content))
    print(f"AI: {result.content}")

print (chat_history)

## This is just a simple chatbot (fundamental implementation).