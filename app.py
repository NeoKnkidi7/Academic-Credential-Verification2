import streamlit as st
import pandas as pd
import hashlib
import datetime
import time
import io

# Page configuration
st.set_page_config(
    page_title="Academic Credential Verification",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Generate blockchain-like hash
def generate_blockchain_hash(data):
    return hashlib.sha256(str(data).encode()).hexdigest()[:12] + "..."

# Main application
def main():
    # Sidebar navigation
    with st.sidebar:
        st.title("AcademicVerify")
        st.subheader("Credential Verification System")
        
        menu = st.selectbox("Navigation", ["Dashboard", "Verify Credential", "Institution Portal", "About"])
        st.markdown("---")
        st.info("Blockchain-secured academic credential verification")
        st.markdown("---")
        st.caption("© 2023 AcademicVerify Inc.")

    # Dashboard
    if menu == "Dashboard":
        st.header("📊 Verification Dashboard")
        
        # Stats cards
        col1, col2, col3 = st.columns(3)
        col1.metric("Credentials Verified", "1,842", "12% increase")
        col2.metric("Institutions", "127", "3 new")
        col3.metric("Success Rate", "98.7%")
        
        st.markdown("---")
        
        # Recent activities
        st.subheader("Recent Activities")
        activities = {
            'Timestamp': [
                datetime.datetime.now() - datetime.timedelta(hours=4),
                datetime.datetime.now() - datetime.timedelta(hours=3),
                datetime.datetime.now() - datetime.timedelta(hours=2),
                datetime.datetime.now() - datetime.timedelta(hours=1),
                datetime.datetime.now()
            ],
            'Activity': [
                'Document uploaded', 
                'Institution verified', 
                'Verification completed', 
                'New institution added', 
                'Report generated'
            ],
            'Status': ['Completed'] * 5
        }
        st.dataframe(pd.DataFrame(activities), hide_index=True)
        
        # Verification metrics
        st.subheader("Verification Metrics")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**By Country**")
            country_data = pd.DataFrame({
                'Country': ['USA', 'UK', 'Canada', 'Australia'],
                'Credentials': [850, 420, 320, 150]
            })
            st.bar_chart(country_data.set_index('Country'))
        
        with col2:
            st.write("**By Degree**")
            degree_data = pd.DataFrame({
                'Degree': ['BSc Computer Science', 'MBA', 'PhD Physics', 'BA Economics'],
                'Credentials': [420, 380, 250, 210]
            })
            st.bar_chart(degree_data.set_index('Degree'))
                
    # Verify Credential
    elif menu == "Verify Credential":
        st.header("🔍 Verify Academic Credential")
        
        tab1, tab2 = st.tabs(["Verify by Document", "Verify by ID"])
        
        with tab1:
            uploaded_file = st.file_uploader("Upload academic document (PDF or image)", type=["pdf", "jpg", "jpeg", "png"])
            
            if uploaded_file:
                # Document preview
                if uploaded_file.type == "application/pdf":
                    st.info("PDF document uploaded successfully")
                else:
                    st.image(uploaded_file, width=300)
                
                # Verification process
                if st.button("Start Verification"):
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    steps = [
                        "Uploading document...",
                        "Extracting content...",
                        "Verifying authenticity...",
                        "Checking records...",
                        "Validating blockchain...",
                        "Finalizing..."
                    ]
                    
                    for i, step in enumerate(steps):
                        progress_bar.progress((i + 1) / len(steps))
                        status_text.info(f"⏳ {step}")
                        time.sleep(0.3)
                    
                    st.success("✅ Verification Complete!")
                    
                    # Verification report
                    verification_data = {
                        "Credential ID": "CRED-004",
                        "Institution": "Tech University",
                        "Student": "Sarah Williams",
                        "Degree": "BSc Computer Science",
                        "Issue Date": "2023-06-15",
                        "Blockchain Hash": generate_blockchain_hash("CRED-004"),
                    }
                    
                    st.subheader("Verification Report")
                    for key, value in verification_data.items():
                        st.write(f"**{key}**: {value}")
                    
                    st.success("Blockchain Verification: Valid")
        
        with tab2:
            credential_id = st.text_input("Enter Credential ID")
            
            if st.button("Check Status"):
                if credential_id:
                    # Sample credentials database
                    credentials = {
                        "CRED-001": {
                            "Student": "John Smith",
                            "Degree": "BSc Computer Science",
                            "Status": "Verified"
                        },
                        "CRED-002": {
                            "Student": "Emma Johnson",
                            "Degree": "PhD Physics",
                            "Status": "Verified"
                        }
                    }
                    
                    if credential_id in credentials:
                        cred = credentials[credential_id]
                        st.success(f"✅ Credential Found: {cred['Degree']}")
                        st.write(f"**Student**: {cred['Student']}")
                        st.write(f"**Status**: {cred['Status']}")
                        st.write(f"**Last Verified**: {datetime.date.today()}")
                    else:
                        st.error("❌ Credential ID not found")
                else:
                    st.warning("Please enter a Credential ID")
    
    # Institution Portal
    elif menu == "Institution Portal":
        st.header("🏫 Institution Portal")
        
        tab1, tab2 = st.tabs(["Register", "Manage Credentials"])
        
        with tab1:
            name = st.text_input("Institution Name")
            country = st.selectbox("Country", ["USA", "UK", "Canada", "Other"])
            email = st.text_input("Contact Email")
            
            if st.button("Submit Registration"):
                st.success("Registration submitted successfully!")
                st.info("Verification team will review your application")
                
                st.json({
                    "Institution ID": f"INST-{hashlib.sha256(name.encode()).hexdigest()[:6]}",
                    "Name": name,
                    "Status": "Pending"
                })
        
        with tab2:
            student_name = st.text_input("Student Name")
            degree = st.text_input("Degree Awarded")
            issue_date = st.date_input("Issue Date")
            
            if st.button("Issue Credential"):
                cred_id = f"CRED-{hashlib.sha256(student_name.encode()).hexdigest()[:6]}"
                st.success("🎓 Credential Issued!")
                st.json({
                    "Credential ID": cred_id,
                    "Student": student_name,
                    "Degree": degree,
                    "Issue Date": issue_date.strftime("%Y-%m-%d")
                })
    
    # About
    elif menu == "About":
        st.header("About AcademicVerify")
        st.write("Secure academic credential verification platform")
        
        st.subheader("Our Technology")
        col1, col2, col3 = st.columns(3)
        col1.metric("Blockchain Nodes", "24")
        col2.metric("Institutions", "127")
        col3.metric("Credentials", "18,429")
        
        st.subheader("Contact")
        st.write("📧 support@academicverify.com  \n🌐 www.academicverify.com  \n🏢 Matatiele, Ha Maloto, 4730")

# Run the app
if __name__ == "__main__":
    main()
