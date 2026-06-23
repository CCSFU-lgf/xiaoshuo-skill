# xiaoshuo-skill 安装脚本

import os
import sys

def install():
    """安装xiaoshuo-skill"""
    print("=" * 60)
    print("xiaoshuo-skill 安装脚本")
    print("=" * 60)

    # 检查Python版本
    if sys.version_info < (3, 6):
        print("[ERROR] Python版本过低，需要Python 3.6+")
        return False

    print(f"[OK] Python版本: {sys.version}")

    # 检查当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"[OK] 当前目录: {current_dir}")

    # 检查必要文件
    required_files = [
        "xiaoshuo_skill/__init__.py",
        "xiaoshuo_skill/knowledge_base.py",
        "xiaoshuo_skill/book_checker.py",
        "xiaoshuo_skill/tag_matcher.py",
        "xiaoshuo_skill/random_generator.py",
        "xiaoshuo_skill/writing_guide.py"
    ]

    for file in required_files:
        if os.path.exists(file):
            print(f"[OK] 文件存在: {file}")
        else:
            print(f"[ERROR] 文件缺失: {file}")
            return False

    # 验证导入
    try:
        sys.path.insert(0, current_dir)
        from xiaoshuo_skill import XiaoShuoSkill
        print("[OK] 模块导入成功")
    except Exception as e:
        print(f"[ERROR] 模块导入失败: {e}")
        return False

    # 验证功能
    try:
        skill = XiaoShuoSkill()

        # 验证书名检查
        result = skill.check_book_name("《验证书名》")
        print("[OK] 书名检查功能正常")

        # 验证标签匹配
        result = skill.match_tags("《验证书名》")
        print("[OK] 标签匹配功能正常")

        # 验证随机生成
        result = skill.generate_random_tags(count=1)
        print("[OK] 随机生成功能正常")

        # 验证创作指导
        result = skill.get_writing_guidance(
            main_category="豪门总裁",
            themes=["现代言情"],
            characters=["总裁"],
            plots=["契约婚姻"]
        )
        print("[OK] 创作指导功能正常")

    except Exception as e:
        print(f"[ERROR] 功能验证失败: {e}")
        return False

    print("\n" + "=" * 60)
    print("[SUCCESS] xiaoshuo-skill 安装成功！")
    print("=" * 60)

    print("\n使用方法:")
    print("1. 导入模块: from xiaoshuo_skill import XiaoShuoSkill")
    print("2. 创建实例: skill = XiaoShuoSkill()")
    print("3. 使用功能: skill.check_book_name('《书名》')")

    print("\n示例文件:")
    print("- example.py: 基本使用示例")
    print("- demo.py: 功能演示")

    print("\n文档文件:")
    print("- README.md: 项目说明")
    print("- USAGE.md: 使用指南")
    print("- DEVELOPMENT.md: 开发总结")

    return True

def main():
    """主函数"""
    try:
        success = install()
        if success:
            print("\n安装完成！现在可以使用xiaoshuo-skill了。")
        else:
            print("\n安装失败！请检查错误信息。")
            sys.exit(1)
    except Exception as e:
        print(f"\n安装过程中发生错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()