import streamlit as st
st.set_page_config(page_title="相册网站", page_icon="🐾")

image_ua = [
    {
        'url': 'https://tse1-mm.cn.bing.net/th/id/OIP-C.XrioiabkHAO8ejwBxQ0VFwHaE7?w=268&h=180&c=7&r=0&o=7&cb=ucfimg2&pid=1.7&rm=3&ucfimg=1',
        'text': '海马'
    },
    {
        'url': 'https://tse1-mm.cn.bing.net/th/id/OIP-C.WmnveGScAUpPLtEjBaILjwAAAA?w=293&h=195&c=7&r=0&o=7&cb=ucfimg2&pid=1.7&rm=3&ucfimg=1',
        'text': '海狮'
    },
    {
        'url': 'https://tse3-mm.cn.bing.net/th/id/OIP-C.u_fS7nS5RRGI2xYoUV-6nQHaEo?w=314&h=195&c=7&r=0&o=7&cb=ucfimg2&pid=1.7&rm=3&ucfimg=1',
        'text': '大象'
    }
]

# 将当前的索引存储到内存中，如果内存中没有ind，我才要设0，如果有就不设置ind
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 用三列布局实现图片居中（左右列留白，中间列放图片）
cols = st.columns([1, 2, 1])  # 左右列宽度1，中间列宽度2，可根据需求调整比例
with cols[1]:
    st.image(image_ua[st.session_state['ind']]['url'], caption=image_ua[st.session_state['ind']]['text'])

# 课本P73 分列容器
c1, c2 = st.columns(2)

def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(image_ua)

with c1:
    # 课本P22 按钮
    st.button('上一张', use_container_width=True)
with c2:
    st.button('下一张', use_container_width=True, on_click=nextImg)
