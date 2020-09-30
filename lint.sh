#!/bin/bash
#
# work-schedule-genディレクトリ以下（appディレクトリと同じ階層）をカレントディレクトリにしてから実行
#

# 1行文字数制限は無視（F401,E501）
echo "全てのPythonスクリプトを整形中..."
autopep8 --in-place --aggressive --ignore errors=E226,E24,W50,W690,F401,E501 app/*.py
autopep8 --in-place --aggressive --ignore errors=E226,E24,W50,W690,F401,E501 app/modules/*.py

echo "全てのPythonスクリプトのフォーマットの問題点を検出中..."
result=`flake8 --extend-ignore=F401,E501 app/`
if ["$result" -eq ""]
then
  echo "問題点は見つかりませんでした。"
else
  echo "$result"
fi