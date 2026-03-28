import streamlit as st
import os
from core.contract_engine import analyze_contract_v50000

# --- CONFIG ---
st.set_page_config(page_title="TEXO Contract Pentagon", page_icon="⚖️", layout="wide")

# --- STYLE PREMIUM ---
st.markdown("""
<style>
    .stApp { background-color: #0A1931 !important; color: #ffffff !important; }
    h1, h2, h3, h4, h5, h6, p, span, div, li, label, .stMarkdown { color: #ffffff !important; }
    .main-header { color: #FFD700 !important; font-weight: 800; font-size: 32px; text-align: center; border-bottom: 2px solid #FFD700; padding-bottom: 10px; margin-bottom: 20px; }
    .stButton>button { background: #152A4A !important; color: #FFD700 !important; border: 1px solid #FFD700 !important; border-radius: 12px; font-weight: bold; height: 3.5em; width: 100%; }
    .stButton>button:hover { background: #FFD700 !important; color: #0A1931 !important; transform: scale(1.02); transition: 0.2s; }
    .report-card { padding: 20px; border-radius: 12px; border: 1px solid rgba(255, 215, 0, 0.3); background-color: rgba(25, 42, 74, 0.6) !important; margin-bottom: 15px; }
    .pillar-tag { color: #FFD700 !important; font-weight: 900; border-left: 6px solid #FFD700; padding-left: 15px; }
    .ai-decode-box { background: rgba(33, 150, 243, 0.1); padding: 10px; border-radius: 8px; border-left: 4px solid #2196f3; }
    .expert-advice-box { background: rgba(255, 152, 0, 0.1); padding: 10px; border-radius: 8px; border-left: 4px solid #ff9800; margin-top: 5px; }
    .footer { text-align: center; color: #888; font-size: 12px; margin-top: 50px; }
</style>
""", unsafe_allow_html=True)

# --- AUTH ---
def check_password():
    if "authenticated" not in st.session_state: st.session_state.authenticated = False
    if st.session_state.authenticated: return True
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h2 style='text-align: center; color: #FFD700;'>🏦 PENTAGON AUDIT CENTER</h2>", unsafe_allow_html=True)
        pwd = st.text_input("Mật khẩu truy cập Stealth:", type="password")
        if st.button("KÍCH HOẠT HỆ THỐNG"):
            if pwd == "texo2026":
                st.session_state.authenticated = True
                st.rerun()
            else: st.error("❌ Truy cập không hợp lệ.")
    return False

if not check_password(): st.stop()

# --- MAIN ---
st.markdown("<div class='main-header'>🏛️ AI CONTRACT AUDIT (PENTAGON V5.0)</div>", unsafe_allow_html=True)

f_contract = st.file_uploader("Chi tiết hồ sơ đối soát (.docx)", type=["docx"])

if f_contract and st.button("🚀 RA LỆNH PHÂN TÍCH MA TRẬN"):
    with st.spinner("AI Pentagon đang giải mã đa tầng..."):
        try:
            ta = f"t_{f_contract.name}"
            with open(ta, "wb") as f:
                f.write(f_contract.getbuffer())
            
            res = analyze_contract_v50000(ta)
            
            st.success("🎉 Ma trận Pentagon V5.0 giải mã hoàn tất.")
            st.balloons()
            
            # Overview Metrics
            ds = res["dossier"]
            c1, c2, c3 = st.columns(3)
            c1.metric("💰 Tổng Giá trị", ds["total"])
            c2.metric("⌚ Thời hạn", ds["duration"])
            c3.metric("🧾 Thuế VAT", ds["vat"])
            
            c4, c5, c6 = st.columns(3)
            c4.metric("👥 Nhân sự", f"{ds['exp_count']} người")
            c5.metric("👨‍💻 Thù lao", ds["exp_cost"])
            c6.metric("📦 Khác", ds["other"])
            
            st.markdown("---")
            st.markdown("### 🔍 Phân tích 5 Trụ cột Ma trận")
            
            mp = {
                "⚖️ PHÁP LÝ": "⚖️ PHÁP LÝ", 
                "💸 TÀI CHÍNH": "💸 TÀI CHÍNH", 
                "🛠️ KỸ THUẬT": "🛠️ KỸ THUẬT", 
                "👥 NHÂN SỰ": "👥 NHÂN SỰ", 
                "📅 TIẾN ĐỘ": "📅 TIẾN ĐỘ"
            }
            
            for label, key in mp.items():
                data_p = [item for item in res["detailed_audit"] if item["Nhóm"] == key]
                with st.expander(f"{label} ({len(data_p)} vấn đề)", expanded=True):
                    if data_p:
                        for item in data_p:
                            with st.container():
                                st.markdown(f"<div class='report-card'><div class='pillar-tag'>{item['Hạng mục']} | {item['Trạng thái']}</div>", unsafe_allow_html=True)
                                st.markdown(f"**📖 Trích dẫn:** *{item['Trích dẫn nguyên văn (Evidence)']}*")
                                st.markdown(f"<div class='ai-decode-box'>🤖 <b>AI Giải mã:</b> {item['AI Giải mã nội dung (Description)']}</div>", unsafe_allow_html=True)
                                st.markdown(f"<div class='expert-advice-box'>💡 <b>Khuyên dùng:</b> {item['Khuyến nghị của AI (Advice)']}</div>", unsafe_allow_html=True)
                                st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.write("✅ Đảm bảo an toàn chuyên môn.")
                        
            if os.path.exists(ta): os.remove(ta)
        except Exception as e:
            st.error(f"❌ Lỗi ma trận: {e}")

st.markdown("<div class='footer'>TEXO Engineering Department | Pentagon Intelligence System | Hoàng Đức Vũ</div>", unsafe_allow_html=True)
