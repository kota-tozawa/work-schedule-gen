***
## 勤務表生成手順（Docker）
- Docker、Git をインストール。
### 今は仮の自分用手順
- `docker build --tag k1038/work-schedule-gen:latest .`
- `docker container run --name work-schedule-app -it -d k1038/work-schedule-gen:latest`
- `docker ps`
- `docker container exec -it work-schedule-app bash`
- `python main.py`
- `exit`
- `docker container cp work-schedule-app:/app/generated/. ~/`

- `docker container start work-schedule-app`
- `docker container stop work-schedule-app`

***
## 開発環境構築＆勤務表生成（Mac OS X）
[**事前にインストールしておくもの**]
- Git
- Docker
- Visual Studio Code などのエディタ
- （必要に応じて）Homebrew
（`pyenv`, `pyenv-virtualenv`は Homebrew を用いてインストールすることもできます。）

[**注意**]
下記手順では、`python 3.5.0`の仮想環境を導入します。
すでにインストールしてあるならば、`pyenv`, `pyenv-virtualenv`のインストール手順はスキップして大丈夫です。

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

下記を実行したのち、再度`pyenv install 3.5.0`を実行してください：
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
8. 仮想環境をアクティベート。
```
pyenv activate venv_3.5.0
```
9. バージョンが`3.5.0`に切り替わったか確認。
```
python --version
```
10. 勤務表生成に必要なパッケージをインストール。
```
pip install -r requirements.txt
```
11. カレントディレクトリを`work_schedule_gen/modules`にしてから、対話型のpythonスクリプトを実行し、目的の年月の勤務表を生成。
```
cd work_schedule_gen/modules
python main.py
```
12.  `work_schedule_gen/generated`に生成されたファイルがあるので、好きな場所に移動・コピーしても良いし、`generated`に置いたまま記入してもOKです。その場合は、同じ年月の勤務表を生成して上書きしないよう気をつけてください。
13.  仮想環境をディアクティベート。
```
pyenv deactivate venv_3.5.0
```
14.  次に生成する時は、`8.`,`10.`~`13.`の手順のみ行えば良い。
***
[参考]

- https://qiita.com/Kodaira_/items/feadfef9add468e3a85b
- https://qiita.com/nsas454/items/c5bd3a535205d434234e
- https://note.nkmk.me/python-pip-install-requirements/

- https://xlrd.readthedocs.io/en/latest/api.html
- https://xlutils.readthedocs.io/en/latest/

***
### 参考
- https://qiita.com/Kodaira_/items/feadfef9add468e3a85b
- https://qiita.com/nsas454/items/c5bd3a535205d434234e
- https://note.nkmk.me/python-pip-install-requirements/

- https://xlrd.readthedocs.io/en/latest/api.html
- https://xlutils.readthedocs.io/en/latest/