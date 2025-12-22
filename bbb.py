import streamlit as st
import pandas as pd
import altair as alt  # 用于自定义多系列面积图


# 页面标题（横向显示）
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
