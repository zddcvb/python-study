import os


class FileCheck(object):
    msg = ""

    @staticmethod
    def check(file_path):
        if os.path.exists(file_path) and os.path.isdir(file_path):
            list_files = os.listdir(file_path)
            if len(list_files) > 0:
                abs_path = os.path.abspath(file_path)
                base_name = os.path.basename(file_path)
                for list_file in list_files:
                    file = abs_path + "/" + list_file
                    file_base_name = os.path.basename(file)
                    if os.path.isfile(file):
                        if list_file.endswith("_data"):
                            if FileCheck.check_data_file(list_file):
                                continue
                            else:
                                return FileCheck.msg
                        elif list_file.endswith("swf") or list_file.endswith("mp4"):
                            if FileCheck.check_swf_and_mp4(file):
                                continue
                            else:
                                return FileCheck.msg
                        elif list_file.endswith("png"):
                            if FileCheck.check_png_file(file):
                                continue
                            else:
                                return FileCheck.msg
                        elif file_base_name == (base_name + ".txt"):
                            continue
                        else:
                            FileCheck.msg = "%s多余" % list_file
                            return FileCheck.msg
                    else:
                        FileCheck.check(file)
        FileCheck.msg = "文件校验成功"
        return FileCheck.msg

    @staticmethod
    def check_data_file(list_file):
        if list_file.endswith("_data"):
            info = list_file.split("_")
            if len(info) < 6:
                FileCheck.msg = list_file + "编写有问题"
                return False
            elif len(info) == 6:
                if info[4] == "1" or info[4] == "0":
                    return True
                return False
        else:
            return False

    @staticmethod
    def check_swf_and_mp4(list_file):
        if list_file.endswith(".mp4"):
            swf_file = list_file.replace("mp4", "swf")
            if os.path.exists(swf_file) == False:
                return True
            else:
                FileCheck.msg = swf_file + "重复出现！！！"
                return False
        if list_file.endswith(".swf"):
            mp4_file = list_file.replace("swf", "mp4")
            if os.path.exists(mp4_file):
                FileCheck.msg = list_file + "重复出现！！！"
                return False
            else:
                return True
        return False

    @staticmethod
    def check_png_file(list_file):
        if list_file.__contains__("_选中.png"):
            icon_unselected_name = list_file.replace("_选中", "_未选中")
            if os.path.exists(icon_unselected_name):
                return True
            else:
                FileCheck.msg = icon_unselected_name + "不存在！"
                return False
        elif list_file.__contains__("_未选中.png"):
            icon_selected_name = list_file.replace("_未选中", "_选中")
            if os.path.exists(icon_selected_name):
                return True
            else:
                FileCheck.msg = icon_selected_name + "不存在！"
                return False
        elif list_file.__contains__("bg.png"):
            return True
        elif list_file.__contains__("_h_0") or list_file.__contains__("_s_0"):
            return True
        else:
            FileCheck.msg = list_file + "多余！"
            return False
        return False


def main():
    result = FileCheck.check("D:/1/咕噜咕噜变")
    print(result)


if __name__ == '__main__':
    main()
