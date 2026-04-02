"""
小红书笔记自动发布脚本
使用 Playwright 操作小红书创作者中心发布图文笔记

用法:
  python publish.py                    # 交互模式（先登录再发布）
  python publish.py --login-only       # 仅登录并保存 cookie
  python publish.py --publish-only     # 使用已保存的 cookie 直接发布
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

# ── 配置 ──────────────────────────────────────────────
COOKIE_FILE = Path(__file__).parent / "cookies.json"
IMAGES_DIR = Path(__file__).parent / "images"

NOTE_TITLE = "Claude Code Skills 全景指南 | 100+宝藏技能一键装机"

NOTE_CONTENT = """终于把市面上所有 Claude Code Skills 整理完了！

作为 AI 编程工作站的核心扩展，Skills 才是 Claude Code 真正的效率密码。花了好几天调研了 GitHub 上 100+ 个高 Star 项目，按用户画像分类整理成了一份超全指南。

装机必备 TOP 7：

1. everything-claude-code（133k Star）
整个生态的「操作系统」级框架

2. gstack（62k Star）
YC CEO Garry Tan 的配置，23天暴涨62k

3. antigravity-awesome-skills（30k Star）
1340+ Skills 一键安装

4. planning-with-files（18k Star）
Manus 风格持久化规划

5. humanizer（12k Star）
去除 AI 写作痕迹

6. prompt-master（4.4k Star）
AI 提示词大师

7. claude-code-guide（3.8k Star）
入门到精通指南

分类覆盖：全栈开发 / 安全攻防 / 科研知识管理 / 营销 SEO / 游戏开发 / 写作翻译 / 产品商务 / 设计可视化

仓库还预装了 3 个必备 Skills，克隆即用！

GitHub 搜索：claude-skills-review
作者：hauser-zhang"""

NOTE_TAGS = [
    "ClaudeCode", "AI编程", "Skills", "开发者工具",
    "效率工具", "GitHub", "AI工作站", "编程"
]

CREATOR_URL = "https://creator.xiaohongshu.com/publish/publish"
LOGIN_URL = "https://creator.xiaohongshu.com/login"


def save_cookies(context):
    """保存浏览器 cookie 到文件"""
    cookies = context.cookies()
    COOKIE_FILE.write_text(json.dumps(cookies, ensure_ascii=False, indent=2))
    print(f"[OK] Cookie 已保存到 {COOKIE_FILE}")


def load_cookies(context):
    """从文件加载 cookie"""
    if not COOKIE_FILE.exists():
        return False
    cookies = json.loads(COOKIE_FILE.read_text())
    context.add_cookies(cookies)
    print(f"[OK] Cookie 已从 {COOKIE_FILE} 加载")
    return True


def wait_for_login(page):
    """等待用户手动扫码登录"""
    print("\n" + "=" * 50)
    print("请在浏览器中扫码登录小红书创作者中心")
    print("登录成功后脚本会自动继续...")
    print("=" * 50 + "\n")

    # 等待跳转到创作者后台（最多 5 分钟）
    try:
        page.wait_for_url("**/publish/**", timeout=300_000)
        print("[OK] 登录成功！")
        return True
    except Exception:
        print("[FAIL] 登录超时，请重试")
        return False


def upload_images(page):
    """上传图片（如果 images 目录存在且有图片）"""
    if not IMAGES_DIR.exists():
        print("[INFO] 未找到 images 目录，跳过图片上传")
        return False

    image_files = sorted([
        f for f in IMAGES_DIR.iterdir()
        if f.suffix.lower() in ('.jpg', '.jpeg', '.png', '.webp', '.gif')
    ])

    if not image_files:
        print("[INFO] images 目录为空，跳过图片上传")
        return False

    print(f"[INFO] 找到 {len(image_files)} 张图片，开始上传...")

    # 小红书创作者中心的上传按钮
    upload_input = page.locator('input[type="file"]').first
    for img in image_files:
        upload_input.set_input_files(str(img))
        print(f"  上传: {img.name}")
        time.sleep(2)  # 等待上传完成

    time.sleep(3)
    print("[OK] 图片上传完成")
    return True


def fill_note(page):
    """填写笔记标题和正文"""
    print("[INFO] 填写笔记内容...")

    # 等待编辑器加载
    time.sleep(3)

    # 填写标题
    title_input = page.locator('[placeholder*="标题"]').first
    if title_input.is_visible():
        title_input.click()
        title_input.fill(NOTE_TITLE)
        print(f"  标题: {NOTE_TITLE[:30]}...")
    else:
        # 备用选择器
        title_input = page.locator('.title-input, #title, [class*="title"] input, [class*="title"] textarea').first
        if title_input.is_visible():
            title_input.click()
            title_input.fill(NOTE_TITLE)

    time.sleep(1)

    # 填写正文
    content_area = page.locator('[placeholder*="正文"], [placeholder*="内容"], .ql-editor, [contenteditable="true"]').first
    if content_area.is_visible():
        content_area.click()
        # 使用 keyboard.type 逐字输入（更可靠）
        page.keyboard.type(NOTE_CONTENT, delay=5)
        print("  正文: 已填写")
    else:
        print("[WARN] 未找到正文输入框，请手动填写")

    time.sleep(1)

    # 添加话题标签
    for tag_text in NOTE_TAGS[:5]:  # 小红书限制话题数
        try:
            tag_btn = page.locator('[class*="tag"], [class*="topic"], #add-tag').first
            if tag_btn.is_visible():
                tag_btn.click()
                time.sleep(0.5)
                page.keyboard.type(tag_text, delay=20)
                time.sleep(1)
                # 选择第一个推荐话题
                page.keyboard.press("Enter")
                time.sleep(0.5)
        except Exception:
            pass

    print("[OK] 笔记内容填写完成")


def publish_note(page):
    """点击发布按钮"""
    print("\n[INFO] 准备发布...")
    print("[WARN] 请检查浏览器中的内容是否正确")

    # 等待用户确认
    input("\n按 Enter 键确认发布（或 Ctrl+C 取消）...")

    # 查找发布按钮
    publish_btn = page.locator('button:has-text("发布"), [class*="publish"] button, .submit-btn').first
    if publish_btn.is_visible():
        publish_btn.click()
        print("[OK] 已点击发布按钮")
        time.sleep(5)

        # 检查是否发布成功
        if "success" in page.url or "publish" not in page.url:
            print("[OK] 笔记发布成功！")
        else:
            print("[INFO] 请检查浏览器确认发布状态")
    else:
        print("[WARN] 未找到发布按钮，请手动点击发布")


def main():
    parser = argparse.ArgumentParser(description="小红书笔记发布工具")
    parser.add_argument("--login-only", action="store_true", help="仅登录并保存 cookie")
    parser.add_argument("--publish-only", action="store_true", help="使用已保存 cookie 直接发布")
    args = parser.parse_args()

    print("🐙 Claude Code Skills 全景指南 - 小红书发布工具")
    print("=" * 50)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,  # 必须可视化（需要扫码登录）
            slow_mo=100,
        )
        context = browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        )
        page = context.new_page()

        # 尝试加载已有 cookie
        has_cookies = False
        if args.publish_only:
            has_cookies = load_cookies(context)

        if has_cookies:
            page.goto(CREATOR_URL)
            time.sleep(3)
            # 检查是否真的登录了
            if "login" in page.url:
                print("[WARN] Cookie 已过期，需要重新登录")
                has_cookies = False

        if not has_cookies:
            # 打开登录页
            page.goto(LOGIN_URL)
            time.sleep(2)
            if not wait_for_login(page):
                browser.close()
                return

            # 保存 cookie
            save_cookies(context)

            if args.login_only:
                print("[OK] 仅登录模式，cookie 已保存。下次用 --publish-only 发布")
                browser.close()
                return

            # 导航到发布页
            page.goto(CREATOR_URL)
            time.sleep(3)

        # 上传图片
        upload_images(page)

        # 填写内容
        fill_note(page)

        # 发布
        publish_note(page)

        # 保持浏览器打开一段时间
        print("\n浏览器将在 30 秒后关闭（或按 Ctrl+C 手动关闭）...")
        try:
            time.sleep(30)
        except KeyboardInterrupt:
            pass

        browser.close()

    print("\n[DONE] 完成！")


if __name__ == "__main__":
    main()
