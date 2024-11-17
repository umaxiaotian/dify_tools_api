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

