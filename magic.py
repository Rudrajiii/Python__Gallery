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
