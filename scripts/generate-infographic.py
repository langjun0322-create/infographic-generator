#!/usr/bin/env python3
"""
高密度信息图生成器 - 调用 Nano Banana Pro 生成专业级信息图表
"""

import sys
import subprocess
from datetime import datetime
from pathlib import Path

# Nano Banana Pro 脚本路径
NANO_BANANA_SCRIPT = Path.home() / ".openclaw/workspace/skills/nano-banana-pro/scripts/generate_image.py"


def check_dependencies():
    """检查依赖是否就绪"""
    result = subprocess.run(["command", "-v", "uv"], capture_output=True)
    if result.returncode != 0:
        print("❌ 错误：uv 未安装")
        sys.exit(1)
    
    if not NANO_BANANA_SCRIPT.exists():
        print(f"❌ 错误：Nano Banana Pro 脚本不存在")
        sys.exit(1)
    
    import os
    if not os.environ.get("GEMINI_API_KEY"):
        print("⚠️  GEMINI_API_KEY 未设置")
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
