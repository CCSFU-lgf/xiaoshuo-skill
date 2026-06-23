# xiaoshuo-skill 使用示例

from xiaoshuo_skill import XiaoShuoSkill

def main():
    """主函数"""
    # 创建技能实例
    skill = XiaoShuoSkill()

    print("=" * 60)
    print("小说创作辅助技能 - 使用示例")
    print("=" * 60)

    # 示例1：检查书名
    print("\n[示例1] 检查书名")
    print("-" * 40)
    book_name = "《重生之都市修仙》"
    result = skill.check_book_name(book_name)
    print(f"书名：{book_name}")
    if result['valid']:
        print("检查结果：书名符合平台规范")
    else:
        print("检查结果：书名不符合平台规范")
    if result['violations']:
        print("违规项：")
        for violation in result['violations']:
            print(f"  - {violation}")
    if result['suggestions']:
        print("修改建议：")
        for suggestion in result['suggestions']:
            print(f"  - {suggestion}")

    # 示例2：匹配标签
    print("\n[示例2] 匹配标签")
    print("-" * 40)
    book_name = "《豪门总裁的替身新娘》"
    result = skill.match_tags(book_name)
    print(f"书名：{book_name}")
    print(f"主分类：{result['main_category']}")
    print(f"主题：{', '.join(result['themes'])}")
    print(f"角色：{', '.join(result['characters'])}")
    print(f"情节：{', '.join(result['plots'])}")
    print(f"匹配置信度：{result['confidence']:.2%}")

    # 示例3：随机生成
    print("\n[示例3] 随机生成标签组合")
    print("-" * 40)
    result = skill.generate_random_tags(count=3)
    for i, (combination, description) in enumerate(zip(result['combinations'], result['descriptions'])):
        print(f"\n组合{i+1}:")
        print(f"  主分类：{combination['main_category']}")
        print(f"  主题：{', '.join(combination['themes'])}")
        print(f"  角色：{', '.join(combination['characters'])}")
        print(f"  情节：{', '.join(combination['plots'])}")
        print(f"  描述：{description}")

    # 示例4：创作指导
    print("\n[示例4] 创作指导")
    print("-" * 40)
    main_category = "豪门总裁"
    themes = ["现代言情", "豪门世家"]
    characters = ["总裁", "大小姐"]
    plots = ["契约婚姻", "先婚后爱"]

    result = skill.get_writing_guidance(main_category, themes, characters, plots)
    print(f"主分类：{main_category}")
    print(f"主题：{', '.join(themes)}")
    print(f"角色：{', '.join(characters)}")
    print(f"情节：{', '.join(plots)}")

    print("\n开篇建议：")
    for tip in result['opening_tips']:
        print(f"  - {tip}")

    print("\n参考作品：")
    for work in result['reference_works']:
        print(f"  - {work}")

    print("\n写作技巧：")
    for tip in result['writing_tips'][:5]:  # 只显示前5条
        print(f"  - {tip}")

    print("\n去AI味建议：")
    for tip in result['avoid_ai_taste'][:5]:  # 只显示前5条
        print(f"  - {tip}")

    # 示例5：获取知识库内容
    print("\n[示例5] 获取知识库内容")
    print("-" * 40)
    platform_rules = skill.get_platform_rules()
    print("平台规则摘要：")
    for rule in platform_rules['basic_requirements'][:3]:  # 只显示前3条
        print(f"  - {rule}")

    content_safety = skill.get_content_safety()
    print("\n内容安全红线：")
    for rule in content_safety['forbidden_content'][:3]:  # 只显示前3条
        print(f"  - {rule}")

    work_tags = skill.get_work_tags()
    print(f"\n作品标签数量：")
    print(f"  主分类：{len(work_tags['main_categories'])}个")
    print(f"  主题：{len(work_tags['themes'])}个")
    print(f"  角色：{len(work_tags['characters'])}个")
    print(f"  情节：{len(work_tags['plots'])}个")

    print("\n" + "=" * 60)
    print("示例结束")
    print("=" * 60)

if __name__ == "__main__":
    main()