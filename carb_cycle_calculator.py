import streamlit as st

def calculate_macros(weight):
    # Daily intake
    carbs_per_day = weight * 2
    fat_per_day = weight * 0.8
    protein_per_day = weight * 1

    # Weekly intake totals
    weekly_carbs = carbs_per_day * 7
    weekly_fat = fat_per_day * 7
    weekly_protein = protein_per_day * 7

    # Carb cycling plan for different days
    high_carb_day_carbs = weekly_carbs * 0.5 / 2
    high_carb_day_fat = weekly_fat * 0.15 / 2
    low_carb_day_carbs = weekly_carbs * 0.15 / 2
    low_carb_day_fat = weekly_fat * 0.5 / 2
    moderate_carb_day_carbs = weekly_carbs * 0.35 / 3
    moderate_carb_day_fat = weekly_fat * 0.35 / 3

    # Output results
    st.write(f"Daily and weekly nutrition intake for weight: {weight} kg")
    st.write(f"Daily carbs intake: {carbs_per_day:.1f} g")
    st.write(f"Daily fat intake: {fat_per_day:.1f} g")
    st.write(f"Daily protein intake: {protein_per_day:.1f} g")
    st.write()
    st.write(f"Weekly carbs intake: {weekly_carbs:.1f} g")
    st.write(f"Weekly fat intake: {weekly_fat:.1f} g")
    st.write(f"Weekly protein intake: {weekly_protein:.1f} g")
    st.write()
    st.write("Carb Cycling Plan:")
    st.write(f"High Carb Days (2 days) - Daily carbs: {high_carb_day_carbs:.1f} g, Fat: {high_carb_day_fat:.1f} g")
    st.write(f"Low Carb Days (2 days) - Daily carbs: {low_carb_day_carbs:.1f} g, Fat: {low_carb_day_fat:.1f} g")
    st.write(f"Moderate Carb Days (3 days) - Daily carbs: {moderate_carb_day_carbs:.1f} g, Fat: {moderate_carb_day_fat:.1f} g")
    st.write()
    st.write("Protein intake recommendation: Consume 20-40g of protein per meal, every 3-4 hours.")

st.title("Carb Cycling Nutrition Calculator")
weight = st.number_input("Enter weight (kg):", min_value=30.0, max_value=150.0, step=0.1)
if weight:
    calculate_macros(weight)
