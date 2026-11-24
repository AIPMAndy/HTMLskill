# HTMLskill

> **Python-first HTML 生成框架** — 用 Python 编写，生成精美 HTML

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![CI](https://github.com/AIPMAndy/HTMLskill/workflows/CI/badge.svg)](https://github.com/AIPMAndy/HTMLskill/actions)

**[示例代码](./examples/)** | **[English README](README.md)** | **[文档](https://github.com/AIPMAndy/HTMLskill/tree/main/docs)**

HTMLskill 将 Python 的简洁性与专业设计系统相结合，无需模板、无需构建工具——只需 Python 代码即可生成生产级 HTML 页面。

---

## 🎯 为什么选择 HTMLskill？

### 传统 HTML 生成方法的问题

| 传统方法 | HTMLskill |
|---------|-----------|
| 🤯 混合 Python 逻辑和 HTML 模板 | ✅ 纯 Python，无需切换上下文 |
| 🎨 每个元素手动编写 CSS | ✅ 内置设计系统（8px 网格，WCAG AA） |
| 📱 从零开始实现响应式设计 | ✅ 默认移动优先 |
| 🔧 复杂构建工具（Webpack、Vite） | ✅ 零构建步骤，即时输出 |
| 🌐 单独的国际化文件 | ✅ 内置 CJK 字体优化 |

### 真实对比示例

**传统方法（Jinja2 + 手动 CSS）：**
```python
# template.html
<div class="hero" style="padding: 64px 24px; background: linear-gradient(...)">
  <h1 style="font-size: 48px; font-weight: 700; margin-bottom: 16px;">
    {{ title }}
  </h1>
  <p style="font-size: 20px; color: #666; margin-bottom: 32px;">
    {{ description }}
  </p>
  <a href="{{ cta_link }}" style="background: #007bff; color: white; ...">
    {{ cta_text }}
  </a>
</div>
```

**HTMLskill 方法：**
```python
import htmlskill as hs

@hs.page(mode="web-prototype", design_system="huashu")
def landing_page():
    with hs.hero(gradient="blue"):
        hs.heading("用 Python 更快构建", level=1)
        hs.text("无需模板，无需构建工具，只需 Python 代码。")
        hs.button("开始使用", href="/docs", style="primary")
```

**结果：** 简洁的 Python 代码 → 专业 HTML，具有响应式设计、无障碍访问和优化字体。

---

## ✨ 核心特性

### 🐍 Python 优先的 API
- **基于装饰器**：`@hs.page()` 定义页面，`@hs.component()` 定义组件
- **上下文管理器**：`with hs.section():` 实现嵌套布局
- **类型提示**：完整的 IDE 自动补全和类型检查
- **线程安全**：可在 Web 框架中使用（Flask、FastAPI、Django）

### 🎨 专业设计系统
- **8px 网格系统**：一致的间距和对齐
- **WCAG AA 合规**：无障碍的颜色对比度和字体大小
- **CJK 字体优化**：完美渲染中文/日文/韩文
- **默认响应式**：移动优先的断点（sm、md、lg、xl）

### 🧩 丰富的组件库

**基础组件：**
```python
hs.heading("标题", level=1)
hs.text("段落文本")
hs.button("点击我", style="primary")
hs.image("photo.jpg", alt="照片")
hs.spacer(size="lg")
hs.divider()
```

**布局组件：**
```python
with hs.container(max_width="lg"):
    with hs.grid(columns=3, gap="md"):
        hs.text("列 1")
        hs.text("列 2")
        hs.text("列 3")
```

**复合组件：**
```python
with hs.hero(gradient="purple"):
    hs.heading("欢迎")
    hs.button("开始使用")

with hs.features(columns=3):
    hs.feature(icon="⚡", title="快速", description="...")
    hs.feature(icon="🎨", title="美观", description="...")
```

---

## 🚀 快速开始

### 安装

```bash
git clone https://github.com/AIPMAndy/HTMLskill.git
cd HTMLskill
python -m pip install -r requirements.txt
python -m pip install -e .
```

### 60 秒教程

在仓库根目录运行自带的示例：

```bash
python examples/00-minimal.py
```

在浏览器中打开 `examples/output/minimal.html`。[完整落地页示例](./examples/02-complete-landing.py) 演示了怎样组织更多页面内容。

---

## 📚 使用场景

## 安装

```bash
# 克隆仓库
git clone https://github.com/AIPMAndy/HTMLskill.git
cd HTMLskill

# 安装依赖
pip install -r requirements.txt

# 开发模式安装
pip install -e .
```

## 路线图

### Phase 1: MVP (当前 - 2-3 周)
- 核心 Python API ✅
- 基础组件 ✅
- 3 种输出模式 🚧
- HTML 渲染 🚧

### Phase 2: 设计系统 (1-2 周)
- huashu-design 资产协议
- 5 维度专家评审
- 反 AI-slop 规则

### Phase 3: 模板与导出 (2-3 周)
- 9 种输出模式
- 75+ 模板库
- 多格式导出 (PDF/PNG/MP4/GIF/PPTX)

## 架构

```
用户 Python 代码
    ↓
@page 装饰器 → RenderContext
    ↓
组件 → 添加到上下文
    ↓
渲染器 → Jinja2 模板
    ↓
单文件 HTML 输出
```

## 技术栈

- Python 3.10+
- Jinja2 (模板)
- Tailwind CSS (样式)
- Playwright (验证)
- Click (CLI)

## 开发

```bash
# 运行测试
pytest tests/ -v

# 带覆盖率运行
pytest tests/ --cov=htmlskill --cov-report=html

# 格式化代码
black htmlskill/ tests/

# 代码检查
flake8 htmlskill/ tests/
```

## 许可证

MIT License - 详见 [LICENSE](LICENSE)

## 作者

**Andy** - [@AIPMAndy](https://github.com/AIPMAndy)

灵感来源：
- [Mesop](https://github.com/google/mesop) - Python UI 框架
- [huashu-design](https://github.com/alchaincyf/huashu-design) - 设计系统
- [html-anything](https://github.com/nexu-io/html-anything) - 多模板 HTML 生成器

---

**注意**: 本项目正在积极开发中。v1.0.0 发布前 API 可能会有变化。
