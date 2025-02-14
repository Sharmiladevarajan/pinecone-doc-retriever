
from langchain_core.prompts import ChatPromptTemplate
from services.prompts import open_ai_summary
from services.constant_functions import get_llm


def call_openai_llm(content):
    try:
        
        llm=get_llm()
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    open_ai_summary,
                ),
                ("human", "Do summarize the content"),
            ]
        )

        chain = prompt | llm
        response=chain.invoke(
            {
                
                "content_list": content,
            }
        )
        return response.content
    except Exception as e:
        print(e)

