import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(page_title="Modern Med Warrior, my Da", page_icon="💊", layout="centered")

# --- Custom CSS (The Ethereal Theme) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #050505;
    }
    h1, h2, h3 {
        color: #E0B0FF !important; /* Mauve */
        font-family: 'Helvetica Neue', sans-serif;
        text-shadow: 0 0 10px #8A2BE2;
    }
    .stFileUploader label {
        color: #D8BFD8 !important;
        font-size: 1.1rem;
    }
    /* Style the success boxes to be purple/dark */
    .stAlert {
        background-color: #1a0b2e;
        color: #E0B0FF;
        border: 1px solid #8A2BE2;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header Section ---
st.title("🛡️ Protocol: Health Restoration")
st.write("Stay the course. Finish the mission.")

# --- The Countdown (Target: Feb 14, 23:00) ---
# We keep the flip clock because it looks cool as a "Mission Timer"
flip_clock_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');
    body { background-color: transparent; font-family: 'Bebas Neue', cursive; margin:0; }
    .container { display: flex; justify-content: center; gap: 15px; }
    .card {
        background-color: #111; color: #bf00ff;
        font-size: 50px; padding: 10px; border-radius: 8px;
        min-width: 60px; text-align: center;
        box-shadow: 0 0 15px rgba(191, 0, 255, 0.3); border: 1px solid #333;
    }
    .label { color: #D8BFD8; font-size: 14px; text-align: center; font-family: sans-serif; margin-top:5px;}
</style>
</head>
<body>
<div class="container">
    <div><div class="card" id="days">00</div><div class="label">DAYS</div></div>
    <div><div class="card" id="hours">00</div><div class="label">HOURS</div></div>
    <div><div class="card" id="minutes">00</div><div class="label">MINS</div></div>
</div>
<script>
    const countDownDate = new Date("Feb 14, 2026 23:00:00 GMT+0200").getTime();
    setInterval(function() {
        const now = new Date().getTime();
        const distance = countDownDate - now;
        document.getElementById("days").innerHTML = Math.floor(distance / (1000 * 60 * 60 * 24));
        document.getElementById("hours").innerHTML = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        document.getElementById("minutes").innerHTML = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    }, 1000);
</script>
</body>
</html>
"""
components.html(flip_clock_html, height=120)
st.caption("Time remaining until course completion")

st.divider()

# --- Daily Check-In Logic ---
st.subheader("📝 Daily Checks with Canis")

# We create tabs for each major mealtime
tab1, tab2, tab3 = st.tabs(["🌅 Morning", "☀️ Afternoon", "🌙 Evening"])

def check_in_section(key_prefix, label_meal, label_meds):
    """Reusable function to create the uploaders"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"**Step 1:** {label_meal}")
        meal_pic = st.file_uploader("Upload Meal Pic", type=['jpg','png'], key=f"{key_prefix}_meal")
        
    with col2:
        st.info(f"**Step 2:** {label_meds}")
        med_pic = st.file_uploader("Upload Meds Pic", type=['jpg','png'], key=f"{key_prefix}_meds")

    # Validation Logic
    if meal_pic and med_pic:
        st.success("✅ Checkpoint Cleared! Healing Process: +10 XP")
        st.balloons() # Confetti animation!
        # Optional: Display the images they just uploaded
        with st.expander("View Proof"):
            c1, c2 = st.columns(2)
            c1.image(meal_pic, width=150)
            c2.image(med_pic, width=150)
    elif meal_pic or med_pic:
        st.warning("⚠️ Uhm, Incomplete! (respectfully) Please upload both to clear this checkpoint.")

# --- Populating the Tabs ---

with tab1:
    st.write("Start the day right. Fuel first, then armour - Bible read?")
    check_in_section("morning", "Eat Breakfast (Coat the stomach!)", "Take Morning Dose 💊")

with tab2:
    st.write("Keep the momentum. You're doing great, Bobo")
    check_in_section("noon", "Eat Lunch", "Take Afternoon Dose 💊")

with tab3:
    st.write(" Yes, unfortunate that I'm still 35 Km away, but time to rest soon. Wrap up.")
    check_in_section("night", "Eat Dinner", "Take Night Dose 💊")

# --- Progress Bar (Visual Motivation) ---
st.divider()
st.subheader("🧬 Course Integrity")

# Calculate today's progress based on uploads
# This resets if they refresh the page, but gives instant dopamine
uploads_count = 0
if st.session_state.get('morning_meal') and st.session_state.get('morning_meds'): uploads_count += 1
if st.session_state.get('noon_meal') and st.session_state.get('noon_meds'): uploads_count += 1
if st.session_state.get('night_meal') and st.session_state.get('night_meds'): uploads_count += 1

progress = int((uploads_count / 3) * 100)
st.progress(progress)

if progress == 100:
    st.write("🌟 **Daily Objective Complete.** Rest well, warrior.")
else:
    st.write(f"Daily Completion: **{progress}%**")
