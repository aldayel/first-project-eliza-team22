import streamlit as st
import base64

# List of team members with their name, role, description
team_members = [
    {"name": "Rahaf Masmali", "role": "Frontend", "description": "Programmed and designed the user interface.", "image": "assets/character.png"},
    {"name": "Feras Alswaid", "role": "Backend", "description": "Collected key terms and designed scenarios to improve chatbot responses.", "image": "assets/character.png"},
    {"name": "Marwan Al-Hindi", "role": "Backend", "description": "Mapped questions with answers and selected the most suitable response.", "image": "assets/character.png"},
    {"name": "Dania Al-Daisi", "role": "Data Collector", "description": "Contributed to planning and collected key keywords.", "image": "assets/character.png"},
    {"name": "Abdullah Al-Dail", "role": "Data Collector", "description": "Contributed to planning and collected key keywords.", "image": "assets/character.png"},
]

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

with open("./styles/team.css") as f:
    css = f.read()
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.markdown('<h1 class="team-title">Our Team ☕</h1>', unsafe_allow_html=True)


# Create columns dynamically based on the number of team members
# This ensures that all members are displayed in a structured layout
columns = st.columns(len(team_members))

# Loop through each team member and create their individual profile card
for col, member in zip(columns, team_members):
    image_base64 = get_base64_image(member["image"])
    
    col.markdown(
        f"""
        <div class="team-card">
            <div class="team-image-container">
                <img src="data:image/png;base64,{image_base64}" alt="{member['name']}">
            </div>
            <p class="team-name">{member['name']}</p>
            <p class="team-role">{member['role']}</p>
            <p class="team-description">{member['description']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )