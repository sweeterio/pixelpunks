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

def remove(p, name):
    data = [list(d) for d in p[2]]
    path = Path(name)
    asia  = Path('asia') / name
    other  = Path('other') / name
    if data[-1][36:40] == [219, 177, 128, 255]:
        print(f'{name} -> asia')
        path.replace(asia)        
    else:
        path.replace(other)

if __name__ == '__main__':

    for i in range(0,10000):
        name = f'punk{i:0=4d}.png'
        p = download(name)
        remove(p, name)