class person: #OOP programming in py
  user_name="Rudra"
  user_occupation="Mern developer"
  user_salary="200$/M"
  def __init__(self,us,oc):
    self.user_name=us
    self.user_occupation=oc
    # self.user_salary=sa
  def get_user_info(self):
    print(f"{self.user_name} is a professional {self.user_occupation}")

user_0=person("harry","HR")
user_1=person("rony","PM")
user_0.get_user_info()
see=(list(user_0.user_name))
k=" ".join(see)
print(k)
user_1.get_user_info()
print(user_1.user_name)
class person: #OOP programming in py
  user_name="Rudra"
  user_occupation="Mern developer"
  user_salary="200$/M"
  def get_user_info(self):#we can also use lambda expression here
  # get_user_info=lambda self: f"{self.user_name} is good"
    print(f"{self.user_name} is a professional {self.user_occupation}")
another_person=person()
old_get=person()
add_one_more=person()
another_person.user_name="Aniket"
another_person.user_occupation="Professor of Quantum mechanics"
another_person.user_salary="50$/M"
print(another_person)
print(add_one_more)
# print(another_person.get_user_info())
another_person.get_user_info()
# print(old_get.get_user_info())
old_get.get_user_info()
add_one_more.user_name="sam"
add_one_more.user_occupation="Teacher"
add_one_more.user_salary="10$/M"
# print(add_one_more.get_user_info())
add_one_more.get_user_info()
def Average(*args):
  sum = 0
  for arg in args:
    sum = sum + arg
  print("Average is:",sum/len(args))
Average(1,2,3,4,5,6)
