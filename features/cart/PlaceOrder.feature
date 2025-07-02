@placeorder
  Feature: Place order Functionality

    Scenario: Complete checkout for placed item
      Given user logged in and has item in cart
      When the user complete the checkout
      And order is confirmed
      Then order placed successfully