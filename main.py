from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Any, List
import re

# ------------------ EDIT THESE ------------------
FULL_NAME_LOWER = "anshika_Srivastava"
DOB_DDMMYYYY     = "20092004"
EMAIL_ID         = "anshika.srivastava2022@vitstudent.ac.in"
ROLL_NUMBER      = "22BCT0072"
# ------------------------------------------------

app = FastAPI(title="BFHL API", version="1.0.0")

class Payload(BaseModel):
    data: List[Any] = Field(default_factory=list)

def is_integer_like(x: Any) -> bool:
    if isinstance(x, int):
        return True
    if isinstance(x, str) and re.fullmatch(r"[+-]?\d+", x.strip()):
        return True
    return False

def is_alpha_string(x: Any) -> bool:
    return isinstance(x, str) and re.fullmatch(r"[A-Za-z]+", x) is not None

def alt_caps_reverse_concat(alpha_tokens: List[str]) -> str:
    joined = "".join(alpha_tokens)
    rev = joined[::-1]
    out_chars = []
    for i, ch in enumerate(rev):
        out_chars.append(ch.upper() if i % 2 == 0 else ch.lower())
    return "".join(out_chars)

@app.get("/")
def root():
    return {"message": "Hello, FastAPI is working!"}

@app.post("/bfhl")
def bfhl(payload: Payload):
    data = payload.data or []

    even_numbers: List[str] = []
    odd_numbers: List[str] = []
    alphabets: List[str] = []
    special_characters: List[str] = []
    total = 0
    alpha_tokens_for_concat: List[str] = []

    for item in data:
        s = str(item)

        if is_integer_like(item):
            n = int(s)
            total += n
            if n % 2 == 0:
                even_numbers.append(s)
            else:
                odd_numbers.append(s)
        elif is_alpha_string(item):
            alphabets.append(s.upper())
            alpha_tokens_for_concat.append(s)
        else:
            special_characters.append(s)

    concat_string = alt_caps_reverse_concat(alpha_tokens_for_concat)

    return {
        "is_success": True,
        "user_id": f"{FULL_NAME_LOWER}_{DOB_DDMMYYYY}",
        "email": EMAIL_ID,
        "roll_number": ROLL_NUMBER,
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(total),
        "concat_string": concat_string
    }

@app.get("/bfhl")
def bfhl_get():
    return {"operation_code": 1}
