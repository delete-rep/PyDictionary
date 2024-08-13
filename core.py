"""_summary_

Returns:
    _type_: _description_
"""
from rich.table import Table
from rich.layout import Layout
from rich.layout import Layout
from rich.padding import Padding
from globals import PRIMARY_KEY_WORD_MAPPING 
SUGGESTIONS= {
"add" : "function: [grey]ADD[grey] \n this is a function used to add other note types",
"delete ": "used to delete other notes and take a variety of notes",
"dictionary" : "find items in the dicionary",
"find": "[#363838] [code]FIND[/code] a function which return a words meaning if found \n Parameters : a [blue]single-word[/blue][/#363838]",

}

class Core():
    """_summary_
    """
    def __init__(self,layout:Layout) -> None:
        """_summary_

        Args:
            layout (Layout): _description_
        """
        self.text= ""
        self.layout = layout
        self.formated_text = ""
        self.suggestion = ""
        self.running = True
        self.lexicon = None
        self.table = None
        import json
        with open("dictionary.json","r")as json_file:
            self.lexicon = json.load(json_file)
        

    def save_key(self,key):
        """_summary_

        Args:
            key (_type_): _description_
        """
        input_string :str= str(key)
        input_string = input_string.replace("'","")
        match input_string:

            case "Key.space":
                input_string = " "

            case "Key.backspace":
                input_string = ""
                self.text =  self.text[:-2]

            case "Key.enter":
                self.process(user_input=self.text,layout=self.layout)
                self.text = ""

            case _:
                pass

        if len(input_string) <2:
            self.text += input_string
            self.format_text()
            self.edit_suggestion()
            self.show_similar_words()
    def show_similar_words(self):
        
        max_count =6 
        count = 0
        input_list = self.text.split(" ")
        word =input_list[-1]
        if word == "" and len(input_list )> 1: word = input_list[-2]

        self.table =  Table(expand=True,show_edge=False)
        self.table.add_column()
        for key,value in self.lexicon.items():
            if key.startswith(word):
                
                if count < max_count:

                    self.table.add_row(f"{key}")
        
                                    
                    self.table.add_row("")
                    
                    count+=1
        self.layout["view"].update(Padding(self.table,pad =(0,40),expand=True))
    def contains_primary_key(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        for i in self.text.split():
            if i in PRIMARY_KEY_WORD_MAPPING:
                return True
        return False
    
    def edit_suggestion(self):
        """_summary_
        """
        if len(self.text )< 1:
            self.suggestion = "[#363838] primary commands inlucde [A D D] [#363838]"
        if  not self.contains_primary_key():
            arr = self.text.split(" ")
            matching_words = [word for word in PRIMARY_KEY_WORD_MAPPING if word.startswith(arr[-1])]
            if len(matching_words) > 0:
                if matching_words[0] in SUGGESTIONS:
                    self.suggestion = SUGGESTIONS[matching_words[0]]

    def format_text(self):
        """_summary_
        """
        string_list =self.text.split(" ")
        for index ,i in enumerate(string_list):
            if i in PRIMARY_KEY_WORD_MAPPING:
                string_list[index] = "[code ] "  + i.upper() + "[/code]"
            if i in PRIMARY_KEY_WORD_MAPPING:
                string_list[index] = "[blue] "  + i + ": [/blue]"
        self.formated_text = " ".join(string_list)

    def process(self,layout : Layout = None ,user_input:str= ""):
        """_summary_

        Args:
            layout (Layout, optional): _description_. Defaults to None.
            user_input (str, optional): _description_. Defaults to "".
        """


        string_list : list= user_input.split(" ")
        
        for word in (string_list[:2]):
            if  word in PRIMARY_KEY_WORD_MAPPING:
                function : callable = PRIMARY_KEY_WORD_MAPPING[word]
                string_list.remove(word)
                function(lexicon = self.lexicon,layout = layout,input_list = string_list,core = self)

            