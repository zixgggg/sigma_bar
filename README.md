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
*default* mean if config.ini has no that key, program will use a hardcode value inside  
two type of block:[sigmabar] and custom block  
[sigmabar] for the special key  
custom block for general key  
example:  
```
[pactl_volume]
command=echo -n $(pactl get-sink-volume @DEFAULT_SINK@ | awk '{print $5}'&&echo "(" &&echo $(pactl get-sink-mute @DEFAULT_SINK@) && echo ")" && echo $(pactl get-default-sink))
label=volume:
```  
### special key need to stay at [sigmabar] block:    
```width=int```  
set bar width  
*default:1920*  
example:  
```width=1920```  


```height=int```  
set bar height  
*default:30*  
example:  
```height=20```


```bar_height_is_font_size=bool```  
set bar height as font height  
*default:false*  
example:  
```bar_height_is_font_size=true```  
```true``` accepted value are ```1``` ```yes``` ```true``` ```on```  
```false``` accepted value are ```0``` ```no``` ```false``` ```off```  
value don't care uppercase or lowercase(config power by python buildin module configparser)  


```bar_and_text_gap=int```  
set gap between text and bar height edge  
*default:0*  
example:  
```bar_and_text_gap=10```  


```update_grid=float```  
bar refresh grid  
*default:0.5*  
example:  
```update_grid=1```  


```bar_split_sign=str```  
set a text between block text  
*default:   |   *  
example:  
```bar_split_sign=|```  


```font=str```  
set text font path  
*default:""*  
example:  
```font=/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc```  
```font=/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf```  
generally fonts at ```/usr/share/fonts/```  
```fc-list``` command can show the fonts been installed  


```font_size=int```  
set font size  
*default=20*  
example:  
```font_size=67```  


```background_color_r=int```  
set background color r in rgb  
*default=0*  
example:  
```background_color_r=67```  


```background_color_g=int```  
set background color g in rgb  
*default=0*  
example:  
```background_color_g=67```  


```background_color_b=int```  
set background color b in rgb  
*default=0*  
example:  
```background_color_b=67```  


```text_color_r=int```  
set text color r in rgb  
*default=255*  
example:  
```text_color_r=67```  


```text_color_g=int```  
set text color g in rgb  
*default=255*  
example:  
```text_color_g=67```  


```text_color_b=int```  
set text color b in rgb  
*default=255*  
example:  
```text_color_b=67```  


### general key in custom block:  
```command=str```  
set command to execute(command output will show on bar)  
*default:""*  
example:  
```command=echo 67```  


```label=str```  
set label splice at command output front  
*default=""*  
example:  
```label=67```  
