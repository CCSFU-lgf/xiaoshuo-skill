# xiaoshuo-skill 小说创作辅助技能

from .book_checker import BookChecker
from .tag_matcher import TagMatcher
from .random_generator import RandomGenerator
from .writing_guide import WritingGuide
from .knowledge_base import KnowledgeBase

__version__ = "0.0.1"
__author__ = "XiaoShuo Skill Developer"

class XiaoShuoSkill:
    """小说创作辅助技能主类"""

    def __init__(self):
        self.knowledge_base = KnowledgeBase()
        self.book_checker = BookChecker(self.knowledge_base)
        self.tag_matcher = TagMatcher(self.knowledge_base)
        self.random_generator = RandomGenerator(self.knowledge_base)
        self.writing_guide = WritingGuide(self.knowledge_base)

    def check_book_name(self, book_name: str) -> dict:
        """
        检查书名是否符合平台规范

        Args:
            book_name: 小说书名

        Returns:
            dict: 包含检查结果的字典
        """
        return self.book_checker.check(book_name)

    def match_tags(self, book_name: str, genre_hint: str = None) -> dict:
        """
        根据书名匹配作品标签

        Args:
            book_name: 小说书名
            genre_hint: 类型提示

        Returns:
            dict: 包含推荐标签的字典
        """
        return self.tag_matcher.match(book_name, genre_hint)

    def generate_random_tags(self, count: int = 3, avoid_duplicates: bool = True) -> dict:
        """
        生成随机标签组合

        Args:
            count: 生成数量
            avoid_duplicates: 是否避免重复

        Returns:
            dict: 包含随机标签组合的字典
        """
        return self.random_generator.generate(count, avoid_duplicates)

    def get_writing_guidance(self, main_category: str, themes: list, characters: list, plots: list) -> dict:
        """
        获取基于标签的创作指导

        Args:
            main_category: 主分类
            themes: 主题列表
            characters: 角色列表
            plots: 情节列表

        Returns:
            dict: 包含创作指导的字典
        """
        return self.writing_guide.get_guidance(main_category, themes, characters, plots)

    def get_knowledge_base(self) -> dict:
        """获取知识库内容"""
        return self.knowledge_base.get_all()

    def get_platform_rules(self) -> dict:
        """获取平台规则"""
        return self.knowledge_base.get_platform_rules()

    def get_content_safety(self) -> dict:
        """获取内容安全须知"""
        return self.knowledge_base.get_content_safety()

    def get_work_tags(self) -> dict:
        """获取作品标签"""
        return self.knowledge_base.get_work_tags()

    def generate_unique_combinations(self, count: int = 5) -> dict:
        """
        生成不重复的标签组合

        Args:
            count: 生成数量

        Returns:
            dict: 包含不重复标签组合的字典
        """
        return self.random_generator.generate_unique_combinations(count)

    def generate_by_category(self, main_category: str, count: int = 3) -> dict:
        """
        根据主分类生成随机标签组合

        Args:
            main_category: 主分类
            count: 生成数量

        Returns:
            dict: 包含随机标签组合的字典
        """
        return self.random_generator.generate_by_category(main_category, count)

    def generate_by_theme(self, theme: str, count: int = 3) -> dict:
        """
        根据主题生成随机标签组合

        Args:
            theme: 主题
            count: 生成数量

        Returns:
            dict: 包含随机标签组合的字典
        """
        return self.random_generator.generate_by_theme(theme, count)