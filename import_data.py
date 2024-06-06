import os
import django
import pandas as pd
from datetime import datetime

# 設定環境變數和 Django 設定模組
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')  # 替換為你的 Django 專案設定模組
django.setup()

from stockanalysis.models import News  # 確保在 django.setup() 之後導入 Django 模型

def import_data_from_excel(file_path):
    try:
        # 讀取 Excel 檔案
        df = pd.read_excel(file_path)

        # 遍歷資料並插入資料庫
        for index, row in df.iterrows():
            # 轉換日期欄位為正確格式
            full_post_time = datetime.strptime(row['發文完整時間'], "%Y/%m/%d").strftime("%Y-%m-%d")

            # 插入資料庫
            News.objects.create(
                title=row['標題'],
                full_post_time=full_post_time,
                author=row['作者'],
                url=row['網址'],
                upvotes=row['總推文數'],
                downvotes=row['總噓文數'],
                arrows=row['總箭頭數'],
                content=row['內文'],
                source_page=row['來源網頁'],
                sentiment_feedback=row['情緒分析回饋']
            )
        
        print("Data imported successfully")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    excel_file_path = 'ptt_stock_sentiment_220525-240525.xlsx'  # 設置 Excel 檔案路徑
    import_data_from_excel(excel_file_path)
