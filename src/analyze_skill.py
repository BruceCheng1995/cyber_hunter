from imghdr import tests
import numpy as np
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image

class analyzer():
    def __init__(self, sourcepath, tmppath):
        self.sourcepath = sourcepath
        self.tmppath = tmppath
        
        self.skill_box = (770, 275, 900, 425)
        self.offset = np.array((25, 39))
        self.gap = np.array((16, 50))
        self.level_mat = (self.offset, self.gap)

        self.ch_ocr = PaddleOCR(use_angle_cls=True, lang='ch')

    def analyze(self, _img):

        img_path = self.sourcepath + _img
        # tmp_path = self.tmppath + _img
        # result_path = resultpath + _img

        # crop skill information into tem_path
        level_slice = Image.open(img_path).convert('RGB').crop(self.skill_box)#.save(tmp_path)

        # analyze image
        result = self.ch_ocr.ocr(np.array(level_slice), cls=True)

        # detact skill level
        # level_slice = Image.open(tmp_path)
        for line in range(len(result)):
            startPos = self.level_mat[0] + (0, line * self.level_mat[1][1])
            result[line].append(0.0)
            for gird in range(7):
                pos = startPos + (gird * self.level_mat[1][0], 0)
                pixel = level_slice.getpixel(tuple(pos))
                if pixel[2] > 200:
                    result[line][2] += 1

        # for line in result:
        #     print(_img, line)

        # boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        level = [line[2] for line in result]

        # # draw result
        # tmp_img = Image.open(tmp_path)
        # im_show = draw_ocr(tmp_img, boxes, txts, level,
        #                    font_path=rootpath+'ppocr_img/fonts/simfang.ttf')
        # im_show = Image.fromarray(im_show)
        # im_show.save(result_path)
        
        return [txts,level]
