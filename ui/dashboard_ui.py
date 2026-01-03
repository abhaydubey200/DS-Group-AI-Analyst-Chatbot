    elif page == "Deep Analysis":
        st.markdown("<h3>Deep Analysis & Root Cause 🔍</h3>", unsafe_allow_html=True)

        from ui.components.analysis_section import render_analysis_section
        from ui.components.insight_card import render_insight_card

        # Analysis sections
        col1, col2 = st.columns(2)
        with col1:
            render_analysis_section(
                "Sales Trend Analysis",
                "Understanding overall sales movement over time"
            )
        with col2:
            render_analysis_section(
                "Regional Contribution Analysis",
                "Identifying regions driving growth or decline"
            )

        col3, col4 = st.columns(2)
        with col3:
            render_analysis_section(
                "Product-wise Variance",
                "Detecting products causing revenue fluctuations"
            )
        with col4:
            render_analysis_section(
                "Customer Segment Analysis",
                "Evaluating behavior of key customer groups"
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # Insight Cards
        render_insight_card(
            "Key Insight",
            "North region contributed 42% of total sales growth in the last quarter.",
            level="info"
        )

        render_insight_card(
            "Risk Alert",
            "Top 3 products show declining sales despite overall market growth.",
            level="warning"
        )

        render_insight_card(
            "Critical Observation",
            "High dependency on a single distributor increases revenue risk.",
            level="critical"
        )
