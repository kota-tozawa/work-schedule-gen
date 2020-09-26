# 勤務表生成手順（Mac OS X）
***
[**事前にインストールしておくもの**]
- Git
- Visual Studio Code などのエディタ
（Vim, Emacs などなんでも構いません。）

[**注意**]
下記手順では、`python 3.5.0`の仮想環境を導入する。
すでにインストールしてあるならば、`pyenv`, `pyenv-virtualenv`のインストール手順はとばして大丈夫です。
***
1. zsh で下記を実行し、Pythonの実行環境を管理するツール「pyenv」を使えるようにする。
（普段 bash を使っているなら bash をベースに下記手順を行っても大丈夫です。）
```
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
```
2. 下記を`.zprofile`に書き込む。
（`vi ~/.zprofile`などで書き込んでください。`.zprofile`がホームディレクトリになければ作成してください。）
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
```
3. 下記を`.zshrc`に書き込む。
```
eval "$(pyenv init -)"
```
4. 仮想環境用の python 3.5.0 をインストール。（使用するライブラリの関係上 python 3.5.0 を用います。）
```
pyenv install 3.5.0
```
[**インストール中に`Ignoring ensurepip failure: pip 7.1.2 requires SSL/TLS`というエラーが発生したら**]
下記を実行：
```
brew uninstall --ignore-dependencies openssl@1.1
pyenv install 3.5.0
```
5. 下記を実行し、pyenv のプラグイン「pyenv-virtualenv」を使えるようにする。
```
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
```
6. 下記を`.zshrc`に書き込む。
```
eval "$(pyenv virtualenv-init -)"
```
7. 仮想環境の作成。
```
pyenv virtualenv 3.5.0 venv_3.5.0
```
8. 仮想環境をアクティベート。（ディアクティベート：`pyenv deactivate`）
```
pyenv activate venv_3.5.0
```
9. バージョンが`3.5.0`に切り替わったか確認。
```
python --version
```
9. 勤務表生成に必要なパッケージをインストール。
```
pip install -r requirements.txt
```
10. 対話型の python スクリプトを実行し、目的の年月の勤務表を生成。
```
python work_schedule_gen/work_schedule_gen.py
```
***

# 勤務表生成手順（Windows 10）

***
[参考]
https://qiita.com/Kodaira_/items/feadfef9add468e3a85b
https://qiita.com/nsas454/items/c5bd3a535205d434234e
https://note.nkmk.me/python-pip-install-requirements/

https://pypi.org/project/xlrd2/
https://pypi.org/project/xlwt-fix/
https://pypi.org/project/xlutils/