import pandas as pd
import streamlit as st

from eda2 import DEFAULT_DATA_PATH, run_graph_stress_prediction


def _apply_theme() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap');
        html, body, [class*="css"] {
            font-family: 'Space Grotesk', sans-serif;
        }
        .stApp {
            background: radial-gradient(circle at 20% 10%, #f6efe5 0%, #fffaf3 40%, #eef3ea 100%);
            color: #1d2a22;
        }
        .block-container {
            max-width: 1050px;
            padding-top: 1.5rem;
        }
        .hero {
            background: linear-gradient(120deg, #1f4037, #4f7942);
            border-radius: 16px;
            padding: 1rem 1.2rem;
            color: #f7fff6;
            margin-bottom: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _load_input(file) -> pd.DataFrame:
    if file is None:
        return pd.read_csv(DEFAULT_DATA_PATH)
    return pd.read_csv(file)


def main() -> None:
    st.set_page_config(
        page_title="Financial Stress Graph Dashboard",
        page_icon="📊",
        layout="wide",
    )
    _apply_theme()

    st.markdown(
        """
        <div class="hero">
            <h2>Financial Stress Graph Dashboard</h2>
            <p>Graph-based stress estimation using EMI, expense, and savings behavior.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    uploaded = st.sidebar.file_uploader("Upload aggregated CSV", type=["csv"])
    data = _load_input(uploaded)
    output, graph = run_graph_stress_prediction(data)

    st.sidebar.markdown(f"**Rows:** {len(output)}")
    st.sidebar.markdown(f"**Graph nodes:** {graph.number_of_nodes()}")
    st.sidebar.markdown(f"**Graph edges:** {graph.number_of_edges()}")

    stress_filter = st.multiselect(
        "Filter by stress level",
        options=sorted(output["graph_stress"].unique().tolist()),
        default=sorted(output["graph_stress"].unique().tolist()),
    )

    filtered = output[output["graph_stress"].isin(stress_filter)].copy()

    c1, c2, c3 = st.columns(3)
    c1.metric("High Stress", int((filtered["graph_stress"] == "HIGH").sum()))
    c2.metric("Medium Stress", int((filtered["graph_stress"] == "MEDIUM").sum()))
    c3.metric("Low Stress", int((filtered["graph_stress"] == "LOW").sum()))

    st.subheader("Stress Distribution")
    st.bar_chart(filtered["graph_stress"].value_counts())

    st.subheader("Customer Risk Table")
    st.dataframe(
        filtered[
            [
                "customer_id",
                "month",
                "total_income",
                "total_expense",
                "total_emi",
                "emi_ratio",
                "expense_ratio",
                "net_savings_ratio",
                "graph_stress_score",
                "graph_stress",
            ]
        ],
        use_container_width=True,
    )


if __name__ == "__main__":
    main()
