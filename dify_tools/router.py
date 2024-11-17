from fastapi import APIRouter
import dify_tools.functions as fnc
import dify_tools.schemas as schemas

router = APIRouter()


@router.post("/synonym")
async def dify_synonym(prompt: schemas.SynonymRequest):
    """
    Difyから受けとったプロンプトをシノニムマップを使って置き換えます。
    """
    return await fnc.synonym(prompt.prompt)
