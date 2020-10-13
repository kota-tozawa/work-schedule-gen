#!/bin/sh
#
# PYTHONPATHを設定しないと, カバレッジレポート作成時に「no module named ~」エラーにが出る．
# このシェルスクリプトを実行する際には，下記のPYTHONPATHのところのコメントアウトを外したのち，自分の環境に合うようパスを修正してください．
#

# export PYTHONPATH="${PYTHONPATH}:/Your/path/to/work-schedule-gen/app/components"

rm -r ./docs/*

echo "テスト結果レポート生成中..."
cd app
python -m pytest --html=test_result_report.html
mkdir ../docs/test_result
mv assets ../docs/test_result/
mv test_result_report.html ../docs/test_result/
echo "生成完了."

echo "カバレッジレポートを生成中..."
python -m pytest -v --cov=./tests --cov-report=html
mkdir ../docs/test_coverage
mv htmlcov ../docs/test_coverage/
mv .coverage ../docs/test_coverage/
echo "生成完了."
echo "生成されたレポートはdocsディレクトリ配下にあります。"