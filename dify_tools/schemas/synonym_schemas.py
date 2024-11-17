from pydantic import BaseModel


# リクエストボディのスキーマを定義
class SynonymRequest(BaseModel):
    prompt: str
