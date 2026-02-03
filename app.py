import streamlit as st
import streamlit.components.v1 as components

# --- Page Configuration ---
st.set_page_config(page_title="The Countdown", page_icon="\I0001F48A", layout="centered")

# --- Custom CSS for the Ethereal Black & Purple Theme ---
# This sets the background to black and adds the purple glow effects
st.markdown("""
    <style>
    /* Force the main background to be black */
    .stApp {
        background-color: #000000;
    }
    
    /* Text Styling */
    h1 {
        color: #E0B0FF !important; /* Mauve/Purple */
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
        text-shadow: 0 0 20px #8A2BE2; /* Ethereal Glow */
        font-weight: 300;
    }
    
    p {
        color: #D8BFD8;
        text-align: center;
        font-size: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Title Section ---
st.title("✨ Can you feel the healing, Da ✨")
st.write("Moments until we swallow the last of the quadriceps")

# --- The Flip Clock Component (HTML/JS/CSS) ---
# We use HTML/JS here because Streamlit's native python loop is too slow 
# for a smooth "second-by-second" animation.
flip_clock_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');

    body {
        background-color: transparent;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 300px;
        margin: 0;
        font-family: 'Bebas Neue', cursive;
    }

    .container {
        display: flex;
        gap: 20px;
    }

    .time-segment {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    /* The "Flip Card" look */
    .card {
        background-color: #111;
        color: #bf00ff; /* Electric Purple */
        font-size: 80px;
        padding: 20px 10px;
        border-radius: 10px;
        min-width: 100px;
        text-align: center;
        position: relative;
        box-shadow: 0 0 25px rgba(191, 0, 255, 0.4); /* Ethereal Glow */
        border: 1px solid #333;
    }

    /* The "Split" line in the middle of the card */
    .card::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 0;
        right: 0;
        height: 2px;
        background: #000;
        opacity: 0.8;
    }

    .label {
        color: #D8BFD8;
        margin-top: 10px;
        font-size: 18px;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-family: sans-serif;
    }

    @media (max-width: 600px) {
        .card { font-size: 40px; min-width: 60px; padding: 10px 5px; }
        .container { gap: 10px; }
    }
</style>
</head>
<body>

<div class="container">
    <div class="time-segment">
        <div class="card" id="days">00</div>
        <div class="label">Days</div>
    </div>
    <div class="time-segment">
        <div class="card" id="hours">00</div>
        <div class="label">Hours</div>
    </div>
    <div class="time-segment">
        <div class="card" id="minutes">00</div>
        <div class="label">Minutes</div>
    </div>
    <div class="time-segment">
        <div class="card" id="seconds">00</div>
        <div class="label">Seconds</div>
    </div>
</div>

<script>
    // Set the date we're counting down to (Feb 14, 2026 23:00:00 SAST)
    // SAST is UTC+2
    const countDownDate = new Date("Feb 14, 2026 23:00:00 GMT+0200").getTime();

    const x = setInterval(function() {
        const now = new Date().getTime();
        const distance = countDownDate - now;

        // Time calculations
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Update the HTML elements
        document.getElementById("days").innerHTML = days < 10 ? "0" + days : days;
        document.getElementById("hours").innerHTML = hours < 10 ? "0" + hours : hours;
        document.getElementById("minutes").innerHTML = minutes < 10 ? "0" + minutes : minutes;
        document.getElementById("seconds").innerHTML = seconds < 10 ? "0" + seconds : seconds;

        // If the count down is finished, display text
        if (distance < 0) {
            clearInterval(x);
            document.querySelector(".container").innerHTML = "<h1 style='color:#bf00ff'>IT IS TIME</h1>";
        }
    }, 1000);
</script>

</body>
</html>
"""

# Inject the HTML component
components.html(flip_clock_html, height=400)

st.divider()
st.caption("📍 Timezone: South Africa Standard Time (SAST)")
