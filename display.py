import streamlit as st
import pandas as pd
import os

with open("report.txt", "r") as f:
    report = f.read().split("<<<>>><<<<>>><<<>>>换行标记<<<>>><<<<>>><<<>>>")
    
    
traffic_folder = "asset/traffic"
competitor_folder = "asset/competitor"


def 公司介绍():
    # st.markdown("# 公司介绍")
    st.image("asset/screenshot.png")
    st.markdown(report[1])
    
def Linkedin账号():
    # st.markdown("# Linkedin账号")
    st.markdown(report[2])
    
def 社交媒体():
    # st.markdown("# 社交媒体情况")
    st.markdown(report[3])
    
def 网络流量():
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
    # st.markdown("# 近期新闻")
    st.markdown(report[5])

def 财务情况():
    # st.markdown("# 财务情况")
    st.markdown(report[6])
def 市场情况():
    # st.markdown("# 市场情况")
    if os.path.exists(os.path.join(competitor_folder, "competitors.csv")):
        st.markdown("## 竞争对手汇总")
        st.dataframe(pd.read_csv(os.path.join(competitor_folder, "competitors.csv")))
    st.markdown(report[7])
def 招聘情况():
    # st.markdown("# 招聘情况")
    st.markdown(report[8])
    
pg = st.navigation({report[0]:[公司介绍,Linkedin账号,社交媒体,网络流量,近期新闻,财务情况,市场情况,招聘情况]})
pg.run()