from langchain_openai.chat_models import ChatOpenAI
import dotenv,os
dotenv.load_dotenv()


def split_text_into_chunks(text_file,chunk_size):
    with open(text_file, 'r') as file:
        text = file.read()
    words = text.split()
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks



def get_llm():
    try:
        return ChatOpenAI(
        temperature=0,
            model="gpt-4o-mini",
           api_key=os.getenv("gpt_key")  ,    )
    except Exception as e:
        print(e,"connetion")