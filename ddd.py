import streamlit as st

st.set_page_config(page_title='音乐播放器', page_icon='🎵')
image_ua = [
    {
        'url': 'https://music.163.com/song/media/outer/url?id=280015379.mp3',
        'image':'https://p1.music.126.net/r1AKMenByofI7Qqj3E5EqQ==/109951172091080013.jpg?param=130y130',
        'text': '火山灰'
    },
    {
        'url': 'https://music.163.com/song/media/outer/url?id=2750712929.mp3',
        'image':'https://p1.music.126.net/r1AKMenByofI7Qqj3E5EqQ==/109951172091080013.jpg?param=130y130',
        'text': '飞鸟在风暴中'
    },
    {
        'url': 'https://music.163.com/song/media/outer/url?id=2756051000.mp3',
        'image':'https://p1.music.126.net/r1AKMenByofI7Qqj3E5EqQ==/109951172091080013.jpg?param=130y130',
        'text': '银色荒原'
    }
]

st.title('🎵音乐播放器')
st.text('使用Streamlit制作的简单音乐播放器，支持切歌和基本播放控制')
if'ind'not in st.session_state:
    st.session_state['ind']=0
c1,c2=st.columns([1,2])
def lastMusic():
    st.session_state['ind'] = (st.session_state['ind']-1)%len(image_ua)
def nextMusic():
    st.session_state['ind'] = (st.session_state['ind']+1)%len(image_ua)
with c1:
    st.image(image_ua[st.session_state['ind']]['image'])
with c2:       
    st.subheader(image_ua[st.session_state['ind']]['text'])
    st.audio(image_ua[st.session_state['ind']]['url'])            
c11,c22=st.columns(2)



with c11:
    st.button('上一首',use_container_width=True,on_click=lastMusic)

with c22:
    st.button('下一首',use_container_width=True,on_click=nextMusic)



            
    
        
    
