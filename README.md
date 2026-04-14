# 🎨 高密度信息图生成器 (infographic-generator)

<p align="center">
  <strong>基于 Nano Banana Pro 生成专业级信息图表</strong>
</p>

<p align="center">
  <a href="#-快速开始"><img src="https://img.shields.io/badge/快速开始-3 分钟-blue?style=for-the-badge" alt="快速开始"></a>
  <a href="#-功能特性"><img src="https://img.shields.io/badge/功能-风格选择-green?style=for-the-badge" alt="功能特性"></a>
  <a href="#-配置说明"><img src="https://img.shields.io/badge/配置-API_Key-orange?style=for-the-badge" alt="配置说明"></a>
</p>

---

## 📖 目录

- [简介](#-简介)
- [功能特性](#-功能特性)
- [快速开始](#-快速开始)
- [配置说明](#-配置说明)
- [使用指南](#-使用指南)
- [风格模板](#-风格模板)
- [输出示例](#-输出示例)
- [常见问题](#-常见问题)
- [技术栈](#-技术栈)
- [许可证](#-许可证)

---

## ✨ 简介

**infographic-generator** 是一个专业的信息图生成工具，基于 Nano Banana Pro (Gemini 3 Pro Image) 生成高密度、专业级信息图表。

**适用场景：**
- 📊 技术教程可视化
- 📈 产品对比分析
- 🧠 知识体系梳理
- 💡 创意头脑风暴
- 📝 学习笔记整理

---

## 🚀 功能特性

| 功能 | 说明 | 状态 |
|------|------|------|
| **双风格支持** | Claude 风格 + 手绘风格 | ✅ |
| **智能配置** | 首次使用自动检测并引导配置 | ✅ |
| **多分辨率** | 2K (默认) / 4K (可选) | ✅ |
| **批量生成** | 支持 1-10 张系列图 | ✅ |
| **配色模板** | 内置专业配色方案 | ✅ |
| **布局规范** | 蛇形路径 / 有机混乱布局 | ✅ |

---

## 🎯 快速开始

### 1️⃣ 安装依赖

确保已安装以下依赖：

```bash
# 检查 uv 是否安装
which uv

# 如未安装，执行：
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2️⃣ 配置 API Key

```bash
# 获取 Gemini API Key
# 访问：https://aistudio.google.com/apikey

# 设置环境变量
export GEMINI_API_KEY="your_api_key_here"

# 永久配置（可选）
echo 'export GEMINI_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc
```

### 3️⃣ 运行生成器

```bash
cd ~/.openclaw/workspace/skills/infographic-generator
python3 scripts/generate-infographic.py
```

**首次运行时会自动启动配置向导！** 🎉

---

## ⚙️ 配置说明

### 环境变量

| 变量名 | 必填 | 说明 |
|--------|------|------|
| `GEMINI_API_KEY` | ✅ | Gemini API Key |

### 配置文件

详细配置说明见 [`CONFIG.md`](CONFIG.md)

### 依赖检查

运行前自动检查：
- ✅ uv 是否安装
- ✅ Nano Banana Pro 脚本是否存在
- ✅ GEMINI_API_KEY 是否配置

---

## 📝 使用指南

### 基本流程

```
1. 运行脚本 → python3 scripts/generate-infographic.py
2. 选择风格 → A (Claude) / B (手绘，默认)
3. 输入主题 → 信息图核心主题
4. 输入描述 → 补充说明（可选）
5. 设置数量 → 1-10 张
6. 输入模块 → 至少 3 个核心模块
7. 选择分辨率 → 2K (推荐) / 4K
8. 开始生成 → 等待完成
```

### 交互示例

```bash
🎨 高密度信息图生成器
════════════════════════════════════════════

🎨 选择信息图风格
════════════════════════════════════════════
【A】Claude 风格 - 高密度专业知识图谱
   • 专业矢量图标 + 蛇形路径布局
   • 适合：技术教程、产品对比、系统架构

【B】手绘笔记风格 - Sketchnote（默认）⭐
   • 手绘涂鸦 + 马克笔效果 + 网格纸质感
   • 适合：头脑风暴、创意笔记、创意构思
════════════════════════════════════════════

请选择风格 (A/B，直接回车默认 B): B

✅ 已选择：手绘风格

📝 请输入信息图内容：
主题：AI Agent 生态系统
描述（可选）:
图片数量 (1-10，默认 1): 1

📋 请输入要展示的核心模块（每行一个，直接回车结束）：
模块 1: 核心架构
模块 2: 记忆系统
模块 3: 工具集成
模块 4: 技能系统
模块 5: 

📐 选择分辨率：
【1】2K (1920x2560) - 推荐，生成快 (~60 秒)
【2】4K (3840x5120) - 高质量，生成慢 (~120 秒)
请选择 (1/2，默认 1): 1

🚀 开始生成 1 张手绘风格信息图...
   分辨率：2K
   主题：AI Agent 生态系统
   模块数：4

🎨 正在生成：2026-04-14-18-30-00-sketch-ai-agent-ecosystem-01.png (2K)
✅ 生成成功
   ✅ [1/1] 完成：2026-04-14-18-30-00-sketch-ai-agent-ecosystem-01.png

════════════════════════════════════════════
🎉 生成完成！
════════════════════════════════════════════

📁 输出目录：/home/admin/.openclaw/workspace/skills/infographic-generator/output
🎨 风格：手绘风格
📐 分辨率：2K
📊 总数：1 张
```

---

## 🎨 风格模板

### 模板 A：Claude 风格专业知识图谱

**特点：**
- 专业矢量图标
- 蛇形路径布局（S 形蜿蜒）
- 暖米白背景 + 赤陶红/桃色模块
- 顶部横幅 + 图例键

**适用场景：**
- 技术教程
- 产品对比
- 系统架构
- 知识体系

**配色方案：**

| 用途 | 色值 | 说明 |
|------|------|------|
| 背景 | #F5F2ED | 暖米白/奶油色 |
| 核心模块 | #D97B54 | 深赤陶红 |
| 功能模块 | #F8D7BF | 柔和桃色 |
| 集成模块 | #2D2926 | 深炭灰 |

---

### 模板 B：手绘笔记风格（默认）⭐

**特点：**
- 手绘涂鸦效果
- 马克笔质感
- 网格纸背景 + 墨水飞溅
- 活力橙色高亮

**适用场景：**
- 头脑风暴
- 创意笔记
- 创意构思
- 学习笔记

**配色方案：**

| 用途 | 色值 | 说明 |
|------|------|------|
| 背景 | #F5F5DC | 网格纸 + 墨水飞溅 |
| 墨水色 | #1A1A1A | 炭黑色马克笔 |
| 强调色 | #FF7000 | 活力橙色 |
| 高光线 | #FFFFFF | 白色细线笔触 |

---

## 📊 输出示例

### 文件命名规则

```
{时间戳}-{风格前缀}-{主题简写}-{序号}.png

示例：
2026-04-14-18-30-00-sketch-ai-agent-ecosystem-01.png
2026-04-14-18-35-00-pro-product-comparison-02.png
```

### 输出规格

| 规格 | 值 |
|------|-----|
| **比例** | 3:4 (竖版) |
| **分辨率** | 2K (1920x2560) / 4K (3840x5120) |
| **模块数** | 模板 A: 10-23 个 / 模板 B: 10-15 个 |
| **图片数量** | 1-10 张（用户指定） |
| **文件格式** | PNG |

### 生成时间

| 分辨率 | 时间 | 文件大小 |
|--------|------|----------|
| **2K** | ~60 秒 | 5-10MB |
| **4K** | ~120 秒 | 15-25MB |

---

## ❓ 常见问题

### Q1: GEMINI_API_KEY 未设置

**错误信息：**
```
⚠️ 首次使用检测：GEMINI_API_KEY 未配置
```

**解决方案：**
```bash
export GEMINI_API_KEY="your_api_key"
# 或添加到 ~/.bashrc
echo 'export GEMINI_API_KEY="your_api_key"' >> ~/.bashrc
source ~/.bashrc
```

---

### Q2: uv 未安装

**错误信息：**
```
❌ 错误：uv 未安装
```

**解决方案：**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

### Q3: Nano Banana Pro 脚本不存在

**错误信息：**
```
❌ 错误：Nano Banana Pro 脚本不存在
```

**解决方案：**
```bash
# 检查路径是否正确
ls ~/.openclaw/workspace/skills/nano-banana-pro/scripts/generate_image.py

# 如未安装，先安装 Nano Banana Pro skill
```

---

### Q4: 如何选择风格？

**直接回答：**
- 技术内容 → 选 A（Claude 风格）
- 创意内容 → 选 B（手绘风格，默认）
- 不确定 → 直接回车（默认 B）

---

### Q5: 生成的图片在哪里？

**输出目录：**
```
~/.openclaw/workspace/skills/infographic-generator/output/
```

---

## 🛠️ 技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| **Python** | 3.8+ | 主语言 |
| **Nano Banana Pro** | Gemini 3 Pro Image | 图像生成 |
| **uv** | latest | Python 包管理 |
| **@larksuiteoapi/node-sdk** | 1.60.0 | (可选) 飞书集成 |

---

## 📚 相关文档

- [`SKILL.md`](SKILL.md) - 技能详细说明
- [`CONFIG.md`](CONFIG.md) - 配置指南
- [`references/color-templates.md`](references/color-templates.md) - 配色方案详情
- [`references/infographic-prompt-template.txt`](references/infographic-prompt-template.txt) - 提示词模板

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

**开发环境设置：**
```bash
# 克隆仓库
git clone https://github.com/langjun0322-create/infographic-generator.git

# 安装依赖
cd infographic-generator
pip install -r requirements.txt

# 运行测试
python3 scripts/generate-infographic.py --test
```

---

## 📄 许可证

MIT License © 2026 JunEr

---

## 🔗 链接

- **GitHub 仓库**: https://github.com/langjun0322-create/infographic-generator
- **Skill Hub**: (待发布)
- **问题反馈**: https://github.com/langjun0322-create/infographic-generator/issues

---

<p align="center">
  <strong>Made with ❤️ by JunEr</strong>
</p>

<p align="center">
  <em>最后更新：2026-04-14 | 版本：v2.1</em>
</p>
