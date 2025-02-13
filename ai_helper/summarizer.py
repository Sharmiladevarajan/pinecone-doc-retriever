from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
import boto3
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from services.prompts import summary_prompt
from langchain_community.chat_models import BedrockChat
import dotenv
dotenv.load_dotenv()


def get_boto3_bedrock():
    return boto3.client(
        "",
        aws_access_key_id=os.getenv("AWS_ACCESS"),
        aws_secret_access_key=os.getenv("SECRET_ACCESS_KEY"),
        region_name="us-east-1",
    )


def get_llm(boto3_bedrock):
    return BedrockChat(
        model_id=os.getenv("MODEL_ID"),
        client=boto3_bedrock,
        region_name="us-east-1",
        model_kwargs={"temperature": 0.7}
    )

def call_llm(content):
    try:
        boto3_bedrock = get_boto3_bedrock()
        llm = get_llm(boto3_bedrock)
        class case_creation_parser(BaseModel):
            summary: str = Field(description="gives the summary of the content")
            
        case_parser = JsonOutputParser(pydantic_object=case_creation_parser)
        prompt= PromptTemplate(template=summary_prompt, input_variables=["content_list"])
        case_creation_interaction = prompt | llm | case_parser
       
        response = case_creation_interaction.invoke(
            {"content_list": content}
        )
        return response["summary"]
    except Exception as e:
            print('inexcep',str(e))



