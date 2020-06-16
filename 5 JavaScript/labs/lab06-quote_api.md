
# Lab 6: Random Quote

Before starting, check out the doc on [APIs and AJAX](../docs/13%20-%20APIs%20and%20Ajax.md).

Use the [favqs.com](https://favqs.com/api/) api to show a random quote. Send a `GET` request to `https://favqs.com/api/qotd`, extract the relevant information, and display it on the page.

## Version 2

The API also supports browsing quotes. Add an `input type="text"` and a `search button`, then use the `filter` query parameter to get a bunch of quotes. Then you can show those quotes in a list. In order to get authorization for this request, we need to add a request header with the authorization token.

```javascript
let headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
```

## Version 3 (optional)

Add next page / previous page buttons, and the `page` query parameter to move between pages.
