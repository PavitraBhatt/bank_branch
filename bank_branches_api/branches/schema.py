import graphene
from graphene_django import DjangoObjectType
from graphene import relay
from .models import Bank, Branch

class BankType(DjangoObjectType):
    class Meta:
        model = Bank
        interfaces = (relay.Node,)

class BranchType(DjangoObjectType):
    class Meta:
        model = Branch
        interfaces = (relay.Node,)

class Query(graphene.ObjectType):
    branches = relay.ConnectionField(BranchType)
    
    def resolve_branches(self, info, **kwargs):
        return Branch.objects.select_related('bank').all()

schema = graphene.Schema(query=Query)