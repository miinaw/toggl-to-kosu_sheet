# toggl-to-kosu_sheet
[toggl](https://toggl.com/)からエクスポートしたCSVデータを工数用のCSVデータに変換する

## 工数シートに必要なデータ
- 日付
- 業務内容
- 工数（時間)
- 工数区分 => togglでTagとして設定しておく

## 手順
1. `pip install pandas`
2. togglからエクスポートしたCSVデータを`Toggl-report.csv`という名前でディレクトリ内に保存
3. `python tggleToKosu.py`で実行
4. `Toggl-to-kosu.csv`というファイル名で工数用のCSVデータが書き出される

### ※pipコマンドが使えないとき
easy_install
`sudo easy_install pip`
