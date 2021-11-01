Feature: Marketplace

Scenario: Check curated card details

	Given Open the website
	When I go to "Marketplace"
	Then The title is "Marketplace"
	Then I filter "curated" cards 
	Then I scroll down
	Then I click the cards
	

Scenario: Check all card details

	Given Open the website
	When I go to "Marketplace"
	Then The title is "Marketplace"
	Then I scroll down
	Then I click the cards
	

