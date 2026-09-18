# TS-TEST004






#あなたはWebアプリ開発者です。
Azure App Services で構築する Web API のソースコードセットを作成してください。

#条件
・使用する環境は FastAPI、Python、Pythonバージョンは3.13
・Dockerを使用し、dockerfile、requirements.txt、pyproject.tom、main.py を生成してください。
・サービスは「/」、「/help」を用意してください。 リターン値は json 形式でそれぞれ固有な値を返してください。



Quick setup — if you’ve done this kind of thing before
or	

https://github.com/Hororoku/FastAPI-004.git
Get started by creating a new file or uploading an existing file. We recommend every repository include a README, LICENSE, and .gitignore.

create a new repository on the command line
echo "# FastAPI-004" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Hororoku/FastAPI-004.git
git push -u origin main

push an existing repository from the command line
git remote add origin https://github.com/Hororoku/FastAPI-004.git
git branch -M main
git push -u origin main






GitHub Actions（CI/CD）
Azure App Service for Containers に自動デプロイする YAML**

以下は Azure Web App for Containers にデプロイする標準構成。
GitHub Secrets に以下を登録しておく必要がある：

| Secret 名                             | 内容                                                |
| ---                                   | ---                                                 |
| ``AZURE_WEBAPP_NAME``                 | App Service 名                                      |
| ``AZURE_WEBAPP_PUBLISH_PROFILE``      | App Service の Publish Profile XML                  |
| ``AZURE_CONTAINER_REGISTRY``          | ACR のログインサーバー名（例: myregistry.azurecr.io） |
| ``AZURE_CONTAINER_REGISTRY_USERNAME`` | ACR ユーザー名                                       |
| ``AZURE_CONTAINER_REGISTRY_PASSWORD`` | ACR パスワード                                       |










