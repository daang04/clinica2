import streamlit as st

# Diccionario de roles autorizados
ROLES = {
    "daang0406@gmail.com": "Ingeniero Clínico",
    "jear142003@gmail.com": "Practicante"
}

st.title("Portal de Autenticación con Roles")

# Autenticación
if not st.user.is_logged_in:
    st.login("google")
    st.stop()

# Obtener usuario
email = st.user.email
name = st.user.name
role = ROLES.get(email)

# Control de acceso
if role is None:
    st.error("🚫 Acceso denegado. Tu cuenta no está autorizada para ver esta aplicación.")
    st.stop()

# =============================
# ✅ Sidebar (sólo si logueado)
# =============================
with st.sidebar:
    st.markdown(f"👤 **{name}**")
    st.markdown(f"📧 {email}")
    st.markdown(f"🛡️ Rol: `{role}`")
    menu = st.selectbox("Navegación", ["Inicio", "Perfil", "Configuración"])

# =============================
# 🎯 Contenido según menú
# =============================
st.success(f"Bienvenido, {name} ({role})")

if menu == "Inicio":
    st.write("🧭 Estás en la página de inicio.")
elif menu == "Perfil":
    st.write("👤 Esta es tu información de perfil.")
    st.image(st.user.picture)
    st.json(st.user.to_dict())
elif menu == "Configuración":
    st.write("⚙️ Aquí puedes configurar tu entorno (futuro).")

# Botón de logout
if st.button("Cerrar sesión"):
    st.logout()
