from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def get_items():
    with open("data/items.json") as f:
        return json.load(f)

@app.get("/")
def home(request: Request):
    items = get_items()
    return templates.TemplateResponse(request, "index.html", {"items": items})

@app.get("/item/{item_id}")
def item_detail(request: Request, item_id: int):
    items = get_items()
    item = next((i for i in items if i["id"] == item_id), None)
    return templates.TemplateResponse(request, "item.html", {"item": item})