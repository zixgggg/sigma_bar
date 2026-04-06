import dearpygui.dearpygui as dpg
import subprocess
import time
import configparser
dpg.create_context()
config = configparser.ConfigParser()
config.read("config.ini")
cmd=config["time"]["commend"]
d=subprocess.check_output(cmd,shell=True).decode("utf-8").strip()
#d=subprocess.check_output(["date '+%Y-%m-%d %H:%M:%S'"],shell=True).decode("utf-8").strip()
c=subprocess.check_output(["""sar -u 1 1 | tail -1 | awk '{printf "%.2f%%", 100 - $NF}'"""],shell=True).decode("utf-8").strip()

with dpg.window(tag="pw"):
    with dpg.group(horizontal=True):
        dpg.add_text(d,tag="date_tag")
        dpg.add_spacer(width=20)
        dpg.add_text(c,tag="cpu_tag")

dpg.set_primary_window("pw", True)
dpg.create_viewport(title="sigma_bar",resizable=False,x_pos=0,y_pos=0,width=1920,height=30,decorated=False,always_on_top=True,disable_close=True)
dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running():
    d=subprocess.check_output(["date '+%Y-%m-%d %H:%M:%S'"],shell=True).decode("utf-8").strip()
    c=subprocess.check_output(["""sar -u 1 1 | tail -1 | awk '{printf "%.2f%%", 100 - $NF}'"""],shell=True).decode("utf-8").strip()
    dpg.set_value("date_tag",d)
    dpg.set_value("cpu_tag",f"cpu:{c}")
    print("this will run every frame")
    dpg.render_dearpygui_frame()
#dpg.start_dearpygui()
dpg.destroy_context()
