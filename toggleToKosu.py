import pandas as pd

# Toggl-report.csv 読み込み
df = pd.read_csv('Toggl-report.csv', sep=',')

# 必要なデータの変数定義
date = (df['Start date'])
time = (df['Duration'])
description = (df['Description'])
division = (df['Tags'])
replace_date = date.str.replace('-', '/')
split_time = time.str.split(':')
hr = []
min = []
sec = []
kosu_data = []

def main():
  res_kosu()

  # DataFrameを作成してCSV書き出し
  kosu_df = (pd.DataFrame(kosu_data, columns=['日付', '業務内容', '工数（時間', '工数区分']))
  kosu_df.to_csv('Toggl-to-kosu.csv', sep=',', index=False)

# 工数シートデータの生成
def res_kosu():
  for index, row in enumerate(df.index):
    hr = (int(split_time[index][0]))
    min = (int(split_time[index][1]))
    sec = (int(split_time[index][2]))
    
    # 30秒以上の場合は1分繰り上げ
    if sec > int(30):
      min = min + int(1)

    # 55分以上の場合は1時間繰り上げ
    if min >= int(55):
      hr = hr + int(1)
      min = int(0)

    # 分を時間に変換
    min_to_hr = "{:.2f}".format((min / (int(60))))
    
    # データ配列の生成
    kosu = float(hr) + float(min_to_hr)
    kosu_data.append([replace_date[index], description[index], str(kosu), division[index]])
  return kosu_data

# main関数呼び出し
if __name__ == "__main__":
    main()