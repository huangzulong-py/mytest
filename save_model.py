import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split
import pickle
from joblib import dump  # 新增joblib导入
import time

# 1. 数据加载与预处理（完全保留你的逻辑）
start_time = time.time()
df = pd.read_csv(
    'student_data_adjusted_rounded.csv',
    encoding='utf-8-sig',
    dtype={
        '学号': str,          
        '性别': 'category',  
        '专业': 'category'
    }
)
df.dropna(inplace=True)
print(f"数据集形状：{df.shape}（耗时{time.time()-start_time:.2f}秒）")
print("特征列：", df.columns.tolist())

# 2. 定义特征和目标变量（完全保留）
features = df[['性别', '专业', '每周学习时长（小时）', '上课出勤率', '期中考试分数', '作业完成率']]
target = df['期末考试分数']

# 3. 分类特征编码（完全保留）
features_encoded = pd.get_dummies(features, drop_first=False)
print("编码后的特征列数：", len(features_encoded.columns.tolist()))

# 4. 划分训练集（完全保留）
x_train, x_test, y_train, y_test = train_test_split(
    features_encoded, target, train_size=0.8, random_state=42, shuffle=True
)

# 5. 模型训练（完全保留你的参数）
rfr = RandomForestRegressor(
    n_estimators=150,    
    random_state=42,
    n_jobs=-1,           
    max_depth=12,        
    min_samples_leaf=5   
)
train_start = time.time()
rfr.fit(x_train, y_train)
print(f"模型训练完成（耗时{time.time()-train_start:.2f}秒）")

# 6. 模型评估（完全保留）
y_pred = rfr.predict(x_test)
print(f"模型评估结果：")
print(f"决定系数（R²）：{r2_score(y_test, y_pred):.4f}")
print(f"平均绝对误差（MAE）：{mean_absolute_error(y_test, y_pred):.2f}分")

# 7. 保存模型（仅改模型为joblib保存，其余配置文件仍用pickle）
dump(rfr, 'rfr_model.joblib', compress=3)  # 替换pickle.dump为joblib.dump（压缩减小体积）
with open('feature_names.pkl', 'wb') as f:
    pickle.dump(features_encoded.columns.tolist(), f)
with open('unique_values.pkl', 'wb') as f:
    pickle.dump({
        '性别': df['性别'].unique().tolist(),
        '专业': df['专业'].unique().tolist()
    }, f)

print(f"全部流程完成（总耗时{time.time()-start_time:.2f}秒）")
