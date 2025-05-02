
import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Remote Team Monitoring - Divisi Keuangan")

if 'data' not in st.session_state:
    st.session_state.data = []

with st.form("activity_form"):
    nama = st.selectbox("Nama Tim", ["Account Payable", "Account Receivable", "Treasury Operation"])
    aktivitas = st.text_input("Aktivitas yang dilakukan")
    status = st.selectbox("Status", ["To Do", "In Progress", "Done"])
    submit = st.form_submit_button("Submit")

    if submit:
        st.session_state.data.append({
            "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Nama Tim": nama,
            "Aktivitas": aktivitas,
            "Status": status
        })
        st.success("Aktivitas berhasil dicatat!")

st.header("📊 Status Tim")
df = pd.DataFrame(st.session_state.data)

if not df.empty:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("To Do", df[df["Status"] == "To Do"].shape[0])
    with col2:
        st.metric("In Progress", df[df["Status"] == "In Progress"].shape[0])
    with col3:
        st.metric("Done", df[df["Status"] == "Done"].shape[0])

    st.divider()
    st.header("📋 Aktivitas Terbaru")
    st.dataframe(df.sort_values(by="Waktu", ascending=False), use_container_width=True)
else:
    st.info("Belum ada aktivitas yang dicatat.")
