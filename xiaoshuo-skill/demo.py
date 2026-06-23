# xiaoshuo-skill 演示脚本

from xiaoshuo_skill import XiaoShuoSkill

def demo_basic_usage():
    """演示基本使用"""
    print("=" * 60)
    print("xiaoshuo-skill 基本功能演示")
    print("=" * 60)

    # 创建技能实例
    skill = XiaoShuoSkill()

    # 1. 书名检查
    print("\n[1] 书名检查")
    print("-" * 40)
    book_names = [
        "《重生之都市修仙》",
        "《赌博人生》",
        "《豪门总裁的替身新娘》",
        "《色情小说》"
    ]

    for book_name in book_names:
        result = skill.check_book_name(book_name)
        status = "PASS" if result['valid'] else "FAIL"
        print(f"{book_name}: {status}")
        if not result['valid']:
            print(f"  Violations: {result['violations']}")

    # 2. 标签匹配
    print("\n[2] 标签匹配")
    print("-" * 40)
    book_name = "《豪门总裁的替身新娘》"
    result = skill.match_tags(book_name)
    print(f"Book: {book_name}")
    print(f"Category: {result['main_category']}")
    print(f"Themes: {', '.join(result['themes'])}")
    print(f"Characters: {', '.join(result['characters'])}")
    print(f"Plots: {', '.join(result['plots'])}")
    print(f"Confidence: {result['confidence']:.2%}")

    # 3. 随机生成
    print("\n[3] 随机生成")
    print("-" * 40)
    result = skill.generate_random_tags(count=3)
    for i, combo in enumerate(result['combinations']):
        print(f"Combo {i+1}: {combo['main_category']} + {'+'.join(combo['themes'])}")

    # 4. 创作指导
    print("\n[4] 创作指导")
    print("-" * 40)
    result = skill.get_writing_guidance(
        main_category="豪门总裁",
        themes=["现代言情", "豪门世家"],
        characters=["总裁", "大小姐"],
        plots=["契约婚姻", "先婚后爱"]
    )
    print("Opening tips:")
    for tip in result['opening_tips'][:3]:
        print(f"  - {tip}")
    print("Reference works:")
    for work in result['reference_works'][:3]:
        print(f"  - {work}")

def demo_advanced_usage():
    """演示高级功能"""
    print("\n" + "=" * 60)
    print("xiaoshuo-skill 高级功能演示")
    print("=" * 60)

    skill = XiaoShuoSkill()

    # 1. 获取知识库
    print("\n[1] 知识库内容")
    print("-" * 40)
    knowledge = skill.get_knowledge_base()
    print(f"Platform rules: {len(knowledge['platform_rules'])} sections")
    print(f"Content safety: {len(knowledge['content_safety'])} sections")
    print(f"Work tags: {len(knowledge['work_tags'])} categories")

    # 2. 按分类生成
    print("\n[2] 按分类生成")
    print("-" * 40)
    result = skill.generate_by_category("豪门总裁", count=2)
    for i, combo in enumerate(result['combinations']):
        print(f"Combo {i+1}: {combo['main_category']} + {'+'.join(combo['themes'])}")

    # 3. 按主题生成
    print("\n[3] 按主题生成")
    print("-" * 40)
    result = skill.generate_by_theme("现代言情", count=2)
    for i, combo in enumerate(result['combinations']):
        print(f"Combo {i+1}: {combo['main_category']} + {'+'.join(combo['themes'])}")

    # 4. 不重复组合
    print("\n[4] 不重复组合")
    print("-" * 40)
    result = skill.generate_unique_combinations(count=3)
    for i, combo in enumerate(result['combinations']):
        print(f"Combo {i+1}: {combo['main_category']} + {'+'.join(combo['themes'])}")

def demo_practical_scenario():
    """演示实际场景"""
    print("\n" + "=" * 60)
    print("xiaoshuo-skill 实际场景演示")
    print("=" * 60)

    skill = XiaoShuoSkill()

    # 场景1：新手作者
    print("\n[场景1] 新手作者 - 不知道写什么")
    print("-" * 40)
    result = skill.generate_random_tags(count=3)
    print("Recommended combinations:")
    for i, combo in enumerate(result['combinations']):
        print(f"  {i+1}. {combo['main_category']} + {'+'.join(combo['themes'])}")
        print(f"     Characters: {', '.join(combo['characters'])}")
        print(f"     Plots: {', '.join(combo['plots'])}")

    # 场景2：有明确想法
    print("\n[场景2] 有明确想法 - 有书名")
    print("-" * 40)
    book_name = "《重生之都市修仙》"
    print(f"Book name: {book_name}")

    # 检查书名
    check_result = skill.check_book_name(book_name)
    if check_result['valid']:
        print("Book name: PASS")

        # 匹配标签
        tag_result = skill.match_tags(book_name)
        print(f"Category: {tag_result['main_category']}")
        print(f"Themes: {', '.join(tag_result['themes'])}")

        # 获取创作指导
        guide_result = skill.get_writing_guidance(
            tag_result['main_category'],
            tag_result['themes'],
            tag_result['characters'],
            tag_result['plots']
        )
        print("Opening tips:")
        for tip in guide_result['opening_tips'][:2]:
            print(f"  - {tip}")
    else:
        print(f"Book name: FAIL")
        print(f"Violations: {check_result['violations']}")

    # 场景3：需要创作指导
    print("\n[场景3] 需要创作指导 - 已选定标签")
    print("-" * 40)
    main_category = "豪门总裁"
    themes = ["现代言情", "豪门世家"]
    characters = ["总裁", "大小姐"]
    plots = ["契约婚姻", "先婚后爱"]

    print(f"Category: {main_category}")
    print(f"Themes: {', '.join(themes)}")
    print(f"Characters: {', '.join(characters)}")
    print(f"Plots: {', '.join(plots)}")

    result = skill.get_writing_guidance(main_category, themes, characters, plots)
    print("\nWriting guidance:")
    print("Opening tips:")
    for tip in result['opening_tips'][:2]:
        print(f"  - {tip}")
    print("Reference works:")
    for work in result['reference_works'][:2]:
        print(f"  - {work}")

def main():
    """主函数"""
    demo_basic_usage()
    demo_advanced_usage()
    demo_practical_scenario()

    print("\n" + "=" * 60)
    print("Demo completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()