from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from typing import TypedDict, Annotated, Optional

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

#schema
class Review(TypedDict):
    key_themes: Annotated[list[str], "must write down key themes in the review"] ##annnotated is like adding metadtata aka extra info or instructions
    summary: Annotated[str, "must write down a summary of the review"]

structured_output = model.with_structured_output(Review)

prompt = """
I go to scholl, aguy bully me, i got knocked out by khabib, i sad, i want to cry, but i cant, i want to die, but i cant, i want to sleep, but i cant, what should i do? 
"""

result = structured_output.invoke(prompt)
print(result)