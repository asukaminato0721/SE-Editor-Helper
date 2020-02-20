# MSE Quick Fix Formula Script

[中文版]()

MathStackExchange has a function to edit other people's answers. Because the built-in editor function is sort of weak, it is very laborious to modify the formula. So I wrote this script.

> mathematica stack exchange has this [脚本](https://github.com/halirutan/SE-Editor-Buttons), But only for Mathematica users

## Require

`re` and `pyperclip`

## Usage

1. `Ctrl` +`A`, `Ctrl` +`C`, copy the document to be modified to the clipboard.
2. Run the script
3. `Ctrl` +`V`, paste the answer back

## Feature

1. Single line `$ formula $` matches directly
2. Single line `$$ formula $$` matches directly
3. Multiple lines `$$ formula $$` match directly

## TODO

- [ ] Longest match (if `arcsin` is matched,`sin` is no longer matched)

## Updating Record

### version 0.5(beta)

Achieved the longest match. You cannot match `\\` in `$$ $$`, otherwise an error will occur.

### version 0.4

Thanks to [this developer](https://github.com/t-k-) for the script `replace_post_tex`, which enhances the conversion effect and can match multi-line formulas. (TODO: longest match (if `arcsin` is matched,`sin` is no longer matched))

Because I don't know how to write regularity, regularity related content is deleted

### version 0.3

Add regular judgment (`re` library required) (multi-line formula matching function is missing) Thanks to [HydrogenDeuterium] (https://github.com/HydrogenDeuterium)

### version 0.2

Improved the script to read the clipboard directly (requires `pyperclip` library) (unstable, such as using will be matched as u\sin g, rules need to be added to compensate, but it can match multi-line formulas)

### version 0.1

Brute-force match, replace in a specified txt

## PR is welcomed