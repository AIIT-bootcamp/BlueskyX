# 事前準備

## .envファイルの作成

.env.sampleをコピーして.envファイルを作成する

# ローカルでの動作の手順

以下カレントディレクトリがbootcamp23summer-hackathon-1/hackathon_1の状態

1. poetryでパッケージのインストール
1. poetryで既存の設定を反映
1. poetry shell
1. この状態でpoetry run ファイル名 で動作確認可能

### poetryでパッケージのインストール

```
poetry add <package-name>
```

### poetryで既存の設定を反映

```
poetry update
``````

### poetryで仮想環境に入る

```
poetry shell
```

### poetryでファイル実行

```
poetry run python main.py 
```