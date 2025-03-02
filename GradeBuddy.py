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

def calculate_grade_effect(current_grade, test_weight, test_score):
    try:
        test_weight = test_weight / 100
        remaining_weight = 1 - test_weight
        new_grade = (current_grade * remaining_weight) + (test_score * test_weight)
        return new_grade
    except:
        return "Invalid input. Please enter valid numbers."

def calculate_total_points_effect(current_grade, total_points, final_worth, test_score):
    try:
        remaining_points = total_points - final_worth
        new_grade = ((current_grade / 100) * remaining_points + test_score) / total_points * 100
        return new_grade
    except:
        return "Invalid input. Please enter valid numbers."

st.set_page_config(page_title="GradeBuddy", layout="centered")
st.title("📚 GradeBuddy: Grade Effect & Final Exam Calculator 🎯")
st.markdown("Calculate how a test affects your grade OR what you need on your final!")

st.markdown("## Step 1: Choose Calculator")
calc_choice = st.radio("Select an option", ["📊 Grade Effect Calculator", "🎓 Final Exam Calculator"])

if calc_choice == "📊 Grade Effect Calculator":
    st.markdown("## 📊 Grade Effect Calculator")
    st.markdown("### Step 2: Enter Your Current Grade")
    current_grade_effect = st.number_input("Your Current Grade (%)", min_value=0.0, max_value=100.0, step=0.1, key="effect_current", help="This is your current overall grade before the new test.")

    total_points_based = st.radio("Is this test graded on total points?", ["Yes", "No"], index=1, help="Select 'Yes' if your test is scored based on total points instead of percentages.")
    
    if total_points_based == "Yes":
        total_points = st.number_input("Total Points Possible", min_value=1, step=1, help="Enter the total points the test is worth.")
        final_worth = st.number_input("Final Worth Points", min_value=1, step=1, help="Enter the total points your final test is worth.")
        test_score = st.number_input("Test/Quiz Score (Points Earned)", min_value=0.0, step=0.1, help="Enter how many points you earned on the test.")
        
        if st.button("📊 Calculate Grade Impact"):
            new_grade = calculate_total_points_effect(current_grade_effect, total_points, final_worth, test_score)
            st.success(f"Your new grade after this test is **{new_grade:.2f}%**!")
    
    else:
        st.markdown("### Step 3: Enter Test Details")
        test_weight = st.slider("Test/Quiz Weight (%)", 1, 100, 10, help="Enter the percentage weight of the test in your overall grade.")
        test_score = st.number_input("Test/Quiz Score (%)", min_value=0.0, max_value=100.0, step=0.1, help="Enter the percentage score you received on the test.")
        
        if st.button("📊 Calculate Grade Impact"):
            new_grade = calculate_grade_effect(current_grade_effect, test_weight, test_score)
            st.success(f"Your new grade after this test is **{new_grade:.2f}%**!")

elif calc_choice == "🎓 Final Exam Calculator":
    st.markdown("## 🎓 Final Exam Calculator")
    st.markdown("### Step 2: Choose Your Grading Scale")
    scale = st.radio("Grading Scale", [7, 10], format_func=lambda x: "7-Point Scale (93=A, 85=B, etc.)" if x == 7 else "10-Point Scale (90=A, 80=B, etc.)", help="Select the grading scale used by your school.")

    st.markdown("### Step 3: Enter Your Exam Details")
    exam_weight = st.slider("Final Exam Weight (%)", 5, 50, 20, help="Enter the percentage weight of your final exam in your overall grade.")

    st.markdown("### Step 4: Enter Your Current Grade")
    current_grade = st.number_input("Your Current Grade (%)", min_value=0.0, max_value=100.0, step=0.1, help="Enter your current overall grade before the final exam.")

    desired_grade_input = st.text_input("### Step 5: Enter Your Desired Grade (Letter or %)", help="Enter the letter grade or percentage you want as your final grade.")

    if st.button("🎯 Calculate My Final Exam Score"):
        if desired_grade_input.isdigit():
            desired_grade_input = float(desired_grade_input)
        
        needed_score = calculate_needed_score(scale, exam_weight, current_grade, desired_grade_input)
        
        if isinstance(needed_score, str):
            st.error(needed_score)
        else:
            st.success(f"You need a **{needed_score:.2f}%** on your final exam!")
            
            if needed_score <= 50:
                st.markdown("**✅ You're cruising! This will be a breeze!**")
            elif needed_score <= 70:
                st.markdown("**📚 Manageable! Stay focused and you'll get there!**")
            elif needed_score <= 90:
                st.markdown("**💪 This will take some effort! Time to study hard!**")
            elif needed_score <= 100:
                st.markdown("**🔥 It's crunch time! Give it everything you've got!**")
            else:
                st.markdown("**😬 Well... miracles can happen, right?**")

st.markdown("---")
st.markdown("**📜 Changelog**")
st.text("Version 1.5 - Grade Effect Calculator added! Now you can check how a test impacts your grade using either total points or percentage weight.")
