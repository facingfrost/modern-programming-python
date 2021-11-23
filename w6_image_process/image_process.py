from PIL import Image
import PIL.ImageFilter
import PIL.ImageEnhance
import os
import matplotlib.pyplot as plt


class Filter:
    def __init__(self, image):
        self.image = image

    def filter(self):
        pass


class EdgeExtraction(Filter):
    def filter(self):
        self.image = self.image.filter(PIL.ImageFilter.FIND_EDGES)
        return self.image


class Sharpen(Filter):
    def filter(self):
        self.image = self.image.filter(PIL.ImageFilter.SHARPEN)
        return self.image


class Blur(Filter):
    def filter(self):
        self.image = self.image.filter(PIL.ImageFilter.BLUR)
        return self.image


class Resize(Filter):

    def filter(self, ratio):
        '''
        :param ratio: 调整大小的比例
        :return:
        '''
        width = self.image.size[0]  # 获取宽度
        height = self.image.size[1]  # 获取高度
        self.image = self.image.resize((int(width * ratio), int(height * ratio)), Image.ANTIALIAS)
        return self.image


class Bright(Filter):

    def filter(self, factor_num):
        '''
        :param factor_num: 增强亮度的参数
        :return:
        '''
        enh_bri = PIL.ImageEnhance.Brightness(self.image)
        self.image = enh_bri.enhance(factor=factor_num)
        return self.image


class ImageShop:
    def __init__(self, path, file_format):
        '''
        :param path: 要处理的图片路径
        :param file_format: 图片格式
        '''
        # 图片路径
        self.path = path
        # 图片格式
        self.file_format = file_format
        # 图片实例
        self.image = []
        # 处理之后的图片
        self.adjusted = []
        # 存储操作
        self.operation = []

    def load_images(self):
        '''
        :return: 加载指定路径下指定格式的所有图片到类中
        '''
        if self.path[-1] == "/":
            for f_name in os.listdir(self.path):
                if f_name.endswith(self.file_format):
                    now_directory = self.path + f_name
                    self.image.append(Image.open(now_directory))
        else:
            self.image.append(Image.open(self.path))

    def __batch_ps(self, img_order):
        '''
        对指定的图片进行处理
        :param img_order: 要处理的图片在self.image中的索引
        :return:
        '''
        for j in self.operation:
            if j[0] == "EdgeExtraction":
                self.image[img_order] = EdgeExtraction(self.image[img_order]).filter()
                print("EdgeExtraction!")
            elif j[0] == "Sharpen":
                self.image[img_order] = Sharpen(self.image[img_order]).filter()
                print("Sharpen!")
            elif j[0] == "Blur":
                self.image[img_order] = Blur(self.image[img_order]).filter()
                print("Blur!")
            elif j[0] == "Resize":
                self.image[img_order] = Resize(self.image[img_order]).filter(j[1])
                print("Resize!")
            else:
                self.image[img_order] = Bright(self.image[img_order]).filter(j[1])
                print("Bright!")

    def batch_ps(self, operation):
        '''
        输入每一张图片到__batch_ps()
        :param operation: 存储操作参数的列表，元素是元组，元组的第一个元素是操作名，后面的元素是参数
        :return:
        '''
        self.operation = operation
        for origin_img_order in range(len(self.image)):
            self.__batch_ps(origin_img_order)
        self.adjusted = self.image

    def display(self, row_num, col_num, sum_num):
        '''
        :param row_num: 显示行数
        :param col_num: 显示列数
        :param sum_num: 显示的最大图片数量
        :return:
        '''
        for img_num in range(1, sum_num + 1):
            plt.subplot(row_num, col_num, img_num)
            plt.imshow(self.adjusted[img_num - 1])
            plt.axis('off')
        plt.show()

    def save(self, save_path, output_format):
        '''
        :param save_path: 保存路径
        :param output_format: 输出图片格式
        :return:
        '''
        for i in range(len(self.adjusted)):
            self.adjusted[i].save(save_path + str(i) + output_format)


class TestImageShop(ImageShop):
    def __init__(self, path, file_format, operation, output_path, row_num, col_num, sum_num):
        '''
        :param path: 输入图片路径
        :param file_format: 图片格式
        :param operation: 操作参数
        :param output_path: 输出路径
        :param row_num: 展示的行数
        :param col_num: 展示的列数
        :param sum_num: 展示的最大图片数量
        '''
        super().__init__(path, file_format)
        self.operation = operation
        self.output_path = output_path
        self.row_num = row_num
        self.col_num = col_num
        self.sum_num = sum_num


if __name__ == "__main__":
    photoshop = TestImageShop("./待处理图片/", ".jpg", [("Bright", 1.5), ("Resize", 0.3), ("Blur", 0)], "./批量输出图片/", 1, 5, 5)
    photoshop.load_images()
    photoshop.batch_ps(photoshop.operation)
    photoshop.display(photoshop.row_num, photoshop.col_num, photoshop.sum_num)
    photoshop.save(photoshop.output_path, photoshop.file_format)
