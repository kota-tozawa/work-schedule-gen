## Dockerコンテナ上で開発環境構築&勤務表生成
### 事前にインストールしておくもの
- Docker
### TODO 今は仮の自分用手順
- `docker build --tag k1038/work-schedule-gen:latest .`
- `docker container run --name work-schedule-app -it -d k1038/work-schedule-gen:latest`
- `docker ps`
- `docker container exec -it work-schedule-app bash`
- `python main.py`
- `exit`
- `docker container cp work-schedule-app:/app/generated/. ~/`

- `docker container stop work-schedule-app`
- `docker container start work-schedule-app`

- `docker rm work-schedule-app`
- `docker rmi -f k1038/work-schedule-gen`
