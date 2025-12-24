import streamlit as st

# 设置页面标题
st.set_page_config(page_title="视频中心")

# 视频列表
video_arr = [
    {
        'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/37/17/34206321737/34206321737-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1766568058&trid=08ec7ba97506424181cd8c17013d3e8O&os=estghw&uipk=5&nbs=1&oi=143446004&platform=html5&mid=0&gen=playurlv3&og=hw&upsig=af01a291c7f4bd29d343c064c2fa9b51&uparams=e,deadline,trid,os,uipk,nbs,oi,platform,mid,gen,og&bvc=vod&nettype=1&bw=660455&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3',
        'title': '熊出没-第1集'
    },
    {
        'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/37/17/34206321737/34206321737-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1766568058&trid=08ec7ba97506424181cd8c17013d3e8O&os=estghw&uipk=5&nbs=1&oi=143446004&platform=html5&mid=0&gen=playurlv3&og=hw&upsig=af01a291c7f4bd29d343c064c2fa9b51&uparams=e,deadline,trid,os,uipk,nbs,oi,platform,mid,gen,og&bvc=vod&nettype=1&bw=660455&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3',
        'title': '熊出没-第2集'
    },
    {
        'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/07/35/33940373507/33940373507-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&deadline=1766568176&oi=143443039&trid=a6dbb5f5be8c4e4283bb80755d341f5O&gen=playurlv3&nbs=1&uipk=5&platform=html5&os=estghw&og=hw&upsig=0c66ee62fea42e369a7c7250b149496c&uparams=e,mid,deadline,oi,trid,gen,nbs,uipk,platform,os,og&bvc=vod&nettype=1&bw=629513&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3',
        'title': '熊出没-第3集'
    },
    {
        'url': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4',
        'title': '熊出没-第4集'
    },
    {
        'url': 'https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4',
        'title': '熊出没-第5集'
    }
]

# 初始化当前剧集索引
if 'ind' not in st.session_state:
    st.session_state.ind = 0

# 动态显示当前剧集标题
st.title(video_arr[st.session_state.ind]['title'])

# 播放当前视频
st.video(video_arr[st.session_state.ind]['url'])

# 定义切换函数
def playVideo(index):
    st.session_state.ind = index

# 创建横向按钮：使用 columns
cols = st.columns(len(video_arr))  # 创建与视频数量相同的列

for i, col in enumerate(cols):
    with col:
        st.button(
            f"第{i+1}集",
            key=f"btn_{i}",
            on_click=playVideo,
            args=(i,),
            use_container_width=True  # 让按钮填满列宽，更美观
        )
