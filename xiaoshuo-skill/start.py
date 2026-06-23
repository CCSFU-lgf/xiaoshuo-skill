# xiaoshuo-skill 启动脚本

import sys
import os

def main():
    """主函数"""
    print("=" * 60)
    print("欢迎使用 xiaoshuo-skill 小说创作辅助技能")
    print("=" * 60)

    # 添加当前目录到Python路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, current_dir)

    try:
        from xiaoshuo_skill import XiaoShuoSkill
        print("[OK] 技能加载成功")
    except Exception as e:
        print(f"[ERROR] 技能加载失败: {e}")
        print("请先运行 install.py 安装技能")
        return

    skill = XiaoShuoSkill()

    while True:
        print("\n" + "-" * 60)
        print("请选择功能:")
        print("1. 检查书名")
        print("2. 匹配标签")
        print("3. 随机生成")
        print("4. 创作指导")
        print("5. 查看示例")
        print("0. 退出")
        print("-" * 60)

        choice = input("请输入选项 (0-5): ").strip()

        if choice == "0":
            print("感谢使用 xiaoshuo-skill，再见！")
            break

        elif choice == "1":
            book_name = input("请输入书名: ").strip()
            if book_name:
                result = skill.check_book_name(book_name)
                print(f"\n检查结果:")
                if result['valid']:
                    print("  状态: 符合平台规范")
                else:
                    print("  状态: 不符合平台规范")
                    print("  违规项:")
                    for violation in result['violations']:
                        print(f"    - {violation}")
                    print("  修改建议:")
                    for suggestion in result['suggestions']:
                        print(f"    - {suggestion}")

        elif choice == "2":
            book_name = input("请输入书名: ").strip()
            if book_name:
                result = skill.match_tags(book_name)
                print(f"\n标签匹配结果:")
                print(f"  主分类: {result['main_category']}")
                print(f"  主题: {', '.join(result['themes'])}")
                print(f"  角色: {', '.join(result['characters'])}")
                print(f"  情节: {', '.join(result['plots'])}")
                print(f"  置信度: {result['confidence']:.2%}")

        elif choice == "3":
            count = input("请输入生成数量 (默认3): ").strip()
            count = int(count) if count.isdigit() else 3
            result = skill.generate_random_tags(count=count)
            print(f"\n随机生成 {count} 个标签组合:")
            for i, combo in enumerate(result['combinations']):
                print(f"\n组合 {i+1}:")
                print(f"  主分类: {combo['main_category']}")
                print(f"  主题: {', '.join(combo['themes'])}")
                print(f"  角色: {', '.join(combo['characters'])}")
                print(f"  情节: {', '.join(combo['plots'])}")

        elif choice == "4":
            print("\n请输入标签信息:")
            main_category = input("主分类: ").strip()
            themes = input("主题 (多个用逗号分隔): ").strip().split(',')
            characters = input("角色 (多个用逗号分隔): ").strip().split(',')
            plots = input("情节 (多个用逗号分隔): ").strip().split(',')

            # 清理输入
            themes = [t.strip() for t in themes if t.strip()]
            characters = [c.strip() for c in characters if c.strip()]
            plots = [p.strip() for p in plots if p.strip()]

            if main_category and themes and characters and plots:
                result = skill.get_writing_guidance(main_category, themes, characters, plots)
                print(f"\n创作指导:")
                print("\n开篇建议:")
                for tip in result['opening_tips']:
                    print(f"  - {tip}")
                print("\n参考作品:")
                for work in result['reference_works']:
                    print(f"  - {work}")
                print("\n写作技巧:")
                for tip in result['writing_tips'][:5]:
                    print(f"  - {tip}")
                print("\n去AI味建议:")
                for tip in result['avoid_ai_taste'][:5]:
                    print(f"  - {tip}")
            else:
                print("[ERROR] 请填写完整的标签信息")

        elif choice == "5":
            print("\n运行示例...")
            os.system(f"python {os.path.join(current_dir, 'example.py')}")

        else:
            print("[ERROR] 无效选项，请重新输入")

if __name__ == "__main__":
    main()