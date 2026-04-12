import dearpygui.dearpygui as dpg
import subprocess
import time
import configparser
dpg.create_context()
config = configparser.ConfigParser()
config.read("config.ini")
all_cmd=""

#cmd=config["time"]["commend"]
#d=subprocess.check_output(cmd,shell=True).decode("utf-8").strip()
#print(config.sections())
"""
for block in config.sections():#取得所有區塊的特定區塊
    keys=config.options(block)#取得特定區塊所有鍵
    for key in keys:
        value=config[block][key]#取得特定鍵下的值
"""
#print(config.options(config.sections()))
#d=subprocess.check_output(["date '+%Y-%m-%d %H:%M:%S'"],shell=True).decode("utf-8").strip()
#c=subprocess.check_output(["""sar -u 1 1 | tail -1 | awk '{printf "%.2f%%", 100 - $NF}'"""],shell=True).decode("utf-8").strip()
#    cmd=subprocess.check_output(value,shell=True).decode("utf-8").strip()
#    all_cmd=all_cmd+cmd+"   "
    
with dpg.window(tag="win"):
    with dpg.group(horizontal=True):
        dpg.add_text(all_cmd,tag="all_cmd_tag")
        #dpg.add_spacer(width=20)
        #dpg.add_text(i,tag="cpu_tag")

dpg.set_primary_window("win", True)
dpg.create_viewport(title="sigma_bar",resizable=False,x_pos=0,y_pos=0,width=1920,height=30,decorated=False,always_on_top=True,disable_close=True)
dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running():
    all_cmd=""
    for block in config.sections():#取得所有區塊的特定區塊
        keys=config.options(block)#取得特定區塊所有鍵
        for key in keys:
            value=config[block][key]#取得特定鍵下的值
            cmd=subprocess.check_output(value,shell=True).decode("utf-8").strip()
            all_cmd=all_cmd+cmd+"   "
    dpg.set_value("all_cmd_tag",all_cmd)

    print("this will run every frame")
    dpg.render_dearpygui_frame()
#dpg.start_dearpygui()
dpg.destroy_context()
