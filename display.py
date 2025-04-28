import streamlit as st
import pandas as pd
import os

base_dir = "company_report"

report = None
traffic_folder = None
competitor_folder = None

# 初始化会话状态
if 'view_company' not in st.session_state:
    st.session_state.view_company = False
    
if 'selected_report' not in st.session_state:
    st.session_state.selected_report = None

def 公司介绍():
    st.session_state.view_company = True
    # st.markdown("# 公司介绍")
    st.image(base_dir+"/"+st.session_state.selected_report+"/asset/screenshot.png")
    st.markdown(report[1])

def Linkedin账号():
    st.session_state.view_company = True
    # st.markdown("# Linkedin账号")
    st.markdown(report[2])

def 社交媒体():
    st.session_state.view_company = True
    # st.markdown("# 社交媒体情况")
    st.markdown(report[3])

def 网络流量():
    st.session_state.view_company = True
    # st.markdown("# 网站流量")
    st.markdown("## 图表展示")
    png_files = [os.path.join(traffic_folder, file) for file in os.listdir(traffic_folder) if file.endswith(".png")]
    for i in range(0, len(png_files), 2):
        col1, col2 = st.columns(2)
        with col1:
            if i < len(png_files):
                st.image(png_files[i])
        with col2:
            if i + 1 < len(png_files):
                st.image(png_files[i + 1])
    st.markdown(report[4])

def 近期新闻():
    st.session_state.view_company = True
    # st.markdown("# 近期新闻")
    st.markdown(report[5])

def 财务情况():
    st.session_state.view_company = True
    # st.markdown("# 财务情况")
    st.markdown(report[6])

def 市场情况():
    st.session_state.view_company = True
    st.markdown("从similar web获取的竞对信息（依据网络流量归类）请参考\"网络流量\"页面。")
    # st.markdown("# 市场情况")
    if os.path.exists(os.path.join(competitor_folder, "competitors.csv")):
        st.markdown("## 竞争对手汇总")
        st.dataframe(pd.read_csv(os.path.join(competitor_folder, "competitors.csv")))
    st.markdown(report[7])

def 招聘情况():
    st.session_state.view_company = True
    # st.markdown("# 招聘情况")
    st.markdown(report[8])

# 表单函数
def 提交报告生成任务():
    st.title("GaorongVC Company Researcher")
    with st.sidebar:
        st.title("历史报告列表")
        if os.path.exists(base_dir):
            # TODO 重复的文件夹名称
            for report_folder in os.listdir(base_dir):
                folder_path = os.path.join(base_dir, report_folder)
                if os.path.isdir(folder_path):
                    if st.button(report_folder, key=report_folder):
                        st.session_state.view_company = True
                        st.session_state.selected_report = report_folder
                        st.rerun()


    with st.form("report_form"):
        company_name = st.text_input("公司名称")
        company_url = st.text_input("公司URL")
        submitted = st.form_submit_button("提交",disabled=True)
        if submitted:
            if company_name and company_url or True:
                with st.spinner("正在生成报告，大约需要10分钟左右，请耐心等待", show_time=True):
                    import time
                    time.sleep(5)
                st.session_state.view_company = True
                st.rerun()
            else:
                st.error("请填写完整的公司名称和URL")

# 根据会话状态显示页面
if not st.session_state.view_company:
    提交报告生成任务()
    st.warning("目前生成报告还不可用，请点击左侧目录进入", icon="⚠️")
else:
    with open(base_dir+"/"+st.session_state.selected_report+"/report.txt", "r", encoding="utf-8") as f:
        report = f.read().split("<<<>>><<<<>>><<<>>>换行标记<<<>>><<<<>>><<<>>>")
    traffic_folder = base_dir+"/"+st.session_state.selected_report+"/asset/traffic"
    competitor_folder = base_dir+"/"+st.session_state.selected_report+"/asset/competitor"
    pg = st.navigation({report[0]:[公司介绍,Linkedin账号,社交媒体,网络流量,近期新闻,财务情况,市场情况,招聘情况]})
    pg.run()
    st.markdown(
        """
        <style>
        /* 隐藏中间的标记和样式注入 */
        .element-container:has(style){
            display: none;
        }
        #floating-btn-anchor {
            display: none;
        }
        .element-container:has(#floating-btn-anchor) {
            display: none;
        }

        /* 修改紧跟在标记之后的 button 样式 */
        .element-container:has(#floating-btn-anchor) + div button {
            position: fixed;
            bottom: 50px;
            right: 50px;
            z-index: 9999;
            background-color: rgb(221, 41, 96);
            color: white;
            border: none;
            border-radius: 50px;
            padding: 12px 25px;
            font-size: 16px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown('<span id="floating-btn-anchor"></span>', unsafe_allow_html=True)
    back_btn = st.button("返回报告列表")
    if back_btn:
        if "view_company" in st.session_state:
            st.session_state["view_company"] = False
        pg = st.navigation([提交报告生成任务])
        pg.run()
        st.rerun()
    