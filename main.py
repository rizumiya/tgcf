import streamlit
import subprocess

# Judul halaman
st.title("Aplikasi Streamlit Sederhana")

# Tampilkan teks menggunakan st.write()
st.write("Selamat datang di aplikasi Streamlit sederhana!")

# Tampilkan gambar menggunakan st.image()
if st.button("Klik!"):
  try:
    subprocess.run(['tgcf-web'])
  except:
    subprocess.run(['cd', 'tgcf/web_ui'])
    subprocess.run(['python', 'run.py'])
