# cyber_hunter

识别《怪物猎人崛起：曙光》护石系统数据
将护石获取界面的完整截图（720P）输入系统，程序将识别并输出该护石的

- 技能名称
- 技能等级
- 孔位信息

该项目通过纯图片分析，配合百度文件识别项目 [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) 实现

## Installation

1. 安装百度 PaddleOCR

```bash
python3 -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
```

2. 安装 PaddleOCR Whl Package

```bash
pip install "paddleocr>=2.0.1" # Recommend to use version 2.0.1+
```

## Using

直接运行 `src/main.py` 即可

```bash
python3 src/main.py
```

该范例将读取 `test_imgs/mhrs` 路径下的所有文件，并尝试识别其中的护石数据。数据将被打印出来

## Roadmap

1. HDMI 信号采集，导出事实游戏画面
2. 支持 OCR 结果模糊匹配，降低错误率
3. 联动 <https://github.com/BruceCheng1995/Joycontrol_amiibo_MHRS> 项目，实现自动炼金并识别筛选有价值的护石
4. 为各个自动化项目提供准确性校验服务
