class AddToCartPage():
    PRODUCT_LIST = "xpath =//*[@class='inventory_item_name ' and text()='{PRODUCT_NAME}']"
    ADD_TO_CART="xpath=//*[@class='inventory_item_name ' and text()='{PRODUCT_NAME}']//following::div//button[text()='Add to cart']"
    REMOVE_FROM_CART="xpath=//*[@class='inventory_item_name ' and text()='{PRODUCT_NAME}']//following::div//button[text()='Remove']"
    CART= "xpath=//span[@data-test='shopping-cart-badge']"