import streamlit as st


history = []
grade_letter = ""


grades = {
    "A": [90, 100],
    "B": [80, 89],
    "C": [70, 79],
    "D": [60, 69],
    "F": [0, 59]
}

st.title("Grade Checker")
with st.form("Hey"):
    col1, col2 = st.columns(2)
    grade = st.number_input("Enter your Score 0-100", min_value=1, max_value=100, value=1)
    submit_button = st.form_submit_button(label="Check Grade")

if grades["A"][0] >= grade and grade >= grades["A"][1]:
    grade_letter = "A"
elif grades["B"][0] >= grade and grade >= grades["B"][1]:
    grade_letter = "B"
elif grades["C"][0] >= grade and grade >= grades["C"][1]:
    grade_letter = "C"
elif grades["D"][0] >= grade and grade >= grades["D"][1]:
    grade_letter = "D"
elif grades["F"][0] >= grade and grade >= grades["F"][1]:
    grade_letter = "F"


if submit_button:
    st.success(f"Score: {grade} → Grade: {grade_letter}")
    
    st.title("Grade History")
    
    history.append((grade, grade_letter))
    st.subheader("History")
    for i in history:
        st.write(f"Score: {i[0]} → Grade: {i[1]}")





# import streamlit as st


# col1, col2 = st.columns(2)

# st.title("Pizza Builder")
# with st.form("Hey"):
#     st.write("Build your own pizza!")
#     with col1:
#         size = st.selectbox("Size", ["Small", "Medium", "Large"])
#     with col2:
#         quantity = st.number_input("Quantity", min_value=1, max_value=10, value=1)
    
#     toppings = st.multiselect(
#         "Toppings",
#         ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Extra cheese"],
#     )
#     submit_button = st.form_submit_button(label="Place order")
# if submit_button = True:
#     st.title("Order Summary")












# import streamlit as st
# import time
# import random

# st.header("Trip Packer")

# # Towel = "Towel"
# # Sunscreen = "Sunscreen"
# # Swimsuit = "Swimsuit"
# # Flip-flops = "Flip-Flops"
# # Sunglasses = "Sunglasses"
# # Hiking_Boots = "Hiking Boots"
# # Jacket = "Jacket"
# # Water_bottle = "Water Bottle"
# # Trail_map = "Trail Map"
# # Gloves = "Gloves"
# # Comfortable_shoes = "Comfortable Shoes"
# # City_map = "City Map"
# # Camera = "Camera"
# # Umbrella = "Umbrella"
# # Portable_charger = "Portable Charger"
# # Tent = "Tent"
# # Sleeping_bag = "Sleeping Bag"
# # Flashlight = "Flashlight"
# # Bug_Spray = "Bug Spray"
# # Matches = "Matches"

# for value in list1:
#     packing += value
#     packing += ", "




# with st.sidebar:
#     where = st.selectbox("Where are you going", ["Beach", "Mountains", "City", "Camping"])
# if where == "Beach":    
#     list1 = st.multiselect("Select items to pick", ["Sunscreen", "Swimsuit", "Towel", "Flip-flops", "Sunglasses"])
#     done1 = st.checkbox("Mark everything as packed")
#     st.write("Packing: ", Towel)
#     for value in list1:
#         packing += value
#         packing += ", "
#     st.write(packing)
#     if done1 == True:
#         st.success("You're all packed")
# if where == "Mountains":    
#     list2 = st.multiselect("Select items to pick", ["Hiking Boots", "Jacket", "Water bottle", "Trail Map", "Gloves"])
#     done2 = st.checkbox("Mark everything as packed  ")
#     st.write("Packing: ", list2)
#     if done2 == True:
#         st.success("You're all packed")
# if where == "City":    
#     list3 = st.multiselect("Select items to pick", ["Comfortable Shoes", "City Map", "Camera", "Umbrella", "Portable Charger"])
#     done3 = st.checkbox("Mark everything as packed   ") 
#     st.write("Packing: ", list3)
#     if done3 == True:
#         st.success("You're all packed")
# if where == "Camping":    
#     list4 = st.multiselect("Select items to pick", ["Tent", "Sleeping Bag", "Flashlight", "Bug Spray", "Matches"])
#     don4 = st.checkbox("Mark everything as packed    ")
#     st.write("Packing: ", list4)
#     if don4 == True:
#         st.success("You're all packed")


























# # st.header("Mood Movie Picker")
# # movies = {
# #         "Happy": ("The Secret Life of Pets", "A fun lighthearted animated comedy."),
# #         "Sad": ("Coco", "A beautiful story about family and memory."),
# #         "Excited": ("Mad Max: Fury Road", "Non-stop action from start to finish."),
# #         "Bored": ("Everything Everywhere All at Once", "Wildly unpredictable and creative."),
# #         "Scared": ("Get Out", "A gripping psychological thriller.")
# #     }

# # col1, col2 = st.columns(2)

# # with st.form("Cool"):
# #     mood = st.radio("How are you feeling?", ["Happy", "Sad", "Excited", "Bored", "Scared"])
# #     st.form_submit_button("Pick a Movie")

# #     if mood == "Happy":
# #         st.write(movies["Happy"])

# #     if mood == "Sad":
# #         st.write(movies["Sad"])
                
# #     if mood == "Excited":
# #         st.write(movies["Excited"])

# #     if mood == "Scared":
# #         st.write(movies["Scared"])


