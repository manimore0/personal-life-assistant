import streamlit as st

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="JARVIS Life Assistant",
    page_icon="🤖",
    layout="wide",
)

# ==================================================
# THEME STATE
# ==================================================
if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = True

# ==================================================
# TOP RIGHT TOGGLE
# ==================================================
left_spacer, right_toggle = st.columns([8, 1])

with right_toggle:
    st.session_state["dark_mode"] = st.toggle(
        "🌙 Dark Mode",
        value=st.session_state["dark_mode"],
    )

dark = st.session_state["dark_mode"]

# ==================================================
# COLORS
# ==================================================
if dark:
    BG = "#05070D"
    BG2 = "#0B0F1A"
    TEXT = "#FFFFFF"
    SUBTEXT = "#CBD5E1"
    PRIMARY = "#FF2D2D"
    SECONDARY = "#FFD700"
else:
    BG = "#F8FAFC"
    BG2 = "#FFFFFF"
    TEXT = "#111827"
    SUBTEXT = "#6B7280"
    PRIMARY = "#C1121F"
    SECONDARY = "#D4AF37"

# ==================================================
# CSS
# ==================================================
st.markdown(
    f"""
    <style>
    .stApp {{
        background:
            radial-gradient(circle at 50% 18%, {PRIMARY}22, transparent 25%),
            radial-gradient(circle at 50% 18%, {SECONDARY}22, transparent 40%),
            linear-gradient(135deg, {BG} 0%, {BG2} 100%);
        color: {TEXT};
    }}

    h1, h2, h3, p, div, span {{
        color: {TEXT} !important;
    }}

    .main-container {{
        text-align: center;
        padding-top: 2rem;
    }}

    /* ==========================================
       ENERGY ORB
       ========================================== */
    .energy-orb {{
        width: 340px;
        height: 340px;
        margin: 0 auto;
        position: relative;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
    }}

    /* OUTER AURA */
    .energy-orb::before {{
        content: "";
        position: absolute;
        inset: -45px;
        border-radius: 50%;
        background:
            radial-gradient(
                circle,
                rgba(255,255,255,0.10) 0%,
                rgba(0,255,255,0.18) 25%,
                rgba(255,45,45,0.14) 45%,
                rgba(255,215,0,0.10) 60%,
                transparent 75%
            );
        filter: blur(22px);
        animation: aura-pulse 4s ease-in-out infinite;
    }}

    /* MAIN REACTOR */
    .arc-reactor {{
        width: 300px;
        height: 300px;
        border-radius: 50%;
        position: relative;

        background:
            /* White-hot core */
            radial-gradient(circle at center,
                rgba(255,255,255,1) 0%,
                rgba(255,255,255,0.95) 5%,
                rgba(0,255,255,0.9) 8%,
                rgba(0,255,255,0.18) 14%,
                transparent 18%
            ),

            /* Cyan plasma ring */
            radial-gradient(circle at center,
                transparent 0%,
                transparent 18%,
                rgba(0,255,255,0.95) 19%,
                rgba(0,255,255,0.15) 24%,
                transparent 25%
            ),

            /* Gold ring */
            radial-gradient(circle at center,
                transparent 0%,
                transparent 30%,
                rgba(255,215,0,0.95) 31%,
                rgba(255,215,0,0.15) 35%,
                transparent 36%
            ),

            /* Red ring */
            radial-gradient(circle at center,
                transparent 0%,
                transparent 42%,
                rgba(255,45,45,0.95) 43%,
                rgba(255,45,45,0.15) 47%,
                transparent 48%
            );

        border: 4px solid rgba(255,215,0,0.35);

        box-shadow:
            0 0 35px rgba(0,255,255,0.85),
            0 0 90px rgba(255,45,45,0.65),
            0 0 160px rgba(255,215,0,0.45),
            inset 0 0 40px rgba(255,255,255,0.30);

        animation: reactor-pulse 3s ease-in-out infinite;
    }}

    /* OUTER SEGMENTED RING */
    .arc-reactor::before {{
        content: "";
        position: absolute;
        inset: -14px;
        border-radius: 50%;

        background:
            repeating-conic-gradient(
                from 0deg,
                rgba(255,215,0,0.95) 0deg 8deg,
                transparent 8deg 18deg,
                rgba(255,45,45,0.85) 18deg 24deg,
                transparent 24deg 36deg
            );

        -webkit-mask:
            radial-gradient(
                circle,
                transparent 0 78%,
                white 79% 88%,
                transparent 89%
            );
        mask:
            radial-gradient(
                circle,
                transparent 0 78%,
                white 79% 88%,
                transparent 89%
            );

        animation: rotate-clockwise 12s linear infinite;
        filter: drop-shadow(0 0 12px rgba(255,215,0,0.55));
    }}

    /* INNER TECH RING */
    .arc-reactor::after {{
        content: "";
        position: absolute;
        inset: 34px;
        border-radius: 50%;

        background:
            repeating-conic-gradient(
                from 180deg,
                rgba(0,255,255,0.95) 0deg 6deg,
                transparent 6deg 15deg,
                rgba(255,255,255,0.9) 15deg 18deg,
                transparent 18deg 30deg
            );

        -webkit-mask:
            radial-gradient(
                circle,
                transparent 0 62%,
                white 63% 74%,
                transparent 75%
            );
        mask:
            radial-gradient(
                circle,
                transparent 0 62%,
                white 63% 74%,
                transparent 75%
            );

        animation: rotate-counter 8s linear infinite;
        filter: drop-shadow(0 0 8px rgba(0,255,255,0.7));
    }}

    .jarvis-title {{
        font-size: 5rem;
        font-weight: 900;
        letter-spacing: -2px;
        margin-top: 2rem;
        margin-bottom: 0.5rem;
        background: linear-gradient(90deg, {PRIMARY}, {SECONDARY});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    .jarvis-subtitle {{
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }}

    .jarvis-description {{
        font-size: 1.15rem;
        color: {SUBTEXT} !important;
    }}

    /* ANIMATIONS */
    @keyframes reactor-pulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.05); }}
    }}

    @keyframes aura-pulse {{
        0%, 100% {{
            transform: scale(1);
            opacity: 0.85;
        }}
        50% {{
            transform: scale(1.10);
            opacity: 1;
        }}
    }}

    @keyframes rotate-clockwise {{
        from {{ transform: rotate(0deg); }}
        to   {{ transform: rotate(360deg); }}
    }}

    @keyframes rotate-counter {{
        from {{ transform: rotate(360deg); }}
        to   {{ transform: rotate(0deg); }}
    }}

    @media (max-width: 768px) {{
        .jarvis-title {{
            font-size: 3.2rem;
        }}

        .jarvis-subtitle {{
            font-size: 1.2rem;
        }}

        .energy-orb {{
            width: 260px;
            height: 260px;
        }}

        .arc-reactor {{
            width: 220px;
            height: 220px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ==================================================
# MAIN CONTENT
# ==================================================
# Replace ONLY the MAIN CONTENT section at the bottom of your file
# with this code.

st.html(
    """
    <div class="main-container">
        <div class="energy-orb">
            <div class="arc-reactor"></div>
        </div>

        <div class="jarvis-title">God's Fav Child</div>

        <div class="jarvis-subtitle">
            PERSONAL LIFE OPERATING SYSTEM
        </div>

        <div class="jarvis-description">
            Designed to organize your goals, reminders, habits,
            and daily execution.
        </div>
    </div>
    """
)
# ==================================================
# IMPORT BACKEND FUNCTIONS
# ==================================================
from db import (
    initialize_db,
    add_reminder,
    get_all_reminders,
    update_reminder_title,
    delete_reminder,
    mark_reminder_done,
)

# Initialize database
initialize_db()

# ==================================================
# SIDEBAR - REMINDER ACTIONS
# ==================================================
with st.sidebar:
    st.markdown("## 📋 Reminder Actions")

    # Add Reminder
    with st.expander("➕ Add Reminder"):
        new_title = st.text_input(
            "Title",
            key="sidebar_new_title",
        )
        new_description = st.text_area(
            "Description",
            key="sidebar_new_description",
        )

        if st.button("Add", key="sidebar_add_btn"):
            if new_title.strip():
                add_reminder(
                    new_title,
                    new_description if new_description else None,
                    None,
                )
                st.success("Reminder added.")
                st.rerun()
            else:
                st.warning("Enter a title.")

    # Edit Reminder
    reminders_for_edit = get_all_reminders()

    if reminders_for_edit:
        with st.expander("✏️ Edit Reminder"):
            reminder_options = {
                f"{r[0]} - {r[1]}": r[0]
                for r in reminders_for_edit
            }

            selected_label = st.selectbox(
                "Select Reminder",
                list(reminder_options.keys()),
                key="edit_select",
            )

            selected_id = reminder_options[selected_label]

            current_title = next(
                r[1]
                for r in reminders_for_edit
                if r[0] == selected_id
            )

            edited_title = st.text_input(
                "New Title",
                value=current_title,
                key="edited_title",
            )

            if st.button("Save Changes", key="save_edit_btn"):
                update_reminder_title(
                    selected_id,
                    edited_title,
                )
                st.success("Reminder updated.")
                st.rerun()

        # Delete Reminder
        with st.expander("🗑 Delete Reminder"):
            delete_label = st.selectbox(
                "Select Reminder to Delete",
                list(reminder_options.keys()),
                key="delete_select",
            )

            delete_id = reminder_options[delete_label]

            if st.button("Delete", key="delete_btn"):
                delete_reminder(delete_id)
                st.success("Reminder deleted.")
                st.rerun()

        # Mark Done
        with st.expander("✅ Mark as Done"):
            done_label = st.selectbox(
                "Select Reminder",
                list(reminder_options.keys()),
                key="done_select",
            )

            done_id = reminder_options[done_label]

            if st.button("Mark Done", key="done_btn"):
                mark_reminder_done(done_id)
                st.success("Reminder marked as done.")
                st.rerun()

# ==================================================
# MAIN AREA - REMINDER TABLE
# ==================================================
st.markdown("---")
st.subheader("📋 My Reminders")

reminders = get_all_reminders()

if reminders:
    table_data = []

    for reminder in reminders:
        table_data.append(
            {
                "ID": reminder[0],
                "Title": reminder[1],
                "Description": (
                    reminder[2]
                    if len(reminder) > 2 and reminder[2]
                    else ""
                ),
                "Due Date": (
                    reminder[3]
                    if len(reminder) > 3 and reminder[3]
                    else ""
                ),
                "Status": (
                    reminder[4]
                    if len(reminder) > 4
                    else "pending"
                ),
            }
        )

    st.dataframe(
        table_data,
        use_container_width=True,
        hide_index=True,
    )
else:
    st.info("No reminders found.")

# ==================================================
# JARVIS CHAT BAR
# ==================================================
st.markdown("---")
st.subheader("🎙️ JARVIS Command Bar")

command = st.chat_input(
    "Type a command... e.g. remind me to call mom tomorrow"
)

if command:
    import re

    # Split input into multiple reminders using:
    # new lines, semicolons, or commas
    parts = re.split(r"[\n;,]+", command)

    reminders_to_add = [
        part.strip()
        for part in parts
        if part.strip()
    ]

    if reminders_to_add:
        for reminder_text in reminders_to_add:
            add_reminder(
                reminder_text,
                None,
                None,
            )

        if len(reminders_to_add) == 1:
            st.success(
                f"Added 1 reminder: {reminders_to_add[0]}"
            )
        else:
            st.success(
                f"Added {len(reminders_to_add)} reminders successfully."
            )

        st.rerun()
    else:
        st.warning("No valid reminders found.")