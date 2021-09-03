import png
import requests
from pathlib import Path

src = 'https://www.larvalabs.com/public/images/cryptopunks/'

def download(name):
    
    r = requests.get(src + name)
    if r.status_code == 200:
        open(name, 'wb').write(r.content)

    r=png.Reader(name)
    p = r.read()

    return p


def mkdir(dir):

    path = Path(dir)
    if not path.is_dir():
        path.mkdir()


def remove(p, name):

    data = [list(d) for d in p[2]]
    path = Path(name)
    asia  = Path('asia') / name
    other  = Path('other') / name
    if data[-1][36:40] == [219, 177, 128, 255]: # 判断是否是黄种人
        print(f'{name} -> asia')
        path.replace(asia)        
    else:
        path.replace(other)

if __name__ == '__main__':

    mkdir('asia')  # 如果没有 asia 目录，则创建
    mkdir('other') # 如果没有 other 目录，则创建

    for i in range(0,10000):  # 下载从 0000 到 0009 的 punk
        name = f'punk{i:0=4d}.png'
        p = download(name) # 下载 punkxxxx.png
        remove(p, name)    # 移动到对应目录