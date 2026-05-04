from pyscript import document

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

def render_list():
    output = document.getElementById("output")
    output.innerHTML = "".join(f"<p>{cm.introduce()}</p>" for cm in classmates)

def show_list(e):
    render_list()  # always replaces, never appends

def add_classmate(e):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    subject = document.getElementById("favsub").value

    classmates.append(Classmate(name, section, subject))

    # Clear the input fields
    document.getElementById("name").value = ""
    document.getElementById("section").value = ""
    document.getElementById("favsub").value = ""

    render_list()  # show updated list immediately, no duplicates


