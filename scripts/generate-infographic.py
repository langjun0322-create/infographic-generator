#!/usr/bin/env python3
"""
高密度信息图生成器 - 调用 Nano Banana Pro 生成专业级信息图表
"""

import sys
import subprocess
import os
from datetime import datetime
from pathlib import Path

# 当前脚本所在目录
SCRIPT_DIR = Path(__file__).parent.parent

# Nano Banana Pro 脚本路径
NANO_BANANA_SCRIPT = Path.home() / ".openclaw/workspace/skills/nano-banana-pro/scripts/generate_image.py"

# 配置脚本路径
SETUP_SCRIPT = SCRIPT_DIR / "scripts" / "setup-config.py"


def check_config():
    """检查配置，首次使用时引导用户配置"""
    config_file = SCRIPT_DIR / "CONFIG.md"
    
    # 检查环境变量
    if not os.environ.get("GEMINI_API_KEY"):
        print("⚠️  首次使用检测：GEMINI_API_KEY 未配置")
        print()
        
        # 检查配置脚本是否存在
        if SETUP_SCRIPT.exists():
            print("🚀 启动配置向导...")
            subprocess.run([sys.executable, str(SETUP_SCRIPT)])
            
            # 重新检查环境变量
            if not os.environ.get("GEMINI_API_KEY"):
                print("\n❌ 配置未完成，无法继续")
                print("📖 请查看 CONFIG.md 了解详细配置步骤")
                sys.exit(1)
        else:
            print("📖 请查看 CONFIG.md 了解配置步骤")
            sys.exit(1)
    
    api_key = os.environ.get("GEMINI_API_KEY", "")
    masked_key = f"{api_key[:10]}...{api_key[-5:]}" if len(api_key) > 15 else "***"
    print(f"✅ API 配置就绪：{masked_key}")


def check_dependencies():
    """检查依赖是否就绪"""
    # 先检查配置
    check_config()
    
    # 检查 uv
    result = subprocess.run(["command", "-v", "uv"], capture_output=True)
    if result.returncode != 0:
        print("❌ 错误：uv 未安装")
        print("💡 安装命令：curl -LsSf https://astral.sh/uv/install.sh | sh")
        sys.exit(1)
    
    # 检查 Nano Banana Pro 脚本
    if not NANO_BANANA_SCRIPT.exists():
        print(f"❌ 错误：Nano Banana Pro 脚本不存在")
        print(f"   路径：{NANO_BANANA_SCRIPT}")
        print("💡 请先安装 Nano Banana Pro skill")
        sys.exit(1)


def generate_filename(topic: str, index: int) -> str:
    """生成带时间戳的文件名"""
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    safe_topic = topic.replace(" ", "-").lower()[:20]
    return f"{timestamp}-{safe_topic}-{index:02d}.png"


def generate_image(prompt: str, filename: str, resolution: str = "2K"):
    """调用 Nano Banana Pro 生成图片"""
    cmd = ["uv", "run", str(NANO_BANANA_SCRIPT), "--prompt", prompt, "--filename", filename, "--resolution", resolution]
    
    print(f"🎨 正在生成：{filename} ({resolution})")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ 生成成功")
        return result.stdout.strip()
    else:
        print(f"❌ 生成失败：{result.stderr}")
        return None


def build_prompt(topic: str, description: str, modules: list) -> str:
    """构建信息图生成提示词"""
    modules_text = "\n".join([f"- {m}" for m in modules])
    
    return f"""Create a high-density infographic about「{topic}」. {description}

COLOR PALETTE: Warm Off-White (#F4F1EA), Light Peach→Orange (#ECA882→#E27B58), Deep Rust (#A64B36), Dark Charcoal (#2A2A2A). NO neon/cold colors.

LAYOUT: 6-7 modules with coordinate labels. Lab manual aesthetic. HIGH DENSITY.

MODULES:
{modules_text}

TYPOGRAPHY: Bold Brutalist headers, technical print body.
AVOID: ❌ Cute doodles ❌ Empty space ❌ Flat icons

Aspect Ratio: 3:4. Include "模板 by WaytoAGI" in bottom-right.
"""


def main():
    check_dependencies()
    
    print("🎨 高密度信息图生成器")
    topic = input("主题：").strip()
    description = input("描述：").strip()
    count = int(input("图片数量 (3-10): ").strip())
    
    modules = [
        "BRAND ARRAY: 4x4 or 3x3 matrix",
        "SPECS SCALE: Technical ruler",
        "DEEP DIVE: Technical sketch with callouts",
        "SCENARIO GRID: Comparison cards",
        "WARNING ZONE: Pitfalls to Avoid",
        "QUICK CHECK: Dense summary table",
        "STATUS BAR: Information stack"
    ]
    
    for i in range(1, count + 1):
        filename = generate_filename(topic, i)
        prompt = build_prompt(topic, description, modules)
        generate_image(prompt, filename, "4K")
    
    print("🎉 完成!")


if __name__ == "__main__":
    main()
