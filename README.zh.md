# HTMLSkill - Python 优先的 HTML 生成框架

> **状态**: 🚧 Alpha - Phase 1 MVP 开发中

一个 Python 优先的 HTML 生成框架，融合了：
- **Mesop 风格 API** - 声明式 Python 装饰器和组件
- **huashu-design 设计系统** - 专业设计约束（8px 网格、WCAG AA 对比度、CJK 字体）
- **html-anything 模板** - 9 种输出模式（网页、幻灯片、海报、社交卡片等）

## 快速开始

```python
import htmlskill as hs

@hs.page(mode="web-prototype", design_system="huashu")
def landing_page():
    hs.heading("欢迎使用 HTMLSkill", level=1)
    hs.text("用 Python 代码构建专业级 HTML", size="large")
    hs.button("立即开始", style="primary")

# 生成单文件 HTML
ctx = landing_page()
# (渲染引擎即将在后续提交中完成)
```

## 功能特性 (Phase 1 MVP)

- ✅ **Python API** - `@page` 和 `@component` 装饰器
- ✅ **基础组件** - heading, text, button, image, spacer, divider
- 🚧 **布局组件** - container, grid, section (开发中)
- 🚧 **复合组件** - hero, features, cta, navbar, footer (开发中)
- 🚧 **3 种输出模式** - web-prototype, deck, infographic (开发中)
- 🚧 **设计约束** - 8px 网格、对比度检查 (开发中)
- 🚧 **HTML 导出** - 单文件内联资源 (开发中)

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
