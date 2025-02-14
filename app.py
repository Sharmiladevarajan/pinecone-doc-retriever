from flask import Flask, request, jsonify
from flask_cors import CORS
# from apis.retrive_doc import retrive_doc
from apis.retrive import retrive_record

app = Flask(__name__)
CORS(app) 


# @app.route('/retrive_document', methods=['POST'])
# def retrive_data(): 
#     try:
#         return jsonify({"data":retrive_doc(request.get_json()["query"]),"status_code":200})
#     except Exception as e:
#         return jsonify({"data":e,"status_code":400})
@app.route('/retrive_record', methods=['POST'])
def retrive_data(): 
    try:
        return jsonify({"data":retrive_record(request.get_json()["query"]),"status_code":200})
    except Exception as e:
        return jsonify({"data":e,"status_code":400})
    


if __name__ == "__main__":
   app.run(port=808)
