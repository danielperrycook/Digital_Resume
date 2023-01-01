from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
profile_pic1 = current_dir / "assets" / "profile-pic1.png"
profile_pic2 = current_dir / "assets" / "profile-pic2.png"
profile_pic3 = current_dir / "assets" / "profile-pic3.png"
profile_pic4 = current_dir / "assets" / "profile-pic4.png"
profile_pic5 = current_dir / "assets" / "profile-pic5.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Daniel Cook"
PAGE_ICON = ":wave:"
NAME = "Daniel Cook, PMP, CISSP"
DESCRIPTION = """
Senior Telecommunications Engineer 
"""
DESCRIPTION2 = """
🪂 82nd Airborne Division, US Army
"""
EMAIL = "daniel.perry.cook@gmail.com"


SOCIAL_MEDIA = {
    "💼 LinkedIn": "https://www.linkedin.com/in/danielcook34/",
    "👨‍💻 GitHub": "https://github.com/danielperrycook",
}
PROJECTS = {
    "🏆 Active Duty Historical End-strength - Comparing Military Size over the last 2 years": "https://youtu.be/Sb0A9i6d320",
    #"🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    #"🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    #"🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
profile_pic1 = Image.open(profile_pic1)
profile_pic2 = Image.open(profile_pic2)
profile_pic3 = Image.open(profile_pic3)
profile_pic4 = Image.open(profile_pic4)
profile_pic5 = Image.open(profile_pic5)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("💼 [Linkedin](https://www.linkedin.com/in/danielcook34/)"+"  "+"  👨‍💻 [GitHub](https://github.com/danielperrycook)")

# --- SOCIAL LINKS ---
#st.write('\n')
#cols = st.columns(len(SOCIAL_MEDIA))
#for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
#    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Executive Summary")
st.write(
    """
Senior Telecommunications Engineer and Integrated Product Support (IPS) Analyst with 
10+ years of experience developing, managing, and applying electronic systems maintenance 
life cycle sustainment and IPS strategies worldwide. Mastery level expertise in Joint 
Capabilities Integration and Development System (JCIDS) and life cycle logistics for 
emerging Army materiel solutions. Dynamic and inclusive leader, mentor, and team builder 
with a proven record of generating and building relationships, managing projects from 
concept to completion, and coaching team members to success.
"""
)

# --- Education ---
st.write('\n')
st.subheader("Education")
st.write(
    """
- 🎓 Master of Science – Cybersecurity Studies (with Honors) ▪ American Military University (2019)
- 🎓 Bachelor of Arts – Computer Science/Religion (Cum Laude) ▪ Mid-America Nazarene University (2003)
"""
)

# --- Certifications ---
st.write('\n')
st.subheader("Certifications")
st.write(
    """
- 📜 Project Management Professional (PMP License# 1982747)
- 📜 Certified Information Systems Security Professional (CISSP License# 516827)
- 📜 COMPTIA Security+, Network+, A+ (License# QSV9J9VCQD44KN85)
- 📜 Microsoft Certified: Azure Fundamentals (I367-9826)
- 📜 Microsoft Certified: Power BI Data Analyst Associate (I503-1293)
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- Job 1 ---
col3, col4 = st.columns([2, 20])
with col3:
    st.image(profile_pic1, width=30)
with col4:
    st.subheader("Senior Telecommunications Engineer")

st.write("82nd Airborne Division | Fort Bragg, NC | JUN 2020 – Present")
st.write(
    """
    Senior Chief Electronics and Communications Engineer responsible for Signal readiness of 
    19,000 Paratroopers and 40,000 communication devices, Chief Advisor to the Command General 
    concerning all Electronic Maintenance of Army common and COTS (Commercial-off-the-Shelf) 
    equipment, coordinating mission synchronization for deployable C&E (Communication & Electronic) 
    Shops, monitoring warranty repairs and modifications, and Subsystem Management of Electronic Systems.
    """
)
st.write(
    """
- ► Scripted Communication Maintenance Analytic Dashboards across the 18th Airborne Corps Signal Community, developing a single detailed repository that Staff Officers to Electronic Technicians can all action readiness tasks together.
- ► Implemented Communication Inspection Programs for Division S6 Shops and developed preventive maintenance plans for 21 Communication Platforms; finished FY 22 with Division Operation Readiness Rating of 95% for entire year.
- ► Establish Division Worldwide Maps Repository for Joint Battle Command - Platforms (JBC-P); instrumental in meeting Immediate Response Force (IRF) requirements to deploy worldwide within 18 hours of notification.
"""
)

# --- Job 2 ---
st.write('\n')
col3, col4 = st.columns([2, 20])
with col3:
    st.image(profile_pic2, width=40)
with col4:
    st.subheader("Chief Electronics/Communications Technician")

st.write("3rd Psychological Operations Battalion | Fort Bragg, NC | 2017 - 2020")
st.write(
    """
    Chief Electronics/Communication Technician supporting two Psychological Operations 
    Groups (Airborne); responsible for the field-level maintenance of Army common, PSYOP 
    unique and Special Operations Forces ground communications and armament equipment; 
    reviewing and supervising maintenance reports crucial to the mission; provides logistical 
    support and mission coordination for six deployable technician teams, monitoring warranty 
    repair and modification updates, and safety of use program for electronic equipment.
    """
)
st.write(
    """
- ► Launched SDN Repair/Refurbishment Facility and 3D Printing Facility for the PSYOP Regiment, which provided services and ability to fabricate parts for the new 53 New Satellite Nodes fielded to the Regiment. 
- ► Led Standardization and Product Improvement efforts with multiple programs including Radio-in-a-Box (RIAB) and Military Information Support Operations Print (MISOP)-Light: coordinating remote operation and maintenance to over 250 Soldiers.
- ► Prepared and deployed technician teams that assessed and repaired 15 radio and cell towers in support of 2017 hurricane relief efforts; constructed 5 radios and towers in Jordan and Turkey in support of on-going combat operations against ISIS.
"""
)

# --- Job 3 ---
st.write('\n')
col3, col4 = st.columns([2, 20])
with col3:
    st.image(profile_pic3, width=40)
with col4:
    st.subheader("Chief Electronics/Communications Technician")

st.write("2nd Armored Brigade Combat Team | Fort Hood, TX | 2014 - 2017")
st.write(
    """
    Senior Electronics Maintenance Technician for entire 2d Armored Brigade 
    Combat Team, 1st Calvary Division, managing maintenance and repair of the 
    WIN-T assets to include JNN/CPN/HCLOS/STT/CPP systems, JBC-P systems 
    including FBCB2/JCR/LOG systems, tactical radios, special electronic/night 
    vision devices and cryptographic devices. 
    """
)
st.write(
    """
- ► Skillfully Managed $2.5million worth of Communication Spares during 9-month rotation to Korea and throughout numerous Training Exercises: zero losses to property or equipment, and operational rate communication systems of 95%.
- ► Implemented Brigade-wide upgrade of 195 Simple Key Loaders (SKLs), managed Hard Drive Exchange Program for 1200 Tactical Systems, and issued over $3M worth of new communication equipment throughout the Brigade Reset Phase.
"""
)

# --- Job 4 ---
st.write('\n')
col3, col4 = st.columns([2, 20])
with col3:
    st.image(profile_pic4, width=40)
with col4:
    st.subheader("Special Missions Non-Commissioned Officer")

st.write("White House Communications Agency | Washington, DC  | 2008 - 2014")
st.write(
    """
    Senior Special Missions Technician serving as the focal point for the design, 
    coordination and worldwide deployment of dedicated secure communication links 
    in direct support of the President of the United States, National Security 
    Council and others as directed for secure communications with foreign leadership.
    """
)
st.write(
    """
- ► Developed and implemented new secure communications to over 20 foreign countries with direct communications access to the White House: providing 100% visibility and critical situational awareness to both the Agency and our foreign customers.
- ► Oversaw network of over CONUS 250 short-haul and long-haul Presidential circuits to include: installation, maintenance, and continuous deployment and redeployment of secure Head of State circuits.
- ► Managed 500-item Communications Security (COMSEC) account with 100% accountability; worked directly with the NSA to deploy 213 cryptographic devices to include the STE, vIPer, SECTRA, SG-175Ds, and SG-250 cryptographic families.
"""
)

# --- Job 5 ---
st.write('\n')
col3, col4 = st.columns([2, 20])
with col3:
    st.image(profile_pic5, width=40)
with col4:
    st.subheader("Radio/COMSEC Repairer")

st.write("3rd Stryker Brigade Combat Team | Fort Lewis, WA | 2004 - 2008")
st.write(
    """
    Radio-COMSEC Technician charged to troubleshoot and diagnose causes of malfunctions 
    on a wide range of electronic equipment. Conduct exchanges faulty equipment, 
    perform difficult or complex repairs of defective components, subassemblies, and 
    related cabling, and ensure that National Security Agency (NSA) approved components 
    are used in COMSEC/CCI repairs. Provides shop supervisor with equipment repair status, 
    priorities, and necessity for bench stock resupply. Performs final or quality control 
    inspection of repaired equipment. Controls and accounts for CCI within the repair facility.
    """
)
st.write(
    """
- ► Served as Radio Maintenance Team Lead, supervising repair to systems, equipment and subassemblies by adjusting, aligning, repairing, and replacing defective components, cryptographic items, or line replaceable units (LRU).
- ► During 15-month deployment to Iraq, selected to as Lead Communicator for Stryker Recovery Team in support of Operation Iraqi Freedom, recovering 33 damaged vehicles during 50 missions. 
"""
)