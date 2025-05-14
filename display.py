import streamlit as st
import pandas as pd
import subprocess
import time
import os
import sys 

python_path = sys.executable
# st.write(f"当前运行的 Python 路径: {python_path}")
# from importlib.metadata import distributions
# packages = []
# for dist in distributions():
#     name = dist.metadata['Name']
#     version = dist.version
#     if name:
#         packages.append((name, version))

# packages.sort(key=lambda x: x[0].lower())

# for name, version in packages:
#     st.write(f"{name}=={version}")

base_dir = "company_report"
LOCK_FILE = "report_generation.lock"

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
    st.image(base_dir+"/"+st.session_state.selected_report+"/asset/screenshot.png")
    st.markdown(report[1])

def Linkedin账号():
    st.session_state.view_company = True
    st.text("本页内容采集于历史Linkedin账号信息，内容可能不准确。")
    st.markdown(report[2])

def 社交媒体():
    st.session_state.view_company = True
    st.markdown(report[3])

def 网络流量():
    st.session_state.view_company = True
    png_files = [os.path.join(traffic_folder, file) for file in os.listdir(traffic_folder) if file.endswith(".png")]
    if png_files:
        st.markdown("## 图表展示")
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
    st.markdown(report[5])

def 财务情况():
    st.session_state.view_company = True
    st.markdown(report[6])

def 市场情况():
    st.session_state.view_company = True
    st.markdown("从similar web获取的竞对信息（依据网络流量归类）请参考\"网络流量\"页面。")
    if os.path.exists(os.path.join(competitor_folder, "competitors.csv")):
        st.markdown("## 竞争对手汇总")
        st.dataframe(pd.read_csv(os.path.join(competitor_folder, "competitors.csv")))
    st.markdown(report[7])

def 招聘情况():
    st.session_state.view_company = True
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
        # ,disabled=True
        submitted = st.form_submit_button("提交")
        if submitted:
            if company_name and company_url:
                if os.path.exists(LOCK_FILE):
                    st.error("目前别的用户正在生成报告，请稍后再试")
                else:
                    with open(LOCK_FILE, "w") as f:
                        f.write("locked")
                    try:
                        with st.spinner("正在生成报告，大约需要10分钟左右，请耐心等待", show_time=True):
                            try:
                                env = os.environ.copy() 
                                env.update(st.secrets)
                                process = subprocess.Popen(
                                    [python_path, "agno_client.py", company_name, company_url],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT,
                                    text=True,
                                    bufsize=1,
                                    universal_newlines=True,
                                    env=env
                                )
                                def stream_and_print_output(stream):
                                    for line in iter(stream.readline, ''):
                                        print(line, end='')  # 输出到命令行
                                        yield line  # 输出到 Streamlit
                                    stream.close()

                                with st.expander("后台日志"):
                                    st.write_stream(stream_and_print_output(process.stdout))
                                process.wait()
                                if process.returncode != 0:
                                    st.error(f"命令执行失败，返回码: {process.returncode}")
                                else:
                                    st.success("报告生成成功！正在跳转...")
                                    time.sleep(2)
                                    st.session_state.view_company = True
                                    st.session_state.selected_report = company_name
                                    st.rerun()
                            except Exception as e:
                                st.error(f"执行命令时出错: {str(e)}")
                    except Exception as e:
                        st.error("报告生成失败，请稍后再试")
                    finally:
                        if os.path.exists(LOCK_FILE):
                            os.remove(LOCK_FILE)
            else:
                st.error("请填写完整的公司名称和URL")

def main():
    # 根据会话状态显示页面
    if not st.session_state.view_company:
        提交报告生成任务()
        # st.warning("目前生成报告还不可用，请点击左侧目录进入", icon="⚠️")
    else:
        with open(base_dir+"/"+st.session_state.selected_report+"/report.txt", "r", encoding="utf-8") as f:
            global report
            report = f.read().split("<<<>>><<<<>>><<<>>>换行标记<<<>>><<<<>>><<<>>>")
        global traffic_folder
        global competitor_folder
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
    
    
if __name__ == "__main__":
    main()