#!/bin/sh
#
# work-schedule-genディレクトリ以下（appディレクトリと同じ階層）をカレントディレクトリにしてから実行
#

# Pythonコーディング規約PEP8
# https://pep8.readthedocs.io/en/release-1.7.x/intro.html

echo "全てのPythonスクリプトを整形中..."
autopep8 --in-place --recursive --ignore errors=F401,E501 app
autopep8 --in-place --recursive --select=E226,E24 app
echo "整形が完了しました。"

echo "全てのPythonスクリプトのフォーマットの問題点を検出中..."
result=`flake8 --extend-ignore=F401,E501 app/`
if ["$result" -eq ""]
then
  echo "問題点は見つかりませんでした。"
else
  echo "フォーマットの問題が検出されました。"
  echo "整理された問題点は以下の通りです："
  echo "$result"
fi