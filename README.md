# dify_tools

Dify用の拡張機能APIのサンプルです。このプロジェクトでは、日本語の自然言語処理を行うために `SudachiPy` や `GiNZA` を活用しています。

## プロジェクト情報

- **バージョン**: 0.1.0
- **作者**: Yuma Obata (<yuma@umaxiaotian.com>)
- **ライセンス**: MIT
- **Pythonバージョン**: 3.12以上

依存関係は `Poetry` で管理されています。

## セットアップ

### 1. リポジトリのクローン

```bash
git clone https://github.com/your-repo/dify_tools.git
cd dify_tools
poetry install
```

## 使い方
### 2. Difyで読み取れる形のopenapiを生成
```bash
poetry run generate-openapi
```

### 3. 生成物をdifyに貼り付ける
distというフォルダが作られその中に、openapiファイルが作成されますので、コピーしてそのまま貼り付けます。

![image](https://github.com/user-attachments/assets/da19d550-f134-4a72-bed2-a4e238abee67)

### 4. 認証設定
以下のように設定します。

![image](https://github.com/user-attachments/assets/29762608-85e9-4dee-94c0-94b49938fa3f)
