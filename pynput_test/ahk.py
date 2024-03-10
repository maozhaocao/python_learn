import os

ahk_folder = r'C:\Users\maozhaocao\Desktop\SET_AHK\SET_AHK'

gamer = {"元素": [1, 4, 8],
         "力法": [2],
         "奶萝": [3, 5],
         "井盖": [7],
         "召唤": [6],
         "奶爸": [9],
         "奶妈": [10],
         "刃影": [11],
         "剑魂": [12],
         "缪斯": [13],
         "旅人": [14],
         "巫女": [15],
         "红眼": [16]
         }

id_dict = {}
for key in gamer.keys():
    id_list = gamer[key]
    for gamer_id in id_list:
        id_dict[gamer_id] = key


def run_shenyuan(id_list_shenyuan):
    for cur_id in id_list_shenyuan:
        cur_gamer = id_dict[cur_id]
        ahk_exe_name = os.path.join(ahk_folder, f"AHK_深渊_{cur_gamer}")
        os.system(ahk_exe_name)


if __name__ == '__main__':
    run_shenyuan([1])
    # os.system(os.path.join(ahk_folder, f"SET_AHK.exe"))
print()
