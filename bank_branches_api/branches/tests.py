from django.test import TestCase
from .models import Bank, Branch

class BranchModelTest(TestCase):
    def setUp(self):
        self.bank = Bank.objects.create(name='Test Bank')
        self.branch = Branch.objects.create(
            branch='Test Branch', 
            bank=self.bank, 
            ifsc='TEST0001'
        )

    def test_branch_creation(self):
        self.assertTrue(isinstance(self.branch, Branch))
        self.assertEqual(self.branch.__str__(), 'Test Branch - Test Bank')