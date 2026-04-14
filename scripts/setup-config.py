#!/usr/bin/env python3
"""
配置管理工具 - 首次使用时生成配置文件
"""

import os
import sys
from pathlib import Path

# 配置文件路径
CONFIG_TEMPLATE = """# 信息图生成器配置

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
"""


def check_config_exists(skill_dir: Path) -> bool:
    """检查配置文件是否已存在"""
    config_file = skill_dir / "CONFIG.md"
    return config_file.exists()


def check_env_configured() -> bool:
    """检查环境变量是否已配置"""
    return bool(os.environ.get("GEMINI_API_KEY"))


def create_config_file(skill_dir: Path):
    """创建配置文件"""
    config_file = skill_dir / "CONFIG.md"
    config_file.write_text(CONFIG_TEMPLATE.strip(), encoding='utf-8')
    print(f"✅ 配置文件已创建：{config_file}")


def print_setup_guide():
    """打印配置指南"""
    guide = """
╔═══════════════════════════════════════════════════════════╗
║           🎨 信息图生成器 - 首次配置指南                    ║
╚═══════════════════════════════════════════════════════════╝

📌 推荐使用：Nano Banana Pro ⭐

🔑 配置步骤：

1️⃣  获取 Gemini API Key
   👉 访问：https://aistudio.google.com/apikey

2️⃣  设置环境变量
   👉 运行以下命令（替换 your_api_key 为你的真实 Key）：
   
   export GEMINI_API_KEY="your_api_key"

3️⃣  永久配置（可选）
   👉 添加到 ~/.bashrc：
   
   echo 'export GEMINI_API_KEY="your_api_key"' >> ~/.bashrc
   source ~/.bashrc

4️⃣  验证配置
   👉 运行：echo $GEMINI_API_KEY

✅ 配置完成后，重新运行此脚本即可开始生成信息图！

───────────────────────────────────────────────────────────

💡 为什么推荐 Nano Banana Pro？

• 专为信息图优化的提示词模板
• 内置多种专业配色方案（Claude 风格、手绘风格等）
• 自动应用蛇形路径、模块布局等专业设计
• 支持 2K/4K 分辨率，生成速度快
• 完善的错误处理和质量检查

───────────────────────────────────────────────────────────

📖 详细配置说明请查看：CONFIG.md

"""
    print(guide)


def main():
    """主函数"""
    skill_dir = Path(__file__).parent.parent
    
    print("🔍 检查配置状态...")
    
    # 检查配置文件
    if not check_config_exists(skill_dir):
        print("📝 首次使用，创建配置文件...")
        create_config_file(skill_dir)
    
    # 检查环境变量
    if not check_env_configured():
        print("⚠️  GEMINI_API_KEY 未配置")
        print()
        print_setup_guide()
        
        # 询问用户是否现在配置
        response = input("\n是否现在配置 GEMINI_API_KEY？(y/n): ").strip().lower()
        if response == 'y':
            api_key = input("请输入 Gemini API Key: ").strip()
            if api_key:
                # 设置当前会话的环境变量
                os.environ["GEMINI_API_KEY"] = api_key
                print("✅ 环境变量已设置（当前会话有效）")
                print("\n💡 提示：要永久配置，请运行以下命令：")
                print(f"   echo 'export GEMINI_API_KEY=\"{api_key[:10]}...'\" >> ~/.bashrc")
                print("   source ~/.bashrc")
            else:
                print("❌ 未输入 API Key")
                sys.exit(1)
        else:
            print("\n📖 查看详细配置指南：CONFIG.md")
            sys.exit(0)
    else:
        api_key = os.environ.get("GEMINI_API_KEY", "")
        masked_key = f"{api_key[:10]}...{api_key[-5:]}" if len(api_key) > 15 else "***"
        print(f"✅ GEMINI_API_KEY 已配置：{masked_key}")
        print("\n✨ 配置完成！可以开始生成信息图了～")
        print("\n💡 提示：推荐使用 Nano Banana Pro 获得最佳效果")


if __name__ == "__main__":
    main()
