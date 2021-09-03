# 下载 10000 张 CryptoPunks

通过代码下载 10000 张 CryptoPunks

并根据肤色把黄种人头像放在 asia 目录下

其他头像放在 other 目录下

## 执行

先安装依赖库 pypng, requests

```
pip install pypng
pip install requests
```

执行

```Python
python download.py
```

查看当前目录，已经生成了 asia,other 目录，其中不断出现新的 punk 图片。
