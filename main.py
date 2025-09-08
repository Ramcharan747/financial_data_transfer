from flask import Flask, request, jsonify
from openbb import obb

app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_openbb_data():
    data = request.get_json()
    symbol = data.get('symbol', 'AAPL')
    start_date = data.get('start_date', '2020-01-01')

    try:
        stock_data = obb.stocks.load(symbol=symbol, start_date=start_date).to_df()
        return stock_data.to_json(orient='split')
    except Exception as e:
        return jsonify({"error": str(e)})
