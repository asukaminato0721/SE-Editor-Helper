# MSE 快速修正公式脚本

mse 有 edit 别人答案的功能，由于自带的编辑器功能很弱，所以修改公式很费力。就写了这个脚本。

> mathematica stack exchange 有这个 [脚本](https://github.com/halirutan/SE-Editor-Buttons), 但是仅面向 Mathematica 使用者

## Require

`re` 库与 `pyperclip` 库

## Usage

1. `Ctrl`+`A` ，`Ctrl`+`C` ，把待修改文稿复制到剪贴板上。
2. 运行脚本
3. `Ctrl`+`V`，把答案粘贴回去

## Feature

1. 单行 `$formula$` 直接匹配
2. 单行 `$$formula$$` 直接匹配
3. 多行 `$$formula$$` 直接匹配

## TODO

- [ ] 最长匹配（如匹配了 `arcsin` 就不再匹配 `sin`）

## Updating Record

### version 0.4

感谢 [这位开发者](https://github.com/t-k-) 提供的脚本 `replace_post_tex` , 增强了转化效果，可匹配多行公式

因为不会正则，删去了正则相关内容

### version 0.3

加入正则判断（需要 `re` 库）（多行公式匹配功能缺失）Thanks to [HydrogenDeuterium](https://github.com/HydrogenDeuterium)

### version 0.2

改进脚本，使其直接读取剪贴板（需要 `pyperclip` 库）（不稳定，比如 using 会被匹配成 u\sin g , 需要加规则来弥补，但是能匹配多行公式）

### version 0.1

暴力匹配，在一个指定 txt 里完成替换

## PR is welcomed