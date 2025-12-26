import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image
import io
import os

# ---------------------- 全局配置（唯一）----------------------
st.set_page_config(
    page_title="多功能综合网站",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------- 侧边栏导航（按要求修改）----------------------
st.sidebar.markdown("<div style='color: #2980b9; font-size: 1.5rem; font-weight: bold;'>🌐 功能导航</div>", unsafe_allow_html=True)
st.sidebar.markdown("---")

# 用radio直接展开所有功能模块（替换原selectbox，无需收起）
nav_option = st.sidebar.radio(
    "",  # 去除多余标题，保持简洁
    [
        "🏫 学校介绍",
        "🍜 南宁美食仪表盘",
        "🖼️ 图片相册",
        "🎵 音乐播放器",
        "🎬 视频中心",
        "📝 个人简历生成器"
    ]
)

st.sidebar.markdown("---")

# ---------------------- 主页面内容 ----------------------
if nav_option == "🏫 学校介绍":
    st.title("🏫 学校介绍")
    st.markdown("---")
    
    # 添加指定图片地址（按要求设置）
    school_img_url = "https://tse1-mm.cn.bing.net/th/id/OIP-C.oCw_uQR9NQaU2F8p5eFZbAHaEK?w=287&h=180&c=7&r=0&o=5&pid=1.7"
    st.image(school_img_url, caption="学校风貌", width=800)
    
    st.markdown("---")
    st.subheader("学校概况")
    st.write("""
    广西职业学院（广西经济管理学院）坐落于广西南宁市，是由自治区人民政府举办、自治区教育厅主管的公办全日制本科学校，
    致力于培养区域社会发展所需要的应用型、技术技能型人才。
    
    学校源于1951年创办的广西人民革命大学，历经广西行政干部学校、广西经济干部学校等发展阶段，
    2019年正式设置为本科层次职业学校，在不同历史时期始终围绕广西经济建设主线，坚守办学初心，
    为广西建设和社会发展作出了突出贡献，享有良好的办学声誉和广泛的社会影响。
    """)
    
    st.subheader("核心优势")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 学科齐全")
        st.markdown("- 8大学科门类")
        st.markdown("- 38个本科专业")
        st.markdown("- 多个省级特色专业")
    with col2:
        st.markdown("### 师资雄厚")
        st.markdown("- 博士硕士教师400+人")
        st.markdown("- 省级教学团队3个")
        st.markdown("- 双师型教师占比超60%")
    with col3:
        st.markdown("### 就业优质")
        st.markdown("- 毕业生就业率95%以上")
        st.markdown("- 校企合作单位200+家")
        st.markdown("- 全区就业工作先进单位")

elif nav_option == "🍜 南宁美食仪表盘":
    # 完全保留bbb.py原始代码
    st.title("南宁美食数据仪表盘")
    # 1. 南宁美食店铺分布（map，文字横向）
    st.subheader("南宁美食店铺分布")
    df_shops = pd.DataFrame({
        "店铺名称": ["复记老友粉", "舒记老友粉", "爱民螺蛳粉", "万国酒家", "粉之都"],
        "评分": [4.8, 4.7, 4.6, 4.9, 4.5],
        "lat": [22.82, 22.81, 22.80, 22.82, 22.79],
        "lon": [108.37, 108.36, 108.35, 108.38, 108.34]
    })
    st.map(df_shops)
    # 2. 店铺评分柱状图（bar_chart，文字横向）
    st.subheader("南宁美食店铺评分")
    df_bar = df_shops[["店铺名称", "评分"]].set_index("店铺名称")
    st.bar_chart(df_bar)
    # 3. 5家餐厅12个月价格走势（Altair图表，名称完整显示）
    st.subheader("5家餐厅招牌菜12个月价格走势")
    df_price_trend = pd.DataFrame({
        "月份": ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"],
        "复记老友粉（老友粉）": [12, 12, 13, 13, 14, 14, 15, 15, 14, 14, 13, 13],
        "舒记老友粉（老友粉）": [11, 12, 12, 13, 13, 14, 14, 15, 14, 14, 13, 12],
        "爱民螺蛳粉（螺蛳粉）": [10, 10, 11, 11, 12, 12, 13, 13, 12, 12, 11, 11],
        "万国酒家（柠檬鸭）": [45, 46, 45, 47, 48, 48, 49, 50, 49, 48, 47, 46],
        "粉之都（桂林米粉）": [8, 8, 9, 9, 10, 10, 11, 11, 10, 10, 9, 9]
    })
    df_price_long = df_price_trend.melt(
        id_vars="月份", 
        var_name="餐厅及菜品",
        value_name="价格（元）"
    )
    price_chart = alt.Chart(df_price_long).mark_line().encode(
        x=alt.X("月份:N", title="月份"),
        y=alt.Y("价格（元）:Q", title="价格"),
        color=alt.Color(
            "餐厅及菜品:N", 
            title="餐厅及招牌菜",
            legend=alt.Legend(orient="bottom", labelLimit=60, symbolSize=100)
        ),
        tooltip=["月份:N", "餐厅及菜品:N", "价格（元）:Q"]
    ).properties(width=700, height=400)
    st.altair_chart(price_chart, use_container_width=True)
    # 4. 多餐厅老友粉月销量走势（仿第一张图的多系列面积图）
    st.subheader("南宁老友粉月销量走势")
    # 构造多餐厅的老友粉月销量数据
    df_sales_trend = pd.DataFrame({
        "月份": ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"],
        "复记老友粉": [200, 220, 210, 240, 280, 290, 320, 310, 270, 260, 230, 210],
        "舒记老友粉": [180, 200, 190, 220, 260, 270, 300, 290, 250, 240, 210, 190],
        "爱民老友粉": [150, 170, 160, 190, 230, 240, 270, 260, 220, 210, 180, 160],
        "粉之都老友粉": [120, 140, 130, 160, 200, 210, 240, 230, 190, 180, 150, 130]
    })
    # 转长格式适配Altair
    df_sales_long = df_sales_trend.melt(
        id_vars="月份",
        var_name="餐厅",
        value_name="月销量"
    )
    # 多系列面积图（仿示例图样式：透明重叠+hover提示+底部图例）
    sales_chart = alt.Chart(df_sales_long).mark_area(opacity=0.7).encode(
        x=alt.X("月份:N", title="月份"),
        y=alt.Y("月销量:Q", title="月销量"),
        color=alt.Color(
            "餐厅:N",
            title="餐厅",
            legend=alt.Legend(orient="bottom", symbolSize=100)
        ),
        tooltip=[
            alt.Tooltip("月份:N", title="月份"),
            alt.Tooltip("餐厅:N", title="餐厅"),
            alt.Tooltip("月销量:Q", title="老友粉月销量")
        ]
    ).properties(
        width=700,
        height=400
    )
    st.altair_chart(sales_chart, use_container_width=True)
    # 5. 店铺详情表
    st.subheader("南宁美食店铺详情")
    st.dataframe(df_shops)
    # 6. 餐厅详情
    st.subheader("餐厅详情")
    df_restaurant_info = pd.DataFrame({
        "店铺名称": ["复记老友粉", "舒记老友粉", "爱民螺蛳粉", "万国酒家", "粉之都"],
        "评分": [4.8, 4.7, 4.6, 4.9, 4.5],
        "人均消费": [15, 14, 12, 50, 10],
        "特色菜品": [
            "• 老友粉\n• 老友炒粉",
            "• 老友粉\n• 老友伊面",
            "• 螺蛳粉\n• 鸭脚煲",
            "• 柠檬鸭\n• 老友鱼",
            "• 桂林米粉\n• 牛腩粉"
        ]
    })
    selected_shop = st.selectbox("选择餐厅查看详情", df_restaurant_info["店铺名称"])
    shop_detail = df_restaurant_info[df_restaurant_info["店铺名称"] == selected_shop].iloc[0]
    col_info, col_dish = st.columns(2)
    with col_info:
        st.write(f"**{shop_detail['店铺名称']}**")
        st.write(f"评分\n{shop_detail['评分']}/5.0")
        st.write(f"人均消费\n{shop_detail['人均消费']}元")
    with col_dish:
        st.write("**推荐菜品**")
        st.write(shop_detail["特色菜品"])
    st.write("**当前拥挤程度**")
    crowd_rate = 80
    st.progress(crowd_rate)
    st.caption(f"{crowd_rate}% 拥挤")
    # 7. 今日午餐推荐
    st.subheader("今日午餐推荐")
    st.markdown("""
    <div style="background-color: #e63946; color: white; padding: 3px 8px; border-radius: 4px; display: inline-block;">
    推荐午餐
    </div>
    """, unsafe_allow_html=True)
    st.info("今日推荐：老友螺蛳粉套餐")
    st.caption("今日推荐：营养均衡·不会胖（中辣）")
    lunch_img_url = "https://img.shetu66.com/2022/11/05/1667578776753380.jpg"
    st.image(lunch_img_url, caption="老友螺蛳粉套餐（含酸笋、炸蛋）")

elif nav_option == "🖼️ 图片相册":
    # 完全保留ccc.py原始代码（修复上一张按钮功能）
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
    # 初始化索引
    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0
    # 三列布局居中显示图片
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.image(image_ua[st.session_state['ind']]['url'], caption=image_ua[st.session_state['ind']]['text'])
    # 切换按钮
    c1, c2 = st.columns(2)
    def prevImg():
        st.session_state['ind'] = (st.session_state['ind'] - 1) % len(image_ua)
    def nextImg():
        st.session_state['ind'] = (st.session_state['ind'] + 1) % len(image_ua)
    with c1:
        st.button('上一张', use_container_width=True, on_click=prevImg)
    with c2:
        st.button('下一张', use_container_width=True, on_click=nextImg)

elif nav_option == "🎵 音乐播放器":
    # 完全保留ddd.py原始代码
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

elif nav_option == "🎬 视频中心":
    # 完全保留eee.py原始代码
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

elif nav_option == "📝 个人简历生成器":
    # 完全保留fff.py原始代码
    # 顶部标题
    st.markdown("""
    # 🎯 个人简历生成器  
    使用 Streamlit 创建您的个性化简历
    """)
    # 添加样式美化（深色背景 + 白色文字）
    st.markdown("""
    <style>
        .stApp {
            background-color: #1e1e1e;
            color: #e6e6e6;
        }
        h1, h2, h3 {
            color: #00c8ff !important;
        }
        .stTextInput>div>div>input {
            background-color: #2d2d2d !important;
            color: #e6e6e6 !important;
        }
        .stNumberInput>div>div>input {
            background-color: #2d2d2d !important;
            color: #e6e6e6 !important;
        }
        .stSlider>div>div>div {
            background-color: #2d2d2d !important;
        }
        .stSelectbox>div>div>div {
            background-color: #2d2d2d !important;
            color: #e6e6e6 !important;
        }
    </style>
    """, unsafe_allow_html=True)
    # 主体布局：左右两栏
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("📝 个人信息表单")
        # 基本信息
        name = st.text_input("姓名", "帅哥", key="name")
        position = st.text_input("职位", "CEO", key="position")
        phone = st.text_input("电话", "13168575451", key="phone")
        email = st.text_input("邮箱", "4646465611@qq.com", key="email")
        birth_date = st.date_input("出生日期", value=None, key="birth_date")
        gender = st.radio("性别", ["男", "女", "其他"], index=0, key="gender")
        education = st.selectbox("学历", ["本科", "硕士", "博士"], index=0, key="education")
        
        # 语言能力（多选）
        languages = st.multiselect("语言能力", ["中文", "英语", "日语"], default=["中文", "英语"], key="languages")
        
        # 技能（多选）
        skills = st.multiselect("技能（可多选）", 
                               ["Java", "HTML/CSS", "机器学习", "Python", "SQL", "C++"], 
                               default=["Java", "HTML/CSS", "机器学习", "Python"], 
                               key="skills")
        
        # 工作经验（滑块，范围0-30年）
        work_years = st.slider("工作经验（年）", 0, 30, 6, key="work_years")
        
        # 薪资范围（滑块，单位：元）
        salary_range = st.slider("期望薪资范围（元）", 5000, 50000, (10123, 29390), key="salary_range")
        
        # 个人简介
        bio = st.text_area("个人简介", """
        """, key="bio")
        
        # 每日最长联系时间
        max_online_time = st.number_input(
            "每日最长联系时间（分钟）",
            min_value=1,
            max_value=24 * 60,  # 1440分钟 = 24小时
            value=120,
            step=15,
            key="max_online_time"
        )
        
        # 头像上传
        uploaded_file = st.file_uploader("上传个人照片", type=["jpg", "jpeg", "png"], accept_multiple_files=False, key="avatar")
        if uploaded_file is not None:
            try:
                image = Image.open(uploaded_file)
                st.image(image, caption="上传的头像", use_container_width=True)
            except Exception as e:
                st.error(f"图片加载失败: {str(e)}")
        else:
            # 检查本地文件是否存在，不存在则使用在线占位图
            if os.path.exists("default.png"):
                st.image("default.png", caption="默认头像", use_container_width=True)
            else:
                placeholder_url = "https://so1.360tres.com/t012473c2d69aa76afb.jpg"
                st.image(placeholder_url, caption="默认头像", use_container_width=True)
    with col2:
        st.subheader("📄 简历实时预览")
        # 顶部姓名和头像
        st.markdown(f"<h1 style='color: #00c8ff; font-size: 28px;'>{name}</h1>", unsafe_allow_html=True)
        
        # 头像（右侧）
        if uploaded_file is not None:
            try:
                image = Image.open(uploaded_file)
                st.image(image, width=120, use_container_width=False)
            except:
                if os.path.exists("default.png"):
                    st.image("default.png", width=120, use_container_width=False)
                else:
                    st.image("https://via.placeholder.com/150/000000/ffffff?text=Avatar", width=120, use_container_width=False)
        else:
            if os.path.exists("default.png"):
                st.image("default.png", width=120, use_container_width=False)
            else:
                st.image("https://so1.360tres.com/t012473c2d69aa76afb.jpg", width=120, use_container_width=False)
        # 个人信息（两栏布局）
        col_a, col_b = st.columns(2)
        with col_a:
            st.write("**性别**: ", gender)
            st.write("**学历**: ", education)
            st.write("**工作年限**: ", work_years, "年")
            st.write("**最佳联系时间**: ", max_online_time, "分钟")
        with col_b:
            st.write("**职位**: ", position)
            st.write("**电话**: ", phone)
            st.write("**邮箱**: ", email)
            st.write("**出生日期**: ", birth_date.strftime("%Y/%m/%d") if birth_date else "未填写")
        # 技能展示
        st.markdown("---")
        st.subheader("🛠️ 专业技能")
        for skill in skills:
            st.markdown(f"• <span style='color: #00c8ff;'>{skill}</span>", unsafe_allow_html=True)
        # 个人简介
        st.markdown("---")
        st.subheader("📝 个人简介")
        st.markdown(bio)
        # 薪资范围（带颜色提示）
        st.markdown("---")
        st.markdown(f"<p style='color: #00c8ff; font-weight: bold;'>期望薪资范围: {salary_range[0]} - {salary_range[1]} 元</p>", unsafe_allow_html=True)
       
