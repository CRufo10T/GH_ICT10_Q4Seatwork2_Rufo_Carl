from pyscript import display, document

class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}."


# Initial classmates
classmates = [
    Classmate("Renzo", "Topaz", "Cat"),
    Classmate("Jalainie", "Topaz", "PE"),
    Classmate("Calvin", "Topaz", "PE"),
    Classmate("Sebastian", "Topaz", "Social Studies"),
    Classmate("Alejandro", "Topaz", "PE"),
]


def show_list(e):
    for cm in classmates:
        display(cm.introduce(), target="output")
  


def add_classmate(e):
    name= document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("favsub").value

    diction = {
        "name":name,
        "section":section,
        "favorite_subject":subject
    }
    new_classmate = Classmate(**diction)
    classmates.append(new_classmate)
    display("classmate added succesfully", target='output')


