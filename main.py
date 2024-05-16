from fastapi import FastAPI

from Word import Word
from db_sdk import DatabaseRepository
from dictionary_sdk import DictionaryClient

app = FastAPI()

dictionary_sdk = DictionaryClient()
db_sdk = DatabaseRepository()


@app.get("/words/get_random_word")
async def get_random_word(user_id: int):
    word: Word = db_sdk.get_random_word(user_id=user_id)
    word.extra_info = dictionary_sdk.get_definition(word.word_spell)
    return word


@app.get("/users/user_exists")
async def user_exists(user_id: int):
    return db_sdk.user_exists(user_id)


@app.get("/users/user_has_name")
async def user_has_name(user_id: int):
    return db_sdk.user_has_name(user_id)


@app.post("/users/create_user")
async def create_user(user_id: int, user_name: str):
    db_sdk.create_user(user_id=user_id, name=user_name)
    return "User created successfully"


@app.put("/users/update_name")
async def update_name(user_id: int, user_name: str):
    db_sdk.update_user_name(user_id=user_id, user_name=user_name)
    return "Name updated successfully"


@app.post("/suggestions/add_suggestion")
async def add_suggestion(word_id: str, user_id: int):
    db_sdk.add_suggestion(word_id=word_id, user_id=user_id)
    return {"message": "Suggestion added successfully"}


@app.put("/suggestions/update_suggestion")
async def update_suggestion(word_id: str, user_id: int, passed: int):
    db_sdk.update_suggestion(word_id=word_id, user_id=user_id, passed=passed)
    return {"message": "Suggestion updated successfully"}


@app.get("/statistics/get_total_words_passed_count")
async def get_total_words_passed_count(user_id: int):
    return db_sdk.get_total_words_passed_count(user_id=user_id)


@app.get("/statistics/get_total_words_count")
async def get_total_words_count():
    return db_sdk.get_total_words_count()
