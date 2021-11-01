Feature: Sorting

Scenario: Default is sorted by Sales Volume

	Given Open the website
	When I click "Sort By"
	When I click "Sales Volume" in the dropdown-list
	Then All Collectibles are sorted by "Sales Volume"

Scenario: Sorted by Most Likes

	Given Open the website
	When I click "Sort By"
	When I click "Most Likes" in the dropdown-list
	Then All Collectibles are sorted by "Most Likes"

Scenario: Sorted by Most Views

	Given Open the website
	When I click "Sort By"
	When I click "Most Views" in the dropdown-list
	Then All Collectibles are sorted by "Most Views"

	