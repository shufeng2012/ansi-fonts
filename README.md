<div align="middle">

# ANSI Fonts
✨ This package can make your output colorful and beautiful! ✨

![License](https://shields.io/badge/License-MIT-green) ![Python](https://shields.io/badge/Python-3.14.2-green?logo=python) ![C++](https://shields.io/badge/C++-14-green?logo=cplusplus) ![shufeng2012](https://shields.io/badge/shufeng2012-repo-green?logo=github)

</div>

<details>
<summary>Table of Contents</summary>

+ [✨Features](#features)
+ [🖼️Demo](#demo)
+ [🚀Fast Start](#fast-start)
+ [📖Using It](#using-it)
+ [❓FAQs](#faqs)
+ [📄License](#license)
+ [🙏Thanks](#thanks)

</details>

# ✨Features
+ **➕More styles than *colorama***: Supports more styles such as **bold**, *italic*, etc.
+ **💪Powerful mix() function**: Both font color and font variation can be **used at the same time**.
+ **🎛️Modularity functions**: Provide functions with separate styles, such as *color()* and *variant()*.

# 🖼️Demo
**Example of use**:
```python
# Python
import AnsiFontsPackage as afp
print(color("Hello world!", afp.RED))
print(variant("Hello world!", afp.BOLD))
print(mix("Hello world!", fg_color=afp.RED, variant=afp.UDLINE))
```

```cpp
// C++
#include<AnsiFontsPackage>
int main() {
	cout << color("Hello world!", RED) << endl;
	cout << variant("Hello world!", BOLD) << endl;
	cout << mix("Hello world!", RED, CLEAR, UDLINE) << endl;
	return 0;
}
```

Please execute the code under `test/` to see the specific results.

# 🚀Fast Start
+ Clone this repository.
```bash
git clone https://github.com/shufeng2012/ansi-fonts
```
+ Import it into your code.

# 📖Using It
> [Important]
> Cannot use both fg_color and bg_color!

**color() function definition**:
```
method color(
	string/str: string
	fg_color: string = CLEAR
	bg_color: string = CLEAR
	clear: boolean = true
) -> string
```
**variant() function definition**:
```
method variant(
	string/str: string
	variant: string = CLEAR
	clear: boolean = true
) -> string
```
**mix() function definition**:
```
method mix(
	string/str: string
	fg_color: string = CLEAR
	bg_color: string = CLEAR
	variant: string = CLEAR
	clear: boolean = true
) -> string
```
**Parameter parsing**:
+ **string/str**: The string that will be operated on.
+ **fg_color**: Foreground color.
+ **bg_color**: Background color.
+ **variant**: Font variation.
+ **clear**: Whether to clear.
**Constants:**
+ *Colors*:
	+ Foreground colors: RED GREEN YELLOW BLUE PURPLE CYAN
	+ Background colors: BG_RED BG_GREEN BG_YELLOW BG_BLUE BG_PURPLE BG_CYAN
+ *Variants*: BOLD DARKEN ITALIC UDLINE *SLOW_FLASH* *FAST_FLASH* INVCOLOR INVISIBLE STKETHROUGH

# ❓FAQs
+ **Q: Cannot use *SLOW_FLASH* or *FAST_FLASH*?**
+ A: Some terminals may not support the flashing function, which needs to be turned on manually.

# 📄License
This project uses the MIT open source license. Click [here](https://github.com/shufeng2012/ansi-fonts/blob/main/LICENSE) to view.

# 🙏Thanks
Thank you to everyone who contributed to this project!
