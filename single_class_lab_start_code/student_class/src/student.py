class Student:
    def __init__(self,Name,Cohort):
        self.name = Name
        self.cohort = Cohort

    def talk(self):
        return "I can talk!"

    def student_has_name(self,Name):
        return Name

    def student_has_cohort(self,Cohort):
        return Cohort
    
    def student_can_update_name(self,Name):
        return Name

    def student_can_change_cohort(self,Cohort):
        return Cohort       
        


