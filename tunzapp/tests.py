from django.test import TestCase
from .models import Child,Profile,FinancialNeed

# Create your tests here.
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.valarie= Profile(full_name = 'Valarie Rono', email ='valarie.chelagat@gmail.com',location='Nairobi',phone_number='0722000000')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.valarie,Profile))

        # Testing Save Method
    def test_save_method(self):
        self.valarie.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

     
     
class FinancialNeedTestClass(TestCase):
    def setUp(self):
        self.needs1=FinancialNeed(needs="needs")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.needs1,FinancialNeed))

class ChildTestClass(TestCase):
    def setUp(self):
      self.child = Child.objects.create(full_name='victoria rono',image='/default.jpg',gender='Female',age='18',family_members='5',bio='Be happy',location='Nairobi',school_grade='400',school='Moi Girls',class_overall='form 4',dreams='doctor')

    def test_instance(self):
        self.assertTrue(isinstance(self.child, Child))

    def test_save_child(self):
        self.child.save_child()
        child = Child.objects.all()
        self.assertTrue(len(child) > 0)

    def test_delete_child(self):
        self.child.delete_child()
        child = Child.objects.all()
        self.assertTrue(len(child) < 1)
    
