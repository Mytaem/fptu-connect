from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import network
from src.src_w2.net_stats_w2 import compute_stats
from src.src_w3.path_w3 import shortest_path
from src.src_w4.topk_w4 import topk_by_degree
import os
from PIL import Image
import uuid

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

os.makedirs("static/uploads", exist_ok=True)
os.makedirs("data", exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    stats = compute_stats(network.sn)
    return templates.TemplateResponse("index.html", {"request": request, "stats": stats})

@app.get("/student/{sid}", response_class=HTMLResponse)
async def student_profile(request: Request, sid: str):
    if sid not in network.sn.students:
        return RedirectResponse("/")
    student = network.sn.students[sid]
    return templates.TemplateResponse("profile.html", {
        "request": request,
        "student": student,
        "network": network
    })

@app.get("/add", response_class=HTMLResponse)
async def add_form(request: Request):
    return templates.TemplateResponse("add.html", {"request": request})

@app.post("/add")
async def add_student(
    name: str = Form(...),
    sid: str = Form(...),
    avatar: UploadFile = File(None)
):
    avatar_path = "static/default.jpg"
    if avatar and avatar.filename:
        ext = os.path.splitext(avatar.filename)[1].lower()
        if ext in [".jpg", ".jpeg", ".png"]:
            filename = f"{uuid.uuid4()}{ext}"
            avatar_path = f"static/uploads/{filename}"
            content = await avatar.read()
            with open(avatar_path, "wb") as f:
                f.write(content)
            try:
                img = Image.open(avatar_path).convert("RGB")
                img = img.resize((200, 200), Image.Resampling.LANCZOS)
                img.save(avatar_path, "JPEG", quality=85)
            except:
                pass

    network.sn.add_student(sid, name, avatar_path)
    network.generate_graph()
    return RedirectResponse(f"/student/{sid}", status_code=303)

@app.get("/path", response_class=HTMLResponse)
async def path_form(request: Request):
    return templates.TemplateResponse("path.html", {"request": request, "path": None})

@app.post("/path", response_class=HTMLResponse)
async def find_path(request: Request, start: str = Form(...), goal: str = Form(...)):
    path = shortest_path(network.sn, start, goal)
    return templates.TemplateResponse("path.html", {
        "request": request,
        "path": path,
        "network": network
    })

@app.get("/leaderboard", response_class=HTMLResponse)
async def leaderboard(request: Request):
    top_students = topk_by_degree(network.sn, 10)
    return templates.TemplateResponse("leaderboard.html", {
        "request": request,
        "top_students": top_students
    })