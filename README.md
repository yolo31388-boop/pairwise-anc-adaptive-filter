# pairwise-anc-adaptive-filter

## 领域

游戏、图形与多媒体

## 主题

主动降噪自适应滤波

## 说明

统一采样时钟、变步长收敛、次级路径在线辨识。

初始状态下 `av/anc_filter.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
