# app.py - FPTU CONNECT 3.0
from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from PIL import Image
import network, os, uuid, shutil
from src.src_w2.net_stats_w2 import compute_stats
from src.src_w4.suggest_w4 import suggest_friends
from src.src_w3.path_w3 import shortest_path
from src.src_w4.topk_w4 import topk_by_degree

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Danh sách bài viết (tạm)
posts = []

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    stats = compute_stats(network.sn)
    return templates.TemplateResponse("index.html", {
        "request": request, "stats": stats, "network": network, "posts": posts[-3:]
    })

@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/student/{sid}", response_class=HTMLResponse)
async def student(request: Request, sid: str):
    if sid not in network.sn.students:
        return HTMLResponse("Không tìm thấy!", status_code=404)
    info = network.sn.students[sid]
    friends = list(network.sn.friends_of(sid))[:12]
    suggestions = suggest_friends(network.sn, sid, top_n=6)
    user_posts = [p for p in posts if p["user_id"] == sid]
    return templates.TemplateResponse("profile.html", {
        "request": request, "info": info, "friends": friends,
        "sid": sid, "suggestions": suggestions, "network": network,
        "posts": user_posts
    })

@app.get("/add", response_class=HTMLResponse)
async def add_profile_form(request: Request):
    return templates.TemplateResponse("add_profile.html", {"request": request})

@app.post("/add")
async def save_profile(
    request: Request,
    id: str = Form(...), name: str = Form(...), faculty: str = Form(...),
    hometown: str = Form(...), classes: str = Form(None), clubs: str = Form(None),
    avatar: UploadFile = File(None)
):
    classes = [c.strip() for c in (classes or "").split(",") if c.strip()]
    clubs = [c.strip() for c in (clubs or "").split(",") if c.strip()]
    
    avatar_path = "default.jpg"
    if avatar and avatar.filename:
        ext = avatar.filename.split(".")[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        path = os.path.join(UPLOAD_DIR, filename)
        with open(path, "wb") as f:
            shutil.copyfileobj(avatar.file, f)
        avatar_path = f"uploads/{filename}"
    
    user_data = {
        "id": id, "name": name, "faculty": faculty,
        "hometown": hometown, "classes": classes, "clubs": clubs,
        "avatar": avatar_path
    }
    network.sn.students[id] = user_data
    
    return templates.TemplateResponse("add_profile.html", {
        "request": request, "msg": f"Đã tạo hồ sơ {name}!"
    })

@app.post("/post")
async def create_post(
    request: Request,
    user_id: str = Form(...), content: str = Form(...),
    image: UploadFile = File(None)
):
    image_path = None
    if image and image.filename:
        ext = image.filename.split(".")[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        path = os.path.join(UPLOAD_DIR, filename)
        with open(path, "wb") as f:
            shutil.copyfileobj(image.file, f)
        image_path = f"uploads/{filename}"
    
    posts.append({
        "user_id": user_id,
        "content": content,
        "image": image_path,
        "name": network.sn.students[user_id]["name"]
    })
    return RedirectResponse(f"/student/{user_id}", status_code=303)

@app.get("/leaderboard", response_class=HTMLResponse)
async def leaderboard(request: Request):
    topk = topk_by_degree(network.sn, 20)
    return templates.TemplateResponse("leaderboard.html", {
        "request": request, "topk": topk, "network": network
    })

@app.get("/path", response_class=HTMLResponse)
async def path_form(request: Request):
    return templates.TemplateResponse("path.html", {"request": request})

@app.post("/path", response_class=HTMLResponse)
async def path_result(request: Request, start: str = Form(...), goal: str = Form(...)):
    path = shortest_path(network.sn, start, goal)
    return templates.TemplateResponse("path.html", {
        "request": request, "start": start, "goal": goal, "path": path
    })