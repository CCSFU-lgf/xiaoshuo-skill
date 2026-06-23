# xiaoshuo-skill 使用指南

## 快速开始

### 1. 安装与导入

```python
# 确保在正确的目录中
import sys
sys.path.insert(0, "xiaoshuo-skill")

# 导入技能
from xiaoshuo_skill import XiaoShuoSkill
```

### 2. 基本使用

```python
# 创建技能实例
skill = XiaoShuoSkill()

# 检查书名
result = skill.check_book_name("《重生之都市修仙》")
print(result)

# 匹配标签
result = skill.match_tags("《豪门总裁的替身新娘》")
print(result)

# 随机生成
result = skill.generate_random_tags(count=3)
print(result)

# 创作指导
result = skill.get_writing_guidance(
    main_category="豪门总裁",
    themes=["现代言情", "豪门世家"],
    characters=["总裁", "大小姐"],
    plots=["契约婚姻", "先婚后爱"]
)
print(result)
```

## 功能详解

### 1. 书名检查

检查书名是否符合平台规范，包括：
- 长度检查（2-30字符）
- 敏感词检查
- 特殊字符检查
- 平台名称检查
- 品牌名称检查

```python
# 正常书名
result = skill.check_book_name("《重生之都市修仙》")
# 返回：{'valid': True, 'message': '[OK] 书名符合平台规范', ...}

# 违规书名
result = skill.check_book_name("《赌博人生》")
# 返回：{'valid': False, 'violations': ['书名包含敏感词：赌博'], ...}
```

### 2. 标签匹配

根据书名智能匹配作品标签：
- 主分类（21个）
- 主题（25个）
- 角色（40个）
- 情节（92个）

```python
result = skill.match_tags("《豪门总裁的替身新娘》")
# 返回：
# {
#     'main_category': '豪门总裁',
#     'themes': ['现代言情', '豪门世家'],
#     'characters': ['总裁', '大小姐'],
#     'plots': ['契约婚姻', '先婚后爱'],
#     'confidence': 1.0
# }
```

### 3. 随机生成

为没有明确目标的用户提供随机标签组合：

```python
# 生成3个随机组合
result = skill.generate_random_tags(count=3)

# 生成不重复的组合
result = skill.generate_unique_combinations(count=5)

# 根据分类生成
result = skill.generate_by_category("豪门总裁", count=3)

# 根据主题生成
result = skill.generate_by_theme("现代言情", count=3)
```

### 4. 创作指导

基于标签提供创作建议：
- 开篇建议
- 参考作品
- 写作技巧
- 去AI味建议

```python
result = skill.get_writing_guidance(
    main_category="豪门总裁",
    themes=["现代言情", "豪门世家"],
    characters=["总裁", "大小姐"],
    plots=["契约婚姻", "先婚后爱"]
)

# 获取开篇建议
print(result['opening_tips'])

# 获取参考作品
print(result['reference_works'])

# 获取写作技巧
print(result['writing_tips'])

# 获取去AI味建议
print(result['avoid_ai_taste'])
```

## 高级功能

### 1. 获取知识库内容

```python
# 获取所有知识库内容
knowledge = skill.get_knowledge_base()

# 获取平台规则
rules = skill.get_platform_rules()

# 获取内容安全须知
safety = skill.get_content_safety()

# 获取作品标签
tags = skill.get_work_tags()
```

### 2. 批量处理

```python
# 批量检查书名
book_names = ["《重生之都市修仙》", "《赌博人生》", "《豪门总裁的替身新娘》"]
results = [skill.check_book_name(name) for name in book_names]

# 批量匹配标签
results = [skill.match_tags(name) for name in book_names]
```

## 实际应用场景

### 场景1：新手作者

```python
# 用户不知道写什么
result = skill.generate_random_tags(count=5)
for i, combo in enumerate(result['combinations']):
    print(f"方案{i+1}: {combo['main_category']} + {'+'.join(combo['themes'])}")
```

### 场景2：有明确想法

```python
# 用户有书名
book_name = "《重生之都市修仙》"

# 检查书名
check_result = skill.check_book_name(book_name)
if check_result['valid']:
    # 匹配标签
    tag_result = skill.match_tags(book_name)
    print(f"推荐标签: {tag_result}")

    # 获取创作指导
    guide_result = skill.get_writing_guidance(
        tag_result['main_category'],
        tag_result['themes'],
        tag_result['characters'],
        tag_result['plots']
    )
    print(f"开篇建议: {guide_result['opening_tips']}")
else:
    print(f"书名违规: {check_result['violations']}")
```

### 场景3：需要创作指导

```python
# 用户已选定标签
main_category = "豪门总裁"
themes = ["现代言情", "豪门世家"]
characters = ["总裁", "大小姐"]
plots = ["契约婚姻", "先婚后爱"]

# 获取创作指导
result = skill.get_writing_guidance(main_category, themes, characters, plots)

# 打印开篇建议
print("开篇建议:")
for tip in result['opening_tips']:
    print(f"  - {tip}")

# 打印参考作品
print("\n参考作品:")
for work in result['reference_works']:
    print(f"  - {work}")

# 打印去AI味建议
print("\n去AI味建议:")
for tip in result['avoid_ai_taste']:
    print(f"  - {tip}")
```

## 注意事项

1. **书名检查**：确保书名不包含敏感词和特殊字符
2. **标签匹配**：根据书名内容智能匹配，但可能需要人工调整
3. **随机生成**：确保组合合理，避免矛盾
4. **创作指导**：参考建议，但不要完全依赖
5. **去AI味**：多参考热门作品，加入个人风格

## 常见问题

### Q1: 为什么书名检查不通过？
A1: 可能包含敏感词、特殊字符、平台名称或品牌名称。检查返回的`violations`字段。

### Q2: 标签匹配不准确怎么办？
A2: 可以手动调整标签，或使用`genre_hint`参数提供类型提示。

### Q3: 如何生成不重复的组合？
A3: 使用`generate_unique_combinations()`方法。

### Q4: 创作指导中的参考作品准确吗？
A4: 参考作品是基于标签推荐的同类热门作品，可以作为参考。

## 更新日志

### V0.0.1 (2026-06-23)
- 初始版本发布
- 实现书名检查功能
- 实现标签匹配功能
- 实现随机生成功能
- 实现创作指导功能