# work-schedule-gen
勤務表生成する仕組み

## 生成手順（初回）
1. Dockerをインストール．
https://docs.docker.com/get-docker/
2. Dockerアカウントを作成．
https://hub.docker.com/
3. zsh，コマンドプロンプトなどを立ち上げて下記を実行しログイン．
```
$ docker login
```
4. Dockerイメージを取得．
```
$ docker pull k1038/work-schedule-app:latest
```
5. コンテナを立ち上げる．
```
$ docker container run --name work-schedule-app -it -d k1038/work-schedule-app:latest
```
6. コンテナでbashを起動．
```
$ docker container exec -it work-schedule-app bash
```
7. bashで下記を実行し勤務表生成．
```bash
:/work-schedule-gen/app# python main.py
```
8. bashから抜ける．
```bash
:/work-schedule-gen/app# exit
```
9. コンテナから勤務表をコピー．（下記ではホームディレクトリにコピー．`~/`を変えることでコピー先のディレクトリを変えられる．）
```
$ docker container cp work-schedule-app:work-schedule-gen/app/generated/. ~/
```
10. コンテナを停止．
```
$ docker container stop work-schedule-app
```

## 生成手順（2回目以降）
1. コンテナを起動．
```
$ docker container start work-schedule-app
```
2. コンテナでbashを起動．
```
$ docker container exec -it work-schedule-app bash
```
3. bashで下記を実行し勤務表生成．
```bash
:/work-schedule-gen/app# python main.py
```
4. bashから抜ける．
```bash
:/work-schedule-gen/app# exit
```
5. コンテナから勤務表をコピー．（下記ではホームディレクトリ にコピー．`~/`を変えることでコピー先のディレクトリを変えられる．）
```
$ docker container cp work-schedule-app:work-schedule-gen/app/generated/. ~/
```
6. コンテナを停止．
```
$ docker container stop work-schedule-app
```
***

## 開発環境構築（macOS Catalina）
### 事前にインストールしておくもの
- Git
- Docker
- Visual Studio Code
- （必要に応じて）Homebrew \
（`pyenv`, `pyenv-virtualenv`は Homebrew を用いてインストールすることもできます．）

### 開発環境構築手順
1. zsh で下記を実行し，Pythonの実行環境を管理するツール「pyenv」を使えるようにする．\
（普段 bash を使っているなら bash をベースに下記手順を行っても大丈夫です．）
```zsh
$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv
```
2. 下記を`.zprofile`に書き込む．\
（`vi ~/.zprofile`などで書き込んでください．`.zprofile`がホームディレクトリになければ作成してください．）
```zsh
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
```
3. 下記を`.zshrc`に書き込む．
```
eval "$(pyenv init -)"
```
4. 仮想環境用の python 3.6.2 をインストール．（使用するライブラリの関係上 python 3.6.2 を用います．）
```zsh
$ pyenv install 3.6.2
```
#### インストール中に`Ignoring ensurepip failure: pip 7.1.2 requires SSL/TLS`というエラーが発生したら
下記を実行してください：
```zsh
$ brew uninstall --ignore-dependencies openssl@1.1
$ pyenv install 3.6.2
```
5. 下記を実行し，pyenv のプラグイン pyenv-virtualenv を使えるようにする．
```zsh
$ git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
```
6. 下記を`.zshrc`に書き込む．
```
eval "$(pyenv virtualenv-init -)"
```
7. 仮想環境の作成．
```zsh
$ pyenv virtualenv 3.6.2 venv_3.6.2
```
8. 下記を実行しwork-schedule-genレポジトリをクローンする．
```zsh
$ git clone https://github.com/kota-tozawa/work-schedule-gen.git
$ cd work-schedule-gen
```
9. 仮想環境をアクティベート（ディアクティベート：`$ pyenv deactivate venv_3.6.2`）．
```zsh
$ pyenv activate venv_3.6.2
```
10. バージョンが`3.6.2`に切り替わったか確認．
```zsh
$ python --version
```
11. 開発に必要なパッケージをインストール．
```zsh
$ pip install pipenv
$ pipenv install --dev
```
12. VSCodeで「フォルダを開く」でクローンしたディレクトリを開いた後，コマンドパレットを開き，そこに`>python`と入れ，「Python: Select Interpreter」を選択し，「Python 3.6.2 64-bit (venv_3.6.2)」を選択．

## メモ
### VSCodeの拡張機能・設定
- Python
https://marketplace.visualstudio.com/items?itemName=ms-python.python
- Pylance
https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance
- flake8 / autopep8 導入
https://qiita.com/psychoroid/items/2c2acc06c900d2c0c8cb

### Pythonコードのリント・フォーマット
```zsh
$ cd work-schedule-gen
$ chmod +x ./lint.sh
$ ./lint.sh
```

### UT/IT
```zsh
$ cd work-schedule-gen/app
$ python -m pytest
```
#### UT only
```zsh
$ python -m pytest -m "not integtest"
```
#### IT only
```zsh
$ python -m pytest -m integtest
```
#### レポート生成（テスト結果のレポートとカバリッジレポート）
1. `PYTHONPATH`を設定しないと，カバレッジレポート作成時に「no module named ~」エラーが出る．\
なので，このシェルスクリプトを実行する際には，事前に自分の環境に合うように下記`PYTHONPATH`を修正し，`.zshrc`や`.bashrc`などのファイルに追記．
```zsh
export PYTHONPATH="${PYTHONPATH}:/Your/path/to/work-schedule-gen/app/components"
```
2. 下記を実行．
```zsh
$ cd work-schedule-gen
$ chmod +x ./gen_test_reports.sh
$ ./gen_test_reports.sh
```
