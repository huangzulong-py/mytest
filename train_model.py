import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
import joblib

# 1. 加载数据（指定编码为gbk，适配中文CSV）
# 若gbk报错，可替换为 encoding="gb2312" 或 encoding="ansi"
df = pd.read_csv("insurance-chinese.csv", encoding="gbk")
X = df.drop("医疗费用", axis=1)  # 特征：年龄、性别、BMI等
y = df["医疗费用"]              # 目标：医疗费用

# 2. 定义特征预处理规则（分类特征独热编码，数值特征直接使用）
categorical_cols = ["性别", "是否吸烟", "区域"]
numerical_cols = ["年龄", "BMI", "子女数量"]
preprocessor = ColumnTransformer(
    transformers=[
        ("num", "passthrough", numerical_cols),
        ("cat", OneHotEncoder(drop="first"), categorical_cols)
    ]
)

# 3. 构建模型管道并训练
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())  # 也可替换为RandomForestRegressor提升精度
])
model.fit(X, y)

# 4. 保存模型
joblib.dump(model, "medical_cost_model.joblib")
print("模型已保存为 medical_cost_model.joblib")
