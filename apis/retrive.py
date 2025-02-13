
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
import time,os
import dotenv
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
            # response_summary=call_llm(content)
            return content

    except Exception as e:
        print(e)
        raise ValueError(e)

