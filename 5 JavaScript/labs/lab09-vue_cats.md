

# Lab 9: Cat API w/ Vue

Let's use Vue to build a page where users can look at pictures of cats.

- [APIs and AJAX](../docs/13%20-%20APIs%20and%20Ajax.md)
- [Cat API](https://docs.thecatapi.com/)

## Version 1

Create a page with a button that, when pressed, goes and gets a random cat image and displays it. Copy and paste the url below into your browser and look at the response. You can take the `url` and set it as the `src` attribute of an `img` to display it. [hint](https://docs.thecatapi.com/api-reference/images/images-search) [hint](../docs/Vue.md#2-setting-attributes) [hint](../docs/13%20-%20APIs%20and%20Ajax.md#ajax-in-axios)

`https://api.thecatapi.com/v1/images/search`


## Version 2

There is another part of the cat api which will give a list of categories. Use the response from this api endpoint to build a dropdown list of categories. [hint](https://docs.thecatapi.com/api-reference/categories/categories-list) [hint](../docs/Vue.md#5-input-fields) [hint](../docs/Vue.md#4-loops)

`https://api.thecatapi.com/v1/categories`

Now when the user presses the button to get a random cat image, use the selected category to filter the results.

`https://api.thecatapi.com/v1/images/search?category_ids=1`

