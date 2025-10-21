# 🧩 SageMathLab



<p align="center">
    <a href="https://github.com/hxd77/SageMathLab"><img src="https://raw.githubusercontent.com/hxd77/BlogImage/master/TyporaImage/20251021110145004.png" width=500 ></a>
</p>

<p alt="center">
   <img src=" https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white">
</p>



这是一个关于 **SageMath** 的学习与实验仓库，记录了我在数学计算、代数、数论以及密码学方向的探索与实践。  
无论你是第一次接触 SageMath，还是想用它做数学实验，这个仓库都能提供一些参考与灵感。

---

## 🌱 项目简介

SageMath 是一个强大的开源数学软件系统，集成了数论、代数、微积分、符号计算、图论、密码学等众多领域的功能。  
本仓库旨在通过代码示例和实验笔记，帮助理解数学背后的逻辑与算法实现。

主要内容包括：

- 🔢 **数论计算**：模运算、素数分解、欧几里得算法  
- 🧮 **代数与线性代数**：群、环、域、矩阵计算  
- 🔐 **密码学实验**：RSA、ECC、同态加密基础  
- 🧠 **符号计算与方程求解**  
- 📊 **函数与数据可视化**

---

## 📂 仓库结构

```

SagePlayground/  
├── notebooks/ # Jupyter 或 SageMath Notebook 文件 (.ipynb)  
├── scripts/ # 独立 Sage/Python 脚本 (.sage / .py)  
├── examples/ # 小型演示与数学实例  
├── docs/ # Markdown 格式的学习笔记与文档  
└── README.md

```

---

## 🚀 使用方法

### 1️⃣ 安装 SageMath

你可以在官网或镜像源下载 SageMath：  
👉 https://doc.sagemath.org/html/zh/installation/

也可以使用 conda 或 Docker 安装：

```bash
conda install -c conda-forge sagemath
```

或：

```bash
docker run -it sagemath/sagemath
```

* * *

### 2️⃣ 启动交互环境

```bash
sage -n jupyter
```

启动后，会在浏览器中打开 Jupyter Notebook 界面。

* * *

### 3️⃣ 克隆本仓库

```bash
git clone https://github.com/<你的用户名>/SagePlayground.git
cd SagePlayground
```

* * *

### 4️⃣ 打开并运行示例

进入 `notebooks/` 目录，选择任意 `.ipynb` 文件运行。

* * *

## 💡 示例代码

```python
# 整数分解
n = 1234567891011
factor(n)

# 模逆计算
a, m = 7, 40
inverse_mod(a, m)

# 画出一个函数图像
plot(sin(x), (x, -2*pi, 2*pi))
```

* * *

## 🧰 环境依赖

* SageMath ≥ 9.0
  
* Jupyter Notebook（推荐用于交互式演示）
  

* * *

## 📘 学习资源

* SageMath 官方文档：https://doc.sagemath.org/html/zh/
  
* 官方教程与示例：https://www.sagemath.org/tutorial.html
  
* 社区讨论与问答：https://ask.sagemath.org/
  

* * *

## 📜 开源协议

本项目基于 **MIT License** 开源，欢迎自由使用与修改。

* * *

## ✨ 作者信息

作者：**hxd**

> “数学是理解世界的钥匙，而 SageMath 是打开这把钥匙的工具。”