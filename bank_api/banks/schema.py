import graphene
from graphene_django.types import DjangoObjectType
from branch.models import Branch, Bank

class BankType(DjangoObjectType):
    class Meta:
        model = Bank
        fields = "__all__"

class BranchType(DjangoObjectType):
    bank = graphene.Field(BankType)  
    class Meta:
        model = Branch
        fields = "__all__"

class Query(graphene.ObjectType):
    all_branch = graphene.List(BranchType)

    def resolve_all_branch(self, info):
        pass

schema = graphene.Schema(query=Query)
