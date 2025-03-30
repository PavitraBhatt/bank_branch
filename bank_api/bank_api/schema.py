import graphene
import branch.schema
import banks.schema
from bank_api.resolver import Resolver

class Query(branch.schema.Query, banks.schema.Query, graphene.ObjectType):
    all_branches = graphene.List(branch.schema.BranchType, resolver=Resolver.all_branches)
    all_banks = graphene.List(banks.schema.BankType, resolver=Resolver.all_banks)

schema = graphene.Schema(query=Query)
    