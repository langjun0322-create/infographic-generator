# 信息图生成器配置

## 生图 API 配置

### 方式一：Nano Banana Pro（推荐）⭐

**优势：**
- ✅ 专为信息图优化的提示词模板
- ✅ 自动处理配色方案和布局
- ✅ 支持 2K/4K 分辨率
- ✅ 生成速度快（2K 约 60 秒）

**配置步骤：**

1. 获取 Gemini API Key
   - 访问：https://aistudio.google.com/apikey
   - 创建 API Key

2. 设置环境变量
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```

3. 添加到 ~/.bashrc（永久生效）
   ```bash
   echo 'export GEMINI_API_KEY="your_api_key_here"' >> ~/.bashrc
   source ~/.bashrc
   ```

---

### 方式二：直接调用 Gemini API

**配置步骤：**

1. 获取 Gemini API Key（同上）

2. 在本文件中填写配置：
   ```yaml
   gemini_api_key: "your_api_key_here"
   model: "gemini-2.0-flash-exp-image-generation"
   resolution: "2K"  # 可选：2K, 4K
   ```

---

## 环境变量检查

运行以下命令检查配置是否生效：

```bash
echo $GEMINI_API_KEY
```

如果显示 API Key（部分隐藏），说明配置成功。

---

## 测试生成

配置完成后，运行测试：

```bash
python3 scripts/generate-infographic.py --test
```

---

## 故障排查

### 问题 1：API Key 未设置
**错误信息：** `GEMINI_API_KEY is not set`

**解决方案：**
```bash
export GEMINI_API_KEY="your_key"
# 或添加到 ~/.bashrc
```

### 问题 2：uv 未安装
**错误信息：** `uv not found`

**解决方案：**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 问题 3：Nano Banana Pro 脚本不存在
**错误信息：** `Nano Banana Pro script not found`

**解决方案：**
```bash
# 检查路径是否正确
ls ~/.openclaw/workspace/skills/nano-banana-pro/scripts/generate_image.py
```

---

## 推荐使用 Nano Banana Pro 的原因

1. **专业优化** - 针对信息图生成的提示词工程
2. **配色模板** - 内置 Claude 风格、手绘风格等多种配色方案
3. **布局规范** - 自动应用蛇形路径、模块布局等专业设计
4. **批量生成** - 支持一次性生成 1-N 张系列图
5. **错误处理** - 完善的依赖检查和错误提示

---

*配置文件版本：v1.0 | 更新时间：2026-04-14*
