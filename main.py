from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import text
from sqlalchemy.orm import Session
from db import SessionDepends
from starlette.middleware.sessions import SessionMiddleware
from collections import defaultdict


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(SessionMiddleware, secret_key="MATEO")

def get_db():
    db = SessionDepends()
    try:
        yield db
    finally:
        db.close()

#RUTAS PAGINA PRINCIPAL
#------------------------------------------------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def raiz(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/index.html", response_class=HTMLResponse)
async def raiz(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/templates/index.html", response_class=HTMLResponse)
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

@app.get("/Principal/proyectos.html", response_class=HTMLResponse)
async def proyectos(request:Request):
    return templates.TemplateResponse(request=request, name="Principal/proyectos.html")

#RUTAS INFORMACION MEDIA TECNICA SOFTWARE
#------------------------------------------------------------------------------------------------------------

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

#RUTAS INFORMACION MEDIA TECNICA CONTENIDOS DIGITALES
#------------------------------------------------------------------------------------------------------------

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

@app.get("/templates/Contenidos_digitales/perfil_estudiante_contenidos.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT perfil_estudiante FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 2}).fetchone()
    perfil_estudiante = resultado[0]
    return templates.TemplateResponse("Contenidos_digitales/perfil_estudiante_contenidos.html", {"request": request, "perfil_estudiante":perfil_estudiante})

@app.get("/templates/Contenidos_digitales/opts_laborales_contenidos.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT oportunidades_laborales FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 2}).fetchone()
    oportunidades_laborales = resultado[0]
    return templates.TemplateResponse("Contenidos_digitales/opts_laborales_contenidos.html", {"request": request, "oportunidades_laborales":oportunidades_laborales})

@app.get("/templates/Contenidos_digitales/reseñas_contenidos.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT reseñas FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 2}).fetchone()
    reseñas = resultado[0]
    return templates.TemplateResponse("Contenidos_digitales/reseñas_contenidos.html", {"request": request, "reseñas":reseñas})

#RUTAS INFORMACION MEDIA TECNICA VENTAS DE PRODUCTOS
#------------------------------------------------------------------------------------------------------------

@app.get("/templates/Ventas_productos/info_ventas.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT descripcion FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 3}).fetchone()
    descripcion = resultado[0]
    return templates.TemplateResponse("Ventas_productos/info_ventas.html", {"request": request, "descripcion":descripcion})

@app.get("/templates/Ventas_productos/plan_estudio_ventas.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT plan_estudio FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 3}).fetchone()
    plan_estudio = resultado[0]
    return templates.TemplateResponse("Ventas_productos/plan_estudio_ventas.html", {"request": request, "plan_estudio":plan_estudio})

@app.get("/templates/Ventas_productos/perfil_estudiante_ventas.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT perfil_estudiante FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 3}).fetchone()
    perfil_estudiante = resultado[0]
    return templates.TemplateResponse("Ventas_productos/perfil_estudiante_ventas.html", {"request": request, "perfil_estudiante":perfil_estudiante})

@app.get("/templates/Ventas_productos/opts_laborales_ventas.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT oportunidades_laborales FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 3}).fetchone()
    oportunidades_laborales = resultado[0]
    return templates.TemplateResponse("Ventas_productos/opts_laborales_ventas.html", {"request": request, "oportunidades_laborales":oportunidades_laborales})

@app.get("/templates/Ventas_productos/reseñas_ventas.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT reseñas FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 3}).fetchone()
    reseñas = resultado[0]
    return templates.TemplateResponse("Ventas_productos/reseñas_ventas.html", {"request": request, "reseñas":reseñas})

#RUTAS INFORMACION MEDIA TECNICA ASISTENCIA ADMINISTRATIVA
#------------------------------------------------------------------------------------------------------------

@app.get("/templates/Asistencia_administrativa/info_asis.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT descripcion FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 4}).fetchone()
    descripcion = resultado[0]
    return templates.TemplateResponse("Asistencia_administrativa/info_asis.html", {"request": request, "descripcion":descripcion})

@app.get("/templates/Asistencia_administrativa/plan_estudio_asis.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT plan_estudio FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 4}).fetchone()
    plan_estudio = resultado[0]
    return templates.TemplateResponse("Asistencia_administrativa/plan_estudio_asis.html", {"request": request, "plan_estudio":plan_estudio})

@app.get("/templates/Asistencia_administrativa/perfil_estudiante_asis.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT perfil_estudiante FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 4}).fetchone()
    perfil_estudiante = resultado[0]
    return templates.TemplateResponse("Asistencia_administrativa/perfil_estudiante_asis.html", {"request": request, "perfil_estudiante":perfil_estudiante})

@app.get("/templates/Asistencia_administrativa/opts_laborales_asis.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT oportunidades_laborales FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 4}).fetchone()
    oportunidades_laborales = resultado[0]
    return templates.TemplateResponse("Asistencia_administrativa/opts_laborales_asis.html", {"request": request, "oportunidades_laborales":oportunidades_laborales})

@app.get("/templates/Asistencia_administrativa/reseñas_asis.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT reseñas FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 4}).fetchone()
    reseñas = resultado[0]
    return templates.TemplateResponse("Asistencia_administrativa/reseñas_asis.html", {"request": request, "reseñas":reseñas})

#RUTAS INFORMACION MEDIA TECNICA MANTENIMIENTO DE MOTOS
#------------------------------------------------------------------------------------------------------------

@app.get("/templates/Mantenimiento_motos/info_mantenimiento.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT descripcion FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 5}).fetchone()
    descripcion = resultado[0]
    return templates.TemplateResponse("Mantenimiento_motos/info_mantenimiento.html", {"request": request, "descripcion":descripcion})

@app.get("/templates/Mantenimiento_motos/plan_estudio_mantenimiento.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT plan_estudio FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 5}).fetchone()
    plan_estudio = resultado[0]
    return templates.TemplateResponse("Mantenimiento_motos/plan_estudio_mantenimiento.html", {"request": request, "plan_estudio":plan_estudio})

@app.get("/templates/Mantenimiento_motos/perfil_estudiante_mantenimiento.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT perfil_estudiante FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 5}).fetchone()
    perfil_estudiante = resultado[0]
    return templates.TemplateResponse("Mantenimiento_motos/perfil_estudiante_mantenimiento.html", {"request": request, "perfil_estudiante":perfil_estudiante})

@app.get("/templates/Mantenimiento_motos/opts_laborales_mantenimiento.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT oportunidades_laborales FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 5}).fetchone()
    oportunidades_laborales = resultado[0]
    return templates.TemplateResponse("Mantenimiento_motos/opts_laborales_mantenimiento.html", {"request": request, "oportunidades_laborales":oportunidades_laborales})

@app.get("/templates/Mantenimiento_motos/reseñas_mantenimiento.html", response_class=HTMLResponse)
async def info_software(db: SessionDepends,request:Request):
    consulta = text("SELECT reseñas FROM medias_tecnicas WHERE id = :id")
    resultado = db.execute(consulta, {"id": 5}).fetchone()
    reseñas = resultado[0]
    return templates.TemplateResponse("Mantenimiento_motos/reseñas_mantenimiento.html", {"request": request, "reseñas":reseñas})

#RUTAS INICIO DE SESION
#------------------------------------------------------------------------------------------------------------

@app.post("/templates/Principal/login.html")
async def procesar_login(db : SessionDepends, request: Request, identificacion: str = Form(...), contraseña: str = Form(...)):
    consulta = text("SELECT * FROM usuario WHERE identificacion = :identificacion AND contraseña = :contraseña")
    resultado = db.execute(consulta, {"identificacion": identificacion, "contraseña": contraseña}).fetchone()
    rol = resultado.rol if hasattr(resultado, 'rol') else resultado[3]


    if resultado and rol == "estudiante":
        return templates.TemplateResponse("Principal/inicio_usuario.html", {
            "request": request,
            "identificacion": identificacion,
            "contraseña": contraseña,
            "usuario": resultado,
            "nombre": resultado.nombre if hasattr(resultado, 'nombre') else resultado[3],
            "id": resultado.id if hasattr(resultado, 'id') else resultado[0],
            "rol": resultado.nombre,
            "media_id": resultado.media_id
        }) 
    
    elif resultado and rol == "administrador":
        request.session["nombre_usuario"] = resultado.nombre if hasattr(resultado, "nombre") else resultado[3]
        return templates.TemplateResponse("Admin/inicio_admin.html", {
            "request": request,
            "identificacion": identificacion,
            "contraseña": contraseña,
            "usuario": resultado,
            "nombre_usuario": resultado.nombre if hasattr(resultado, 'nombre') else resultado[3],
            "nombre": resultado.nombre if hasattr(resultado, 'nombre') else resultado[3],
            "id": resultado.id if hasattr(resultado, 'id') else resultado[0],
            "rol": resultado.nombre,
            "media_id": resultado.media_id
        }) 
    
    else:
        return templates.TemplateResponse("Principal/login.html", {"request":request}) 
    
@app.post("/Principal/login.html", response_class=HTMLResponse)
async def procesar_login(db : SessionDepends, request: Request, identificacion: str = Form(...), contraseña: str = Form(...)):
    consulta = text("SELECT * FROM usuario WHERE identificacion = :identificacion AND contraseña = :contraseña")
    resultado = db.execute(consulta, {"identificacion": identificacion, "contraseña": contraseña}).fetchone()
    rol = resultado.rol if hasattr(resultado, 'rol') else resultado[3]


    if resultado and rol == "estudiante":
        return templates.TemplateResponse("Principal/inicio_usuario.html", {
            "request": request,
            "identificacion": identificacion,
            "contraseña": contraseña,
            "usuario": resultado,
            "nombre": resultado.nombre if hasattr(resultado, 'nombre') else resultado[3],
            "id": resultado.id if hasattr(resultado, 'id') else resultado[0],
            "rol": resultado.nombre,
            "media_id": resultado.media_id
        }) 
    
    elif resultado and rol == "administrador":
        return templates.TemplateResponse("Admin/inicio_admin.html", {
            "request": request,
            "identificacion": identificacion,
            "contraseña": contraseña,
            "usuario": resultado,
            "nombre_usuario": resultado.nombre if hasattr(resultado, 'nombre') else resultado[3],
            "nombre": resultado.nombre if hasattr(resultado, 'nombre') else resultado[3],
            "id": resultado.id if hasattr(resultado, 'id') else resultado[0],
            "rol": resultado.nombre,
            "media_id": resultado.media_id
        }) 
    
    else:
        return templates.TemplateResponse("Principal/login.html", {"request":request}) 
    
@app.get("/templates/Principal/Principal/login.html", response_class=HTMLResponse)
async def salir(db: SessionDepends, request: Request):
    return templates.TemplateResponse("index.html", {"request":request})
    
#RUTAS MATERIAL DE AYUDA SOFTWARE
#------------------------------------------------------------------------------------------------------------

@app.post("/material", response_class=HTMLResponse)
async def redirigir_material(db: SessionDepends, request: Request, media: str = Form(...)):
    media_int = int(media)  

    if media_int == 1:
        return templates.TemplateResponse("Software/material_soft.html", {"request": request})
    elif media_int == 2:
        return templates.TemplateResponse("Contenidos_digitales/material_contenidos.html", {"request": request})
    elif media_int == 3:
        return templates.TemplateResponse("Ventas_productos/material_ventas.html", {"request": request})
    elif media_int == 4:
        return templates.TemplateResponse("Asistencia_administrativa/material_asis.html", {"request": request})
    elif media_int == 5:
        return templates.TemplateResponse("Mantenimiento_motos/material_mantenimiento.html", {"request": request})
    else:
        return templates.TemplateResponse("error.html", {"request": request})
    
@app.get("/templates/Software/material_soft.html", response_class=HTMLResponse)
async def material_software(db: SessionDepends, request: Request):
    return templates.TemplateResponse("Software/material_soft.html", {"request": request})

@app.get("/ejercicios_soft.html", response_class=HTMLResponse)
async def ejercicios_software(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, descripcion, dificultad FROM ejercicios WHERE media_id = 1")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    descripciones = [fila[1] for fila in filas]
    dificultades = [fila[2] for fila in filas]

    return templates.TemplateResponse("Software/ejercicios_soft.html", {"request": request, "ejercicio_nombre":nombres, "ejercicio_descripcion":descripciones, "ejercicio_dificultad":dificultades })

@app.get("/templates/Software/ejercicios_soft.html", response_class=HTMLResponse)
async def ejercicios_software(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, descripcion, dificultad FROM ejercicios WHERE media_id = 1")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    descripciones = [fila[1] for fila in filas]
    dificultades = [fila[2] for fila in filas]

    return templates.TemplateResponse("Software/ejercicios_soft.html", {"request": request, "ejercicio_nombre":nombres, "ejercicio_descripcion":descripciones, "ejercicio_dificultad":dificultades })

@app.get("/enlaces_soft.html", response_class=HTMLResponse)
async def enlaces_software(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, enlace FROM enlaces WHERE media_id = 1")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    enlaces = [fila[1] for fila in filas]

    return templates.TemplateResponse("Software/enlaces_soft.html", {"request": request, "enlace_nombre":nombres, "enlace":enlaces})

@app.get("/templates/Software/enlaces_soft.html", response_class=HTMLResponse)
async def enlaces_software(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, enlace FROM enlaces WHERE media_id = 1")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    enlaces = [fila[1] for fila in filas]

    return templates.TemplateResponse("Software/enlaces_soft.html", {"request": request, "enlace_nombre":nombres, "enlace":enlaces})

@app.get("/templates/Software/docs_soft.html", response_class=HTMLResponse)
async def documentos_software(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, documento FROM documentos WHERE media_id = 1")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    documentos = [fila[1] for fila in filas]
    return templates.TemplateResponse("Software/docs_soft.html", {"request": request, "doc_nombre":nombres, "doc_enlace":documentos})

@app.get("/docs_soft.html", response_class=HTMLResponse)
async def documentos_software(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, documento FROM documentos WHERE media_id = 1")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    documentos = [fila[1] for fila in filas]
    return templates.TemplateResponse("Software/docs_soft.html", {"request": request, "doc_nombre":nombres, "doc_enlace":documentos})

@app.get("/templates/Software/grabaciones_soft.html", response_class=HTMLResponse)
async def videos_software(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, video FROM videos WHERE media_id = 1")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    videos = [fila[1] for fila in filas]

    return templates.TemplateResponse("Software/grabaciones_soft.html", {"request": request, "nombre_video":nombres, "video_id":videos})

@app.get("/grabaciones_soft.html", response_class=HTMLResponse)
async def videos_software(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, video FROM videos WHERE media_id = 1")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    videos = [fila[1] for fila in filas]

    return templates.TemplateResponse("Software/grabaciones_soft.html", {"request": request, "nombre_video":nombres, "video_id":videos})

#MATERIAL DE AYUDA CONTENIDOS DIGITALES
#-----------------------------------------------------------------------------------------------------------------------------------------------------

@app.get("/templates/Contenidos_digitales/material_contenidos.html", response_class=HTMLResponse)
async def material_contenidos(db: SessionDepends, request: Request):
    return templates.TemplateResponse("Contenidos_digitales/material_contenidos.html", {"request": request})

@app.get("/templates/Contenidos_digitales/material_contenidos.html", response_class=HTMLResponse)
async def material_contenidos(db: SessionDepends, request: Request):
    return templates.TemplateResponse("Contenidos_digitales/material_contenidos.html", {"request": request})

@app.get("/ejercicios_contenidos.html", response_class=HTMLResponse)
async def ejercicios_contenidos(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, descripcion, dificultad FROM ejercicios WHERE media_id = 2")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    descripciones = [fila[1] for fila in filas]
    dificultades = [fila[2] for fila in filas]

    return templates.TemplateResponse("Contenidos_digitales/ejercicios_contenidos.html", {"request": request, "ejercicio_nombre":nombres, "ejercicio_descripcion":descripciones, "ejercicio_dificultad":dificultades })

@app.get("/templates/Contenidos_digitales/ejercicios_contenidos.html", response_class=HTMLResponse)
async def ejercicios_contenidos(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, descripcion, dificultad FROM ejercicios WHERE media_id = 2")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    descripciones = [fila[1] for fila in filas]
    dificultades = [fila[2] for fila in filas]

    return templates.TemplateResponse("Contenidos_digitales/ejercicios_contenidos.html", {"request": request, "ejercicio_nombre":nombres, "ejercicio_descripcion":descripciones, "ejercicio_dificultad":dificultades })

@app.get("/enlaces_contenidos.html", response_class=HTMLResponse)
async def enlaces_contenidos(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, enlace FROM enlaces WHERE media_id = 2")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    enlaces = [fila[1] for fila in filas]

    return templates.TemplateResponse("Contenidos_digitales/enlaces_contenidos.html", {"request": request, "enlace_nombre":nombres, "enlace":enlaces})

@app.get("/templates/Contenidos_digitales/enlaces_contenidos.html", response_class=HTMLResponse)
async def enlaces_contenidos(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, enlace FROM enlaces WHERE media_id = 2")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    enlaces = [fila[1] for fila in filas]

    return templates.TemplateResponse("Contenidos_digitales/enlaces_contenidos.html", {"request": request, "enlace_nombre":nombres, "enlace":enlaces})

@app.get("/templates/Contenidos_digitales/docs_contenidos.html", response_class=HTMLResponse)
async def documentos_contenidos(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, documento FROM documentos WHERE media_id = 2")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    documentos = [fila[1] for fila in filas]
    return templates.TemplateResponse("Contenidos_digitales/docs_contenidos.html", {"request": request, "doc_nombre":nombres, "doc_enlace":documentos})

@app.get("/docs_contenidos.html", response_class=HTMLResponse)
async def documentos_contenidos(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, documento FROM documentos WHERE media_id = 2")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    documentos = [fila[1] for fila in filas]
    return templates.TemplateResponse("Contenidos_digitales/docs_contenidos.html", {"request": request, "doc_nombre":nombres, "doc_enlace":documentos})

@app.get("/templates/Contenidos_digitales/grabaciones_contenidos.html", response_class=HTMLResponse)
async def videos_contenidos(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, video FROM videos WHERE media_id = 2")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    videos = [fila[1] for fila in filas]

    return templates.TemplateResponse("Contenidos_digitales/grabaciones_contenidos.html", {"request": request, "nombre_video":nombres, "video_id":videos})

@app.get("/grabaciones_contenidos.html", response_class=HTMLResponse)
async def videos_contenidos(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, video FROM videos WHERE media_id = 2")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    videos = [fila[1] for fila in filas]

    return templates.TemplateResponse("Contenidos_digitales/grabaciones_contenidos.html", {"request": request, "nombre_video":nombres, "video_id":videos})

#MATERIAL DE AYUDA VENTAS DE PRODUCTOS
#-----------------------------------------------------------------------------------------------------------------------------------------------------

@app.get("/templates/Ventas_productos/material_ventas.html", response_class=HTMLResponse)
async def material_ventas(db: SessionDepends, request: Request):
    return templates.TemplateResponse("Ventas_productos/material_ventas.html", {"request": request})

@app.get("/templates/Ventas_productos/material_ventas.html", response_class=HTMLResponse)
async def material_ventas(db: SessionDepends, request: Request):
    return templates.TemplateResponse("Ventas_productos/material_ventas.html", {"request": request})

@app.get("/ejercicios_ventas.html", response_class=HTMLResponse)
async def ejercicios_ventas(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, descripcion, dificultad FROM ejercicios WHERE media_id = 3")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    descripciones = [fila[1] for fila in filas]
    dificultades = [fila[2] for fila in filas]

    return templates.TemplateResponse("Ventas_productos/ejercicios_ventas.html", {"request": request, "ejercicio_nombre":nombres, "ejercicio_descripcion":descripciones, "ejercicio_dificultad":dificultades })

@app.get("/templates/Ventas_productos/ejercicios_ventas.html", response_class=HTMLResponse)
async def ejercicios_ventas(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, descripcion, dificultad FROM ejercicios WHERE media_id = 3")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    descripciones = [fila[1] for fila in filas]
    dificultades = [fila[2] for fila in filas]

    return templates.TemplateResponse("Ventas_productos/ejercicios_ventas.html", {"request": request, "ejercicio_nombre":nombres, "ejercicio_descripcion":descripciones, "ejercicio_dificultad":dificultades })

@app.get("/enlaces_ventas.html", response_class=HTMLResponse)
async def enlaces_ventas(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, enlace FROM enlaces WHERE media_id = 3")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    enlaces = [fila[1] for fila in filas]

    return templates.TemplateResponse("Ventas_productos/enlaces_ventas.html", {"request": request, "enlace_nombre":nombres, "enlace":enlaces})

@app.get("/templates/Ventas_productos/enlaces_ventas.html", response_class=HTMLResponse)
async def enlaces_ventas(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, enlace FROM enlaces WHERE media_id = 3")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    enlaces = [fila[1] for fila in filas]

    return templates.TemplateResponse("Ventas_productos/enlaces_ventas.html", {"request": request, "enlace_nombre":nombres, "enlace":enlaces})

@app.get("/templates/Ventas_productos/docs_ventas.html", response_class=HTMLResponse)
async def documentos_ventas(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, documento FROM documentos WHERE media_id = 3")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    documentos = [fila[1] for fila in filas]
    return templates.TemplateResponse("Ventas_productos/docs_ventas.html", {"request": request, "doc_nombre":nombres, "doc_enlace":documentos})

@app.get("/docs_ventas.html", response_class=HTMLResponse)
async def documentos_ventas(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, documento FROM documentos WHERE media_id = 3")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    documentos = [fila[1] for fila in filas]
    return templates.TemplateResponse("Ventas_productos/docs_ventas.html", {"request": request, "doc_nombre":nombres, "doc_enlace":documentos})

@app.get("/templates/Ventas_productos/grabaciones_ventas.html", response_class=HTMLResponse)
async def videos_ventas(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, video FROM videos WHERE media_id = 3")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    videos = [fila[1] for fila in filas]

    return templates.TemplateResponse("Ventas_productos/grabaciones_ventas.html", {"request": request, "nombre_video":nombres, "video_id":videos})

@app.get("/grabaciones_ventas.html", response_class=HTMLResponse)
async def videos_ventas(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, video FROM videos WHERE media_id = 3")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    videos = [fila[1] for fila in filas]

    return templates.TemplateResponse("Ventas_productos/grabaciones_ventas.html", {"request": request, "nombre_video":nombres, "video_id":videos})

#MATERIAL DE AYUDA ASISTENCIA ADMINISTRATIVA
#-----------------------------------------------------------------------------------------------------------------------------------------------------

@app.get("/templates/Asistencia_administrativa/material_asis.html", response_class=HTMLResponse)
async def material_asistencia(db: SessionDepends, request: Request):
    return templates.TemplateResponse("Asistencia_administrativa/material_asis.html", {"request": request})

@app.get("/templates/Asistencia_administrativa/material_asis.html", response_class=HTMLResponse)
async def material_asistencia(db: SessionDepends, request: Request):
    return templates.TemplateResponse("Asistencia_administrativa/material_asis.html", {"request": request})

@app.get("/ejercicios_asis.html", response_class=HTMLResponse)
async def ejercicios_asistencia(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, descripcion, dificultad FROM ejercicios WHERE media_id = 4")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    descripciones = [fila[1] for fila in filas]
    dificultades = [fila[2] for fila in filas]

    return templates.TemplateResponse("Asistencia_administrativa/ejercicios_asis.html", {"request": request, "ejercicio_nombre":nombres, "ejercicio_descripcion":descripciones, "ejercicio_dificultad":dificultades })

@app.get("/templates/Asistencia_administrativa/ejercicios_asis.html", response_class=HTMLResponse)
async def ejercicios_asistencia(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, descripcion, dificultad FROM ejercicios WHERE media_id = 4")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    descripciones = [fila[1] for fila in filas]
    dificultades = [fila[2] for fila in filas]

    return templates.TemplateResponse("Asistencia_administrativa/ejercicios_asis.html", {"request": request, "ejercicio_nombre":nombres, "ejercicio_descripcion":descripciones, "ejercicio_dificultad":dificultades })

@app.get("/enlaces_asis.html", response_class=HTMLResponse)
async def enlaces_asistencia(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, enlace FROM enlaces WHERE media_id = 4")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    enlaces = [fila[1] for fila in filas]

    return templates.TemplateResponse("Asistencia_administrativa/enlaces_asis.html", {"request": request, "enlace_nombre":nombres, "enlace":enlaces})

@app.get("/templates/Asistencia_administrativa/enlaces_asis.html", response_class=HTMLResponse)
async def enlaces_asistencia(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, enlace FROM enlaces WHERE media_id = 4")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    enlaces = [fila[1] for fila in filas]

    return templates.TemplateResponse("Asistencia_administrativa/enlaces_asis.html", {"request": request, "enlace_nombre":nombres, "enlace":enlaces})

@app.get("/templates/Asistencia_administrativa/docs_asis.html", response_class=HTMLResponse)
async def documentos_asistencia(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, documento FROM documentos WHERE media_id = 4")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    documentos = [fila[1] for fila in filas]
    return templates.TemplateResponse("Asistencia_administrativa/docs_asis.html", {"request": request, "doc_nombre":nombres, "doc_enlace":documentos})

@app.get("/docs_asis.html", response_class=HTMLResponse)
async def documentos_asistencia(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, documento FROM documentos WHERE media_id = 4")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    documentos = [fila[1] for fila in filas]
    return templates.TemplateResponse("Asistencia_administrativa/docs_asis.html", {"request": request, "doc_nombre":nombres, "doc_enlace":documentos})

@app.get("/templates/Asistencia_administrativa/grabaciones_asis.html", response_class=HTMLResponse)
async def videos_asistencia(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, video FROM videos WHERE media_id = 4")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    videos = [fila[1] for fila in filas]

    return templates.TemplateResponse("Asistencia_administrativa/grabaciones_asis.html", {"request": request, "nombre_video":nombres, "video_id":videos})

@app.get("/grabaciones_asis.html", response_class=HTMLResponse)
async def videos_asistencia(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, video FROM videos WHERE media_id = 4")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    videos = [fila[1] for fila in filas]

    return templates.TemplateResponse("Asistencia_administrativa/grabaciones_asis.html", {"request": request, "nombre_video":nombres, "video_id":videos})

#MATERIAL DE AYUDA MANTENIMIENTO DE MOTOS
#-----------------------------------------------------------------------------------------------------------------------------------------------------

@app.get("/templates/Mantenimiento_motos/material_mantenimiento.html", response_class=HTMLResponse)
async def material_mantenimiento(db: SessionDepends, request: Request):
    return templates.TemplateResponse("Mantenimiento_motos/material_mantenimiento.html", {"request": request})

@app.get("/templates/Mantenimiento_motos/material_mantenimiento.html", response_class=HTMLResponse)
async def material_mantenimiento(db: SessionDepends, request: Request):
    return templates.TemplateResponse("Mantenimiento_motos/material_mantenimiento.html", {"request": request})

@app.get("/ejercicios_mantenimiento.html", response_class=HTMLResponse)
async def ejercicios_mantenimiento(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, descripcion, dificultad FROM ejercicios WHERE media_id = 5")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    descripciones = [fila[1] for fila in filas]
    dificultades = [fila[2] for fila in filas]

    return templates.TemplateResponse("Mantenimiento_motos/ejercicios_mantenimiento.html", {"request": request, "ejercicio_nombre":nombres, "ejercicio_descripcion":descripciones, "ejercicio_dificultad":dificultades })

@app.get("/templates/Mantenimiento_motos/ejercicios_mantenimiento.html", response_class=HTMLResponse)
async def ejercicios_mantenimiento(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, descripcion, dificultad FROM ejercicios WHERE media_id = 5")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    descripciones = [fila[1] for fila in filas]
    dificultades = [fila[2] for fila in filas]

    return templates.TemplateResponse("Mantenimiento_motos/ejercicios_mantenimiento.html", {"request": request, "ejercicio_nombre":nombres, "ejercicio_descripcion":descripciones, "ejercicio_dificultad":dificultades })

@app.get("/enlaces_mantenimiento.html", response_class=HTMLResponse)
async def enlaces_mantenimiento(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, enlace FROM enlaces WHERE media_id = 5")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    enlaces = [fila[1] for fila in filas]

    return templates.TemplateResponse("Mantenimiento_motos/enlaces_mantenimiento.html", {"request": request, "enlace_nombre":nombres, "enlace":enlaces})

@app.get("/templates/Mantenimiento_motos/enlaces_mantenimiento.html", response_class=HTMLResponse)
async def enlaces_mantenimiento(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, enlace FROM enlaces WHERE media_id = 5")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    enlaces = [fila[1] for fila in filas]

    return templates.TemplateResponse("Mantenimiento_motos/enlaces_mantenimiento.html", {"request": request, "enlace_nombre":nombres, "enlace":enlaces})

@app.get("/templates/Mantenimiento_motos/docs_mantenimiento.html", response_class=HTMLResponse)
async def documentos_mantenimiento(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, documento FROM documentos WHERE media_id = 5")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    documentos = [fila[1] for fila in filas]
    return templates.TemplateResponse("Mantenimiento_motos/docs_mantenimiento.html", {"request": request, "doc_nombre":nombres, "doc_enlace":documentos})

@app.get("/docs_mantenimiento.html", response_class=HTMLResponse)
async def documentos_mantenimiento(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, documento FROM documentos WHERE media_id = 5")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    documentos = [fila[1] for fila in filas]
    return templates.TemplateResponse("Mantenimiento_motos/docs_mantenimiento.html", {"request": request, "doc_nombre":nombres, "doc_enlace":documentos})

@app.get("/templates/Mantenimiento_motos/grabaciones_mantenimiento.html", response_class=HTMLResponse)
async def videos_mantenimiento(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, video FROM videos WHERE media_id = 5")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    videos = [fila[1] for fila in filas]

    return templates.TemplateResponse("Mantenimiento_motos/grabaciones_mantenimiento.html", {"request": request, "nombre_video":nombres, "video_id":videos})

@app.get("/grabaciones_mantenimiento.html", response_class=HTMLResponse)
async def videos_mantenimiento(db: SessionDepends, request: Request):
    consulta = text("SELECT nombre, video FROM videos WHERE media_id = 5")
    resultado = db.execute(consulta)
    filas = resultado.fetchall()
    nombres = [fila[0] for fila in filas]
    videos = [fila[1] for fila in filas]

    return templates.TemplateResponse("Mantenimiento_motos/grabaciones_mantenimiento.html", {"request": request, "nombre_video":nombres, "video_id":videos})

#RUTAS ADMINISTRADOR
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.get("/panel_admin.html", response_class=HTMLResponse)
async def panel_admin(db:SessionDepends, request: Request):
    nombre_usuario = request.session.get("nombre_usuario", "Invitado")    
    consulta = text("""
        SELECT 
            usuario.nombre,
            usuario.identificacion,
            medias_tecnicas.nombre,
            usuario.grado
        FROM usuario
        JOIN medias_tecnicas ON usuario.media_id = medias_tecnicas.id
    """)
    resultado = db.execute(consulta).fetchall()
    usuarios = [
        {
            "nombre": fila[0],
            "identificacion": fila[1],
            "media_tecnica": fila[2],
            "grado": fila[3]
        }
        for fila in resultado
    ]

    medias_tecnicas = ["Desarrollo de software", "Contenidos digitales", "Ventas de productos en linea", "Asistencia administrativa", "Mantenimiento de motos"]

    return templates.TemplateResponse("Admin/panel_admin.html", {
        "nombre_usuario":nombre_usuario,
        "request": request,
        "usuarios": usuarios,
        "medias_tecnicas": medias_tecnicas
    })

@app.get("/Admin/inicio_admin.html", response_class=HTMLResponse)
async def inicio_admin(db:SessionDepends, request: Request):
    nombre_usuario = request.session.get("nombre_usuario", "Invitado")    
    return templates.TemplateResponse("Admin/inicio_admin.html", {"request":request, "nombre_usuario":nombre_usuario})

@app.get("/Admin/panel_admin.html", response_class=HTMLResponse)
async def panel_admin(db:SessionDepends, request: Request):
    nombre_usuario = request.session.get("nombre_usuario", "Invitado")    
    consulta = text("""
        SELECT 
            usuario.nombre,
            usuario.identificacion,
            medias_tecnicas.nombre,
            usuario.grado
        FROM usuario
        JOIN medias_tecnicas ON usuario.media_id = medias_tecnicas.id
    """)
    resultado = db.execute(consulta).fetchall()
    usuarios = [
        {
            "nombre": fila[0],
            "identificacion": fila[1],
            "media_tecnica": fila[2],
            "grado": fila[3]
        }
        for fila in resultado
    ]

    medias_tecnicas = ["Desarrollo de software", "Contenidos digitales", "Ventas de productos en linea", "Asistencia administrativa", "Mantenimiento de motos"]

    return templates.TemplateResponse("Admin/panel_admin.html", {
        "nombre_usuario":nombre_usuario,
        "request": request,
        "usuarios": usuarios,
        "medias_tecnicas": medias_tecnicas
    })

@app.get("/templates/Admin/inicio_admin.html", response_class=HTMLResponse)
async def inicio_admin(db:SessionDepends, request: Request):
    nombre_usuario = request.session.get("nombre_usuario", None)
    return templates.TemplateResponse("Admin/inicio_admin.html", {"request":request, "nombre_usuario":nombre_usuario})

@app.get("/templates/Principal/inicio_admin.html", response_class=HTMLResponse)
async def inicio_admin(db:SessionDepends, request: Request):
    nombre_usuario = request.session.get("nombre_usuario", None)
    return templates.TemplateResponse("Admin/inicio_admin.html", {"request":request, "nombre_usuario":nombre_usuario})

@app.get("/templates/Admin/panel_admin.html", response_class=HTMLResponse)
async def panel_admin(db:SessionDepends, request: Request):
    nombre_usuario = request.session.get("nombre_usuario", "Invitado")    
    consulta = text("""
        SELECT 
            usuario.nombre,
            usuario.identificacion,
            medias_tecnicas.nombre,
            usuario.grado
        FROM usuario
        JOIN medias_tecnicas ON usuario.media_id = medias_tecnicas.id
    """)
    resultado = db.execute(consulta).fetchall()
    usuarios = [
        {
            "nombre": fila[0],
            "identificacion": fila[1],
            "media_tecnica": fila[2],
            "grado": fila[3]
        }
        for fila in resultado
    ]

    medias_tecnicas = ["Desarrollo de software", "Contenidos digitales", "Ventas de productos en linea", "Asistencia administrativa", "Mantenimiento de motos"]

    return templates.TemplateResponse("Admin/panel_admin.html", {
        "nombre_usuario":nombre_usuario,
        "request": request,
        "usuarios": usuarios,
        "medias_tecnicas": medias_tecnicas
    })

@app.get("/templates/Principal/panel_admin.html", response_class=HTMLResponse)
async def panel_admin(db:SessionDepends, request: Request):
    nombre_usuario = request.session.get("nombre_usuario", "Invitado")    
    consulta = text("""
        SELECT 
            usuario.nombre,
            usuario.identificacion,
            medias_tecnicas.nombre,
            usuario.grado
        FROM usuario
        JOIN medias_tecnicas ON usuario.media_id = medias_tecnicas.id
    """)
    resultado = db.execute(consulta).fetchall()
    usuarios = [
        {
            "nombre": fila[0],
            "identificacion": fila[1],
            "media_tecnica": fila[2],
            "grado": fila[3]
        }
        for fila in resultado
    ]

    medias_tecnicas = ["Desarrollo de software", "Contenidos digitales", "Ventas de productos en linea", "Asistencia administrativa", "Mantenimiento de motos"]

    return templates.TemplateResponse("Admin/panel_admin.html", {
        "nombre_usuario":nombre_usuario,
        "request": request,
        "usuarios": usuarios,
        "medias_tecnicas": medias_tecnicas
    })

@app.get("/templates/Admin/agregar_usuario.html", response_class=HTMLResponse)
async def mostrar_formulario(request: Request, db: SessionDepends):
    consulta = text("SELECT id, nombre FROM medias_tecnicas")
    resultado = db.execute(consulta).fetchall()
    medias_tecnicas = [{"id": fila[0], "nombre": fila[1]} for fila in resultado]

    return templates.TemplateResponse("Admin/agregar_usuario.html", {
        "request": request,
        "medias_tecnicas": medias_tecnicas
    })

@app.post("/templates/Admin/agregar_usuario.html", response_class=HTMLResponse)
async def procesar_formulario(
    request: Request,
    db: SessionDepends,
    nombre: str = Form(...),
    identificacion: str = Form(...),
    contraseña: str = Form(...),
    rol: str = Form(...),
    media_id: int = Form(...),
    grado: int = Form(...)
):
    nombre_usuario = request.session.get("nombre_usuario", "Invitado")    
    consulta = text("""
        INSERT INTO usuario (nombre, identificacion, contraseña, rol, media_id, grado)
        VALUES (:nombre, :identificacion, :contraseña, :rol, :media_id, :grado)
    """)
    db.execute(consulta, {
        "nombre": nombre,
        "identificacion": identificacion,
        "contraseña": contraseña,
        "rol": rol,
        "media_id": media_id,
        "grado": grado
    })
    db.commit()
    return templates.TemplateResponse("Admin/inicio_admin.html", {"request":request, "nombre_usuario":nombre_usuario} ,status_code=303)

@app.get("/templates/Admin/editar_admin.html", response_class=HTMLResponse)
async def mostrar_edicion_admin(request: Request, db: SessionDepends):
    nombre_usuario = request.session.get("nombre_usuario", None)
    if not nombre_usuario:
        return templates.TemplateResponse("/login", {"request":request} ,status_code=303)

    consulta = text("""
        SELECT id, nombre, identificacion, contraseña
        FROM usuario
        WHERE nombre = :nombre AND rol = 'administrador'
    """)
    resultado = db.execute(consulta, {"nombre": nombre_usuario}).fetchone()

    if not resultado:
        return templates.TemplateResponse("/Admin/inicio_admin.html", {"request":request} ,status_code=303)

    usuario = {
        "id": resultado[0],
        "nombre": resultado[1],
        "identificacion": resultado[2],
        "contraseña": resultado[3]
    }

    return templates.TemplateResponse("Admin/editar_admin.html", {
        "request": request,
        "usuario": usuario
    })

@app.post("/templates/Admin/editar_admin.html", response_class=HTMLResponse)
async def actualizar_admin(
    request: Request,
    db: SessionDepends,
    id: int = Form(...),
    nombre: str = Form(...),
    identificacion: str = Form(...),
    contraseña: str = Form(...)
):
    nombre_usuario = request.session.get("nombre_usuario", None)
    consulta = text("""
        UPDATE usuario
        SET nombre = :nombre,
            identificacion = :identificacion,
            contraseña = :contraseña
        WHERE id = :id
    """)
    db.execute(consulta, {
        "id": id,
        "nombre": nombre,
        "identificacion": identificacion,
        "contraseña": contraseña
    })
    db.commit()
    return templates.TemplateResponse("/Admin/inicio_admin.html", {"request":request, "nombre_usuario":nombre_usuario} ,status_code=303)

@app.get("/templates/Admin/Principal/login.html", response_class=HTMLResponse)
async def inicio(db: SessionDepends, request: Request):
    return templates.TemplateResponse("/index.html", {"request":request})

@app.get("/templates/Admin/editar_usuarios.html", response_class=HTMLResponse)
async def mostrar_usuarios_para_editar(request: Request, db: SessionDepends):
    consulta = text("""
        SELECT 
            usuario.id,
            usuario.nombre,
            usuario.identificacion,
            medias_tecnicas.nombre,
            usuario.grado
        FROM usuario
        JOIN medias_tecnicas ON usuario.media_id = medias_tecnicas.id
    """)
    resultado = db.execute(consulta).fetchall()

    usuarios = [
        {
            "id": fila[0],
            "nombre": fila[1],
            "identificacion": fila[2],
            "media_tecnica": fila[3],
            "grado": fila[4]
        }
        for fila in resultado
    ]

    return templates.TemplateResponse("Admin/editar_usuarios.html", {
        "request": request,
        "usuarios": usuarios
    })

@app.get("/editar_usuario/{usuario_id}", response_class=HTMLResponse)
async def cargar_formulario_edicion(usuario_id: int, request: Request, db: SessionDepends):
    consulta = text("""
        SELECT id, nombre, identificacion, contraseña, grado
        FROM usuario
        WHERE id = :id
    """)
    resultado = db.execute(consulta, {"id": usuario_id}).fetchone()

    if not resultado:
        return templates.TemplateResponse("/Admin/editar_usuarios.html", {"request":request} ,status_code=303)

    usuario = {
        "id": resultado[0],
        "nombre": resultado[1],
        "identificacion": resultado[2],
        "contraseña": resultado[3],
        "grado": resultado[4]
    }

    return templates.TemplateResponse("Admin/formulario_editar_usuario.html", {
        "request": request,
        "usuario": usuario
    })

@app.post("/Admin/editar_usuarios.html", response_class=HTMLResponse)
async def guardar_edicion_usuario(
    request: Request,
    db: SessionDepends,
    id: int = Form(...),
    nombre: str = Form(...),
    identificacion: str = Form(...),
    contraseña: str = Form(...),
    grado: int = Form(...)
):
    nombre_usuario = request.session.get("nombre_usuario", None)
    consulta = text("""
        UPDATE usuario
        SET nombre = :nombre,
            identificacion = :identificacion,
            contraseña = :contraseña,
            grado = :grado
        WHERE id = :id
    """)
    db.execute(consulta, {
        "id": id,
        "nombre": nombre,
        "identificacion": identificacion,
        "contraseña": contraseña,
        "grado": grado
    })
    db.commit()
    return templates.TemplateResponse("/Admin/inicio_admin.html", {"request":request, "nombre_usuario":nombre_usuario} ,status_code=303)

@app.get("/Admin/eliminar_usuario.html", response_class=HTMLResponse)
async def mostrar_usuarios_para_eliminar(request: Request, db: SessionDepends):
    consulta = text("""
        SELECT 
            usuario.id,
            usuario.nombre,
            usuario.identificacion,
            medias_tecnicas.nombre,
            usuario.grado
        FROM usuario
        JOIN medias_tecnicas ON usuario.media_id = medias_tecnicas.id
    """)
    resultado = db.execute(consulta).fetchall()

    usuarios = [
        {
            "id": fila[0],
            "nombre": fila[1],
            "identificacion": fila[2],
            "media_tecnica": fila[3],
            "grado": fila[4]
        }
        for fila in resultado
    ]

    return templates.TemplateResponse("Admin/eliminar_usuario.html", {
        "request": request,
        "usuarios": usuarios
    })

@app.post("/eliminar_usuario", response_class=HTMLResponse)
async def eliminar_usuario(request: Request, db: SessionDepends, id: int = Form(...)):
    nombre_usuario = request.session.get("nombre_usuario", None)
    consulta = text("DELETE FROM usuario WHERE id = :id")
    db.execute(consulta, {"id": id})
    db.commit()
    return templates.TemplateResponse("/Admin/inicio_admin.html", {"request":request, "nombre_usuario":nombre_usuario} ,status_code=303)
