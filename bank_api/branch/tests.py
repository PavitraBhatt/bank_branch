import pytest
from graphene.test import Client
from bank_api.schema import schema
from branch.models import Branch
from banks.models import Bank

@pytest.mark.django_db  # Use the database for testing
class TestBranchQuery:

    @pytest.fixture
    def setup_data(self):
        """Set up test data before each test."""
        bank = Bank.objects.create(id=1, name="STATE BANK OF INDIA")
        Branch.objects.create(id=9, branch="WANKANER", ifsc="SBIN0005950", bank=bank)

    def test_fetch_all_branches(self, setup_data):
        """Test retrieving branches using GraphQL query."""
        client = Client(schema)
        query = """
        query {
          allBranch(input: { bank_id: 1 }) {
            branch_id
            branch_name
            branch_ifsc
            bank {
              bank_id
              bank_name
            }
          }
        }
        """
        response = client.execute(query)

        expected_data = {
            "data": {
                "allBranch": [
                    {
                        "branch_id": 9,
                        "branch_name": "WANKANER",
                        "branch_ifsc": "SBIN0005950",
                        "bank": {
                            "bank_id": 1,
                            "bank_name": "STATE BANK OF INDIA"
                        }
                    }
                ]
            }
        }

        assert response == expected_data, f"Expected {expected_data}, but got {response}"

    def test_no_matching_branches(self):
        """Test case where no branch matches the input filter."""
        client = Client(schema)
        query = """
        query {
          allBranch(input: { bank_id: 99 }) {
            branch_id
            branch_name
            branch_ifsc
            bank {
              bank_id
              bank_name
            }
          }
        }
        """
        response = client.execute(query)
        assert response["data"]["allBranch"] == []

    def test_invalid_input(self):
        """Test case with invalid input (non-existent bank_id)."""
        client = Client(schema)
        query = """
        query {
          allBranch(input: { bank_id: "INVALID" }) {
            branch_id
            branch_name
            branch_ifsc
            bank {
              bank_id
              bank_name
            }
          }
        }
        """
        response = client.execute(query)
        assert "errors" in response, "Expected an error due to invalid input"
