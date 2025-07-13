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

# Apply CSS styling directly
st.markdown("""
<style>
/* Main styling */
body {
    background-color: #f0f2f6;
    color: #333;
}
.stApp {
    background: linear-gradient(135deg, #f5f7fa 0%, #e4e7f1 100%);
}

/* Header styling */
.header {
    background: linear-gradient(135deg, #2c3e50 0%, #1a1a2e 100%);
    color: white;
    padding: 1rem;
    border-radius: 0 0 10px 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
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
    transition: all 0.3s ease;
}

.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background: linear-gradient(135deg, #2c3e50 0%, #1a1a2e 100%);
    color: white;
}

/* Progress bar */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #3498db 0%, #2ecc71 100%);
}

/* Custom tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}

.stTabs [data-baseweb="tab"] {
    background: white;
    border-radius: 8px 8px 0 0 !important;
    padding: 10px 20px;
    transition: all 0.3s ease;
}

.stTabs [aria-selected="true"] {
    background: #3498db;
    color: white;
}

/* Custom metrics */
.stMetric {
    background: white;
    border-radius: 10px;
    padding: 1rem;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# Generate blockchain-like hash for credentials
def generate_blockchain_hash(data):
    timestamp = str(datetime.datetime.now())
    data_string = str(data) + timestamp
    return hashlib.sha256(data_string.encode()).hexdigest()[:12] + "..."

# Sample data for demonstration
def generate_sample_data():
    institutions = pd.DataFrame({
        'Institution ID': ['UNIV-001', 'UNIV-002', 'UNIV-003'],
        'Name': ['Tech University', 'Science Institute', 'Global College'],
        'Country': ['USA', 'UK', 'Canada'],
        'Verification Status': ['Verified', 'Verified', 'Pending']
    })
    
    credentials = pd.DataFrame({
        'Credential ID': ['CRED-001', 'CRED-002', 'CRED-003'],
        'Student Name': ['John Smith', 'Emma Johnson', 'Michael Brown'],
        'Institution': ['Tech University', 'Science Institute', 'Global College'],
        'Degree': ['BSc Computer Science', 'PhD Physics', 'MBA'],
        'Issue Date': ['2020-06-15', '2018-12-10', '2021-05-20'],
        'Verification Status': ['Verified', 'Verified', 'Pending'],
        'Blockchain Hash': [generate_blockchain_hash("CRED-001"), 
                            generate_blockchain_hash("CRED-002"), 
                            generate_blockchain_hash("CRED-003")]
    })
    
    return institutions, credentials

# Verification status visualization
def plot_verification_status(df):
    status_counts = df['Verification Status'].value_counts()
    
    fig, ax = plt.subplots(figsize=(6, 3))
    colors = ['#2ecc71' if status == 'Verified' else '#f39c12' if status == 'Pending' else '#e74c3c' for status in status_counts.index]
    ax.barh(status_counts.index, status_counts.values, color=colors)
    ax.set_xlabel('Count')
    ax.set_title('Verification Status Distribution')
    plt.tight_layout()
    return fig

# Main application
def main():
    # Load sample data
    institutions, credentials = generate_sample_data()
    
    # Sidebar with logo and navigation
    with st.sidebar:
        st.markdown('<div class="header">', unsafe_allow_html=True)
        st.image("https://cdn-icons-png.flaticon.com/512/2232/2232688.png", width=80)
        st.title("Academic Credential Verification")
        st.subheader("Secure • Trusted • Global")
        st.markdown('</div>', unsafe_allow_html=True)
        
        menu = st.selectbox("Navigation", ["Dashboard", "Verify Credential", "Institution Portal", "Documentation", "About"])
        st.markdown("---")
        
        st.info("""
        **System Features:**
        - Blockchain-secured verification
        - Global institution database
        - Real-time status tracking
        - Fraud detection
        """)
        
        st.markdown("---")
        st.caption("© 2023 AcademicVerify Inc. All rights reserved.")
    
    # Dashboard
    if menu == "Dashboard":
        st.header("📊 Verification Dashboard")
        
        # Stats cards
        col1, col2, col3 = st.columns(3)
        col1.markdown('<div class="card"><h3>Total Credentials Verified</h3><h1>1,842</h1><p>12% increase</p></div>', unsafe_allow_html=True)
        col2.markdown('<div class="card"><h3>Active Institutions</h3><h1>127</h1><p>3 new</p></div>', unsafe_allow_html=True)
        col3.markdown('<div class="card"><h3>Verification Success Rate</h3><h1>98.7%</h1><p>0.3% improvement</p></div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Verification status charts
        col1, col2 = st.columns([2, 1])
        with col1:
            st.subheader("Recent Verification Activities")
            
            # Create sample activity data
            activities = pd.DataFrame({
                'Timestamp': pd.date_range(end=pd.Timestamp.now(), periods=10, freq='H'),
                'Activity': ['Verification started', 'Document uploaded', 'Institution verified', 
                             'Credential issued', 'Verification completed', 'New institution added',
                             'Credential updated', 'Security audit', 'Blockchain updated', 'Report generated'],
                'Status': ['In Progress', 'Completed', 'Completed', 'Completed', 'Completed',
                           'Completed', 'Completed', 'Completed', 'Completed', 'Completed']
            })
            
            st.dataframe(activities.sort_values('Timestamp', ascending=False).head(5), 
                         hide_index=True, use_container_width=True)
            
            # Verification metrics
            st.subheader("Verification Metrics")
            tab1, tab2, tab3 = st.tabs(["By Country", "By Institution", "By Degree"])
            
            with tab1:
                # Sample country data
                country_data = pd.DataFrame({
                    'Country': ['USA', 'UK', 'Canada', 'Australia', 'Germany'],
                    'Credentials': [850, 420, 320, 150, 102]
                })
                st.bar_chart(country_data.set_index('Country'))
                
            with tab2:
                # Sample institution data
                inst_data = pd.DataFrame({
                    'Institution': ['Tech University', 'Science Institute', 'Global College', 
                                    'Metropolitan University', 'Polytechnic Institute'],
                    'Credentials': [450, 380, 290, 220, 180]
                })
                st.bar_chart(inst_data.set_index('Institution'))
                
            with tab3:
                # Sample degree data
                degree_data = pd.DataFrame({
                    'Degree': ['BSc Computer Science', 'MBA', 'PhD Physics', 
                               'BA Economics', 'MEng Civil Engineering'],
                    'Credentials': [420, 380, 250, 210, 180]
                })
                st.bar_chart(degree_data.set_index('Degree'))
        
        with col2:
            st.subheader("Verification Status")
            st.pyplot(plot_verification_status(credentials))
            
            st.subheader("Security Alerts")
            st.markdown('<div class="card"><p>✅ All systems operational</p></div>', unsafe_allow_html=True)
            st.markdown('<div class="card"><p>ℹ️ 3 pending verifications</p></div>', unsafe_allow_html=True)
            st.markdown('<div class="card"><p>⚠️ 1 document requires additional review</p></div>', unsafe_allow_html=True)
            
            st.subheader("Quick Actions")
            if st.button("🔍 Start New Verification", use_container_width=True):
                st.session_state.menu = "Verify Credential"
                st.experimental_rerun()
                
            if st.button("🏫 Add New Institution", use_container_width=True):
                st.session_state.menu = "Institution Portal"
                st.experimental_rerun()
                
            if st.button("📄 Generate Report", use_container_width=True):
                st.success("Report generation in progress...")
                time.sleep(1)
                st.success("✅ Report generated successfully!")
                
    # Verify Credential
    elif menu == "Verify Credential":
        st.header("🔍 Verify Academic Credential")
        
        tab1, tab2 = st.tabs(["Verify by Document", "Verify by Credential ID"])
        
        with tab1:
            st.subheader("Upload Academic Document")
            uploaded_file = st.file_uploader("Upload PDF, JPG, or PNG of your academic credential", 
                                            type=["pdf", "jpg", "jpeg", "png"])
            
            if uploaded_file is not None:
                # Display document preview
                col1, col2 = st.columns([1, 2])
                with col1:
                    if uploaded_file.type == "application/pdf":
                        st.image("https://cdn-icons-png.flaticon.com/512/337/337946.png", width=100)
                        st.caption("PDF document uploaded")
                    else:
                        st.image(uploaded_file, width=200)
                
                # Extract metadata
                with col2:
                    file_details = {
                        "File Name": uploaded_file.name,
                        "File Type": uploaded_file.type,
                        "File Size": f"{uploaded_file.size / 1024:.2f} KB"
                    }
                    st.json(file_details)
                
                # Verification process
                st.subheader("Verification Process")
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                steps = [
                    "Uploading document...",
                    "Extracting document content...",
                    "Verifying document authenticity...",
                    "Checking against institutional records...",
                    "Validating with blockchain registry...",
                    "Finalizing verification..."
                ]
                
                for i, step in enumerate(steps):
                    progress_bar.progress((i + 1) / len(steps))
                    status_text.info(f"⏳ {step}")
                    time.sleep(0.5)
                
                # Verification result
                progress_bar.empty()
                status_text.empty()
                
                st.success("✅ Verification Complete!")
                
                # Display verification report
                with st.expander("Verification Report", expanded=True):
                    col1, col2 = st.columns(2)
                    
                    # Sample verification data
                    verification_data = {
                        "Credential ID": "CRED-004",
                        "Document Type": "Bachelor's Degree",
                        "Institution": "Tech University",
                        "Student Name": "Sarah Williams",
                        "Degree": "BSc Computer Science",
                        "Issue Date": "June 15, 2023",
                        "Verification Status": "Verified",
                        "Verification Date": datetime.date.today().strftime("%Y-%m-%d"),
                        "Blockchain Hash": generate_blockchain_hash("CRED-004"),
                        "Security Seal": "Valid"
                    }
                    
                    with col1:
                        st.subheader("Credential Details")
                        for key, value in verification_data.items():
                            st.markdown(f"**{key}**: {value}")
                    
                    with col2:
                        st.subheader("Security Validation")
                        st.image("https://cdn-icons-png.flaticon.com/512/545/545783.png", width=80)
                        st.success("Blockchain Verification: Valid")
                        st.success("Digital Signature: Valid")
                        st.success("Document Integrity: Valid")
                        
                        # Generate a sample certificate
                        certificate = f"""
                        <div style="border:2px solid #3498db; border-radius:10px; padding:20px; background:#f8f9fa;">
                            <h2 style="color:#2c3e50; text-align:center;">ACADEMIC CREDENTIAL VERIFICATION</h2>
                            <hr>
                            <p>This document certifies that the academic credential presented by <strong>{verification_data['Student Name']}</strong>
                            from <strong>{verification_data['Institution']}</strong> has been successfully verified.</p>
                            <p><strong>Degree:</strong> {verification_data['Degree']}</p>
                            <p><strong>Verification ID:</strong> {verification_data['Blockchain Hash']}</p>
                            <p><strong>Date Verified:</strong> {verification_data['Verification Date']}</p>
                            <div style="text-align:center; margin-top:20px;">
                                <img src="https://cdn-icons-png.flaticon.com/512/545/545783.png" width="80">
                            </div>
                        </div>
                        """
                        st.markdown(certificate, unsafe_allow_html=True)
                    
                    st.download_button(
                        label="📄 Download Verification Certificate",
                        data=io.BytesIO(certificate.encode()),
                        file_name="verification_certificate.html",
                        mime="text/html"
                    )
        
        with tab2:
            st.subheader("Check Verification Status")
            credential_id = st.text_input("Enter Credential ID")
            
            if st.button("Check Status", type="primary"):
                if credential_id:
                    # Simulate checking against database
                    if credential_id in credentials['Credential ID'].values:
                        result = credentials[credentials['Credential ID'] == credential_id].iloc[0]
                        
                        st.success(f"✅ Credential Found: {result['Degree']}")
                        
                        col1, col2 = st.columns(2)
                        col1.markdown(f"**Student Name**: {result['Student Name']}")
                        col1.markdown(f"**Institution**: {result['Institution']}")
                        col1.markdown(f"**Issue Date**: {result['Issue Date']}")
                        
                        col2.markdown(f"**Verification Status**: {result['Verification Status']}")
                        col2.markdown(f"**Last Verified**: {datetime.date.today().strftime('%Y-%m-%d')}")
                        col2.markdown(f"**Blockchain Hash**: `{result['Blockchain Hash']}`")
                        
                        if result['Verification Status'] == 'Verified':
                            st.balloons()
                    else:
                        st.error("❌ Credential ID not found in our system")
                else:
                    st.warning("Please enter a Credential ID")
    
    # Institution Portal
    elif menu == "Institution Portal":
        st.header("🏫 Institution Portal")
        
        tab1, tab2 = st.tabs(["Register Institution", "Manage Credentials"])
        
        with tab1:
            st.subheader("New Institution Registration")
            
            with st.form("institution_form"):
                name = st.text_input("Institution Name")
                country = st.selectbox("Country", ["USA", "UK", "Canada", "Australia", "Germany", "Other"])
                address = st.text_area("Address")
                contact_name = st.text_input("Contact Person")
                email = st.text_input("Contact Email")
                website = st.text_input("Website")
                accreditation = st.text_input("Accreditation Body")
                
                submitted = st.form_submit_button("Submit Registration")
                
                if submitted:
                    st.success("Registration submitted successfully!")
                    st.info("Our verification team will review your application within 3-5 business days")
                    
                    # Generate institution ID
                    inst_id = f"INST-{hashlib.sha256(name.encode()).hexdigest()[:6].upper()}"
                    st.subheader("Your Institution Details")
                    st.json({
                        "Institution ID": inst_id,
                        "Name": name,
                        "Country": country,
                        "Status": "Pending Verification"
                    })
        
        with tab2:
            st.subheader("Credential Management")
            st.info("Registered institutions can issue and manage academic credentials here")
            
            if st.checkbox("Show Sample Credential Form"):
                with st.form("credential_form"):
                    student_name = st.text_input("Student Full Name")
                    student_id = st.text_input("Student ID")
                    degree = st.text_input("Degree Awarded")
                    major = st.text_input("Major/Field of Study")
                    issue_date = st.date_input("Issue Date")
                    gpa = st.number_input("GPA (if applicable)", min_value=0.0, max_value=4.0, step=0.01)
                    
                    submitted = st.form_submit_button("Issue Credential")
                    
                    if submitted:
                        # Generate credential ID and blockchain hash
                        cred_id = f"CRED-{hashlib.sha256((student_name + degree).encode()).hexdigest()[:6].upper()}"
                        blockchain_hash = generate_blockchain_hash(cred_id)
                        
                        st.success("🎓 Credential Issued Successfully!")
                        st.json({
                            "Credential ID": cred_id,
                            "Student Name": student_name,
                            "Degree": degree,
                            "Issue Date": issue_date.strftime("%Y-%m-%d"),
                            "Blockchain Hash": blockchain_hash,
                            "Verification Status": "Verified"
                        })
    
    # Documentation
    elif menu == "Documentation":
        st.header("📚 Documentation")
        
        st.subheader("How the Verification System Works")
        st.markdown("""
        Our Academic Credential Verification system uses blockchain technology to ensure the authenticity and integrity of academic credentials.
        
        **Verification Process:**
        1. **Document Upload**: Institutions or students upload academic documents
        2. **Content Extraction**: Our system extracts key information from documents
        3. **Blockchain Registration**: Document hashes are recorded on a secure blockchain
        4. **Institution Verification**: We verify documents against institutional records
        5. **Result Issuance**: Verification certificates are issued with blockchain proof
        
        **Security Features:**
        - Immutable blockchain records
        - Cryptographic document hashing
        - Digital signature validation
        - Fraud detection algorithms
        """)
        
        st.subheader("For Students")
        st.markdown("""
        - Upload your academic documents for verification
        - Track verification status in real-time
        - Share verified credentials with employers or institutions
        - Download verification certificates
        """)
        
        st.subheader("For Institutions")
        st.markdown("""
        - Register to become a verified institution
        - Issue blockchain-secured academic credentials
        - Manage student records securely
        - Automate verification requests
        """)
        
        st.subheader("API Access")
        st.code("""
        # Sample API request for verification
        import requests
        
        url = "https://api.academicverify.com/v1/verify"
        payload = {
            "credential_id": "CRED-123456",
            "api_key": "YOUR_API_KEY"
        }
        
        response = requests.post(url, json=payload)
        print(response.json())
        """)
    
    # About
    elif menu == "About":
        st.header("About AcademicVerify")
        
        st.markdown("""
        **AcademicVerify** is a global platform for secure academic credential verification. 
        Our mission is to combat credential fraud and simplify the verification process for 
        educational institutions, employers, and individuals.
        """)
        
        st.subheader("Our Technology")
        col1, col2, col3 = st.columns(3)
        col1.markdown('<div class="card"><h3>Blockchain Nodes</h3><h1>24</h1><p>Globally distributed</p></div>', unsafe_allow_html=True)
        col2.markdown('<div class="card"><h3>Verified Institutions</h3><h1>127</h1><p>Across 35 countries</p></div>', unsafe_allow_html=True)
        col3.markdown('<div class="card"><h3>Credentials Verified</h3><h1>18,429</h1><p>Since 2020</p></div>', unsafe_allow_html=True)
        
        st.subheader("Security Certifications")
        st.markdown("""
        - ISO/IEC 27001:2013 Certified
        - GDPR Compliant
        - SOC 2 Type II Certified
        - Blockchain Security Verified
        """)
        
        st.subheader("Contact Us")
        st.markdown("""
        📧 Email: support@academicverify.com  
        🌐 Website: [www.academicverify.com](https://www.academicverify.com)  
        📞 Phone: +1 (800) 555-0199  
        🏢 Headquarters: San Francisco, CA  
        """)
        
        st.subheader("Join Our Network")
        st.markdown("""
        Interested in becoming a partner institution?  
        [Learn more about our institutional program](https://www.academicverify.com/institutions)
        """)

# Run the app
if __name__ == "__main__":
    main()
