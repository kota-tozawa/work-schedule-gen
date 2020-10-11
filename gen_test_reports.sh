#!/bin/sh

echo "テスト結果レポート生成中..."
cd app
python -m pytest --html=test_result_report.html
mv assets ../docs/
mv test_result_report.html ../docs/
cd ../
echo "生成完了."

echo "カバレッジレポートを生成中..."
python -m pytest -v --cov=app --cov-report=html
mv htmlcov docs/
mv .coverage docs/
echo "生成完了."
echo "生成されたレポートはdocsディレクトリ配下にあります。"