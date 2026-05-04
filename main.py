from pyscript import display, document

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject
    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}."

classmates = [
    Classmate("Renzo", "Topaz", "Cat"),
    Classmate("Jalainie", "Topaz", "PE"),
    Classmate("Calvin", "Topaz", "PE"),
    Classmate("Sebastian", "Topaz", "Social Studies"),
    Classmate("Alejandro", "Topaz", "PE"),
]

def clear_output():
    document.getElementById("output").innerHTML = ""

def show_list(e):
    clear_output()  
    for cm in classmates:
        display(cm.introduce(), target="output", append=True)

def add_classmate(e):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("favsub").value

    new_classmate = Classmate(name, section, subject)
    classmates.append(new_classmate)

    clear_output()  
    display("classmate added successfully", target="output", append=True)


