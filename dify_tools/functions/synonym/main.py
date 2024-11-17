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
    result = []
    doc = nlp(prompt)  # GiNZAで形態素解析

    for token in doc:
        base_form = token.lemma_  # 原型を取得
        if base_form in synonym_dict:  # 辞書に存在すれば置き換え
            result.append(synonym_dict[base_form])
        else:
            result.append(token.text)  # 辞書にない場合はそのまま

    return "".join(result)  # 結果を結合して返す
