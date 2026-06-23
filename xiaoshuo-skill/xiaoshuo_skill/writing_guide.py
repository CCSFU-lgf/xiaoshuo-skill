# 写作指导模块

from typing import Dict, List

class WritingGuide:
    """写作指导类"""

    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        self.reference_works = self._load_reference_works()
        self.writing_tips = self._load_writing_tips()

    def _load_reference_works(self) -> Dict:
        """加载参考作品"""
        return {
            "女频悬疑": [
                "《法医秦明》- 法医破案系列",
                "《白夜追凶》- 双胞胎兄弟破案",
                "《无证之罪》- 高智商犯罪",
                "《暗黑者》- 连环杀手"
            ],
            "古风世情": [
                "《知否知否应是绿肥红瘦》- 宅斗经典",
                "《琅琊榜》- 权谋复仇",
                "《甄嬛传》- 后宫争斗",
                "《庶女攻略》- 宅斗权谋"
            ],
            "科幻末世": [
                "《末世重生之归来》- 末世重生",
                "《星际之全能进化》- 星际机甲",
                "《末日乐园》- 末世生存",
                "《星际之大帅威武》- 星际战争"
            ],
            "女频衍生": [
                "《穿越之福临门》- 穿越种田",
                "《重生之将门毒后》- 重生复仇",
                "《穿越之农女医妃》- 穿越医术",
                "《重生之嫡女祸妃》- 重生宅斗"
            ],
            "国民言情": [
                "《来不及说我爱你》- 民国爱情",
                "《人生若如初相见》- 民国军阀",
                "《锦心似玉》- 民国宅斗",
                "《鬓边不是海棠红》- 民国戏曲"
            ],
            "悬疑脑洞": [
                "《全球高武》- 武道修炼",
                "《诡秘之主》- 克苏鲁风格",
                "《惊悚乐园》- 恐怖游戏",
                "《我有一座冒险屋》- 恐怖冒险"
            ],
            "青春甜宠": [
                "《你好，旧时光》- 校园青春",
                "《最好的我们》- 校园暗恋",
                "《致我们终将逝去的青春》- 青春爱情",
                "《微微一笑很倾城》- 校园网游"
            ],
            "双男主": [
                "《魔道祖师》- 耽美经典",
                "《天官赐福》- 仙侠耽美",
                "《镇魂》- 都市灵异",
                "《默读》- 悬疑推理"
            ],
            "古言脑洞": [
                "《凤囚凰》- 穿越古言",
                "《锦绣未央》- 古言复仇",
                "《花千骨》- 仙侠古言",
                "《三生三世十里桃花》- 仙侠爱情"
            ],
            "现言脑洞": [
                "《我的前半生》- 都市情感",
                "《欢乐颂》- 都市生活",
                "《都挺好》- 家庭伦理",
                "《三十而已》- 都市女性"
            ],
            "玄幻言情": [
                "《花千骨》- 仙侠虐恋",
                "《三生三世十里桃花》- 仙侠爱情",
                "《香蜜沉沉烬如霜》- 仙侠甜宠",
                "《琉璃美人煞》- 仙侠修真"
            ],
            "宫斗宅斗": [
                "《甄嬛传》- 宫斗经典",
                "《如懿传》- 清宫宫斗",
                "《延禧攻略》- 宫斗爽文",
                "《知否知否应是绿肥红瘦》- 宅斗经典"
            ],
            "豪门总裁": [
                "《总裁在上》- 豪门宠文",
                "《亿万老婆买一送一》- 豪门甜宠",
                "《豪门蜜婚：老公大人宠上瘾》- 豪门甜宠",
                "《总裁的替身前妻》- 豪门虐恋"
            ],
            "动漫衍生": [
                "《火影之最强系统》- 火影同人",
                "《海贼王之草帽副船长》- 海贼同人",
                "《名侦探柯南之暗夜协奏曲》- 柯南同人",
                "《龙珠之最强神话》- 龙珠同人"
            ],
            "星光璀璨": [
                "《影帝的公主》- 娱乐圈甜宠",
                "《国民老公带回家》- 娱乐圈爱情",
                "《娱乐圈之女王在上》- 娱乐圈逆袭",
                "《影后重生：总裁大人，求放过》- 娱乐圈重生"
            ],
            "游戏体育": [
                "《全职高手》- 电竞经典",
                "《穿越火线之电竞传奇》- 电竞竞技",
                "《篮球之黄金时代》- 体育竞技",
                "《足球之超级巨星》- 体育竞技"
            ],
            "职场婚恋": [
                "《杜拉拉升职记》- 职场升职",
                "《欢乐颂》- 都市生活",
                "《我的前半生》- 婚姻情感",
                "《都挺好》- 家庭伦理"
            ],
            "双女主": [
                "《她和她的猫》- 双女主情感",
                "《七月与安生》- 双女主友情",
                "《流金岁月》- 双女主友情",
                "《我的天才女友》- 双女主友情"
            ],
            "年代": [
                "《重生之将门毒后》- 重生复仇",
                "《穿越之农女医妃》- 穿越医术",
                "《重生之嫡女祸妃》- 重生宅斗",
                "《穿越之福临门》- 穿越种田"
            ],
            "种田": [
                "《农门福女》- 种田经商",
                "《田园小药娘》- 种田医术",
                "《农女有田：娘子，很彪悍》- 种田女强",
                "《穿越之农女医妃》- 种田医术"
            ],
            "快穿": [
                "《快穿之打脸狂魔》- 快穿打脸",
                "《快穿之拯救反派》- 快穿攻略",
                "《快穿之炮灰女配》- 快穿逆袭",
                "《快穿之完美命运》- 快穿系统"
            ]
        }

    def _load_writing_tips(self) -> Dict:
        """加载写作技巧"""
        return {
            "opening_tips": {
                "女频悬疑": [
                    "第一章：设置悬疑案件，引发读者好奇心",
                    "第二章：引入主角，展现专业能力",
                    "第三章：案件升级，增加紧张感"
                ],
                "古风世情": [
                    "第一章：展现家族背景，设置矛盾冲突",
                    "第二章：主角登场，展现智慧或特殊能力",
                    "第三章：第一次危机，主角化解"
                ],
                "科幻末世": [
                    "第一章：末世降临，展现危机",
                    "第二章：主角觉醒特殊能力",
                    "第三章：第一次生存挑战"
                ],
                "豪门总裁": [
                    "第一章：男女主角相遇，制造冲突",
                    "第二章：展现男主强大气场",
                    "第三章：设置悬念，如契约、替身"
                ]
            },
            "writing_tips": {
                "general": [
                    "黄金三章：前三章必须有强烈冲突和悬念",
                    "爽点密集：每章至少一个小爽点或反转",
                    "节奏紧凑：不要大段心理描写，多用对话推进",
                    "钩子结尾：每章结尾留悬念，让读者追更",
                    "人设鲜明：主角有明确的金手指/优势",
                    "打脸套路：反派小瞧主角 → 主角逆袭打脸"
                ],
                "去_ai_taste": [
                    "避免使用过于完美的对话，加入口语化表达",
                    "减少形容词堆砌，多用动词推进情节",
                    "加入生活化细节，增加真实感",
                    "避免说教式心理描写，通过行动展现性格",
                    "使用网络流行语和热门梗，增加时代感",
                    "加入小缺点和矛盾，让人物更立体"
                ]
            },
            "avoid_ai_taste": [
                "避免使用'不禁'、'竟然'、'居然'等AI常用词",
                "减少'仿佛'、'好像'、'似乎'等模糊词汇",
                "不要过度使用排比句和对仗句",
                "避免说教式心理描写，通过行动展现",
                "加入口语化表达和网络用语",
                "使用具体细节代替笼统描述",
                "加入小缺点和矛盾，让人物更真实",
                "避免过于完美的情节发展"
            ]
        }

    def get_guidance(self, main_category: str, themes: List[str], characters: List[str], plots: List[str]) -> Dict:
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
        # 获取开篇建议
        opening_tips = self._get_opening_tips(main_category, themes, characters, plots)

        # 获取参考作品
        reference_works = self._get_reference_works(main_category, themes)

        # 获取写作技巧
        writing_tips = self._get_writing_tips(main_category, themes, characters, plots)

        # 获取去AI味建议
        avoid_ai_taste = self._get_avoid_ai_taste(main_category, themes, characters, plots)

        return {
            "main_category": main_category,
            "themes": themes,
            "characters": characters,
            "plots": plots,
            "opening_tips": opening_tips,
            "reference_works": reference_works,
            "writing_tips": writing_tips,
            "avoid_ai_taste": avoid_ai_taste
        }

    def _get_opening_tips(self, main_category: str, themes: List[str], characters: List[str], plots: List[str]) -> List[str]:
        """获取开篇建议"""
        tips = []

        # 基础开篇建议
        if main_category in self.writing_tips["opening_tips"]:
            tips.extend(self.writing_tips["opening_tips"][main_category])
        else:
            tips.extend([
                "第一章：设置强烈冲突，吸引读者",
                "第二章：展现主角魅力和能力",
                "第三章：设置悬念，让读者想继续看"
            ])

        # 根据情节补充建议
        if "重生" in plots:
            tips.append("重生文开篇：快速交代重生背景，展现主角优势")
        if "穿越" in plots:
            tips.append("穿越文开篇：快速适应新环境，展现代差优势")
        if "系统" in plots:
            tips.append("系统文开篇：合理设置系统功能，避免过于强大")
        if "宫斗" in plots or "宅斗" in plots:
            tips.append("宫斗/宅斗开篇：快速建立人物关系，设置阵营对立")

        return tips

    def _get_reference_works(self, main_category: str, themes: List[str]) -> List[str]:
        """获取参考作品"""
        works = []

        # 主分类参考作品
        if main_category in self.reference_works:
            works.extend(self.reference_works[main_category])

        # 根据主题补充参考作品
        theme_work_mapping = {
            "古言权谋": ["《琅琊榜》- 权谋复仇", "《庆余年》- 权谋科幻"],
            "悬疑恋爱": ["《法医秦明》- 悬疑爱情", "《暗黑者》- 悬疑推理"],
            "纯爱": ["《魔道祖师》- 耽美经典", "《天官赐福》- 仙侠耽美"],
            "衍生": ["各类同人作品参考"],
            "仕途": ["《侯卫东官场笔记》- 官场小说", "《二号首长》- 官场小说"],
            "综影视": ["各类影视同人作品"],
            "天宅": ["宅斗类作品参考"],
            "第一人称": ["第一人称叙事作品"],
            "赛博朋克": ["《神经漫游者》- 赛博朋克经典"],
            "规则怪谈": ["《规则怪谈》系列作品"],
            "搞笑轻松": ["轻松搞笑类作品"],
            "古代": ["古代背景作品"],
            "悬疑": ["悬疑推理类作品"],
            "谍战": ["《潜伏》- 谍战经典", "《风筝》- 谍战剧"],
            "职场商战": ["《杜拉拉升职记》- 职场小说"],
            "虐恋情深": ["虐恋类作品"],
            "日久生情": ["慢热型爱情作品"],
            "豪门世家": ["豪门类作品"],
            "综漫": ["动漫同人作品"],
            "异世穿越": ["穿越异世界作品"],
            "独宠": ["独宠类甜文"],
            "现代言情": ["现代都市爱情作品"],
            "古代言情": ["古代爱情作品"],
            "武侠": ["武侠类作品"],
            "幻想言情": ["幻想类爱情作品"]
        }

        for theme in themes:
            if theme in theme_work_mapping:
                works.extend(theme_work_mapping[theme])

        # 去重
        works = list(set(works))

        return works[:5]  # 最多返回5个参考作品

    def _get_writing_tips(self, main_category: str, themes: List[str], characters: List[str], plots: List[str]) -> List[str]:
        """获取写作技巧"""
        tips = []

        # 通用写作技巧
        tips.extend(self.writing_tips["writing_tips"]["general"])

        # 根据主分类补充技巧
        category_tips = {
            "女频悬疑": [
                "悬疑文要注重逻辑推理，避免漏洞",
                "设置合理的线索和误导",
                "保持紧张感，但不要过于压抑"
            ],
            "古风世情": [
                "古风文要注重语言风格，避免现代词汇",
                "了解古代礼仪和文化背景",
                "宅斗文要注重人际关系描写"
            ],
            "科幻末世": [
                "末世文要注重生存细节描写",
                "科幻设定要合理，避免过于离谱",
                "保持紧张感和危机感"
            ],
            "豪门总裁": [
                "总裁文要注重男女主角的气场描写",
                "甜宠文要适度，避免过于腻歪",
                "设置合理的冲突和矛盾"
            ]
        }

        if main_category in category_tips:
            tips.extend(category_tips[main_category])

        # 根据情节补充技巧
        if "重生" in plots:
            tips.append("重生文要合理利用前世记忆，避免过于强大")
        if "穿越" in plots:
            tips.append("穿越文要处理好时代差异，避免违和感")
        if "系统" in plots:
            tips.append("系统文要合理设置系统限制，避免无脑开挂")

        return tips

    def _get_avoid_ai_taste(self, main_category: str, themes: List[str], characters: List[str], plots: List[str]) -> List[str]:
        """获取去AI味建议"""
        tips = []

        # 通用去AI味建议
        tips.extend(self.writing_tips["avoid_ai_taste"])

        # 根据主分类补充建议
        category_avoid_tips = {
            "女频悬疑": [
                "避免过于完美的推理过程",
                "加入主角的困惑和失误",
                "使用口语化的对话"
            ],
            "古风世情": [
                "避免过于现代化的对话",
                "加入古风词汇但不要过度",
                "使用生活化细节"
            ],
            "豪门总裁": [
                "避免过于完美的总裁形象",
                "加入生活化场景",
                "使用接地气的对话"
            ]
        }

        if main_category in category_avoid_tips:
            tips.extend(category_avoid_tips[main_category])

        return tips