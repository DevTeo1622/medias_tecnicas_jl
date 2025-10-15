from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text
from sqlalchemy.orm import Session
from db import SessionDepends


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

#RUTAS PAGINA PRINCIPAL

@app.get("/", response_class=HTMLResponse)
async def raiz(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/index.html", response_class=HTMLResponse)
async def raiz(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/templates/Principal/login.html", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(request=request, name="Principal/login.html")

@app.get("/Principal/login.html", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(request=request, name="Principal/login.html")

@app.get("/templates/Principal/sobre_nosotros.html", response_class=HTMLResponse)
async def sobre_nosotros(request:Request):
    return templates.TemplateResponse(request=request, name="Principal/sobre_nosotros.html")

@app.get("/Principal/sobre_nosotros.html", response_class=HTMLResponse)
async def sobre_nosotros(request:Request):
    return templates.TemplateResponse(request=request, name="Principal/sobre_nosotros.html")

@app.get("/templates/Principal/proyectos.html", response_class=HTMLResponse)
async def proyectos(request:Request):
    return templates.TemplateResponse(request=request, name="Principal/proyectos.html")


@app.get("/templates/Software/Info_soft.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT descripcion FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 1}).fetchone()
    descripcion = resultado[0]
    return templates.TemplateResponse("Software/Info_soft.html", {"request": request, "descripcion": descripcion})

@app.get("/templates/Software/plan_estudio_soft.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT plan_estudio FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 1}).fetchone()
    plan_estudio = resultado[0]
    return templates.TemplateResponse("Software/plan_estudio_soft.html", {"request": request, "plan_estudio":plan_estudio})

@app.get("/templates/Software/perfil_estudiante_soft.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT perfil_estudiante FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 1}).fetchone()
    perfil_estudiante = resultado[0]
    return templates.TemplateResponse("Software/perfil_estudiante_soft.html", {"request": request, "perfil_estudiante":perfil_estudiante})

@app.get("/templates/Software/opts_laborales_soft.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT oportunidades_laborales FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 1}).fetchone()
    oportunidades_laborales = resultado[0]
    return templates.TemplateResponse("Software/opts_laborales_soft.html", {"request": request, "oportunidades_laborales":oportunidades_laborales})

@app.get("/templates/Software/reseñas_soft.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT reseñas FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 1}).fetchone()
    reseñas = resultado[0]
    return templates.TemplateResponse("Software/reseñas_soft.html", {"request": request, "reseñas":reseñas})

@app.get("/templates/Contenidos_digitales/info_contenidos.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT descripcion FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 2}).fetchone()
    descripcion = resultado[0]
    return templates.TemplateResponse("Contenidos_digitales/info_contenidos.html", {"request": request, "descripcion":descripcion})

@app.get("/templates/Contenidos_digitales/plan_estudio_contenidos.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT plan_estudio FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 2}).fetchone()
    plan_estudio = resultado[0]
    return templates.TemplateResponse("Contenidos_digitales/plan_estudio_contenidos.html", {"request": request, "plan_estudio":plan_estudio})



@app.post("/templates/Principal/login.html", response_class=HTMLResponse)
async def procesar_login(db : SessionDepends, request: Request, identificacion: str = Form(...), contraseña: str = Form(...)):
    consulta = text("SELECT * FROM usuario WHERE identificacion = :identificacion AND contraseña = :contraseña")
    resultado = db.execute(consulta, {"identificacion": identificacion, "contraseña": contraseña}).fetchone()

    if resultado:
        return templates.TemplateResponse("Software/inicio_usuario_software.html", {
            "request": request,
            "identificacion": identificacion,
            "contraseña": contraseña,
            "usuario": resultado,
            "nombre": resultado.nombre if hasattr(resultado, 'nombre') else resultado[3],
            "id": resultado.id if hasattr(resultado, 'id') else resultado[0],
            "rol": resultado.nombre
        }) 
    
    else:
        return templates.TemplateResponse("Principal/login.html", {"request":request}) 
    
@app.post("/Principal/login.html", response_class=HTMLResponse)
async def procesar_login(db : SessionDepends, request: Request, identificacion: str = Form(...), contraseña: str = Form(...)):
    consulta = text("SELECT * FROM usuario WHERE identificacion = :identificacion AND contraseña = :contraseña")
    resultado = db.execute(consulta, {"identificacion": identificacion, "contraseña": contraseña}).fetchone()

    if resultado:
        return templates.TemplateResponse("Software/inicio_usuario_software.html", {
            "request": request,
            "identificacion": identificacion,
            "contraseña": contraseña,
            "usuario": resultado,
            "nombre": resultado.nombre if hasattr(resultado, 'nombre') else resultado[3],
            "id": resultado.id if hasattr(resultado, 'id') else resultado[0],
            "rol": resultado.nombre
        }) 
    
    else:
        return templates.TemplateResponse("Principal/login.html", {"request":request}) 