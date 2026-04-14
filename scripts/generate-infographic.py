#!/usr/bin/env python3
"""
高密度信息图生成器 - 调用 Nano Banana Pro 生成专业级信息图表

支持两种风格：
- 模板 A：Claude 风格专业知识图谱
- 模板 B：手绘笔记风格（Sketchnote，默认）
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

# 提示词模板路径
PROMPT_TEMPLATE = SCRIPT_DIR / "references" / "infographic-prompt-template.txt"


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
    
    # 检查提示词模板
    if not PROMPT_TEMPLATE.exists():
        print(f"❌ 错误：提示词模板不存在")
        print(f"   路径：{PROMPT_TEMPLATE}")
        sys.exit(1)


def generate_filename(topic: str, index: int, style: str = "B") -> str:
    """生成带时间戳的文件名"""
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    safe_topic = topic.replace(" ", "-").lower()[:20]
    style_prefix = "sketch" if style == "B" else "pro"
    return f"{timestamp}-{style_prefix}-{safe_topic}-{index:02d}.png"


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


def select_style():
    """让用户选择风格"""
    print("\n" + "="*60)
    print("🎨 选择信息图风格")
    print("="*60)
    print("\n【A】Claude 风格 - 高密度专业知识图谱")
    print("   • 专业矢量图标 + 蛇形路径布局")
    print("   • 配色：暖米白背景 + 赤陶红/桃色模块")
    print("   • 适合：技术教程、产品对比、系统架构")
    print("\n【B】手绘笔记风格 - Sketchnote（默认）⭐")
    print("   • 手绘涂鸦 + 马克笔效果 + 网格纸质感")
    print("   • 配色：网格纸背景 + 活力橙色高亮")
    print("   • 适合：头脑风暴、创意笔记、创意构思")
    print("\n" + "="*60)
    
    while True:
        choice = input("\n请选择风格 (A/B，直接回车默认 B): ").strip().upper()
        if choice == "":
            choice = "B"
        
        if choice in ["A", "B"]:
            return choice
        else:
            print("❌ 无效输入，请输入 A 或 B")


def build_prompt(topic: str, description: str, style: str, modules: list) -> str:
    """根据选择的风格构建提示词"""
    
    if style == "A":
        # 模板 A：Claude 风格专业知识图谱
        modules_text = "\n".join([f"- {m}" for m in modules])
        return f"""Create a high-density, professional information design infographic about「{topic}」. {description}

【STYLE】Template A: Claude Style Professional Knowledge Graph

COLOR PALETTE:
- BACKGROUND: Warm Off-White (#F5F2ED)
- HEADER BANNER: Deep Rust (#D97B54) - solid fill
- CORE MODULES: Deep Rust (#D97B54)
- FEATURE MODULES: Light Peach (#F8D7BF)
- INTEGRATION: Dark Charcoal (#2D2926)
- TEXT: White on dark, Dark Charcoal on light
- BORDER: Black 3-4px

LAYOUT:
- Snake Path with 10-23 modules (S-shape winding)
- Short dashed lines with arrows connecting modules
- Module shape: Rounded rectangles (12-16px radius)
- Top banner with title + legend key bar
- Bottom footer with copyright

MODULES:
{modules_text}

TYPOGRAPHY: Inter / PingFang (sans-serif), bold headers, high readability
ASPECT RATIO: 3:4 (portrait)
DENSITY: High information density, minimal margins

AVOID: ❌ Neon colors ❌ 3D effects ❌ Cute doodles ❌ Empty space
"""
    else:
        # 模板 B：手绘笔记风格（默认）
        modules_text = "\n".join([f"- {m}" for m in modules])
        return f"""Create a highly chaotic, hand-drawn Sketchnote style infographic about「{topic}」. {description}

【STYLE】Template B: Hand-drawn Sketchnote Style

COLOR PALETTE:
- BACKGROUND: Grid paper with ink splatters (#F5F5DC)
- INK & TEXT: Charcoal Black (#1A1A1A) with raw marker texture
- ACCENT: Vibrant Safety Orange (#FF7000) for highlights
- HIGHLIGHT: White fine-liner lines for title overlay

VISUAL FEATURES:
- MAIN TITLE: Thick black marker over orange background + white fine-liner tracing
- TYPOGRAPHY: Extremely irregular handwriting, varied size/angle/alignment
- LAYOUT: Chaotic modular clusters with wobbly arrows and doodles
- LINES: Extremely irregular, uneven, natural flow - NO straight lines
- GRAFFITI: Rough chaotic hand-drawn patterns (gears, stick figures, lightbulbs, magnifying glasses, lightning bolts)
- SHADING: Rough quick hand-drawn cross-hatching (diagonal lines) for depth

MODULES:
{modules_text}

MODULE COUNT: 10-15 modules (organic chaotic layout, NO coordinate labels)
ASPECT RATIO: 3:4 (portrait)
DENSITY: High information density with organic chaos

AVOID: ❌ Clean digital fonts ❌ Perfect straight lines ❌ Sterile layout ❌ Machine-perfect alignment
"""


def main():
    check_dependencies()
    
    print("\n" + "="*60)
    print("🎨 高密度信息图生成器")
    print("="*60)
    
    # 选择风格
    style = select_style()
    style_name = "Claude 风格" if style == "A" else "手绘风格"
    print(f"\n✅ 已选择：{style_name}")
    
    # 获取主题和描述
    print("\n📝 请输入信息图内容：")
    topic = input("主题：").strip()
    description = input("描述（可选，直接回车跳过）: ").strip()
    
    if not description:
        description = f"A comprehensive visual guide to {topic}"
    
    # 获取图片数量
    while True:
        try:
            count_str = input("图片数量 (1-10，默认 1): ").strip()
            if count_str == "":
                count = 1
            else:
                count = int(count_str)
                if count < 1 or count > 10:
                    raise ValueError()
            break
        except ValueError:
            print("❌ 无效输入，请输入 1-10 的数字")
    
    # 获取模块内容
    print("\n📋 请输入要展示的核心模块（每行一个，直接回车结束）：")
    modules = []
    while True:
        module = input(f"模块 {len(modules)+1}: ").strip()
        if module == "":
            if len(modules) < 3:
                print("⚠️  至少需要 3 个模块")
            else:
                break
        else:
            modules.append(module)
    
    # 选择分辨率
    print("\n📐 选择分辨率：")
    print("【1】2K (1920x2560) - 推荐，生成快 (~60 秒)")
    print("【2】4K (3840x5120) - 高质量，生成慢 (~120 秒)")
    res_choice = input("请选择 (1/2，默认 1): ").strip()
    resolution = "4K" if res_choice == "2" else "2K"
    
    # 生成图片
    print(f"\n🚀 开始生成 {count} 张{style_name}信息图...")
    print(f"   分辨率：{resolution}")
    print(f"   主题：{topic}")
    print(f"   模块数：{len(modules)}")
    
    for i in range(1, count + 1):
        filename = generate_filename(topic, i, style)
        prompt = build_prompt(topic, description, style, modules)
        result = generate_image(prompt, filename, resolution)
        
        if result:
            print(f"   ✅ [{i}/{count}] 完成：{filename}")
        else:
            print(f"   ❌ [{i}/{count}] 失败")
    
    print("\n" + "="*60)
    print("🎉 生成完成！")
    print("="*60)
    print(f"\n📁 输出目录：{SCRIPT_DIR / 'output'}")
    print(f"🎨 风格：{style_name}")
    print(f"📐 分辨率：{resolution}")
    print(f"📊 总数：{count} 张")


if __name__ == "__main__":
    main()
