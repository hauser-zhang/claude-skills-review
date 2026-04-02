"""
从 gallery.html 截取小红书配图
生成 1080x1440 (3:4) 比例的图片，适合小红书竖版展示
"""

import time
from pathlib import Path

from playwright.sync_api import sync_playwright

OUTPUT_DIR = Path(__file__).parent / "images"
GALLERY_PATH = Path(__file__).parent.parent / "gallery.html"


def capture():
    OUTPUT_DIR.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # 使用移动端视口，模拟小红书阅读体验
        context = browser.new_context(
            viewport={"width": 1080, "height": 1440},
            device_scale_factor=2,
        )
        page = context.new_page()
        page.goto(f"file:///{GALLERY_PATH.as_posix()}")
        time.sleep(2)

        # 截图 1: Hero + 安装 + 目录结构
        page.screenshot(
            path=str(OUTPUT_DIR / "01_hero_install.png"),
            clip={"x": 0, "y": 0, "width": 1080, "height": 1440},
        )
        print("[1/4] Hero + 安装区截图完成")

        # 截图 2: 用户画像 + 装机必备
        page.evaluate("window.scrollTo(0, 1400)")
        time.sleep(1)
        page.screenshot(
            path=str(OUTPUT_DIR / "02_persona_musthave.png"),
            clip={"x": 0, "y": 0, "width": 1080, "height": 1440},
        )
        print("[2/4] 用户画像 + 必备截图完成")

        # 截图 3: 开发者 + 安全
        page.evaluate("window.scrollTo(0, 3200)")
        time.sleep(1)
        page.screenshot(
            path=str(OUTPUT_DIR / "03_dev_security.png"),
            clip={"x": 0, "y": 0, "width": 1080, "height": 1440},
        )
        print("[3/4] 开发者 + 安全截图完成")

        # 截图 4: 研究 + MCP + 路线图
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        page.screenshot(
            path=str(OUTPUT_DIR / "04_research_roadmap.png"),
            clip={"x": 0, "y": 0, "width": 1080, "height": 1440},
        )
        print("[4/4] 研究 + 路线图截图完成")

        browser.close()

    print(f"\n[OK] 4 张配图已保存到 {OUTPUT_DIR}/")


if __name__ == "__main__":
    capture()
