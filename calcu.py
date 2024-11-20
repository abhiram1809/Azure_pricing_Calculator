import streamlit as st

# Azure Pricing Data (assumed from the document)
compute_prices = {"Instance A4 (8 vCPUs, 14 GB RAM)": 537}
storage_price_per_tb = 20  # USD per terabyte
database_prices = {
    "SQL Database (2 vCPUs)": 368,
    "MySQL (2 vCPUs)": 124,
    "Redis Cache (2 vCPUs)": 153,
}
generative_ai_prices = {
    "GPT-4.0": {"input_token": 0.000005, "output_token": 0.000015},
    "GPT-4.0 Mini": {"input_token": 0.00000015, "output_token": 0.0000006},
    "Embedding Models (Large)": 0.00000013,
    "Embedding Models (Small)": 0.00000002,
}
hours_per_month = 730  # Assumed constant

# Streamlit App
st.title("Azure Pricing Calculator")

st.sidebar.header("Customize Your Configuration")

# Compute Services
st.sidebar.subheader("Compute Services")
selected_compute = st.sidebar.selectbox("Select Compute Instance", list(compute_prices.keys()))
num_instances = st.sidebar.number_input("Number of Instances", min_value=0, value=1, step=1)

# Storage Services
st.sidebar.subheader("Storage Services")
storage_size_tb = st.sidebar.number_input("Storage Size (TB)", min_value=0.0, value=1.0, step=0.1)

# Database Services
st.sidebar.subheader("Database Services")
selected_database = st.sidebar.selectbox("Select Database Type", list(database_prices.keys()))
num_databases = st.sidebar.number_input("Number of Databases", min_value=0, value=1, step=1)

# Generative AI Services
st.sidebar.subheader("Generative AI Models")
selected_model = st.sidebar.selectbox("Select AI Model", list(generative_ai_prices.keys()))
input_tokens = st.sidebar.number_input("Number of Input Tokens", min_value=0, value=1000000, step=1000)
output_tokens = st.sidebar.number_input("Number of Output Tokens", min_value=0, value=1000000, step=1000)

# Cost Calculations
compute_cost = compute_prices[selected_compute] * num_instances
storage_cost = storage_size_tb * storage_price_per_tb
database_cost = database_prices[selected_database] * num_databases

if "GPT-4.0" in selected_model or "GPT-4.0 Mini" in selected_model:
    ai_cost = (
        input_tokens * generative_ai_prices[selected_model]["input_token"]
        + output_tokens * generative_ai_prices[selected_model]["output_token"]
    )
else:
    ai_cost = input_tokens * generative_ai_prices[selected_model]

total_cost = compute_cost + storage_cost + database_cost + ai_cost

# Display Results
st.header("Cost Breakdown")
st.write(f"**Compute Cost:** ${compute_cost:.2f}")
st.write(f"**Storage Cost:** ${storage_cost:.2f}")
st.write(f"**Database Cost:** ${database_cost:.2f}")
st.write(f"**Generative AI Cost:** ${ai_cost:.2f}")

st.subheader("Total Monthly Cost")
st.write(f"**Total:** ${total_cost:.2f}")

st.write("---")
st.write("Adjust configurations in the sidebar to calculate costs for different setups.")