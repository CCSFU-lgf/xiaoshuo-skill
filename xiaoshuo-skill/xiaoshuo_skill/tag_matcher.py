# 标签匹配模块

import re
from typing import Dict, List, Tuple

class TagMatcher:
    """标签匹配类"""

    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        self.tag_keywords = self._load_tag_keywords()

    def _load_tag_keywords(self) -> Dict:
        """加载标签关键词映射"""
        return {
            # 主分类关键词
            "main_categories": {
                "女频悬疑": ["悬疑", "推理", "探案", "灵异", "破案", "侦探", "警察", "刑警"],
                "古风世情": ["古代", "古风", "权谋", "宫斗", "宅斗", "嫡女", "庶女", "丫鬟"],
                "科幻末世": ["末世", "丧尸", "星际", "机甲", "未来", "科技", "太空", "飞船"],
                "女频衍生": ["同人", "衍生", "穿越", "重生", "系统", "金手指"],
                "国民言情": ["民国", "军阀", "少帅", "小姐", "上海滩", "租界"],
                "悬疑脑洞": ["脑洞", "诡异", "惊悚", "规则怪谈", "无限流", "游戏"],
                "青春甜宠": ["校园", "青春", "高中", "大学", "学霸", "学渣", "初恋"],
                "双男主": ["双男主", "耽美", "BL", "男男", "基友"],
                "古言脑洞": ["古言", "穿越", "重生", "系统", "读心术", "金手指"],
                "现言脑洞": ["现代", "都市", "系统", "读心术", "异能", "超能力"],
                "玄幻言情": ["玄幻", "修仙", "修真", "丹药", "御兽", "萌宠", "仙侠", "武侠"],
                "宫斗宅斗": ["宫斗", "宅斗", "后宫", "皇后", "妃子", "太监", "宫女"],
                "豪门总裁": ["豪门", "总裁", "霸总", "首富", "千金", "少爷", "大小姐"],
                "动漫衍生": ["动漫", "二次元", "游戏", "同人", "穿越"],
                "星光璀璨": ["娱乐", "明星", "综艺", "直播", "音综", "演员", "歌手"],
                "游戏体育": ["游戏", "电竞", "体育", "竞技", "网游", "世界游戏化"],
                "职场婚恋": ["职场", "婚姻", "情感", "日常", "白领", "秘书", "助理"],
                "双女主": ["双女主", "百合", "女女", "闺蜜"],
                "年代": ["年代", "穿越", "重生", "空间", "物资超市", "七八十年代"],
                "种田": ["种田", "空间", "灵泉", "逃荒", "远古", "经商", "基建", "科举", "美食"],
                "快穿": ["快穿", "穿越", "小世界", "任务", "系统"]
            },

            # 主题关键词
            "themes": {
                "古言权谋": ["权谋", "政治", "朝堂", "皇帝", "太子", "王爷"],
                "悬疑恋爱": ["悬疑", "恋爱", "推理", "爱情"],
                "纯爱": ["纯爱", "初恋", "暗恋", "单恋"],
                "衍生": ["同人", "衍生", "改编"],
                "仕途": ["仕途", "官场", "升官", "科举"],
                "综影视": ["综影视", "穿越", "电视剧", "电影"],
                "天宅": ["天宅", "宅斗", "家族"],
                "第一人称": ["第一人称", "我", "自述"],
                "赛博朋克": ["赛博朋克", "未来", "科技", "人工智能"],
                "规则怪谈": ["规则怪谈", "诡异", "惊悚", "游戏"],
                "搞笑轻松": ["搞笑", "轻松", "幽默", "喜剧"],
                "古代": ["古代", "古风", "历史"],
                "悬疑": ["悬疑", "推理", "破案"],
                "谍战": ["谍战", "特工", "间谍", "情报"],
                "职场商战": ["职场", "商战", "商业", "公司"],
                "虐恋情深": ["虐恋", "虐心", "痛苦", "分离"],
                "日久生情": ["日久生情", "慢热", "培养感情"],
                "豪门世家": ["豪门", "世家", "家族", "财富"],
                "综漫": ["综漫", "动漫", "二次元"],
                "异世穿越": ["异世", "穿越", "异世界", "魔法"],
                "独宠": ["独宠", "专宠", "宠爱"],
                "现代言情": ["现代", "都市", "言情"],
                "古代言情": ["古代", "古风", "言情"],
                "武侠": ["武侠", "江湖", "武林", "武功"],
                "幻想言情": ["幻想", "奇幻", "魔法", "异能"]
            },

            # 角色关键词
            "characters": {
                "总裁": ["总裁", "CEO", "董事长", "总裁文"],
                "忠犬": ["忠犬", "忠诚", "守护"],
                "全能": ["全能", "全才", "天才"],
                "白切黑": ["白切黑", "腹黑", "隐藏", "伪装"],
                "双学霸": ["学霸", "学神", "成绩好"],
                "位尊权重": ["皇帝", "王爷", "太子", "权臣"],
                "作精": ["作精", "作天作地", "任性"],
                "大佬": ["大佬", "高手", "强者"],
                "大小姐": ["大小姐", "千金", "富家女"],
                "游戏主播": ["主播", "游戏", "直播"],
                "神探": ["侦探", "警察", "刑警", "破案"],
                "将军": ["将军", "武将", "元帅"],
                "毒医": ["毒医", "医术", "毒术"],
                "厨娘": ["厨娘", "厨师", "美食"],
                "律师": ["律师", "法律", "官司"],
                "医生": ["医生", "医院", "手术"],
                "明星": ["明星", "演员", "歌手"],
                "替身": ["替身", "替代", "冒充"],
                "双面": ["双面", "双重身份", "伪装"],
                "冰山": ["冰山", "冷漠", "高冷"],
                "古灵精怪": ["古灵精怪", "调皮", "活泼"],
                "天作之合": ["天作之合", "命中注定", "缘分"],
                "可盐可甜": ["可盐可甜", "多变", "反差"],
                "无CP": ["无CP", "无男主", "无女主"],
                "病娇": ["病娇", "偏执", "占有欲"],
                "反派": ["反派", "坏人", "BOSS"],
                "萌宝": ["萌宝", "宝宝", "孩子"],
                "宠妻": ["宠妻", "宠爱", "老公"],
                "学霸": ["学霸", "学神", "成绩好"],
                "公主": ["公主", "郡主", "格格"],
                "皇后": ["皇后", "王后", "太后"],
                "王妃": ["王妃", "妃子", "侧妃"],
                "女强": ["女强", "女帝", "女王"],
                "皇叔": ["皇叔", "王爷", "摄政王"],
                "嫡女": ["嫡女", "嫡出", "正室"],
                "精灵": ["精灵", "妖精", "妖怪"],
                "天才": ["天才", "神童", "奇才"],
                "腹黑": ["腹黑", "心机", "城府"],
                "扮猪吃虎": ["扮猪吃虎", "低调", "隐藏实力"],
                "团宠": ["团宠", "万人迷", "受宠"]
            },

            # 情节关键词
            "plots": {
                "代嫁代娶": ["代嫁", "代娶", "替嫁"],
                "攻略反派": ["攻略", "反派", "感化"],
                "风水秘术": ["风水", "秘术", "算命"],
                "斩神衍生": ["斩神", "神话", "神仙"],
                "十日衍生": ["十日", "游戏", "生存"],
                "公版衍生": ["公版", "名著", "改编"],
                "红楼衍生": ["红楼", "红楼梦", "贾宝玉"],
                "甄嬛衍生": ["甄嬛", "后宫", "宫斗"],
                "如懿衍生": ["如懿", "乾隆", "清宫"],
                "男二上位": ["男二", "上位", "备胎"],
                "惊悚游戏": ["惊悚", "游戏", "恐怖"],
                "追夫": ["追夫", "倒追", "女追男"],
                "胎穿": ["胎穿", "穿越", "婴儿"],
                "捉鬼": ["捉鬼", "道士", "驱魔"],
                "剑修": ["剑修", "剑道", "剑仙"],
                "相互救赎": ["救赎", "治愈", "相互"],
                "宠夫": ["宠夫", "宠爱", "老公"],
                "无脑爽": ["无脑爽", "爽文", "打脸"],
                "魂穿": ["魂穿", "穿越", "附身"],
                "黑化": ["黑化", "变坏", "堕落"],
                "养崽": ["养崽", "养娃", "带孩子"],
                "年龄差": ["年龄差", "大叔", "萝莉"],
                "真假千金": ["真假千金", "冒充", "身份"],
                "久别重逢": ["久别重逢", "重逢", "分离"],
                "发家致富": ["发家致富", "赚钱", "创业"],
                "养成": ["养成", "培养", "成长"],
                "互宠": ["互宠", "双向宠爱", "互相"],
                "1v1": ["1v1", "一对一", "专一"],
                "灵魂互换": ["灵魂互换", "身体互换", "交换"],
                "科举": ["科举", "考试", "状元"],
                "年下": ["年下", "姐弟恋", "弟弟"],
                "婚恋": ["婚恋", "结婚", "恋爱"],
                "四合院": ["四合院", "大杂院", "邻居"],
                "电竞": ["电竞", "游戏", "比赛"],
                "双重生": ["双重生", "重生", "回到过去"],
                "前世今生": ["前世今生", "轮回", "转世"],
                "双洁": ["双洁", "处男", "处女"],
                "追妻火葬场": ["追妻", "火葬场", "虐男主"],
                "乡村": ["乡村", "农村", "种地"],
                "逃荒": ["逃荒", "饥荒", "流民"],
                "同人": ["同人", "衍生", "改编"],
                "打脸": ["打脸", "逆袭", "装逼"],
                "破案": ["破案", "破案", "推理"],
                "囤物资": ["囤物资", "囤货", "末世"],
                "钓鱼": ["钓鱼", "渔夫", "捕鱼"],
                "HE": ["HE", " happy ending", "圆满"],
                "相爱相杀": ["相爱相杀", "虐恋", "对立"],
                "暗恋": ["暗恋", "单恋", "暗恋"],
                "逃婚": ["逃婚", "逃婚", "拒婚"],
                "带球跑": ["带球跑", "怀孕", "逃跑"],
                "强强": ["强强", "势均力敌", "对手"],
                "一见钟情": ["一见钟情", "钟情", "心动"],
                "双向奔赴": ["双向奔赴", "互相喜欢", "两情相悦"],
                "破镜重圆": ["破镜重圆", "复合", "和好"],
                "契约婚姻": ["契约婚姻", "假结婚", "协议"],
                "隐婚": ["隐婚", "秘密结婚", "隐藏"],
                "闪婚": ["闪婚", "快速结婚", "闪婚"],
                "今穿古": ["今穿古", "现代穿越古代"],
                "古穿今": ["古穿今", "古代穿越现代"],
                "群穿": ["群穿", "集体穿越", "多人穿越"],
                "护短": ["护短", "保护", "维护"],
                "虐渣": ["虐渣", "报复", "惩罚"],
                "情有独钟": ["情有独钟", "专一", "唯一"],
                "马甲": ["马甲", "马甲文", "多重身份"],
                "先婚后爱": ["先婚后爱", "婚后恋爱", "培养感情"],
                "医术": ["医术", "医生", "治病"],
                "女扮男装": ["女扮男装", "男装", "伪装"],
                "青梅竹马": ["青梅竹马", "从小认识", "发小"],
                "无敌": ["无敌", "最强", "碾压"],
                "民国": ["民国", "军阀", "少帅"],
                "穿书": ["穿书", "穿越书中", "书中世界"],
                "职场": ["职场", "工作", "上班"],
                "家庭": ["家庭", "家人", "亲情"],
                "末世": ["末世", "丧尸", "灾难"],
                "直播": ["直播", "主播", "网红"],
                "无限流": ["无限流", "游戏", "副本"],
                "兽世": ["兽世", "兽人", "动物"],
                "清穿": ["清穿", "清朝", "穿越"],
                "星际": ["星际", "太空", "宇宙"],
                "美食": ["美食", "厨师", "吃货"],
                "盗墓": ["盗墓", "古墓", "探险"],
                "虐文": ["虐文", "虐心", "悲剧"],
                "甜宠": ["甜宠", "甜蜜", "宠爱"],
                "灵异": ["灵异", "鬼怪", "恐怖"],
                "校园": ["校园", "学校", "学生"],
                "系统": ["系统", "金手指", "外挂"],
                "重生": ["重生", "回到过去", "重来"],
                "穿越": ["穿越", "异世界", "穿越"],
                "二次元": ["二次元", "动漫", "漫画"],
                "娱乐圏": ["娱乐圏", "明星", "演艺"],
                "空间": ["空间", "随身空间", "仓库"],
                "推理": ["推理", "侦探", "破案"]
            }
        }

    def match(self, book_name: str, genre_hint: str = None) -> Dict:
        """
        根据书名匹配作品标签

        Args:
            book_name: 小说书名
            genre_hint: 类型提示

        Returns:
            dict: 包含推荐标签的字典
        """
        # 分析书名中的关键词
        keywords = self._extract_keywords(book_name)

        # 匹配主分类
        main_category = self._match_main_category(keywords, genre_hint)

        # 匹配主题
        themes = self._match_themes(keywords, main_category)

        # 匹配角色
        characters = self._match_characters(keywords, main_category)

        # 匹配情节
        plots = self._match_plots(keywords, main_category)

        # 计算匹配置信度
        confidence = self._calculate_confidence(keywords, main_category, themes, characters, plots)

        return {
            "book_name": book_name,
            "main_category": main_category,
            "themes": themes,
            "characters": characters,
            "plots": plots,
            "confidence": confidence,
            "keywords_found": keywords
        }

    def _extract_keywords(self, book_name: str) -> List[str]:
        """从书名中提取关键词"""
        # 移除书名号
        clean_name = book_name.replace("《", "").replace("》", "")

        # 分词（简单实现，实际应该使用更复杂的分词算法）
        keywords = []

        # 检查所有标签关键词
        all_keywords = []
        for category in self.tag_keywords.values():
            for tag, kw_list in category.items():
                all_keywords.extend(kw_list)

        # 去重
        all_keywords = list(set(all_keywords))

        # 检查书名中是否包含这些关键词
        for keyword in all_keywords:
            if keyword in clean_name:
                keywords.append(keyword)

        return keywords

    def _match_main_category(self, keywords: List[str], genre_hint: str = None) -> str:
        """匹配主分类"""
        if genre_hint:
            # 如果有类型提示，直接使用
            for category in self.kb.get_work_tags()["main_categories"]:
                if genre_hint in category:
                    return category

        # 根据关键词匹配
        scores = {}
        for category, kw_list in self.tag_keywords["main_categories"].items():
            score = 0
            for keyword in keywords:
                if keyword in kw_list:
                    score += 1
            if score > 0:
                scores[category] = score

        if scores:
            # 返回得分最高的分类
            return max(scores.items(), key=lambda x: x[1])[0]

        # 默认返回豪门总裁（热门分类）
        return "豪门总裁"

    def _match_themes(self, keywords: List[str], main_category: str) -> List[str]:
        """匹配主题"""
        scores = {}
        for theme, kw_list in self.tag_keywords["themes"].items():
            score = 0
            for keyword in keywords:
                if keyword in kw_list:
                    score += 1
            if score > 0:
                scores[theme] = score

        # 按得分排序，取前两个
        sorted_themes = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        themes = [theme for theme, score in sorted_themes[:2]]

        # 如果不足两个，补充默认主题
        default_themes = {
            "女频悬疑": ["悬疑", "悬疑恋爱"],
            "古风世情": ["古代", "古代言情"],
            "科幻末世": ["异世穿越", "幻想言情"],
            "女频衍生": ["衍生", "综影视"],
            "国民言情": ["民国", "现代言情"],
            "悬疑脑洞": ["悬疑", "规则怪谈"],
            "青春甜宠": ["现代言情", "搞笑轻松"],
            "双男主": ["纯爱", "现代言情"],
            "古言脑洞": ["古代", "幻想言情"],
            "现言脑洞": ["现代言情", "幻想言情"],
            "玄幻言情": ["幻想言情", "武侠"],
            "宫斗宅斗": ["古代", "古言权谋"],
            "豪门总裁": ["现代言情", "豪门世家"],
            "动漫衍生": ["衍生", "综漫"],
            "星光璀璨": ["现代言情", "豪门世家"],
            "游戏体育": ["现代言情", "幻想言情"],
            "职场婚恋": ["现代言情", "职场商战"],
            "双女主": ["纯爱", "现代言情"],
            "年代": ["现代言情", "古代"],
            "种田": ["古代", "古代言情"],
            "快穿": ["异世穿越", "幻想言情"]
        }

        while len(themes) < 2 and main_category in default_themes:
            for default_theme in default_themes[main_category]:
                if default_theme not in themes:
                    themes.append(default_theme)
                    break
            break

        return themes

    def _match_characters(self, keywords: List[str], main_category: str) -> List[str]:
        """匹配角色"""
        scores = {}
        for character, kw_list in self.tag_keywords["characters"].items():
            score = 0
            for keyword in keywords:
                if keyword in kw_list:
                    score += 1
            if score > 0:
                scores[character] = score

        # 按得分排序，取前两个
        sorted_characters = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        characters = [character for character, score in sorted_characters[:2]]

        # 如果不足两个，补充默认角色
        default_characters = {
            "女频悬疑": ["神探", "全能"],
            "古风世情": ["嫡女", "大小姐"],
            "科幻末世": ["大佬", "全能"],
            "女频衍生": ["全能", "天才"],
            "国民言情": ["大小姐", "总裁"],
            "悬疑脑洞": ["神探", "天才"],
            "青春甜宠": ["学霸", "古灵精怪"],
            "双男主": ["忠犬", "冰山"],
            "古言脑洞": ["嫡女", "女强"],
            "现言脑洞": ["大佬", "天才"],
            "玄幻言情": ["女强", "天才"],
            "宫斗宅斗": ["嫡女", "女强"],
            "豪门总裁": ["总裁", "大小姐"],
            "动漫衍生": ["天才", "大佬"],
            "星光璀璨": ["明星", "大小姐"],
            "游戏体育": ["游戏主播", "大佬"],
            "职场婚恋": ["总裁", "女强"],
            "双女主": ["大小姐", "女强"],
            "年代": ["女强", "大佬"],
            "种田": ["厨娘", "女强"],
            "快穿": ["大佬", "天才"]
        }

        while len(characters) < 2 and main_category in default_characters:
            for default_character in default_characters[main_category]:
                if default_character not in characters:
                    characters.append(default_character)
                    break
            break

        return characters

    def _match_plots(self, keywords: List[str], main_category: str) -> List[str]:
        """匹配情节"""
        scores = {}
        for plot, kw_list in self.tag_keywords["plots"].items():
            score = 0
            for keyword in keywords:
                if keyword in kw_list:
                    score += 1
            if score > 0:
                scores[plot] = score

        # 按得分排序，取前两个
        sorted_plots = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        plots = [plot for plot, score in sorted_plots[:2]]

        # 如果不足两个，补充默认情节
        default_plots = {
            "女频悬疑": ["破案", "推理"],
            "古风世情": ["宅斗", "宫斗"],
            "科幻末世": ["末世", "重生"],
            "女频衍生": ["穿书", "重生"],
            "国民言情": ["虐恋情深", "破镜重圆"],
            "悬疑脑洞": ["无限流", "规则怪谈"],
            "青春甜宠": ["暗恋", "双向奔赴"],
            "双男主": ["相互救赎", "1v1"],
            "古言脑洞": ["穿越", "重生"],
            "现言脑洞": ["系统", "重生"],
            "玄幻言情": ["修仙", "重生"],
            "宫斗宅斗": ["宫斗", "宅斗"],
            "豪门总裁": ["契约婚姻", "先婚后爱"],
            "动漫衍生": ["穿书", "重生"],
            "星光璀璨": ["娱乐圈", "打脸"],
            "游戏体育": ["电竞", "重生"],
            "职场婚恋": ["职场", "婚恋"],
            "双女主": ["相互救赎", "1v1"],
            "年代": ["重生", "空间"],
            "种田": ["种田", "发家致富"],
            "快穿": ["快穿", "系统"]
        }

        while len(plots) < 2 and main_category in default_plots:
            for default_plot in default_plots[main_category]:
                if default_plot not in plots:
                    plots.append(default_plot)
                    break
            break

        return plots

    def _calculate_confidence(self, keywords: List[str], main_category: str, themes: List[str], characters: List[str], plots: List[str]) -> float:
        """计算匹配置信度"""
        if not keywords:
            return 0.3  # 没有关键词时置信度较低

        # 基础分数
        base_score = 0.1

        # 关键词匹配分数
        keyword_score = len(keywords) * 0.1

        # 主分类匹配分数
        category_score = 0.2 if main_category else 0

        # 主题匹配分数
        theme_score = len(themes) * 0.1

        # 角色匹配分数
        character_score = len(characters) * 0.1

        # 情节匹配分数
        plot_score = len(plots) * 0.1

        total_score = base_score + keyword_score + category_score + theme_score + character_score + plot_score

        # 限制在0-1之间
        return min(1.0, max(0.0, total_score))