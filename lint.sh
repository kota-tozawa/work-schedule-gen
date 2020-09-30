#!/bin/bash

echo 'コードを整形中...'
autopep8 --in-place --aggressive --ignore errors=E226,E24,W50,W690,F401,E501 app/*.py
autopep8 --in-place --aggressive --ignore errors=E226,E24,W50,W690,F401,E501 app/modules/*.py

echo 'Pythonスクリプトのフォーマットの問題点を検出中...'
result=`flake8 --extend-ignore=F401,E501 app/`
if ["$result" -eq '']
then
  echo '問題点は見つかりませんでした。'
else
  echo "$result"
fi