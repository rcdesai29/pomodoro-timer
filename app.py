import streamlit as st
import time

st.title("Pomodoro Timer")

work_time = st.slider("Work Time (minutes)", 5, 90, 25)
break_time = st.slider("Break Time (minutes)", 1, 30, 5)

def format_time(seconds):
    mins, secs = divmod(seconds, 60)

    return f"{mins} minutes, {secs} seconds"

def pomodoro_timer(work_time, break_time):
    work_seconds = work_time * 60
    break_seconds = break_time * 60

    work_placeholder = st.empty()
    break_placeholder = st.empty()

    work_placeholder.markdown("### WORK!")
    for i in range(work_seconds):
        time.sleep(1)
        work_placeholder.markdown(format_time(work_seconds - i))

    break_placeholder.markdown("### BREAK!")
    for i in range(break_seconds):
        time.sleep(1)
        break_placeholder.markdown(format_time(break_seconds - i))

if st.button("Start Timer"):
    pomodoro_timer(work_time, break_time)
