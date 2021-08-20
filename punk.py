import png
from templete import canvas, man # 导入画布和人物模型
from stickers import cigarette # 导入需要的贴纸


def merge(sticker0, sticker1):
    '''
    将 sticker1 合并到 sticker0
    '''
    colors = sticker0['colors']
    index = {}
    for i,color in enumerate(sticker1['colors']):
        if color not in colors:
            colors.append(color)
            index[i] = colors.index(color)
        else:
            index[i] = colors.index(color)

    for i,row in enumerate(sticker1['data']):
        for j,color in enumerate(row):
            if color > 0:
                sticker0['data'][i][j] = index[color]
    return sticker0


def merges(stickers):
    '''
    从sticker0 sticker1 开始递归合并贴纸
    '''
    if len(stickers) >= 2:
        sticker = merge(stickers.pop(0), stickers.pop(0))
        stickers.insert(0, sticker)
    else:
        return stickers[0]

    return merges(stickers)


def generate(image, name):
    '''
    根据点阵图，生成 png 图片
    name: 生成的图片名称
    '''
    colors = image['colors'][1:]
    palette = [(255, 255, 255, 0)]

    for color in colors:
        color = [int(c, 16) for c in (color[:2], color[2:4], color[4:])]
        palette.append(tuple(color))

    w = png.Writer(len(canvas['data'][0]), len(
        canvas['data']), palette=palette, bitdepth=4)
    f = open(f'{name}.png', 'wb')
    w.write(f, image['data'])


if __name__ == '__main__':
    # canvas, man 是必须的，后面跟多个 sticker
    # 如：[canvas, man, cigarette, glasses]
    stickers = [canvas, man, cigarette] 

    image = merges(stickers)
    generate(image, 'punk')