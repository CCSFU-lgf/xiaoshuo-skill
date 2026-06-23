# 随机生成模块

import random
from typing import Dict, List

class RandomGenerator:
    """随机生成类"""

    def __init__(self, knowledge_base):
        self.kb = knowledge_base

    def generate(self, count: int = 3, avoid_duplicates: bool = True) -> Dict:
        """
        生成随机标签组合

        Args:
            count: 生成数量
            avoid_duplicates: 是否避免重复

        Returns:
            dict: 包含随机标签组合的字典
        """
        work_tags = self.kb.get_work_tags()

        combinations = []
        descriptions = []

        for i in range(count):
            # 随机选择主分类
            main_category = random.choice(work_tags["main_categories"])

            # 随机选择主题（1-2个）
            theme_count = random.randint(1, 2)
            themes = random.sample(work_tags["themes"], theme_count)

            # 随机选择角色（1-2个）
            character_count = random.randint(1, 2)
            characters = random.sample(work_tags["characters"], character_count)

            # 随机选择情节（1-2个）
            plot_count = random.randint(1, 2)
            plots = random.sample(work_tags["plots"], plot_count)

            # 生成描述
            description = self._generate_description(main_category, themes, characters, plots)

            combinations.append({
                "main_category": main_category,
                "themes": themes,
                "characters": characters,
                "plots": plots
            })

            descriptions.append(description)

        return {
            "combinations": combinations,
            "descriptions": descriptions,
            "count": count
        }

    def _generate_description(self, main_category: str, themes: List[str], characters: List[str], plots: List[str]) -> str:
        """生成组合描述"""
        # 构建描述
        theme_str = "、".join(themes)
        character_str = "、".join(characters)
        plot_str = "、".join(plots)

        descriptions = [
            f"这是一个{main_category}类小说，融合了{theme_str}元素，主角是{character_str}，主要情节包括{plot_str}。",
            f"想要写{main_category}？可以尝试{theme_str}风格，塑造{character_str}类型的角色，加入{plot_str}等情节。",
            f"{main_category}爱好者可以尝试：{theme_str}主题 + {character_str}角色 + {plot_str}情节的组合。",
            f"推荐组合：{main_category} + {theme_str} + {character_str} + {plot_str}，这是一个很有潜力的搭配。"
        ]

        return random.choice(descriptions)

    def generate_by_category(self, main_category: str, count: int = 3) -> Dict:
        """
        根据主分类生成随机标签组合

        Args:
            main_category: 主分类
            count: 生成数量

        Returns:
            dict: 包含随机标签组合的字典
        """
        work_tags = self.kb.get_work_tags()

        if main_category not in work_tags["main_categories"]:
            return {
                "error": f"无效的主分类：{main_category}",
                "valid_categories": work_tags["main_categories"]
            }

        combinations = []
        descriptions = []

        for i in range(count):
            # 随机选择主题（1-2个）
            theme_count = random.randint(1, 2)
            themes = random.sample(work_tags["themes"], theme_count)

            # 随机选择角色（1-2个）
            character_count = random.randint(1, 2)
            characters = random.sample(work_tags["characters"], character_count)

            # 随机选择情节（1-2个）
            plot_count = random.randint(1, 2)
            plots = random.sample(work_tags["plots"], plot_count)

            # 生成描述
            description = self._generate_description(main_category, themes, characters, plots)

            combinations.append({
                "main_category": main_category,
                "themes": themes,
                "characters": characters,
                "plots": plots
            })

            descriptions.append(description)

        return {
            "combinations": combinations,
            "descriptions": descriptions,
            "count": count,
            "main_category": main_category
        }

    def generate_by_theme(self, theme: str, count: int = 3) -> Dict:
        """
        根据主题生成随机标签组合

        Args:
            theme: 主题
            count: 生成数量

        Returns:
            dict: 包含随机标签组合的字典
        """
        work_tags = self.kb.get_work_tags()

        if theme not in work_tags["themes"]:
            return {
                "error": f"无效的主题：{theme}",
                "valid_themes": work_tags["themes"]
            }

        combinations = []
        descriptions = []

        for i in range(count):
            # 随机选择主分类
            main_category = random.choice(work_tags["main_categories"])

            # 随机选择另一个主题（1个）
            other_themes = [t for t in work_tags["themes"] if t != theme]
            themes = [theme] + random.sample(other_themes, 1)

            # 随机选择角色（1-2个）
            character_count = random.randint(1, 2)
            characters = random.sample(work_tags["characters"], character_count)

            # 随机选择情节（1-2个）
            plot_count = random.randint(1, 2)
            plots = random.sample(work_tags["plots"], plot_count)

            # 生成描述
            description = self._generate_description(main_category, themes, characters, plots)

            combinations.append({
                "main_category": main_category,
                "themes": themes,
                "characters": characters,
                "plots": plots
            })

            descriptions.append(description)

        return {
            "combinations": combinations,
            "descriptions": descriptions,
            "count": count,
            "theme": theme
        }

    def generate_unique_combinations(self, count: int = 5) -> Dict:
        """
        生成不重复的标签组合

        Args:
            count: 生成数量

        Returns:
            dict: 包含不重复标签组合的字典
        """
        work_tags = self.kb.get_work_tags()

        combinations = []
        descriptions = []
        seen_combinations = set()

        attempts = 0
        max_attempts = count * 10  # 防止无限循环

        while len(combinations) < count and attempts < max_attempts:
            attempts += 1

            # 随机选择主分类
            main_category = random.choice(work_tags["main_categories"])

            # 随机选择主题（1-2个）
            theme_count = random.randint(1, 2)
            themes = random.sample(work_tags["themes"], theme_count)

            # 随机选择角色（1-2个）
            character_count = random.randint(1, 2)
            characters = random.sample(work_tags["characters"], character_count)

            # 随机选择情节（1-2个）
            plot_count = random.randint(1, 2)
            plots = random.sample(work_tags["plots"], plot_count)

            # 创建组合标识
            combination_key = f"{main_category}|{'、'.join(sorted(themes))}|{'、'.join(sorted(characters))}|{'、'.join(sorted(plots))}"

            # 检查是否重复
            if combination_key not in seen_combinations:
                seen_combinations.add(combination_key)

                # 生成描述
                description = self._generate_description(main_category, themes, characters, plots)

                combinations.append({
                    "main_category": main_category,
                    "themes": themes,
                    "characters": characters,
                    "plots": plots
                })

                descriptions.append(description)

        return {
            "combinations": combinations,
            "descriptions": descriptions,
            "count": len(combinations),
            "unique": True
        }