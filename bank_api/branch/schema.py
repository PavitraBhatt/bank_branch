import graphene

# ✅ Define Bank Type
class BankType(graphene.ObjectType):
    bank_id = graphene.Int()
    bank_name = graphene.String()

# ✅ Define Branch Type
class BranchType(graphene.ObjectType):
    branch_id = graphene.Int()
    branch_name = graphene.String()
    branch_ifsc = graphene.String()
    bank_name = graphene.String()
    bank_id = graphene.Int()
    bank = graphene.Field(BankType)  # ✅ Nest BankType inside BranchType

# ✅ Define Input Type
class BranchFilterInput(graphene.InputObjectType):
    bank_id = graphene.Int()
    branch_id = graphene.Int()

# ✅ Define Query Class
class Query(graphene.ObjectType):
    all_branch = graphene.List(BranchType, input=BranchFilterInput())

    # ✅ Fix Resolver to Return ObjectType Instances
    def resolve_all_branch(self, info, input=None):
        from .resolver import resolve_all_branch  # Import resolver
        branches = resolve_all_branch(input)
        
        # ✅ Convert dictionaries into Graphene ObjectType instances
        return [BranchType(**branch) for branch in branches]
