Feature: Subscription


Scenario: sbscribe with a valid email

	Given Open the website
	When I go to "Drops"
	Then I enter a valid email
	Then I click Subscribe button
	Then I click the subcription box
	Then I click Subscribe button
	Then It shows "Click to verify"


Scenario: Cannot sbscribe without checking the box

	Given Open the website
	When I go to "Drops"
	Then I enter a valid email
	Then I click Subscribe button
	Then It shows "Please check the box to subscribe"

Scenario: Cannot sbscribe by enter an invalid email 
#This test result is failed due to a production defect.
	Given Open the website
	When I go to "Drops"
	Then I enter an invalid email
	Then I click the subcription box
	Then I click Subscribe button
	Then It shows "Please enter a valid email address"