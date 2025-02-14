
from pinecone.grpc import PineconeGRPC as Pinecone
import os
import dotenv
from ai_helper.openai_summarizer import call_openai_llm
dotenv.load_dotenv()



def retrive_record(query):
    try:
            
            pc = Pinecone(api_key=os.getenv("key"))
            index="retrival-doc"
            index = pc.Index(index)

            query_embedding = pc.inference.embed(
            model="multilingual-e5-large",
            inputs=[query],
            parameters={
                "input_type": "query"
            }
        )

        # Search the index for the three most similar vectors
            results = index.query(
            namespace="resume",
            vector=query_embedding[0].values,
            top_k=2,
            include_values=False,
            include_metadata=True
        )

            print(results)
        

            content=""
            for  text in results["matches"]:
                
                print(text["metadata"]["source_text"])
                content=content+text["metadata"]["source_text"]
            response_summary=call_openai_llm(content)
            return response_summary

    except Exception as e:
        print(e)
        raise ValueError(e)

