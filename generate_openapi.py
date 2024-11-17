from pathlib import Path
from dify_tools.main import app  # FastAPIアプリをインポート
import yaml  # YAML形式で保存するためのライブラリ

def generate_openapi_yaml():
    """Generate OpenAPI YAML file."""
    # FastAPIのOpenAPIスキーマを取得
    openapi_schema = app.openapi()

    # 不要なスキーマを削除
    if "components" in openapi_schema and "schemas" in openapi_schema["components"]:
        openapi_schema["components"]["schemas"].pop("HTTPValidationError", None)
        openapi_schema["components"]["schemas"].pop("ValidationError", None)

    # 出力先のディレクトリとファイルパス
    output_dir = Path("dist")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "output.yml"

    # openapi_schemaをYAML形式に変換して書き込む
    with output_path.open("w", encoding="utf-8") as f:
        yaml.dump(openapi_schema, f, allow_unicode=True)

    print(f"OpenAPI schema saved to {output_path}")

if __name__ == "__main__":
    generate_openapi_yaml()
