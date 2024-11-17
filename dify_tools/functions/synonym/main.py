import json
import spacy
from pathlib import Path

# カスタム辞書のパス
CUSTOM_DICTIONARY_JSON_PATH = Path("custom_synonym.json")

# JSON辞書を読み込む
def load_synonym_dict(json_path):
    with open(json_path, encoding="utf-8") as f:
        return json.load(f)

synonym_dict = load_synonym_dict(CUSTOM_DICTIONARY_JSON_PATH)

# GiNZAの初期化
nlp = spacy.load("ja_ginza")

async def synonym(prompt: str) -> str:
    """
    GiNZAを用いて文章を形態素解析し、ヒットした単語をシノニムマップの単語と置き換える
    """
    # GiNZAで形態素解析
    doc = nlp(prompt)

    # トークンをシノニム辞書で置き換えつつ結合
    return "".join(
        synonym_dict.get(token.lemma_, token.text) for token in doc
    )
