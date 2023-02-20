"""
Module for shrinking data
"""
import random
def get_lines(path_to_list:str, number_lines:int):
    """
    Get radom films and create new file with it
    """
    getted=""
    all_file=[]
    with open(path_to_list,"r",encoding="utf-8") as file_read:
        while not file_read.readline().startswith("=="):
            pass
        while True:
            readed_line=file_read.readline()
            if readed_line:
                all_file.append(readed_line)
            else:
                break
        for _ in range(number_lines):
            random_index=random.randint(100,1000000)
            getted+=all_file[random_index]
    with open("small_films.list","w",encoding="utf-8") as file_write:
        file_write.write(getted)
get_lines("D:\project_2\lab_1\map_repo\locations.list",15000)
