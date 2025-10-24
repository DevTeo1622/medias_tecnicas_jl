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
        return templates.TemplateResponse("Admin/inicio_admin.html", {
            "request": request,
            "identificacion": identificacion,
            "contraseña": contraseña,
            "usuario": resultado,
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
            "nombre": resultado.nombre if hasattr(resultado, 'nombre') else resultado[3],
            "id": resultado.id if hasattr(resultado, 'id') else resultado[0],
            "rol": resultado.nombre,
            "media_id": resultado.media_id
        }) 
    
    else:
        return templates.TemplateResponse("Principal/login.html", {"request":request}) 
    
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

    return templates.TemplateResponse("Software/docs_soft.html", {"request": request})

@app.get("/docs_soft.html", response_class=HTMLResponse)
async def documentos_software(db: SessionDepends, request: Request):

    return templates.TemplateResponse("Software/docs_soft.html", {"request": request})

@app.get("/templates/Software/grabaciones_soft.html", response_class=HTMLResponse)
async def videos_software(db: SessionDepends, request: Request):

    return templates.TemplateResponse("Software/grabaciones_soft.html", {"request": request})

@app.get("/grabaciones_soft.html", response_class=HTMLResponse)
async def videos_software(db: SessionDepends, request: Request):

    return templates.TemplateResponse("Software/grabaciones_soft.html", {"request": request})