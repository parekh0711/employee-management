from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .forms import form_router
from .users import user_router
from .generate import generate_router


app = FastAPI()
app.include_router(form_router)
app.include_router(generate_router)
app.include_router(user_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"msg": "API up"}
