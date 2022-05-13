# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. 
# Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

from tkinter import S


class Student: 

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def ticket (self):
        print  ("Nombre:" + self.name +",   Nota:" + self.grade)
    
    def results (self):
        if self.grade < "5":
            print ("Student have failed")
        else:
            print("Student have passed")

student1 = Student ("Menganito", "2")
student2 = Student ("Fulanito", "8")

student1.ticket()
student1.results()
student2.ticket()
student2.results()


