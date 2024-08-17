import json
import csv
from io import StringIO
import pandas as pd

def handler(event, context):
    try:
        # POSTリクエストのボディからCSVデータを取得
        csv_data = json.loads(event['body'])['csv_data']
        
        # CSVデータを処理
        df = pd.read_csv(StringIO(csv_data))
        
        # ここで弁当注文の処理を行う
        # 例: 注文の合計を計算
        total_orders = len(df)
        
        # 処理結果を返す
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'注文が正常に処理されました。合計 {total_orders} 件の注文があります。'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }