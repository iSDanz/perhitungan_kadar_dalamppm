import streamlit as st

st.title('Aplikasi perhitungan kadar dalam ppm')

massazat = st.number_input('Masukan nilai massa zat terlarut (mg)')
volume = st.number_input('Masukan nilai volume larutan (L)')

tombol = st.button('Hitung nilai ppm')

if tombol:
    nilai_ppm = massazat/volume
    st.success(f'Nilai kadar dalam ppm adalah {nilai_ppm}')