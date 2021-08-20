# pixelpunks
像素朋克，用代码生成像素头像，发挥创意，让头像飞起来

## 创意

我听说，在区块链上，一张24*24的像素头像可以买到 9050 万美元，真是匪夷所思了

详情请见：

- https://www.36kr.com/p/1339722275117312
- https://zhuanlan.zhihu.com/p/350919003?utm_oi=1309951489352495104
- https://www.larvalabs.com/cryptopunks

其中，最令我震惊的是：

>Q：朋克图像咋产生的？

>A：我们码了些代码来生成了这些角儿，然后一次性跑了通代码，创造了网站上你看到的这10000个。

啥情况，头像还可以代码随机生成？我不信，我也用代码试试！

## 实现

经过研究，发现并不能猴子在键盘上跳舞随机生成的，而是先预设一些素材，包括：人物模型，装饰，然后通过代码随机组合而成。

这些素材虽然寥寥几笔，但也足够传神，称之为像素艺术也不足为奇。

既然如此， 那就用代码实现一下吧，详情见代码。

## 执行

```Python
python punk.py
```
查看当前目录，生成了一个 punk.png 文件

## 
