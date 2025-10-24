import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ===============================
# CONFIGURACIÓN GENERAL
# ===============================
st.set_page_config(
    page_title="CLASES: CUESTIONARIO", 
    page_icon="🎓", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ===============================
# ESTILOS CSS PERSONALIZADOS
# ===============================
st.markdown("""
<style>
    /* Fondo con gradiente */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Contenedor principal con diseño de tarjeta */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        background: white;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        max-width: 800px;
    }
    
    /* Títulos más atractivos */
    h1 {
        color: #667eea !important;
        font-weight: 800 !important;
        text-align: center;
        font-size: 2.5rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    h2 {
        color: #764ba2 !important;
        font-weight: 700 !important;
        margin-top: 2rem !important;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #667eea;
    }
    
    /* Mejorar apariencia de los radio buttons */
    .stRadio > label {
        font-weight: 600;
        color: #2d3748;
        font-size: 1.1rem;
    }
    
    /* Mejorar apariencia de multiselect */
    .stMultiSelect > label {
        font-weight: 600;
        color: #2d3748;
        font-size: 1.1rem;
    }
    
    /* Botón de envío personalizado */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
        font-size: 1.2rem;
        padding: 0.75rem 2rem;
        border-radius: 50px;
        border: none;
        width: 100%;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Estilo para el texto descriptivo */
    .descripcion {
        background: linear-gradient(135deg, #f6f8fb 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        margin-bottom: 2rem;
    }
    
    /* Iconos en los encabezados */
    .emoji-header {
        font-size: 1.5rem;
        margin-right: 0.5rem;
    }
    
    /* Divider personalizado */
    hr {
        margin: 2rem 0;
        border: none;
        height: 2px;
        background: linear-gradient(to right, transparent, #667eea, transparent);
    }
</style>
""", unsafe_allow_html=True)

# ===============================
# HEADER CON LOGO
# ===============================
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # AQUÍ DEBES COLOCAR TU IMAGEN
    # Opción 1: Si tienes la imagen en la misma carpeta que el script
    # st.image("logo.png", use_container_width=True)
    
    # Opción 2: Si tienes la imagen en una carpeta específica
    # st.image("assets/logo.png", use_container_width=True)
    
    # Opción 3: Si quieres usar una URL de internet
    # st.image("https://tu-url.com/logo.png", use_container_width=True)
    
    # Mientras tanto, mostramos un placeholder
    st.markdown("<div style='text-align: center; font-size: 4rem;'>🎓</div>", unsafe_allow_html=True)

st.title("CLASES: CUESTIONARIO")

# Descripción mejorada
st.markdown("""
<div class="descripcion">
    <p style='margin: 0; font-size: 1.1rem; color: #2d3748; line-height: 1.6;'>
        <strong>📊 Sobre este estudio:</strong><br>
        Queremos conocer tus preferencias y necesidades educativas para crear servicios que realmente te ayuden. 
        Tu participación es <strong>100% anónima</strong> y tomará menos de 3 minutos.
    </p>
    <p style='margin-top: 1rem; margin-bottom: 0; font-size: 1rem; color: #667eea;'>
        <strong>🎯 Objetivo:</strong> Mejorar la experiencia educativa con cursos útiles y entretenidos.
    </p>
</div>
""", unsafe_allow_html=True)

# ===============================
# DICCIONARIOS PARA CODIFICACIÓN
# ===============================
CODIGOS = {
    "semestre": {"1°": 1, "2°": 2, "3°": 3, "4°": 4, "5°": 5, "6°": 6},
    "genero": {"Hombre": 1, "Mujer": 2, "Prefiero no decirlo": 3},
    "turno": {"Matutino": 1, "Vespertino": 2},
    "preferencia_pasar": {
        "Estudiar mucho": 1,
        "Pagar un curso extra": 2,
        "Que resuelvan el examen por mí": 3,
        "Ninguna de las anteriores": 4
    },
    "pagarias_rubrica": {"Sí": 1, "No": 2, "Depende del precio": 3},
    "tipo_profesor": {
        "Hombre": 1,
        "Mujer": 2,
        "Un personaje animado en videos": 3,
        "Me da lo mismo mientras aprenda": 4
    },
    "pago_justo": {
        "Menos de $200": 1,
        "$200–$400": 2,
        "$400–$600": 3,
        "Más de $600": 4
    },
    "red_social": {
        "TikTok": 1,
        "Instagram": 2,
        "WhatsApp": 3,
        "YouTube": 4,
        "Facebook": 5
    }
}

# Opciones para multiselect (se codificarán como listas de números)
MATERIAS_OPC = ["Matemáticas / Física", "Química / Biología", "Historia / Sociales", "Artísticas", "Otro"]
RAZONES_OPC = ["Los profes no explican bien", "Son aburridas las clases", "Los alumnos no estudian", "La escuela no importa"]
CURSOS_OPC = ["Programación de videojuegos", "Trucos y secretos de la IA", "Diseño y Marketing", "Inversiones y manejo de dinero", "Otra"]
CONFIANZA_OPC = ["Recomendaciones de amigos", "Ver resultados o reseñas", "Que tenga un personaje animado que explique", "Que ofrezcan prueba gratuita"]

# ===============================
# FORMULARIO
# ===============================
with st.form("catia_form"):
    
    st.markdown("<h2>🧠 Datos Generales</h2>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        semestre = st.radio("¿En qué semestre estás?", ["1°", "2°", "3°", "4°", "5°", "6°"])
        turno = st.radio("¿En qué turno estudias?", ["Matutino", "Vespertino"])
    with col_b:
        genero = st.radio("¿Cuál es tu sexo?", ["Hombre", "Mujer", "Prefiero no decirlo"])
    
    st.markdown("<h2>📚 Dificultades Académicas</h2>", unsafe_allow_html=True)
    materias = st.multiselect(
        "¿Qué materias se te dificultan más?",
        MATERIAS_OPC,
    )
    
    razones = st.multiselect(
        "¿Por qué razones crees que tú o algún amig@ reprueban las materias?",
        RAZONES_OPC,
    )
    
    st.markdown("<h2>💡 Comportamiento y Preferencias</h2>", unsafe_allow_html=True)
    pasar = st.radio(
        "¿Para pasar una materia cuál de las siguientes opciones prefieres?",
        ["Estudiar mucho", "Pagar un curso extra", "Que resuelvan el examen por mí", "Ninguna de las anteriores"],
    )
    
    pagarias = st.radio(
        "¿Pagarías por que te hagan un examen o rúbrica para pasar una materia aburrida?",
        ["Sí", "No", "Depende del precio"],
    )
    
    curso = st.multiselect(
        "¿De cuál de los siguientes temas tomarías un curso?",
        CURSOS_OPC,
    )
    
    col_c, col_d = st.columns(2)
    with col_c:
        profesor = st.radio(
            "Prefieres que te dé clases:",
            ["Hombre", "Mujer", "Un personaje animado en videos", "Me da lo mismo mientras aprenda"],
        )
    with col_d:
        pago = st.radio(
            "¿Cuánto te parece justo pagar por ayuda para pasar una materia difícil?",
            ["Menos de $200", "$200–$400", "$400–$600", "Más de $600"],
        )
    
    st.markdown("<h2>🎯 Marketing y Redes</h2>", unsafe_allow_html=True)
    confianza = st.multiselect(
        "¿Qué te haría confiar en una escuela o persona que ofrece ese tipo de ayuda?",
        CONFIANZA_OPC,
    )
    
    red = st.radio(
        "¿En qué red social pasas más tiempo?",
        ["TikTok", "Instagram", "WhatsApp", "YouTube", "Facebook"],
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    enviado = st.form_submit_button("🚀 Enviar Respuestas")

# ===============================
# GUARDADO DE DATOS CODIFICADOS
# ===============================
if enviado:
    # Codificar multiselect como números separados por comas
    def codificar_multiselect(selecciones, opciones):
        return ", ".join([str(opciones.index(item) + 1) for item in selecciones])
    
    # Crear carpeta y archivo si no existen
    filename = "respuestas.csv"
    existe = os.path.isfile(filename)
    
    # Crear registro de respuesta con CÓDIGOS NUMÉRICOS
    data = {
        "timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "semestre": [CODIGOS["semestre"][semestre]],
        "genero": [CODIGOS["genero"][genero]],
        "turno": [CODIGOS["turno"][turno]],
        "materias_dificiles": [codificar_multiselect(materias, MATERIAS_OPC)],
        "razones_reprobacion": [codificar_multiselect(razones, RAZONES_OPC)],
        "preferencia_pasar": [CODIGOS["preferencia_pasar"][pasar]],
        "pagarias_rubrica": [CODIGOS["pagarias_rubrica"][pagarias]],
        "curso_interes": [codificar_multiselect(curso, CURSOS_OPC)],
        "tipo_profesor": [CODIGOS["tipo_profesor"][profesor]],
        "pago_justo": [CODIGOS["pago_justo"][pago]],
        "confianza_en_ayuda": [codificar_multiselect(confianza, CONFIANZA_OPC)],
        "red_social": [CODIGOS["red_social"][red]],
    }
    
    df = pd.DataFrame(data)
    df.to_csv(filename, mode="a", header=not existe, index=False, encoding="utf-8-sig")
    
    # ===============================
    # ANIMACIÓN DE AGRADECIMIENTO
    # ===============================
    st.success("✅ ¡Gracias por participar en este estudio!")
    st.balloons()
    st.markdown("""
    <div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, #f6f8fb 0%, #e9ecef 100%); border-radius: 15px; margin-top: 2rem;'>
        <h3 style='color: #667eea;'>🎉 ¡Tu opinión es muy valiosa!</h3>
        <p style='color: #2d3748;'>Tus respuestas han sido registradas correctamente y nos ayudarán a mejorar.</p>
    </div>
    """, unsafe_allow_html=True)