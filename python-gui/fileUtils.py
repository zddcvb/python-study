# -*- coding:utf-8 -*-

import os
from domain import *
from imageUtil import ImageUtil


class FileUtils(object):
    lesson_name = ""

    data_infos = []

    abs_path = ""

    def __init__(self):
        print("---__init__-----")

    def __str__(self):
        return "file_utils"

    def __del__(self):
        print("----__del__----")

    @staticmethod
    def read_file(file_path):
        print("----------read_file-----------------")
        if os.path.isdir(file_path):
            list_files = os.listdir(file_path)
            print(list_files)
            if len(list_files) > 1:
                for list_file in list_files:
                    FileUtils.abs_path = os.path.abspath(file_path)
                    FileUtils.lesson_name = os.path.basename(file_path)
                    abs_file = FileUtils.abs_path + "/" + list_file
                    if os.path.isfile(abs_file):
                        if list_file.endswith("_data"):
                            FileUtils.collect_data_info(list_file)
                    else:
                        FileUtils.read_file(abs_file)
                if len(FileUtils.data_infos) > 0:
                    FileUtils.write_json_data_info(FileUtils.abs_path)

    @staticmethod
    def collect_data_info(list_file):
        FileUtils.data_infos.append(list_file)

    @staticmethod
    def write_json_data_info(abs_path):
        # 创建classDetail类，获取相关的数据
        class_detail = FileUtils.create_class_detail()
        # 将数据写入到json文件
        save_path = abs_path + "/" + FileUtils.lesson_name + ".txt"
        FileUtils.write_json(class_detail, save_path)
        FileUtils.clear_cache()

    @staticmethod
    def create_class_detail():
        print("create_class_detail")
        menus = FileUtils.create_menus()
        # 设置lesson_details
        lesson_details = LessonDetail()
        lesson_details.set_select_menus(menus)
        bg_png = "bg.png"
        lesson_details.set_backgroud_pic(bg_png)
        lesson_details.set_title_animate("%s_标题.mp4" % FileUtils.lesson_name)
        print(lesson_details)
        # 设置class_details
        class_details = ClassDetails()
        class_details.set_lesson_name(FileUtils.lesson_name)
        class_details.set_lesson_detail(lesson_details)
        return class_details

    @staticmethod
    def write_json(class_detail, save_path):
        print("write_json")
        json_dict = {"lesson_name": "", "lesson_detail": {}}
        json_dict["lesson_name"] = class_detail.get_lesson_name()
        lesson_detail = class_detail.lesson_detail
        lesson_dict = {}
        lesson_dict["titile_animate"] = lesson_detail.title_animate
        menus_list = []
        menus = lesson_detail.get_select_menus()
        for menu in menus:
            menu_dict = dict(menu)
            menu_dict.pop("index")
            menus_list.append(menu_dict)
            # menus_list.sort("index")
        lesson_dict["select_menus"] = menus_list
        lesson_dict["backgroud_pic"] = lesson_detail.backgroud_pic
        json_dict["lesson_detail"] = lesson_dict
        print(json_dict)
        # 将json数据写入文件中
        f = open(save_path, "w", encoding="utf-8")
        f.write(str(json_dict))
        f.close()

    @staticmethod
    def create_menus():
        menus = []
        for data_info in FileUtils.data_infos:
            info = str(data_info).split("_")
            menu = Menu()
            menu.set_index(info[0])
            menu.set_menu_title(info[1])
            menu.set_pointx(float(info[2]))
            menu.set_pointy(float(info[3]))
            # 设置两张图片
            icon_selected = "%s_%s_选中.png" % (FileUtils.lesson_name, info[1])
            icon_selected_path = "%s/%s" % (FileUtils.abs_path, icon_selected)
            if os.path.exists(icon_selected_path):
                menu.set_icon_selected(icon_selected)
                # 获取图片的长宽
                png_list = ImageUtil.get_png_wh(icon_selected_path)
                menu.set_icon_width(int(png_list[0]))
                menu.set_icon_height(int(png_list[1]))
            else:
                continue
            icon_unselected = "%s_%s_未选中.png" % (FileUtils.lesson_name, info[1])
            icon_unselected_path = "%s/%s" % (FileUtils.abs_path, icon_unselected)
            if os.path.exists(icon_unselected_path):
                menu.set_icon_unselected(icon_unselected)
            else:
                continue
            # 获取动画文件的格式、文件名称
            file_name = "%s_%s" % (FileUtils.lesson_name, info[1])
            file_info = FileUtils.get_animate_info(file_name)
            if file_info.endswith("mp4"):
                menu.set_attribute("mp4")
                menu.set_video_file(file_info)
                menu.set_guide_animate("")
            elif file_info.endswith("swf"):
                if file_info.endswith("_guide.swf"):
                    menu.set_attribute("mp4")
                    menu.set_guide_animate(file_info)
                    mp4_name = file_info.replace("_guide.swf", "")
                    menu.set_video_file(mp4_name)
                else:
                    menu.set_attribute("swf")
                    menu.set_video_file(file_info)
                    menu.set_guide_animate("")
            else:
                continue
            menus.append(menu)
        return menus

    @staticmethod
    def get_animate_info(file_name):
        swf_name = "%s/%s.swf" % (FileUtils.abs_path, file_name)
        mp4_name = "%s/%s.mp4" % (FileUtils.abs_path, file_name)
        guide_name = "%s/%s_guide.swf" % (FileUtils.abs_path, file_name)
        if os.path.exists(mp4_name):
            if os.path.exists(guide_name):
                return os.path.basename(guide_name)
            return os.path.basename(mp4_name)
        if os.path.exists(swf_name):
            return os.path.basename(swf_name)
        return "swf和mp4文件都不存在！"

    @staticmethod
    def clear_cache():
        if len(FileUtils.data_infos):
            FileUtils.data_infos = []

    @staticmethod
    def file_modify(file_path):
        if os.path.isdir(file_path):
            list_files = os.listdir(file_path)
            if len(list_files) > 0:
                file_abs_path = os.path.abspath(file_path)
                for list_file in list_files:
                    path = file_abs_path + os.altsep + list_file
                    if os.path.isfile(path):
                        if list_file.endswith("_data"):
                            if list_file.endswith("_0_data"):
                                print("已有文件")
                            else:
                                new_path = path.replace("_data", "_0_data")
                                print("new_path:" + new_path)
                                open(new_path, "w")
                                os.remove(path)

                        else:
                            continue
                    else:
                        FileUtils.file_modify(path)
        return "修改成功"


def main():
    file_path = "d:/1/躲猫猫"
    # FileUtils.read_file(file_path)
    FileUtils.file_modify(file_path)


if __name__ == '__main__':
    main()
