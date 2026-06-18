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
##### ```true``` accepted value are ```1``` ```yes``` ```true``` ```on```
<br>
##### `false` accepted value are ```0``` ```no``` ```false``` ```off```
<br>
##### value don't care uppercase or lowercase(config power by python buildin module configparser)
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
