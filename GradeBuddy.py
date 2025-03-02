import streamlit as st

def calculate_needed_score(scale, exam_weight, current_grade, desired_grade_input):
    try:
        exam_weight = exam_weight / 100
        remaining_weight = 1 - exam_weight
        
        if isinstance(desired_grade_input, str):
            grading_scale = {"A": 93 if scale == 7 else 90, "B": 85 if scale == 7 else 80, "C": 77 if scale == 7 else 70, "D": 70 if scale == 7 else 60}
            desired_grade = grading_scale.get(desired_grade_input.upper(), None)
            if desired_grade is None:
                return "Invalid desired grade input."
        else:
            desired_grade = desired_grade_input
        
        needed_exam_score = (desired_grade - (current_grade * remaining_weight)) / exam_weight
        return needed_exam_score
    except:
        return "Invalid input. Please enter valid numbers."

st.set_page_config(page_title="GradeBuddy 🎓", layout="centered")
st.title("📚 GradeBuddy: Final Exam Calculator")
st.markdown("Calculate what you need on your final to reach your dream grade! 💪")

st.markdown("### Step 1: Choose Your Grading Scale")
scale = st.radio("Grading Scale", [7, 10], format_func=lambda x: "7-Point Scale (93=A, 85=B, etc.)" if x == 7 else "10-Point Scale (90=A, 80=B, etc.)")

st.markdown("### Step 2: Enter Your Exam Details")
exam_weight = st.slider("📊 Final Exam Weight (%)", 5, 50, 20)

st.markdown("### Step 3: Enter Your Current Grade")
current_grade = st.number_input("📈 Your Current Grade (%)", min_value=0.0, max_value=100.0, step=0.1)

desired_grade_input = st.text_input("### Step 4: Enter Your Desired Grade (Letter or %)")

if st.button("🧮 Calculate My Final Exam Score"):
    if desired_grade_input.isdigit():
        desired_grade_input = float(desired_grade_input)
    
    needed_score = calculate_needed_score(scale, exam_weight, current_grade, desired_grade_input)
    
    if isinstance(needed_score, str):
        st.error(needed_score)
    else:
        st.success(f"📢 You need a **{needed_score:.2f}%** on your final exam!")
        
        if needed_score <= 50:
            st.markdown("🎉 **You're cruising! This will be a breeze!**")
        elif needed_score <= 70:
            st.markdown("😌 **Manageable! Stay focused and you'll get there!**")
        elif needed_score <= 90:
            st.markdown("😬 **This will take some effort! Time to study hard!**")
        elif needed_score <= 100:
            st.markdown("😱 **It's crunch time! Give it everything you've got!**")
        else:
            st.markdown("💀 **Well... miracles can happen, right?**")

st.markdown("---")
st.markdown("📜 **Changelog**")
st.text("Version 1.2 - Streamlit version, improved UI, and humor!")
