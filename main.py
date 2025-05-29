import streamlit as st

# Diccionario de roles autorizados
ROLES = {
    "daang0406@gmail.com": "Ingeniero Clínico",
    "jear142003@gmail.com": "Practicante"
}

# Título
st.title("Portal de Autenticación con Roles")

# Login si no está autenticado
if not st.user.is_logged_in:
    st.login("google")
    st.stop()

# Obtener info del usuario autenticado
email = st.user.email
name = st.user.name
role = ROLES.get(email)

# Si el usuario no está en la lista, denegar acceso
if role is None:
    st.error("🚫 Acceso denegado. Tu cuenta no está autorizada para ver esta aplicación.")
    st.stop()

# Mostrar datos del usuario autorizado
st.success(f"✅ Acceso concedido. Bienvenido, {name} ({role})")
st.write(f"📧 {email}")
st.image(st.user.picture)

# Mostrar detalles del usuario (opcional)
with st.expander("Ver detalles del token"):
    st.json(st.user.to_dict())

# Logout
if st.button("Cerrar sesión"):
    st.logout()

