import json
import spacy
from pathlib import Path
from spacy.language import Language

# カスタム辞書のパス
CUSTOM_DICTIONARY_JSON_PATH = Path("custom_synonym.json")

# JSON辞書を読み込む
def load_synonym_dict(json_path):
    with open(json_path, encoding="utf-8") as f:
        return json.load(f)

synonym_dict = load_synonym_dict(CUSTOM_DICTIONARY_JSON_PATH)

# GiNZAの初期化
nlp = spacy.load("ja_ginza")

@Language.component("merge_prefixed_tokens")
def merge_prefixed_tokens(doc):
    """
    接頭辞を動的に判定し、次のトークンと結合する関数。
    """
    with doc.retokenize() as retokenizer:
        for i, token in enumerate(doc[:-1]):
            # 動的に接頭辞を判定（1文字であり、次のトークンが名詞/形容詞の場合）
            if len(token.text) == 1 and doc[i + 1].pos_ in {"NOUN", "ADJ"}:
                span = doc[i:i + 2]
                retokenizer.merge(span)
    return doc

# カスタムコンポーネントをパイプラインに追加
nlp.add_pipe("merge_prefixed_tokens", last=True)

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
