from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from typing import  Annotated, Literal
from pydantic import BaseModel, Field

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

#schema
from typing import Annotated, Literal
from pydantic import BaseModel, Field

class Review(BaseModel):
    # Modern approach: Annotated + Field for descriptions Field means "Extra rules and instructions"

    key_themes: Annotated[
        list[str], 
        Field(description="must write down key themes in the review")
    ]
    
    summary: Annotated[
        str, 
        Field(description="must write down a summary of the review")
    ]
    ## literal means "Only see Exactly these values, no more, no less"
    sentiment: Annotated[
        Literal["positive", "negative", "neutral"], 
        Field(description="must write down the sentiment of the review")
    ]


structured_output = model.with_structured_output(Review)

prompt = """
I go to scholl, aguy bully me, i got knocked out by khabib, i sad, i want to cry, but i cant, i want to die, but i cant, i want to sleep, but i cant, what should i do? 
"""

result = structured_output.invoke(prompt)
print(result)
