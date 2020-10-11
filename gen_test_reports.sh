#!/bin/sh
#
# PYTHONPATHを設定しないと「no module named ~」エラーになる．
# 下記のコメントアウトしてあるPYTHONPATHを変更して，自分の環境に合うよう設定する．
#

# export PYTHONPATH="${PYTHONPATH}:/Users/your/path/to/work-schedule-gen/app/components"
rm -r ./docs/*
echo "テスト結果レポート生成中..."
cd app
python -m pytest --html=test_result_report.html
mv assets ../docs/
mv test_result_report.html ../docs/
echo "生成完了."

echo "カバレッジレポートを生成中..."
python -m pytest -v --cov=. tests --cov-report=html
mv htmlcov ../docs/
mv .coverage ../docs/
echo "生成完了."
echo "生成されたレポートはdocsディレクトリ配下にあります。"