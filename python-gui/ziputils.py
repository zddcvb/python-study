import zipfile, os


class ZipUtils(object):
    @staticmethod
    def zip(file_path):
        if os.path.isdir(file_path):
            if ZipUtils.checkisExitsDir(file_path):
                ZipUtils.zip(file_path)
            else:
                print("file_path:" + file_path)
                list_files = os.listdir(file_path)
                base_name = file_path.split(os.altsep)[-1]
                print("base_name:" + base_name)
                zip_name = file_path + os.altsep + base_name + ".zip"
                zip = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
                for list_file in list_files:
                    path = os.path.join(file_path, list_file)
                    ZipUtils.zip_file(path, zip)
                return "success"
        return ""

    @staticmethod
    def checkisExitsDir(path):
        list_files = os.listdir(path)
        for list_file in list_files:
            abs_path = os.path.join(path, list_file)
            if os.path.isdir(abs_path):
                return True
        return False

    @staticmethod
    def zip_file(path, zip):
        print("path:" + path)
        zip.write(path)

def main():
    ZipUtils.zip("D:/1/咕噜咕噜变")


if __name__ == '__main__':
    main()

