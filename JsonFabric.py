import json
import os
from tkinter import *


def getjsonfile(choice):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    if choice == 1:

        mod_id = name_modid.get()

        block_name = name_item_block.get()

        block_loc = f"{mod_id}:block/{block_name}"

        blockstate = {
            'variant':
                {'':
                    {'model': f'{block_loc}'}
                 }
        }

        blockmodel = {
            'parent': 'block/cube_all',
            'textures': {
                'all': f'{block_loc}'
            }
        }

        itemmodel = {
            'parent': f"{block_loc}"
        }

        save_file(dir_path, block_name, 'block', blockstate, mod_id)
        save_file(dir_path, block_name, 'block', blockmodel, mod_id)
        save_file(dir_path, block_name, 'block', itemmodel, mod_id)

    elif choice == 2:
        item_name = name_item_block.get()

        mod_id = name_modid.get()

        item = {
            'parent': 'item/generated',
            'textures': {
                'layer0': f'{mod_id}:item/{item_name}'
            }
        }

        save_file(dir_path, item_name, 'item', item, mod_id)


def save_file(directory, name, choice, jsondata, modid):

    if choice == 'item':
        full_directory = f'{directory}/assets/{modid}/models/item'

        if not os.path.exists(full_directory):
            os.makedirs(full_directory)

        with open(f'{full_directory}/{name}.json', 'w') as f:
            json.dump(jsondata, f, ensure_ascii=False, indent=4)
            f.close()

    elif choice == 'block':
        pass

root = Tk()

name_modid = Entry(root, width=30)
name_modid.grid(row=0)
name_modid.insert(0, "Enter your modid:")

name_item_block = Entry(root, width=30)
name_item_block.grid(row=1)
name_item_block.insert(0, "Enter your item or block name:")

block_button = Button(root, text='block')
block_button.grid(row=2, column=0)

item_button = Button(root, text='item', command=lambda: getjsonfile(2))
item_button.grid(row=2, column=1)

root.mainloop()
  