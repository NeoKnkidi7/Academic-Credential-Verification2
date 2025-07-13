import streamlit as st
import pandas as pd
import hashlib
import datetime
import time
import io
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Academic Credential Verification",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Embedded CSS styling
st.markdown("""
<style>
/* Main styling */
.stApp {
    background: linear-gradient(135deg, #f5f7fa 0%, #e4e7f1 100%);
}

/* Card styling */
.card {
    background: white;
    border-radius: 10px;
    padding: 1.5rem;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    margin-bottom: 1rem;
    border-left: 4px solid #3498db;
}

/* Button styling */
.stButton>button {
    background: linear-gradient(135deg, #3498db 0%, #1a5d99 100%);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    font-weight: 600;
}

/* Progress bar */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #3498db 0%, #2ecc71 100%);
}
</style>
""", unsafe_allow_html=True)

# Generate blockchain-like hash
def generate_blockchain_hash(data):
    return hashlib.sha256(str(data).encode()).hexdigest()[:12] + "..."

# Main application
def main():
    # Sidebar navigation
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/2232/2232688.png", width=80)
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
        col1.markdown('<div class="card"><h3>Credentials Verified</h3><h1>1,842</h1><p>12% increase</p></div>', unsafe_allow_html=True)
        col2.markdown('<div class="card"><h3>Institutions</h3><h1>127</h1><p>3 new</p></div>', unsafe_allow_html=True)
        col3.markdown('<div class="card"><h3>Success Rate</h3><h1>98.7%</h1></div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Recent activities
        st.subheader("Recent Activities")
        activities = pd.DataFrame({
            'Timestamp': pd.date_range(end=pd.Timestamp.now(), periods=5, freq='H'),
            'Activity': ['Document uploaded', 'Institution verified', 'Verification completed', 
                         'New institution added', 'Report generated'],
            'Status': ['Completed', 'Completed', 'Completed', 'Completed', 'Completed']
        })
        st.dataframe(activities, hide_index=True, use_container_width=True)
        
        # Verification metrics
        st.subheader("Verification Metrics")
        col1, col2 = st.columns(2)
        with col1:
            country_data = pd.DataFrame({
                'Country': ['USA', 'UK', 'Canada', 'Australia'],
                'Credentials': [850, 420, 320, 150]
            })
            st.bar_chart(country_data.set_index('Country'))
        
        with col2:
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
            uploaded_file = st.file_uploader("Upload academic document", type=["pdf", "jpg", "jpeg", "png"])
            
            if uploaded_file:
                # Document preview
                if uploaded_file.type == "application/pdf":
                    st.image("https://cdn-icons-png.flaticon.com/512/337/337946.png", width=100)
                else:
                    st.image(uploaded_file, width=300)
                
                # Verification process
                st.subheader("Verification Process")
                progress_bar = st.progress(0)
                
                for i, step in enumerate([
                    "Uploading document...",
                    "Extracting content...",
                    "Verifying authenticity...",
                    "Checking records...",
                    "Validating blockchain...",
                    "Finalizing..."
                ]):
                    progress_bar.progress((i + 1) / 6)
                    st.info(f"⏳ {step}")
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
                    st.markdown(f"**{key}**: {value}")
                
                st.success("Blockchain Verification: Valid")
                
                # Certificate download
                certificate = "ACADEMIC CREDENTIAL VERIFICATION\n\n" + \
                              "\n".join([f"{k}: {v}" for k, v in verification_data.items()])
                
                st.download_button(
                    label="📄 Download Certificate",
                    data=certificate,
                    file_name="verification_certificate.txt",
                    mime="text/plain"
                )
        
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
                        st.markdown(f"**Student**: {cred['Student']}")
                        st.markdown(f"**Status**: {cred['Status']}")
                        st.markdown(f"**Last Verified**: {datetime.date.today()}")
                    else:
                        st.error("❌ Credential ID not found")
                else:
                    st.warning("Please enter a Credential ID")
    
    # Institution Portal
    elif menu == "Institution Portal":
        st.header("🏫 Institution Portal")
        
        tab1, tab2 = st.tabs(["Register", "Manage Credentials"])
        
        with tab1:
            with st.form("institution_form"):
                name = st.text_input("Institution Name")
                country = st.selectbox("Country", ["USA", "UK", "Canada", "Other"])
                email = st.text_input("Contact Email")
                
                if st.form_submit_button("Submit"):
                    st.success("Registration submitted successfully!")
                    st.info("Verification team will review your application")
                    
                    st.json({
                        "Institution ID": f"INST-{hashlib.sha256(name.encode()).hexdigest()[:6]}",
                        "Name": name,
                        "Status": "Pending"
                    })
        
        with tab2:
            with st.form("credential_form"):
                student_name = st.text_input("Student Name")
                degree = st.text_input("Degree Awarded")
                issue_date = st.date_input("Issue Date")
                
                if st.form_submit_button("Issue Credential"):
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
        st.markdown("Secure academic credential verification platform")
        
        st.subheader("Our Technology")
        col1, col2, col3 = st.columns(3)
        col1.metric("Blockchain Nodes", "24")
        col2.metric("Institutions", "127")
        col3.metric("Credentials", "18,429")
        
        st.subheader("Contact")
        st.markdown("📧 support@academicverify.com  \n🌐 www.academicverify.com  \n🏢 Matatiele, Ha Maloto, 4730")

# Run the app
if __name__ == "__main__":
    main()

