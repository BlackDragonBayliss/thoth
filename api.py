from flask import Flask, jsonify, request
from dataFrameManager import DataFrameManager
app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    content = request.get_json()
    return_value = 'pass'
    print(str(content))
    response = "success"
    for key, value in content.items():
        if key == 'requestType':
            if value == "calculateDataFramePng":
                # print("panda")
                dataFrameManager = DataFrameManager()
                resultCSV = dataFrameManager.calculateDataFrame(str(content))
                resultCSV = ""
                return resultCSV
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=4460)