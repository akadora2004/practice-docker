# practice-docker

セキュリティ・キャンプ2026全国大会の応募課題に取り組むにあたり、コンテナ技術（Docker）の基礎を理解するために作成した学習用リポジトリです。

## 概要
Flaskを用いたシンプルなWebアプリケーションをDockerコンテナ上で動作させる実験を行いました。

## 実施した手順
以下のコマンドを用いて、コンテナのライフサイクル（ビルド・実行・停止）を確認しました。

1. **イメージのビルド**
   ```bash
   docker image build -t practice-docker:latest .

2. **コンテナの実行**
   ```bash
   docker container run -d -p 8001:5000 --name sample-app practice-docker
   
3. **コンテナの停止**
   ```bash
   docker container stop sample-app