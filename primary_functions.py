from rich.table import Table
from rich.padding import Padding


def find(layout =None,input_list = "",lexicon = None,core= None):
    core.table =  Table(expand=True,show_edge=False)
    core.table.add_column()
        
    word =input_list[-1]
    if word == "" and len(input_list) > 1: 
        word = input_list[-2]
    for key,value in lexicon.items():
        if key.lower() == word.lower():
            
                core.table.add_row(f"{key.upper()}")
                value = value.replace(";","\n")
                                
                core.table.add_row(f"{value}")
    layout["view"].update(Padding(core.table,pad =(0,20),expand=True))     

def dictionary():
    pass

def synonyms():
    return 0
def help():
    pass
def use_case():
    pass