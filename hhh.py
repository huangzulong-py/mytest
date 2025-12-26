import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image
import io
import os

# ---------------------- 全局配置 ----------------------
st.set_page_config(
    page_title="广西职业师范学院综合平台",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 隐藏默认侧边栏+优化导航样式
st.markdown("""
<style>
    [data-testid="collapsedControl"], [data-testid="stSidebar"] {
        display: none !important;
    }
    /* 导航按钮样式：黑色背景+白色文字，选中时红色高亮 */
    .nav-btn {
        background-color: #000000;
        color: #ffffff;
        border: none;
        padding: 8px 16px;
        font-size: 14px;
        cursor: pointer;
        width: 100%;
        border-radius: 2px;
    }
    .nav-btn:hover {
        background-color: #333333;
    }
    .nav-btn.active {
        color: #ff0000;
        text-decoration: underline;
        font-weight: bold;
        background-color: #f5f5f5;
    }
    /* 顶部图片容器样式，避免变形 */
    .top-img-container {
        text-align: center;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------- 初始化会话状态（记录当前选中模块） ----------------------
if "nav_option" not in st.session_state:
    st.session_state.nav_option = "学校介绍"  # 默认选中“数字档案”对应模块


# ---------------------- 顶部栏（正确学校标题图+校徽） ----------------------
# 使用用户指定的广西职业师范学院顶部标题图
st.markdown('<div class="top-img-container">', unsafe_allow_html=True)
st.image(
    "https://tse1-mm.cn.bing.net/th/id/OIP-C.1pT_21NHy-U7PAXWb-lQvgHaCf?w=343&h=117&c=7&r=0&o=5&pid=1.7",
    caption="广西职业师范学院 | Guangxi Vocational Normal University",
    use_container_width=True,
    output_format="png"
)
st.markdown('</div>', unsafe_allow_html=True)


# ---------------------- 顶部并列导航栏 ----------------------
nav_items = [
    ("数字档案", "学校介绍"),
    ("南宁美食数据", "南宁美食仪表盘"),
    ("图片相册", "图片相册"),
    ("音乐播放器", "音乐播放器"),
    ("视频中心", "视频中心"),
    ("个人简历生成器", "个人简历生成器")
]

nav_cols = st.columns(len(nav_items))
for col, (display_name, module_name) in zip(nav_cols, nav_items):
    with col:
        if st.session_state.nav_option == module_name:
            st.markdown(
                f"<button class='nav-btn active' disabled>{display_name}</button>",
                unsafe_allow_html=True
            )
        else:
            if st.button(display_name, key=f"nav_{module_name}", use_container_width=True):
                st.session_state.nav_option = module_name

st.markdown("---")


# ---------------------- 主内容区（核心修正：校徽图片+释义） ----------------------
# ========== 1. 学校介绍（数字档案：更新校徽+修正释义，基于学校官方信息） ==========
if st.session_state.nav_option == "学校介绍":
    st.title("🏫 数字档案 - 广西职业师范学院")
    st.markdown("---")
    
    # 校徽展示（使用用户指定的校徽链接，修正释义：避免混淆广西职业技术学院元素）
    st.subheader("校园标识 - 校徽")
    col_logo, col_intro = st.columns([1, 2])
    with col_logo:
        # 替换为用户指定的校徽图片链接
        st.image(
            "https://tse1-mm.cn.bing.net/th/id/OIP-C.DMd9C-XVKKG811iPYdpjzwHaHY?w=170&h=180&c=7&r=0&o=5&pid=1.7",
            caption="广西职业师范学院校徽",
            use_container_width=True
        )
    with col_intro:
        # 基于学校“职业师范”定位+历史沿革修正释义（排除其他学校的鲁班锁/壮锦等错误元素）
        st.write("""
        校徽设计紧扣“职业师范”办学定位，融合学校历史传承与教育使命：
        1. **核心元素**：包含“广西职业师范学院”中英文校名，底部标注“1951”办学起始年份，体现70余年办学积淀；
        2. **造型寓意**：整体呈圆形，象征学校团结奋进的办学氛围；内部隐含“书本”与“齿轮”抽象符号——“书本”代表师范教育的立德树人本质，“齿轮”凸显职业教育的技术技能培养特色，二者结合体现“师范+职业”双属性；
        3. **色调意义**：以沉稳蓝为基础色，象征教育的理性与严谨；搭配红色点缀（如年份标识），呼应学校源于1951年的红色办学基因，体现“忠信修身、知行修业”的校训精神；
        4. **识别性**：设计简洁大气，既保留传统师范院校的文化底蕴，又突出职业教育的时代特征，符合学校培养“高素质应用型、技术技能型人才和职业教育师资”的定位。
        """)
    
    # 历史沿革（基于官方表格数据，修正时间线）
    st.subheader("历史沿革")
    history_df = pd.DataFrame({
        "创建（变更）时间": ["1951年5月", "1951年10月", "1954年2月", "1979年4月", "1983年7月", "2019年6月"],
        "学校名称": [
            "广西省行政干部训练班",
            "广西人民革命大学",
            "广西省人民政府行政干部学校",
            "广西壮族自治区经济干部学校",
            "广西壮族自治区经济管理干部学院",
            "广西职业师范学院"
        ]
    })
    st.dataframe(history_df, use_container_width=True)
    
    # 2024年专业分数线（新增：基于搜索到的官方数据，分校区展示）
    st.subheader("2024年广西专业录取分数线（部分）")
    # 筛选重点专业，区分本科/专科与校区
    score_df = pd.DataFrame({
        "录取批次": ["本科批", "本科批", "本科批", "专科批", "本科批", "本科批"],
        "科类": ["物理类", "物理类", "历史类", "物理类", "历史类", "物理类"],
        "专业名称": [
            "人工智能（罗文校区）",
            "大数据管理与应用（罗文校区）",
            "财务管理（相思湖校区）",
            "大数据与会计（相思湖校区）",
            "网络与新媒体（相思湖校区）",
            "教育技术学（相思湖校区）"
        ],
        "录取最低分": [421, 419, 455, 369, 445, 414],
        "录取最高分": [473, 462, 478, 421, 472, 447]
    })
    st.dataframe(score_df, use_container_width=True)
    st.caption("数据来源：广西职业师范学院2024年招生公示，完整分数线可查看学校招生网")
    
    # 核心办学数据（基于官方简介）
    st.subheader("核心办学数据")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("办学性质", "公办全日制本科")
    with col2:
        st.metric("本科专业数", "38个")
    with col3:
        st.metric("校区数量", "2个（相思湖/罗文）")
    with col4:
        st.metric("核心定位", "职业师范教育")


# ========== 2. 南宁美食仪表盘（功能保留，优化数据展示） ==========
elif st.session_state.nav_option == "南宁美食仪表盘":
    st.title("南宁美食数据仪表盘")
    st.subheader("南宁美食店铺分布")
    df_shops = pd.DataFrame({
        "店铺名称": ["复记老友粉", "舒记老友粉", "爱民螺蛳粉", "万国酒家", "粉之都"],
        "评分": [4.8, 4.7, 4.6, 4.9, 4.5],
        "lat": [22.82, 22.81, 22.80, 22.82, 22.79],
        "lon": [108.37, 108.36, 108.35, 108.38, 108.34]
    })
    st.map(df_shops)
    
    st.subheader("店铺评分排名（降序）")
    df_bar = df_shops[["店铺名称", "评分"]].set_index("店铺名称").sort_values("评分", ascending=False)
    st.bar_chart(df_bar, use_container_width=True, color="#e63946")
    
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
    price_chart = alt.Chart(df_price_long).mark_line(strokeWidth=2).encode(
        x=alt.X("月份:N", title="月份", axis=alt.Axis(labelAngle=0)),
        y=alt.Y("价格（元）:Q", title="价格（元）", scale=alt.Scale(domain=[0, 55])),
        color=alt.Color(
            "餐厅及菜品:N", 
            title="餐厅及招牌菜",
            legend=alt.Legend(orient="bottom", labelLimit=80, symbolSize=120)
        ),
        tooltip=["月份:N", "餐厅及菜品:N", "价格（元）:Q"]
    ).properties(width=800, height=400)
    st.altair_chart(price_chart, use_container_width=True)


# ========== 3. 图片相册（功能保留） ==========
elif st.session_state.nav_option == "图片相册":
    st.title("🖼️ 图片相册")
    st.caption("支持上一张/下一张切换，展示动物主题图片")
    
    image_list = [
        {
            "url": "https://tse1-mm.cn.bing.net/th/id/OIP-C.XrioiabkHAO8ejwBxQ0VFwHaE7?w=268&h=180&c=7&r=0&o=7&cb=ucfimg2&pid=1.7&rm=3&ucfimg=1",
            "caption": "海马（海洋生物）"
        },
        {
            "url": "https://tse1-mm.cn.bing.net/th/id/OIP-C.WmnveGScAUpPLtEjBaILjwAAAA?w=293&h=195&c=7&r=0&o=7&cb=ucfimg2&pid=1.7&rm=3&ucfimg=1",
            "caption": "海狮（海洋哺乳动物）"
        },
        {
            "url": "https://tse3-mm.cn.bing.net/th/id/OIP-C.u_fS7nS5RRGI2xYoUV-6nQHaEo?w=314&h=195&c=7&r=0&o=7&cb=ucfimg2&pid=1.7&rm=3&ucfimg=1",
            "caption": "大象（陆地哺乳动物）"
        }
    ]
    
    if "img_ind" not in st.session_state:
        st.session_state.img_ind = 0
    
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.image(
            image_list[st.session_state.img_ind]["url"],
            caption=image_list[st.session_state.img_ind]["caption"],
            use_container_width=True
        )
    
    btn_cols = st.columns(2)
    with btn_cols[0]:
        if st.button("上一张", use_container_width=True):
            st.session_state.img_ind = (st.session_state.img_ind - 1) % len(image_list)
    with btn_cols[1]:
        if st.button("下一张", use_container_width=True):
            st.session_state.img_ind = (st.session_state.img_ind + 1) % len(image_list)


# ========== 4. 音乐播放器（功能保留） ==========
elif st.session_state.nav_option == "音乐播放器":
    st.title("🎵 音乐播放器")
    st.caption("支持上一首/下一首切换，播放网易云音乐外链歌曲")
    
    music_list = [
        {
            "audio_url": "https://music.163.com/song/media/outer/url?id=280015379.mp3",
            "cover_url": "https://p1.music.126.net/r1AKMenByofI7Qqj3E5EqQ==/109951172091080013.jpg?param=130y130",
            "title": "火山灰"
        },
        {
            "audio_url": "https://music.163.com/song/media/outer/url?id=2750712929.mp3",
            "cover_url": "https://p1.music.126.net/r1AKMenByofI7Qqj3E5EqQ==/109951172091080013.jpg?param=130y130",
            "title": "飞鸟在风暴中"
        },
        {
            "audio_url": "https://music.163.com/song/media/outer/url?id=2756051000.mp3",
            "cover_url": "https://p1.music.126.net/r1AKMenByofI7Qqj3E5EqQ==/109951172091080013.jpg?param=130y130",
            "title": "银色荒原"
        }
    ]
    
    if "music_ind" not in st.session_state:
        st.session_state.music_ind = 0
    
    col_cover, col_play = st.columns([1, 2])
    with col_cover:
        st.image(
            music_list[st.session_state.music_ind]["cover_url"],
            caption="专辑封面",
            use_container_width=True
        )
    with col_play:
        st.subheader(music_list[st.session_state.music_ind]["title"])
        st.audio(
            music_list[st.session_state.music_ind]["audio_url"],
            format="audio/mp3",
            start_time=0
        )
    
    btn_cols = st.columns(2)
    with btn_cols[0]:
        if st.button("上一首", use_container_width=True):
            st.session_state.music_ind = (st.session_state.music_ind - 1) % len(music_list)
    with btn_cols[1]:
        if st.button("下一首", use_container_width=True):
            st.session_state.music_ind = (st.session_state.music_ind + 1) % len(music_list)


# ========== 5. 视频中心（功能保留） ==========
elif st.session_state.nav_option == "视频中心":
    st.title("🎬 视频中心")
    st.caption("《熊出没》系列剧集播放，支持直接选择集数")
    
    video_list = [
        {"url": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/37/17/34206321737/34206321737-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1766568058&trid=08ec7ba97506424181cd8c17013d3e8O&os=estghw&uipk=5&nbs=1&oi=143446004&platform=html5&mid=0&gen=playurlv3&og=hw&upsig=af01a291c7f4bd29d343c064c2fa9b51&uparams=e,deadline,trid,os,uipk,nbs,oi,platform,mid,gen,og&bvc=vod&nettype=1&bw=660455&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3", "title": "熊出没-第1集"},
        {"url": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/37/17/34206321737/34206321737-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1766568058&trid=08ec7ba97506424181cd8c17013d3e8O&os=estghw&uipk=5&nbs=1&oi=143446004&platform=html5&mid=0&gen=playurlv3&og=hw&upsig=af01a291c7f4bd29d343c064c2fa9b51&uparams=e,deadline,trid,os,uipk,nbs,oi,platform,mid,gen,og&bvc=vod&nettype=1&bw=660455&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3", "title": "熊出没-第2集"},
        {"url": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/07/35/33940373507/33940373507-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&deadline=1766568176&oi=143443039&trid=a6dbb5f5be8c4e4283bb80755d341f5O&gen=playurlv3&nbs=1&uipk=5&platform=html5&os=estghw&og=hw&upsig=0c66ee62fea42e369a7c7250b149496c&uparams=e,mid,deadline,oi,trid,gen,nbs,uipk,platform,os,og&bvc=vod&nettype=1&bw=629513&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3", "title": "熊出没-第3集"},
        {"url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4", "title": "熊出没-第4集"},
        {"url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4", "title": "熊出没-第5集"}
    ]
    
    if "video_ind" not in st.session_state:
        st.session_state.video_ind = 0
    
    st.subheader(video_list[st.session_state.video_ind]["title"])
    st.video(
        video_list[st.session_state.video_ind]["url"],
        format="video/mp4",
        start_time=0
    )
    
    st.subheader("选择集数")
    video_cols = st.columns(len(video_list))
    for i, col in enumerate(video_cols):
        with col:
            if st.button(
                f"第{i+1}集",
                key=f"video_btn_{i}",
                use_container_width=True
            ):
                st.session_state.video_ind = i


# ========== 6. 个人简历生成器（功能保留） ==========
elif st.session_state.nav_option == "个人简历生成器":
    st.title("🎯 个人简历生成器")
    st.caption("填写信息后实时预览简历，支持头像上传")
    
    st.markdown("""
    <style>
        .resume-bg {
            background-color: #1e1e1e;
            color: #e6e6e6;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        .resume-title {
            color: #00c8ff !important;
            border-bottom: 2px solid #00c8ff;
            padding-bottom: 10px;
            margin-bottom: 15px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    col_form, col_preview = st.columns([1, 2])
    with col_form:
        st.subheader("📝 填写个人信息")
        
        name = st.text_input("姓名", "张三", key="resume_name")
        position = st.text_input("应聘职位", "软件工程师", key="resume_pos")
        phone = st.text_input("联系电话", "13800138000", key="resume_phone")
        email = st.text_input("电子邮箱", "zhangsan@example.com", key="resume_email")
        education = st.selectbox("最高学历", ["本科", "硕士", "博士", "专科"], key="resume_edu")
        work_years = st.slider("工作经验（年）", 0, 30, 3, key="resume_work")
        skills = st.multiselect("专业技能", ["Python", "Java", "SQL", "HTML/CSS", "机器学习"], key="resume_skills")
        bio = st.text_area("个人简介", "具备3年软件开发经验，熟练掌握Python、SQL等技术，擅长项目实战与团队协作。", key="resume_bio")
        uploaded_avatar = st.file_uploader("上传头像（可选）", type=["jpg", "jpeg", "png"], key="resume_avatar")
    
    with col_preview:
        st.subheader("📄 简历预览")
        st.markdown('<div class="resume-bg">', unsafe_allow_html=True)
        
        st.markdown(f"<h2 class='resume-title'>{name} - {position}</h2>", unsafe_allow_html=True)
        
        info_cols = st.columns(2)
        with info_cols[0]:
            st.write(f"**学历**：{education}")
            st.write(f"**工作经验**：{work_years}年")
            st.write(f"**电话**：{phone}")
        with info_cols[1]:
            st.write(f"**邮箱**：{email}")
            st.write(f"**更新时间**：实时生成")
            if uploaded_avatar:
                st.image(uploaded_avatar, width=100, caption="个人头像")
            else:
                st.image("https://so1.360tres.com/t012473c2d69aa76afb.jpg", width=100, caption="默认头像")
        
        st.markdown("<h4 class='resume-title'>专业技能</h4>", unsafe_allow_html=True)
        st.write("、".join(skills) if skills else "暂无填写")
        
        st.markdown("<h4 class='resume-title'>个人简介</h4>", unsafe_allow_html=True)
        st.write(bio if bio else "暂无填写")
        
        st.markdown('</div>', unsafe_allow_html=True)
