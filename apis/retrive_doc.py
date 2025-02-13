
# from pinecone.grpc import PineconeGRPC as Pinecone
# from pinecone import ServerlessSpec
# import time,os
# import dotenv
# dotenv.load_dotenv()
# from ai_helper.summarizer import call_llm


# def retrive_doc(query):
#     try:
            
#             pc = Pinecone(api_key=os.getenv("key"))
#             index="retrival-doc"
#             index = pc.Index(index)

#             query_embedding = pc.inference.embed(
#             model="multilingual-e5-large",
#             inputs=[query],
#             parameters={
#                 "input_type": "query"
#             }
#         )

#         # Search the index for the three most similar vectors
#             results = index.query(
#             namespace="resume",
#             vector=query_embedding[0].values,
#             top_k=2,
#             include_values=False,
#             include_metadata=True
#         )

#             print(results)
        

#             content=""
#             for i, text in enumerate(results, 1):
#                 print(f"\nSource Text {i}:")
#                 print(text)
#                 content=content+text
#             response_summary=call_llm(content)
#             return response_summary

#     except Exception as e:
#         print(e)
#         raise ValueError(e)

