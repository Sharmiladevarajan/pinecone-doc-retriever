from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
import time,os
import dotenv
dotenv.load_dotenv()
from services.constant_functions import split_text_into_chunks

def upsert_data():
    try:
        
        pc = Pinecone(api_key=os.getenv("key"))

        result_data=split_text_into_chunks("sample.txt",150)
        print(len(result_data))


        data = []

        for i, element in enumerate(result_data, start=1):
            obj = {
                "id": str(i),
                "text": element,
                "category": "resume"
            }
            data.append(obj)

        data
        embeddings = pc.inference.embed(
            model="multilingual-e5-large",
            inputs=[d["text"] for d in data],
            parameters={
                "input_type": "passage", 
                "truncate": "END"
            }
        )

        print(embeddings)



        index_name = "retrival-doc"
        index = pc.Index(index_name)

        records = []
        for d, e in zip(data, embeddings):
            records.append({
                "id": d["id"],
                "values": e["values"],
                "metadata": {
                    "source_text": d["text"],
                    "category": d["category"]
                }
            })


        index.upsert(
            vectors=records,
            namespace="resume"
        )
        time.sleep(20)
        return True  
    except Exception as e:
        print(e)
        raise ValueError(e)



