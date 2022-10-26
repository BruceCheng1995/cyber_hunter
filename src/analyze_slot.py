from pydoc import tempfilepager
from PIL import Image
import numpy
import cv2

slot_1_box = (905, 215, 930, 235)
slot_2_box = (933, 215, 958, 235)
slot_3_box = (961, 215, 986, 235)
slots_poss = (slot_1_box, slot_2_box, slot_3_box)


def get_crop(_source, _box):
    return Image.open(_source).convert('RGB').crop(_box)  # .save(tmp_path)


def calculate(image1, image2):
    image1 = cv2.cvtColor(numpy.asarray(image1), cv2.COLOR_RGB2BGR)
    image2 = cv2.cvtColor(numpy.asarray(image2), cv2.COLOR_RGB2BGR)
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + \
                (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree


def classify_hist_with_split(image1, image2, size=(256, 256)):
    # image1 = Image.open(image1)
    image2 = Image.open(image2)
    # 将图像resize后，分离为RGB三个通道，再计算每个通道的相似值
    image1 = cv2.cvtColor(numpy.asarray(image1), cv2.COLOR_RGB2BGR)
    image2 = cv2.cvtColor(numpy.asarray(image2), cv2.COLOR_RGB2BGR)
    image1 = cv2.resize(image1, size)
    image2 = cv2.resize(image2, size)
    sub_image1 = cv2.split(image1)
    sub_image2 = cv2.split(image2)
    sub_data = 0
    for im1, im2 in zip(sub_image1, sub_image2):
        sub_data += calculate(im1, im2)
    sub_data = sub_data / 3

    return sub_data


class analyzer():
    def __init__(self,sourcepath,slotpath):
        self.sourcepath = sourcepath
        self.slotpath = slotpath
        pass

    def analyze(self, img):

        source_path = self.sourcepath + img

        res = [0 for _ in range(len(slots_poss))]

        for i in range(len(slots_poss)):
            img1_path = get_crop(source_path, slots_poss[i])
            for level in range(4):
                img2_path = self.slotpath + 'slot_lv' + str(level + 1)+'.png'
                result = classify_hist_with_split(img1_path, img2_path)
                if result[0] > 0.8:
                    res[i] = (level+1)
                # print(img + str(level) + "相似度为：" + "%.2f%%" % (result * 100))
        # print(img, res)

        # Image.open(source_path).crop((905, 215, 986, 235)
                                    #  ).save(tmppath + str(res) + "-" + img)
        
        return res
