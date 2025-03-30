import graphene

class BankType(graphene.ObjectType):
    bank_id = graphene.Int()
    bank_name = graphene.String()

class BranchType(graphene.ObjectType):
    branch_id = graphene.Int()
    branch_name = graphene.String()
    branch_ifsc = graphene.String()
    bank_name = graphene.String()
    bank_id = graphene.Int()
    bank = graphene.Field(BankType) 

class BranchFilterInput(graphene.InputObjectType):
    bank_id = graphene.Int()
    branch_id = graphene.Int()

class Query(graphene.ObjectType):
    all_branch = graphene.List(BranchType, input=BranchFilterInput())

    def resolve_all_branch(self, info, input=None):
        from .resolver import resolve_all_branch  
        branches = resolve_all_branch(input)
        
        return [BranchType(**branch) for branch in branches]
