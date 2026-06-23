# 书名检查模块

import re
from typing import Dict, List, Tuple

class BookChecker:
    """书名检查类"""

    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        self.forbidden_keywords = self._load_forbidden_keywords()

    def _load_forbidden_keywords(self) -> List[str]:
        """加载敏感关键词"""
        return [
            # 政治敏感
            "习近平", "毛泽东", "邓小平", "江泽民", "胡锦涛", "中国共产党",
            "中华人民共和国", "台湾", "西藏", "新疆", "香港", "六四", "天安门",
            "文化大革命", "大跃进", "反右", "人民公社",

            # 色情暴力
            "强奸", "轮奸", "性交", "做爱", "口交", "肛交", "自慰", "手淫",
            "淫荡", "骚货", "贱人", "婊子", "荡妇", "阴茎", "阴道", "乳房",
            "屁股", "大腿", "内裤", "胸罩", "情趣用品", "安全套", "避孕套",

            # 违法内容
            "赌博", "赌场", "老虎机", "扑克牌", "麻将", "彩票", "炒股",
            "毒品", "海洛因", "冰毒", "大麻", "可卡因", "摇头丸", "K粉",
            "邪教", "法轮功", "全能神", "呼喊派", "门徒会", "血水圣灵",

            # 三观问题
            "自杀", "割腕", "跳楼", "上吊", "服毒", "安乐死",
            "杀人", "放火", "投毒", "爆炸", "绑架", "抢劫", "强奸",

            # 未成年人保护
            "幼女", "幼童", "儿童", "小学生", "初中生", "高中生",
            "恋童", "娈童", "儿童色情", "儿童性侵"
        ]

    def check(self, book_name: str) -> Dict:
        """
        检查书名是否符合平台规范

        Args:
            book_name: 小说书名

        Returns:
            dict: 包含检查结果的字典
        """
        violations = []
        suggestions = []

        # 检查书名长度
        if len(book_name) < 2:
            violations.append("书名过短，至少需要2个字符")
            suggestions.append("请增加书名长度")

        if len(book_name) > 30:
            violations.append("书名过长，建议不超过30个字符")
            suggestions.append("请精简书名")

        # 检查敏感词
        found_forbidden = []
        for keyword in self.forbidden_keywords:
            if keyword in book_name:
                found_forbidden.append(keyword)

        if found_forbidden:
            violations.append(f"书名包含敏感词：{', '.join(found_forbidden)}")
            suggestions.append("请移除或替换敏感词")

        # 检查特殊字符
        special_chars = re.findall(r'[!@#$%^&*()_+=\[\{}|;:,.<>?/~`]', book_name)
        if special_chars:
            violations.append(f"书名包含特殊字符：{''.join(special_chars)}")
            suggestions.append("请移除特殊字符")

        # 检查是否包含数字开头
        if book_name and book_name[0].isdigit():
            violations.append("书名不建议以数字开头")
            suggestions.append("建议以汉字或字母开头")

        # 检查是否包含空格
        if ' ' in book_name:
            violations.append("书名包含空格")
            suggestions.append("建议移除空格或使用下划线")

        # 检查是否包含平台名称
        platform_names = ["起点中文网", "晋江文学城", "红袖添香", "潇湘书院"]
        for platform in platform_names:
            if platform in book_name:
                violations.append(f"书名包含平台名称：{platform}")
                suggestions.append("请移除平台名称")

        # 检查是否包含品牌名称
        brand_names = ["苹果", "华为", "小米", "三星", "索尼", "微软", "谷歌", "百度", "腾讯", "阿里巴巴"]
        for brand in brand_names:
            if brand in book_name:
                violations.append(f"书名包含品牌名称：{brand}")
                suggestions.append("请移除品牌名称")

        return {
            "valid": len(violations) == 0,
            "book_name": book_name,
            "violations": violations,
            "suggestions": suggestions,
            "message": "✅ 书名符合平台规范" if len(violations) == 0 else "❌ 书名不符合平台规范"
        }

    def get_violation_details(self, violation_type: str) -> str:
        """获取违规详情"""
        content_safety = self.kb.get_content_safety()

        if violation_type == "政治敏感":
            return content_safety["forbidden_content"][0]
        elif violation_type == "色情暴力":
            return content_safety["forbidden_content"][1]
        elif violation_type == "违法内容":
            return content_safety["forbidden_content"][2]
        elif violation_type == "三观问题":
            return content_safety["forbidden_content"][3]
        elif violation_type == "未成年人保护":
            return content_safety["forbidden_content"][4]
        else:
            return "未知违规类型"