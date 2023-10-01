# aws-cdk-client

AWS Contents Deployment KitをTypescriptで利用するためのdocker

## 事前準備

```
# dockerコンテナ立ち上げ
$ docker-compose up -d --build

# dockerログイン
$ docker exec -it aws-cdk-client bash
```

### バージョン確認

```
# check aws-cdk version
$ aws --version
aws-cli/1.21.12 Python/3.10.0 Linux/5.10.47-linuxkit botocore/1.22.12

# check aws-cdk version
$ cdk --version
1.130.0 (build 9c094ae)

# check typescript version
# tsc -v
Version 4.4.4
```

### AWSアカウントのMFA認証

MFA認証している場合、以下を実行する必要がある
※これをやらないと`cdk deploy`時にアカウントにアクセスできなくてエラーになる
※ローカルで下記処理を実行し、出力された認証情報をコンテナ側でexportする方法でもよし

```
# 認証情報取得
$ aws sts get-session-token --serial-number arn:aws:iam::xxxxxxxxxx:mfa/{IAM_USER_NAME} --token-code xxxxxx
{
    "Credentials": {
        "AccessKeyId": "xxxxxxxxxxxxxxxx",
        "SecretAccessKey": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
        "SessionToken": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "Expiration": "2021-11-07T15:20:34Z"
    }
}

# 認証情報を環境変数に設定
$ export AWS_ACCESS_KEY_ID=xxxxxxxxxxxxxxxx
$ export AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxx
$ export AWS_SESSION_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 開発言語をTypescriptに設定

```
# 開発言語をtypescriptに設定
$ cdk init app --language typescript
```

## コマンドサンプル

```
# CDK Appのスタック一覧確認
$ cdk ls

# typescriptファイルをcompile(通常toolkitが自動実行するので使用しない)
$ npm run build

# デプロイ
$ cdk deploy

# スタックを指定してデプロイ
$ cdk deploy ${StackName}

# CloudFormationのテンプレートファイル生成
$ cdk synth

# CloudFormationのテンプレートファイル生成してファイルに書き出す
$ cdk synth --output ./output

# 差分を確認
$ cdk diff

```