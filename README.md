# sigmabar

## installtion
General funtion(install,uninstall,more actions)
```bash
curl -fsSL https://raw.githubusercontent.com/zixgggg/sigmabar/refs/heads/main/menu.sh|bash
```

just install
```bash
curl -fsSL https://raw.githubusercontent.com/zixgggg/sigmabar/refs/heads/main/install.sh|bash
```

uninstall
```bash
curl -fsSL https://raw.githubusercontent.com/zixgggg/sigmabar/refs/heads/main/uninstall.sh|bash
```

## configtion
config file at ```~/.config/sigmabar/config.ini```
<br>
*default* mean if config.ini has no that key, program will use a hardcode value inside
<br>
all config:
<br>
<br>
```width=int```
<br>
set bar width
<br>
*default:1920*
<br>
example:
<br>
```width=1920```
<br>
<br>
```height=int```
<br>
set bar height
<br>
*default:30*
<br>
example:
<br>
```height=20```
<br>
<br>
```bar_height_is_font_size=bool```
<br>
set bar height as font height
<br>
*default:false*
<br>
example:
<br>
```bar_height_is_font_size=true```
<br>
<br>
```true``` accepted value are ```1``` ```yes``` ```true``` ```on```
<br>
```false``` accepted value are ```0``` ```no``` ```false``` ```off```
<br>
value don't care uppercase or lowercase(config power by python buildin module configparser)
<br>
<br>
```bar_and_text_gap=int```
<br>
set gap between text and bar height edge
<br>
*default:0*
<br>
example:
<br>
```bar_and_text_gap=10```
<br>
<br>
```update_grid=float```
<br>
bar refresh grid
<br>
*default:0.5*
<br>
example:
<br>
```update_grid=1```
<br>
<br>
```bar_split_sign=str```
<br>
set a text between block text
<br>
*default:   |   *
<br>
example:
<br>
```bar_split_sign=|```
<br>
<br>
```font=str```
set text font path
<br>
*default:""*
<br>
example:
<br>
```font=/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc```
<br>
```font=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf```
<br>
<br>
generally fonts at ```/usr/share/fonts/```
<br>
```fc-list``` command can show the fonts been installed
<br>
<br>
```font_size=int```
<br>
set font size
<br>
*default=20*
<br>
example:
<br>
```font_size=67```
<br>
<br>
```background_color_r=int```
<br>
set background color r in rgb 
<br>
*default=0*
<br>
example:
<br>
```background_color_r=67```
<br>
<br>
```background_color_g=int```
<br>
set background color g in rgb 
<br>
*default=0*
<br>
example:
<br>
```background_color_g=67```
<br>
<br>
```background_color_b=int```
<br>
set background color b in rgb 
<br>
*default=0*
<br>
example:
<br>
```background_color_b=67```
<br>
<br>
```text_color_r=int```
<br>
set text color r in rgb 
<br>
*default=255*
<br>
example:
<br>
```text_color_r=67```
<br>
<br>
```text_color_g=int```
<br>
set text color g in rgb 
<br>
*default=255*
<br>
example:
<br>
```text_color_g=67```
<br>
<br>
```text_color_b=int```
<br>
set text color b in rgb 
<br>
*default=255*
<br>
example:
<br>
```text_color_b=67```
<br>
<br>
