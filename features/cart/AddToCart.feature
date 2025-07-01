@cart
  Feature: Add to Cart Functionality

  @addTOCart
  Scenario: Add an item to cart
  Given user logged in with valid credentials
  When user selects the item form product list
  Then the item is added to the cart




