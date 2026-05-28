from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

template1 = PromptTemplate(
    template="""I go to scholl, aguy bully me, i got knocked out by {input}, i sad, i want to cry, but i cant, i want to die, but i cant, i want to sleep, but i cant, what should i do? 
    Answer in a very detailed way, and give me 3 key themes in the review""",
    input_variables=["input"]
)

template2 = PromptTemplate(
    template="""a guy named {name} save me""",
    input_variables=["name"]
)

parser = StrOutputParser()
##StrOutputParser simply converts the AI's complex raw response into a plain text string.


chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({ "input": "khabib" })
print(result)