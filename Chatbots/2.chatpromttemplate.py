from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

chat_template = ChatPromptTemplate([
    ('system', 'you are a helpful {domain} assistant'),
    ('human', 'Explain in simple terms, the concept of {concept}'),

])

prompt = chat_template.invoke({
    'domain': 'math',
    'concept': 'calculus'
})

print(prompt)

## new style creating chatbots by using prompt template, which is more structured and easier to manage. just add model