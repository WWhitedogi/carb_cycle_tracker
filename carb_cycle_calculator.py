import streamlit as st

def calculate_macros(weight):
    # 每日摄入量
    carbs_per_day = weight * 2
    fat_per_day = weight * 0.8
    protein_per_day = weight * 1

    # 每周总摄入量
    weekly_carbs = carbs_per_day * 7
    weekly_fat = fat_per_day * 7
    weekly_protein = protein_per_day * 7

    # 各种碳水日的摄入量
    high_carb_day_carbs = weekly_carbs * 0.5 / 2
    high_carb_day_fat = weekly_fat * 0.15 / 2
    low_carb_day_carbs = weekly_carbs * 0.15 / 2
    low_carb_day_fat = weekly_fat * 0.5 / 2
    moderate_carb_day_carbs = weekly_carbs * 0.35 / 3
    moderate_carb_day_fat = weekly_fat * 0.35 / 3

    # 输出结果
    st.write(f"体重: {weight}kg 的每日和每周营养摄入量:")
    st.write(f"每日碳水摄入: {carbs_per_day:.1f}g")
    st.write(f"每日脂肪摄入: {fat_per_day:.1f}g")
    st.write(f"每日蛋白质摄入: {protein_per_day:.1f}g")
    st.write()
    st.write(f"每周碳水摄入: {weekly_carbs:.1f}g")
    st.write(f"每周脂肪摄入: {weekly_fat:.1f}g")
    st.write(f"每周蛋白质摄入: {weekly_protein:.1f}g")
    st.write()
    st.write("碳水循环计划：")
    st.write(f"高碳日 (2天) - 每天碳水: {high_carb_day_carbs:.1f}g, 脂肪: {high_carb_day_fat:.1f}g")
    st.write(f"低碳日 (2天) - 每天碳水: {low_carb_day_carbs:.1f}g, 脂肪: {low_carb_day_fat:.1f}g")
    st.write(f"中碳日 (3天) - 每天碳水: {moderate_carb_day_carbs:.1f}g, 脂肪: {moderate_carb_day_fat:.1f}g")
    st.write()
    st.write("蛋白质摄入：建议每餐摄入20-40g蛋白质，每3-4小时一次。")

st.title("碳水循环营养计算器")
weight = st.number_input("请输入体重（kg）：", min_value=30.0, max_value=150.0, step=0.1)
if weight:
    calculate_macros(weight)
