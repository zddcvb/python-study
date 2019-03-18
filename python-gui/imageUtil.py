from PIL import Image


class ImageUtil(object):
    @staticmethod
    def get_png_wh(png_path):
        image = Image.open(png_path, "r")
        png_list = image.size
        return png_list
