from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

chain = prompt | model

past_messages = [
    HumanMessage(content="Hi, my name is Alex."),
    AIMessage(content="Hello Alex! How can I help you today?")
]

response = chain.invoke({
    "chat_history": past_messages,
    "input": "What is my name?"
})

print(response.content)

## if u need to use the chat history, just add MessagesPlaceholder in the prompt template, and pass the chat history when invoking the chain. 
# it will automatically format the messages for you.
