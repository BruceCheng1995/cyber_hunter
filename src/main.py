from multiprocessing.forkserver import main
import os
import analyze_skill
import analyze_slot


def clearFolder(_path):
    for item in os.listdir(_path):
        os.remove(_path + item)


rootpath = os.getcwd()

sourcepath = rootpath + '/test_imgs/mhrs/'
tmppath = rootpath + '/test_imgs/mhrs_temp/'
slotpath = rootpath + '/test_imgs/slot/'

anal_skill = analyze_skill.analyzer(sourcepath, tmppath)
anal_slot = analyze_slot.analyzer(sourcepath, slotpath)


def get_stone_info(img):
    skill = anal_skill.analyze(img)
    stone = anal_slot.analyze(img)
    return {
        'skill_info': skill,
        'slot_info': stone
    }


def main():

    clearFolder(tmppath)

    imgs = os.listdir(sourcepath)
    for img in imgs:
        if img.endswith('.png'):
            info = get_stone_info(img)
            print(img, info)


if __name__ == "__main__":
    main()
