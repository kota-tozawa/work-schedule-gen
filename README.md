***
## 勤務表生成手順
### 事前にインストールしておくもの
- Docker
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
## ローカルで開発環境構築＆勤務表生成（Mac OS X）
### 事前にインストールしておくもの
- Git
- Docker
- Visual Studio Code
- （必要に応じて）Homebrew \
（`pyenv`, `pyenv-virtualenv`は Homebrew を用いてインストールすることもできます。）

### 注意
下記手順では、`python 3.5.0`の仮想環境を導入します。\
すでにインストールしてあるならば、`pyenv`, `pyenv-virtualenv`のインストール手順はスキップして大丈夫です。

### 開発環境構築手順
1. zsh で下記を実行し、Pythonの実行環境を管理するツール「pyenv」を使えるようにする。\
（普段 bash を使っているなら bash をベースに下記手順を行っても大丈夫です。）
```zsh
$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv
```
2. 下記を`.zprofile`に書き込む。\
（`vi ~/.zprofile`などで書き込んでください。`.zprofile`がホームディレクトリになければ作成してください。）
```zsh
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
```
3. 下記を`.zshrc`に書き込む。
```
eval "$(pyenv init -)"
```
4. 仮想環境用の python 3.5.0 をインストール。（使用するライブラリの関係上 python 3.5.0 を用います。）
```zsh
$ pyenv install 3.5.0
```
#### インストール中に`Ignoring ensurepip failure: pip 7.1.2 requires SSL/TLS`というエラーが発生したら
下記を実行してください：
```zsh
$ brew uninstall --ignore-dependencies openssl@1.1
$ pyenv install 3.5.0
```
1. 下記を実行し、pyenv のプラグイン pyenv-virtualenv を使えるようにする。
```zsh
$ git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
```
6. 下記を`.zshrc`に書き込む。
```
eval "$(pyenv virtualenv-init -)"
```
7. 仮想環境の作成。
```zsh
$ pyenv virtualenv 3.5.0 venv_3.5.0
```
8. 仮想環境をアクティベート（ディアクティベート：`pyenv deactivate venv_3.5.0`）。
```zsh
$ pyenv activate venv_3.5.0
```
9. バージョンが`3.5.0`に切り替わったか確認。
```zsh
$ python --version
```
10. 勤務表生成に必要なパッケージをインストール。
```zsh
$ pip install -r requirements.lock
```
11. コマンドパレットを開き、そこに`>python`と入れ、「Python: Select Interpreter」を選択し、「Python 3.5.0 64-bit (venv_3.5.0)」を選択。

### 勤務表生成手順
1. カレントディレクトリを`work-schedule-gen/app`にしてから、対話型のpythonスクリプトを実行し、目的の年月の勤務表を生成。
```zsh
$ cd app
$ python main.py
```
2. `app/generated`に生成されたファイルがあるので、好きな場所に移動・コピーしても良いし、`generated`に置いたまま記入してもOKです。その場合は、同じ年月の勤務表を生成して上書きしないよう気をつけてください。

#### VSCodeで開発する際必要な設定
- コード自動整形ツールは、「flake8」を用いる。下記サイトを参考に導入 \
  （「flake8のエラーチェックでpycodestyle(pep8)の1行文字数制限を外す」は行う）
https://qiita.com/psychoroid/items/2c2acc06c900d2c0c8cb
- VSCodeで拡張機能「Pylance」を入れて開発する際、`.vscode/settings.json`に`"python.analysis.extraPaths"`を加えればエラー`reportMissingImports`が消える。
```json
{
    "python.pythonPath": "your/path/to/python3.5",
    "python.analysis.extraPaths": [
        "app"
    ],
}
```
