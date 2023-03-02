Feature: Customers
""" 
Ensure that the database data is loaded corre0ctly and other pages can be accessed
"""

Scenario: success for visiting customer and customer details pages
    Given I navigate to the index pages
    When I click on the link to mdtag details
    Then Madtag's data statistics and analysis page should be displayed


