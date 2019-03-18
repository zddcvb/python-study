# -*- coding:utf-8 -*-


class Menu(object):
    __slots__ = ["index", "pointX", "pointY", "iconWidth", "iconHeight", "icon_selected", "icon_unselected",
                 "menu_title", "attribute", "video_file", "guide_animate"]

    def __init__(self):
        super(Menu, self).__init__()

    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index

    def set_pointx(self, pointX):
        self.pointX = pointX

    def get_pointx(self):
        return self.pointX

    def set_pointy(self, pointY):
        self.pointY = pointY

    def get_pointy(self):
        return self.pointY

    def set_icon_width(self, iconWidth):
        self.iconWidth = iconWidth

    def get_icon_width(self):
        return self.iconWidth

    def set_icon_height(self, iconHeight):
        self.iconHeight = iconHeight

    def get_icon_height(self):
        return self.iconHeight

    def set_icon_selected(self, icon_selected):
        self.icon_selected = icon_selected

    def get_icon_selected(self):
        return self.icon_selected

    def set_icon_unselected(self, icon_unselected):
        self.icon_unselected = icon_unselected

    def get_icon_unselected(self):
        return self.icon_unselected

    def set_menu_title(self, menu_title):
        self.menu_title = menu_title

    def get_menu_title(self):
        return self.menu_title

    def set_attribute(self, attribute):
        self.attribute = attribute

    def get_attribute(self):
        return self.attribute

    def set_video_file(self, video_file):
        self.video_file = video_file

    def get_video_file(self):
        return self.video_file

    def set_guide_animate(self, guide_animate):
        self.guide_animate = guide_animate

    def get_guide_animate(self):
        return self.guide_animate

    def keys(self):
        return ("index", "pointX", "pointY", "iconWidth", "iconHeight", "icon_selected", "icon_unselected",
                "menu_title", "attribute", "video_file", "guide_animate")

    def __getitem__(self, item):
        return getattr(self, item)

    def __str__(self):
        result = "index:%s, pointX:%s, pointY:%s, iconWidth:%s,iconHeight:%s,icon_selected:%s,icon_unselected:%s," \
                 "menu_title:%s,attribute:%s,video_file:%s,guide_animate:%s" % (self.index, self.pointX, self.pointY,
                                                                                self.iconWidth, self.iconHeight,
                                                                                self.icon_selected,
                                                                                self.icon_unselected,
                                                                                self.menu_title, self.attribute,
                                                                                self.video_file, self.guide_animate)
        return result


class LessonDetail(object):
    __slots__ = ["title_animate", "select_menus", "backgroud_pic"]

    def __init__(self):
        super(LessonDetail, self).__init__()

    def set_title_animate(self, title_animate):
        self.title_animate = title_animate

    def get_title_animate(self):
        return self.title_animate

    def set_select_menus(self, select_menus):
        self.select_menus = select_menus

    def get_select_menus(self):
        return self.select_menus

    def set_backgroud_pic(self, backgroud_pic):
        self.backgroud_pic = backgroud_pic

    def get_backgroud_pic(self):
        return self.backgroud_pic

    def keys(self):
        return ("title_animate", "select_menus", "backgroud_pic")

    def __getitem__(self, item):
        return getattr(self, item)

    def __str__(self):

        result = "{title_animate:%s, menus:[" % self.title_animate
        if len(self.select_menus) > 1:
            for menu in self.select_menus:
                result += " { %s }, " % menu.__str__()
        result += "],background_pic:%s}" % self.backgroud_pic
        return result


class ClassDetails(object):
    __slots__ = ["lesson_name", "lesson_detail"]

    def __int__(self):
        super(ClassDetails, self).__int__()

    def set_lesson_name(self, lesson_name):
        self.lesson_name = lesson_name

    def get_lesson_name(self):
        return self.lesson_name

    def set_lesson_detail(self, lesson_detail):
        self.lesson_detail = lesson_detail

    def get_lesson_detail(self):
        return self.lesson_detail

    def keys(self):
        return ("lesson_name", "lesson_detail")

    def __getitem__(self, item):
        return getattr(self, item)

    def __str__(self):
        result = "{lesson_name:%s,lesson_detail:%s}" % (self.lesson_name, self.lesson_detail.__str__())
        return result
