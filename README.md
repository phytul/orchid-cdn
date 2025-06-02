## Front

## Back

## 开始

> python 依赖构建

> 快速初始化 `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`

```bash
# 创建虚拟环境（Virtual Environment）
python -m venv .venv

# 启动虚拟环境
source .venv/bin/activate

# 关闭虚拟环境
deactivate

# 根据 requirements.txt 文件安装依赖
pip install -r requirements.txt

# 生成 or 更新 requirements.txt 文件
pip freeze > requirements.txt
```

### 代码仓库初始化

#### 接口文档

> url: /apidocs

#### 🌳 环境变量管理

> 环境变量管理使用`python-dotenv`包

根目录下创建默认环境变量配置文件：`.flaskenv`

```text
# 项目入口
FLASK_APP=run.py

# Flask 环境
FLASK_ENV=development # development production
```

---

power by @phytul
