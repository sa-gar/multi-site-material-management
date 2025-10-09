import streamlit as st
import json
import datetime
import pandas as pd
import plotly.express as px
import os

# Page configuration

import json

if "multi_site_data" not in st.session_state:
    if os.path.exists("multi_site_materials.json"):
        with open("multi_site_materials.json", "r", encoding="utf-8") as f:
            st.session_state.multi_site_data = json.load(f)
    else:
        st.session_state.multi_site_data = {
            # Initial sample data
        }



def save_data():
    with open("multi_site_data.json", "w") as f:
        json.dump(st.session_state.multi_site_data, f, indent=2, default=str)

st.set_page_config(
    page_title="Zobocon Material Management System",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Beautiful CSS styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    .main {
        font-family: 'Poppins', sans-serif;
    }

    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }

    .site-header {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(245, 87, 108, 0.3);
    }

    .success-box {
        background: linear-gradient(135deg, #56c596, #27ae60);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
    }

    .error-box {
        background: linear-gradient(135deg, #e74c3c, #c0392b);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
    }

    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.3s ease;
        width: 100%;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }

    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    .stApp > header {display: none;}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'multi_site_data' not in st.session_state:
    st.session_state.multi_site_data = {
        "sites": {
            "L&T Site": {
                "location": "L&T Construction Site Location",
                "site_manager": "L&T Site Manager",
                "contact": "+91-XXXXXXXXXX",
                "project_type": "L&T Construction Project",
                "materials": {
                    "asian_fine_putty": {"stock": 40, "used": 0, "unit": "kg", "min_stock": 20, "category": "materials", "rate": 607.7, "code": "AP-PY-03"},
                    "asian_interior_primer": {"stock": 120, "used": 0, "unit": "liters", "min_stock": 50, "category": "materials", "rate": 1416, "code": "AP-PR-01"}
                },
                "tools": {
                    "putty_blade_8inch": {"stock": 48, "used": 0, "unit": "pieces", "min_stock": 10, "category": "tools", "rate": 16.225, "code": "HT-PB-08"},
                    "cutting_plier": {"stock": 1, "used": 0, "unit": "pieces", "min_stock": 2, "category": "tools", "rate": 150.0, "code": "HT-CP-001"}
                },
                "accessories": {
                    "helmet": {"stock": 6, "used": 0, "unit": "pieces", "min_stock": 10, "category": "accessories", "rate": 88.5, "code": "SA-HE-001"},
                    "safety_jacket_orange": {"stock": 4, "used": 0, "unit": "pieces", "min_stock": 8, "category": "accessories", "rate": 57.75, "code": "SA-SJ-OR"}
                }
            },
            "Karle Construction Site": {
                "location": "Karle Project Location",
                "site_manager": "Karle Site Manager", 
                "contact": "+91-YYYYYYYYY",
                "project_type": "Karle Construction Project",
                "materials": {
                    "jk_levelmaxx_putty": {"stock": 3600, "used": 0, "unit": "kg", "min_stock": 100, "category": "materials", "rate": 600.03, "code": "JK-PY-01"},
                    "dulux_interior_primer": {"stock": 297, "used": 23, "unit": "liters", "min_stock": 50, "category": "materials", "rate": 1357, "code": "DL-PR-02"}
                },
                "tools": {
                    "putty_blade_4inch": {"stock": 16, "used": 0, "unit": "pieces", "min_stock": 8, "category": "tools", "rate": 6.2894, "code": "HT-PB-04"},
                    "scaffolding": {"stock": 16, "used": 0, "unit": "sets", "min_stock": 5, "category": "tools", "rate": 5000, "code": "EQ-SC-001"}
                },
                "accessories": {
                    "fall_arrester": {"stock": 6, "used": 0, "unit": "pieces", "min_stock": 4, "category": "accessories", "rate": 1475, "code": "SA-FA-001"},
                    "safety_goggles": {"stock": 17, "used": 0, "unit": "pieces", "min_stock": 10, "category": "accessories", "rate": 37.76, "code": "SA-GO-001"}
                }
            }
        },
        "transactions": [],
        "system_info": {
            "version": "Multi-Site v4.1",
            "last_updated": str(datetime.datetime.now()),
            "total_sites": 2
        }
    }

def save_data():
    """Save data to JSON file"""
    try:
        with open("multi_site_materials.json", 'w', encoding='utf-8') as f:
            json.dump(st.session_state.multi_site_data, f, indent=2, default=str, ensure_ascii=False)
        return True
    except Exception as e:
        st.error(f"Error saving data: {e}")
        return False
        import os

if "multi_site_data" not in st.session_state:
    if os.path.exists("multi_site_data.json"):
        with open("multi_site_data.json") as f:
            st.session_state.multi_site_data = json.load(f)
    else:
        st.session_state.multi_site_data = {
            # Place your initial/sample data structure here
        }


def main():
    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>🏗️ZOBOCON MATERIAL MANAGEMENT SYSTEM 2025</h1>
        <h2>WELCOME TO ZOBOCON</h2>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar navigation
    with st.sidebar:
        st.title("🧭 Navigation")

        # Site selector
        sites = list(st.session_state.multi_site_data['sites'].keys())

        if sites:
            selected_site = st.selectbox(
                "🏢 Select Construction Site",
                [""] + sites,
                help="Choose construction site to manage"
            )
        else:
            selected_site = ""
            st.warning("No sites available. Please add a site first.")

        st.markdown("---")

        # Page navigation
        page = st.selectbox(
            "📋 Select Page",
            [
                "🏠 Multi-Site Dashboard",
                "🏢 Site Management", 
                "📦 Site Inventory",
                "➕ Add Items",
                "➖ Use Items",
                "🔄 Transfer Items",
                "📊 Reports",
                "⚙️ Settings"
            ]
        )

    # Main content area
    if page == "🏠 Multi-Site Dashboard":
        show_dashboard()
    elif page == "🏢 Site Management":
        show_site_management()
    elif page == "📦 Site Inventory":
        show_inventory(selected_site)
    elif page == "➕ Add Items":
        show_add_items(selected_site)
    elif page == "➖ Use Items":
        show_use_items(selected_site)
    elif page == "🔄 Transfer Items":
        show_transfers()
    elif page == "📊 Reports":
        show_reports(selected_site)
    elif page == "⚙️ Settings":
        show_settings()

def show_dashboard():
    """Dashboard with site overview"""
    st.header("🏠 Multi-Site Dashboard")

    sites = st.session_state.multi_site_data['sites']

    if not sites:
        st.warning("⚠️ No sites available. Please add sites in Site Management.")
        return

    # Global metrics
    col1, col2, col3, col4 = st.columns(4)

    total_sites = len(sites)
    total_items = sum(len(site['materials']) + len(site['tools']) + len(site['accessories']) 
                     for site in sites.values())

    total_stock_value = sum(
        item['stock'] * item.get('rate', 0)
        for site in sites.values()
        for category in ['materials', 'tools', 'accessories']
        for item in site[category].values()
    )

    total_low_stock = sum(
        1 for site in sites.values()
        for category in ['materials', 'tools', 'accessories']
        for item in site[category].values()
        if item['stock'] <= item['min_stock']
    )

    with col1:
        st.metric("🏢 Total Sites", total_sites)
    with col2:
        st.metric("📦 Total Items", total_items)
    with col3:
        st.metric("💰 Stock Value", f"₹{total_stock_value:,.0f}")
    with col4:
        st.metric("⚠️ Low Stock", total_low_stock)

    st.divider()

    # Site comparison table
    st.subheader("🏗️ Site Comparison")

    site_data = []
    for site_name, site_info in sites.items():
        site_items = len(site_info['materials']) + len(site_info['tools']) + len(site_info['accessories'])
        site_value = sum(
            item['stock'] * item.get('rate', 0)
            for category in ['materials', 'tools', 'accessories']
            for item in site_info[category].values()
        )

        site_data.append({
            'Site Name': site_name,
            'Location': site_info['location'],
            'Manager': site_info['site_manager'],
            'Total Items': site_items,
            'Stock Value': f"₹{site_value:,.0f}"
        })

    if site_data:
        df = pd.DataFrame(site_data)
        st.dataframe(df, use_container_width=True)

def show_site_management():
    """Site management with add/remove functionality"""
    st.header("🏢 Site Management")

    # Create tabs
    tab1, tab2, tab3 = st.tabs(["📋 View Sites", "➕ Add Site", "❌ Remove Site"])

    with tab1:
        st.subheader("📋 Current Sites")
        sites = st.session_state.multi_site_data['sites']

        if not sites:
            st.info("No sites available. Add your first site using the 'Add Site' tab.")
        else:
            for site_name, site_data in sites.items():
                with st.expander(f"🏢 {site_name}", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"**📍 Location:** {site_data['location']}")
                        st.write(f"**👨‍💼 Manager:** {site_data['site_manager']}")
                    with col2:
                        st.write(f"**📞 Contact:** {site_data['contact']}")
                        st.write(f"**🏗️ Type:** {site_data['project_type']}")

    with tab2:
        st.subheader("➕ Add New Site")

        # Add site form
        st.write("Fill in the details to add a new construction site:")

        # Create input fields
        site_name = st.text_input("🏢 Site Name *", key="new_site_name", placeholder="e.g., ABC Construction Site")
        location = st.text_input("📍 Location *", key="new_location", placeholder="e.g., Mumbai, Maharashtra")
        site_manager = st.text_input("👨‍💼 Site Manager *", key="new_manager", placeholder="e.g., John Doe")
        contact = st.text_input("📞 Contact Number *", key="new_contact", placeholder="e.g., +91-9876543210")
        project_type = st.selectbox("🏗️ Project Type *", [
            "Commercial Construction",
            "Residential Construction", 
            "Infrastructure Project",
            "Industrial Project",
            "Renovation Project",
            "Other"
        ], key="new_project_type")

        # Add site button
        if st.button("➕ Add Site", key="add_site_btn", type="primary"):
            # Validation
            if not site_name or not location or not site_manager or not contact:
                st.error("❌ Please fill in all required fields!")
            elif site_name in st.session_state.multi_site_data['sites']:
                st.error(f"❌ Site '{site_name}' already exists!")
            else:
                # Add the new site
                st.session_state.multi_site_data['sites'][site_name] = {
                    "location": location,
                    "site_manager": site_manager,
                    "contact": contact,
                    "project_type": project_type,
                    "materials": {},
                    "tools": {},
                    "accessories": {}
                }

                # Update system info
                st.session_state.multi_site_data['system_info']['total_sites'] = len(st.session_state.multi_site_data['sites'])
                st.session_state.multi_site_data['system_info']['last_updated'] = str(datetime.datetime.now())

                # Save data
                if save_data():
                    st.markdown(f'<div class="success-box">✅ Site "{site_name}" added successfully!</div>', unsafe_allow_html=True)
                    st.balloons()

                    # Clear the form by rerunning
                    st.rerun()
                else:
                    st.markdown('<div class="error-box">❌ Failed to save site data.</div>', unsafe_allow_html=True)

    with tab3:
        st.subheader("❌ Remove Site")
        sites = st.session_state.multi_site_data['sites']

        if not sites:
            st.info("No sites available to remove.")
        else:
            site_to_remove = st.selectbox("🏢 Select Site to Remove", [""] + list(sites.keys()), key="remove_site_select")

            if site_to_remove:
                st.warning(f"⚠️ Are you sure you want to remove '{site_to_remove}'?")
                st.error("⚠️ This will permanently delete all inventory data for this site!")

                if st.button(f"🗑️ Confirm Removal of '{site_to_remove}'", key="confirm_remove", type="secondary"):
                    # Remove the site
                    del st.session_state.multi_site_data['sites'][site_to_remove]

                    # Update system info
                    st.session_state.multi_site_data['system_info']['total_sites'] = len(st.session_state.multi_site_data['sites'])
                    st.session_state.multi_site_data['system_info']['last_updated'] = str(datetime.datetime.now())

                    # Save data
                    if save_data():
                        st.markdown(f'<div class="success-box">✅ Site "{site_to_remove}" removed successfully!</div>', unsafe_allow_html=True)
                        st.rerun()
                    else:
                        st.markdown('<div class="error-box">❌ Failed to save changes.</div>', unsafe_allow_html=True)

def show_inventory(selected_site):
    """Show site inventory"""
    if not selected_site:
        st.warning("⚠️ Please select a site from the sidebar")
        return

    st.markdown(f"""
    <div class="site-header">
        <h2>📦 Site Inventory: {selected_site}</h2>
    </div>
    """, unsafe_allow_html=True)

    site_data = st.session_state.multi_site_data['sites'][selected_site]

    # Show inventory summary
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Materials", len(site_data['materials']))
    with col2:
        st.metric("Tools", len(site_data['tools']))
    with col3:
        st.metric("Accessories", len(site_data['accessories']))

    st.divider()

    # Display inventory by category
    for category in ['materials', 'tools', 'accessories']:
        if site_data[category]:
            st.subheader(f"📦 {category.title()}")

            items_data = []
            for item_name, item_info in site_data[category].items():
                items_data.append({
                    'Item Name': item_name.replace('_', ' ').title(),
                    'Stock': item_info['stock'],
                    'Unit': item_info['unit'],
                    'Used': item_info['used'],
                    'Min Stock': item_info['min_stock'],
                    'Rate (₹)': f"₹{item_info.get('rate', 0):,.2f}",
                    'Value (₹)': f"₹{item_info['stock'] * item_info.get('rate', 0):,.2f}",
                    'Code': item_info.get('code', 'N/A')
                })

            if items_data:
                df = pd.DataFrame(items_data)
                st.dataframe(df, use_container_width=True)

def show_add_items(selected_site):
    """Add items interface"""
    if not selected_site:
        st.warning("⚠️ Please select a site from the sidebar")
        return

    st.markdown(f"""
    <div class="site-header">
        <h2>➕ Add Items: {selected_site}</h2>
    </div>
    """, unsafe_allow_html=True)

    # Add items form
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📦 Item Details")
        category = st.selectbox("Category *", ["materials", "tools", "accessories"], format_func=lambda x: x.title())

        site_data = st.session_state.multi_site_data['sites'][selected_site]
        existing_items = list(site_data[category].keys()) if category in site_data else []

        item_option = st.radio("Item Type", ["New Item", "Existing Item"])

        if item_option == "Existing Item" and existing_items:
            item_name = st.selectbox("Select Item", existing_items, format_func=lambda x: x.replace('_', ' ').title())
            current_stock = site_data[category][item_name]['stock']
            unit = site_data[category][item_name]['unit']
            st.info(f"Current Stock: {current_stock} {unit}")
        else:
            item_name = st.text_input("Item Name *").lower().replace(' ', '_')
            unit = st.text_input("Unit *", placeholder="pieces, kg, liters, etc.")
            min_stock = st.number_input("Minimum Stock Level *", min_value=1, value=5)
            rate = st.number_input("Rate per Unit (₹)", min_value=0.0, value=0.0, step=0.01)
            item_code = st.text_input("Item Code", placeholder="e.g., SA-HE-001")

        quantity = st.number_input("Quantity to Add *", min_value=1, value=1)

    with col2:
        st.subheader("📋 Additional Details")
        supplier = st.text_input("Supplier/Vendor")
        received_by = st.text_input("Received By *", value="Site Manager")
        invoice_number = st.text_input("Invoice Number")
        purchase_date = st.date_input("Purchase Date", value=datetime.date.today())
        notes = st.text_area("Notes")

    if st.button("➕ Add to Inventory", type="primary"):
        try:
            if item_option == "New Item":
                if item_name and unit and quantity > 0 and received_by:
                    # Add new item
                    site_data[category][item_name] = {
                        'stock': quantity,
                        'used': 0,
                        'unit': unit,
                        'min_stock': min_stock,
                        'category': category,
                        'rate': rate,
                        'code': item_code or 'N/A'
                    }
                    success_msg = f"✅ New item '{item_name.replace('_', ' ').title()}' added with {quantity} {unit}"
                else:
                    st.error("❌ Please fill all required fields for new item")
                    return
            else:
                # Add to existing item
                if item_name and quantity > 0 and received_by:
                    site_data[category][item_name]['stock'] += quantity
                    success_msg = f"✅ Added {quantity} {site_data[category][item_name]['unit']} to '{item_name.replace('_', ' ').title()}'"
                else:
                    st.error("❌ Please fill all required fields")
                    return

            # Record transaction
            transaction = {
                'date': str(datetime.datetime.now()),
                'type': 'added',
                'site': selected_site,
                'category': category,
                'item': item_name,
                'quantity': quantity,
                'supplier': supplier,
                'received_by': received_by
            }
            st.session_state.multi_site_data['transactions'].append(transaction)

            # Save data
            if save_data():
                st.markdown(f'<div class="success-box">{success_msg}</div>', unsafe_allow_html=True)
                st.info(f"New stock level: {site_data[category][item_name]['stock']} {site_data[category][item_name]['unit']}")
            else:
                st.error("❌ Failed to save data")

        except Exception as e:
            st.error(f"❌ Error adding item: {str(e)}")

def show_use_items(selected_site):
    """Use items interface"""
    if not selected_site:
        st.warning("⚠️ Please select a site from the sidebar")
        return

    st.markdown(f"""
    <div class="site-header">
        <h2>➖ Use Items: {selected_site}</h2>
    </div>
    """, unsafe_allow_html=True)

    site_data = st.session_state.multi_site_data['sites'][selected_site]

    # Use items form
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📦 Item Selection")
        category = st.selectbox("Category *", ["materials", "tools", "accessories"], format_func=lambda x: x.title())

        # Get items with stock > 0
        available_items = {name: data for name, data in site_data[category].items() if data['stock'] > 0}

        if available_items:
            item_name = st.selectbox("Select Item *", list(available_items.keys()), 
                                   format_func=lambda x: x.replace('_', ' ').title())

            current_stock = available_items[item_name]['stock']
            unit = available_items[item_name]['unit']

            st.info(f"Available: {current_stock} {unit}")
            quantity = st.number_input(f"Quantity to Use ({unit}) *", min_value=1, max_value=current_stock, value=1)
        else:
            st.warning(f"No {category} with available stock.")
            item_name = None
            quantity = 0

    with col2:
        st.subheader("🔧 Usage Details")
        work_area = st.text_input("Work Area *", placeholder="e.g., Block A - 3rd Floor")
        supervisor = st.text_input("Supervisor *", value="Site Supervisor")
        purpose = st.selectbox("Purpose *", ["Construction", "Maintenance", "Repair", "Installation", "Testing", "Other"])
        usage_date = st.date_input("Usage Date", value=datetime.date.today())
        notes = st.text_area("Usage Notes")

    if st.button("➖ Record Usage", type="primary") and available_items and item_name:
        if quantity > 0 and work_area and supervisor:
            try:
                # Update stock
                site_data[category][item_name]['stock'] -= quantity
                site_data[category][item_name]['used'] += quantity

                # Record transaction
                transaction = {
                    'date': str(datetime.datetime.now()),
                    'type': 'used',
                    'site': selected_site,
                    'category': category,
                    'item': item_name,
                    'quantity': quantity,
                    'work_area': work_area,
                    'supervisor': supervisor,
                    'purpose': purpose
                }
                st.session_state.multi_site_data['transactions'].append(transaction)

                # Save data
                if save_data():
                    remaining = site_data[category][item_name]['stock']
                    st.markdown(f'<div class="success-box">✅ Recorded usage of {quantity} {unit}</div>', unsafe_allow_html=True)
                    st.info(f"Remaining stock: {remaining} {unit}")

                    # Low stock warning
                    if remaining <= site_data[category][item_name]['min_stock']:
                        st.warning(f"⚠️ Low stock alert for {item_name.replace('_', ' ').title()}!")
                else:
                    st.error("❌ Failed to save usage data")

            except Exception as e:
                st.error(f"❌ Error recording usage: {str(e)}")
        else:
            st.error("❌ Please fill all required fields")

def show_transfers():
    """Transfer items between sites"""
    st.header("🔄 Inter-Site Transfer")

    sites = list(st.session_state.multi_site_data['sites'].keys())

    if len(sites) < 2:
        st.warning("⚠️ You need at least 2 sites to perform transfers.")
        return

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📤 Transfer From")
        from_site = st.selectbox("From Site *", sites)

        if from_site:
            from_site_data = st.session_state.multi_site_data['sites'][from_site]
            category = st.selectbox("Category *", ["materials", "tools", "accessories"], format_func=lambda x: x.title())

            available_items = {name: data for name, data in from_site_data[category].items() if data['stock'] > 0}

            if available_items:
                item_name = st.selectbox("Select Item *", list(available_items.keys()),
                                       format_func=lambda x: x.replace('_', ' ').title())

                current_stock = available_items[item_name]['stock']
                unit = available_items[item_name]['unit']
                st.info(f"Available: {current_stock} {unit}")

                quantity = st.number_input(f"Quantity to Transfer ({unit}) *", min_value=1, max_value=current_stock, value=1)
            else:
                st.warning(f"No {category} available for transfer")
                item_name = None
                quantity = 0

    with col2:
        st.subheader("📥 Transfer To")
        to_site_options = [site for site in sites if site != from_site]
        to_site = st.selectbox("To Site *", to_site_options)

        st.subheader("📋 Transfer Details")
        transfer_reason = st.selectbox("Reason *", ["Site Requirement", "Stock Balancing", "Emergency Need", "Other"])
        authorized_by = st.text_input("Authorized By *", value="Site Manager")
        driver_name = st.text_input("Driver *")
        vehicle_number = st.text_input("Vehicle Number")
        transfer_date = st.date_input("Transfer Date", value=datetime.date.today())

    if st.button("🔄 Execute Transfer", type="primary"):
        if available_items and item_name and quantity > 0 and to_site and authorized_by and driver_name:
            try:
                from_site_data = st.session_state.multi_site_data['sites'][from_site]
                to_site_data = st.session_state.multi_site_data['sites'][to_site]

                item_data = from_site_data[category][item_name].copy()

                # Update source site
                from_site_data[category][item_name]['stock'] -= quantity

                # Update destination site
                if item_name in to_site_data[category]:
                    to_site_data[category][item_name]['stock'] += quantity
                else:
                    to_site_data[category][item_name] = item_data
                    to_site_data[category][item_name]['stock'] = quantity
                    to_site_data[category][item_name]['used'] = 0

                # Record transaction
                transaction = {
                    'date': str(datetime.datetime.now()),
                    'type': 'transfer',
                    'from_site': from_site,
                    'to_site': to_site,
                    'category': category,
                    'item': item_name,
                    'quantity': quantity,
                    'authorized_by': authorized_by,
                    'driver_name': driver_name,
                    'vehicle_number': vehicle_number
                }
                st.session_state.multi_site_data['transactions'].append(transaction)

                # Save data
                if save_data():
                    st.markdown(f'<div class="success-box">✅ Successfully transferred {quantity} {item_data["unit"]} of {item_name.replace("_", " ").title()}</div>', unsafe_allow_html=True)
                    st.info(f"From {from_site}: {from_site_data[category][item_name]['stock']} {item_data['unit']} remaining")
                    st.info(f"To {to_site}: {to_site_data[category][item_name]['stock']} {item_data['unit']} total")
                else:
                    st.error("❌ Failed to save transfer data")

            except Exception as e:
                st.error(f"❌ Error executing transfer: {str(e)}")
        else:
            st.error("❌ Please fill all required fields")

def show_reports(selected_site):
    """Show reports"""
    st.header("📊 Reports & Analytics")

    if selected_site:
        st.subheader(f"📈 Reports for: {selected_site}")

        site_data = st.session_state.multi_site_data['sites'][selected_site]

        # Site summary
        col1, col2, col3 = st.columns(3)

        total_items = len(site_data['materials']) + len(site_data['tools']) + len(site_data['accessories'])
        total_value = sum(item['stock'] * item.get('rate', 0) for category in ['materials', 'tools', 'accessories'] for item in site_data[category].values())

        with col1:
            st.metric("Total Items", total_items)
        with col2:
            st.metric("Stock Value", f"₹{total_value:,.0f}")
        with col3:
            transactions = len([t for t in st.session_state.multi_site_data['transactions'] if t.get('site') == selected_site])
            st.metric("Transactions", transactions)

        # Recent transactions
        st.subheader("📋 Recent Transactions")
        site_transactions = [t for t in st.session_state.multi_site_data['transactions'] 
                           if t.get('site') == selected_site or t.get('from_site') == selected_site or t.get('to_site') == selected_site]

        if site_transactions:
            recent = sorted(site_transactions, key=lambda x: x['date'], reverse=True)[:10]
            df = pd.DataFrame([{
                'Date': t['date'][:19],
                'Type': t['type'].title(),
                'Item': t['item'].replace('_', ' ').title(),
                'Quantity': t['quantity']
            } for t in recent])
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No transactions found for this site.")
    else:
        st.warning("Please select a site to view reports.")

def show_settings():
    """System settings"""
    st.header("⚙️ System Settings")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("ℹ️ System Information")
        system_info = st.session_state.multi_site_data['system_info']

        st.info(f"""
        **Version:** {system_info.get('version', 'N/A')}
        **Total Sites:** {system_info.get('total_sites', 0)}
        **Last Updated:** {system_info.get('last_updated', 'N/A')[:19]}
        **Total Transactions:** {len(st.session_state.multi_site_data['transactions'])}
        """)

    with col2:
        st.subheader("💾 Data Management")

        if st.button("📥 Download Backup"):
            json_data = json.dumps(st.session_state.multi_site_data, indent=2, default=str)
            st.download_button(
                label="💾 Download JSON Backup",
                data=json_data,
                file_name=f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )

        if st.button("🔄 Refresh Data"):
            st.success("✅ Data refreshed!")
            st.rerun()

if __name__ == "__main__":
    main()
