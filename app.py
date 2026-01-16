import streamlit as st
import requests
from datetime import datetime

# ========= 配置 =========
GITHUB_USER = "JerryZ8889"
REPO = "worklog"
BRANCH = "main"
RAW_BASE = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO}/{BRANCH}"

st.set_page_config(page_title="工作日志", layout="wide")
st.title("📘 工作日志")

# ========= 读取 index.md =========
index_url = f"{RAW_BASE}/index.md"
index_text = requests.get(index_url).text

# ========= 解析日志文件名 =========
log_files = []
for line in index_text.splitlines():
    if "(" in line and ".md" in line:
        fname = line.split("(")[1].split(")")[0]
        log_files.append(fname)

# ========= 侧边栏选择 =========
selected = st.sidebar.selectbox(
    "选择日期",
    sorted(log_files, reverse=True)
)

# ========= 展示正文 =========
log_url = f"{RAW_BASE}/{selected}"
log_content = requests.get(log_url).text

st.markdown(log_content)
