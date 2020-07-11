
# CSS Properties

For more info, look [here](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) and [here](https://www.w3schools.com/cssref/).


| property | description |
|--- |--- |
| color, background-color | foreground and background color, possible values look like `red`, `#FF0000`, `rgb(255,0,0)` or `rgba(255,0,0,1.0)`  |
| background-image | background image `url(myimage.jpg)`|
| text-align | text alignment, possible values are `left`, `right`, `center` and `justify` |
| display | controls how the element is displayed, possible values are `block`, `inline`, `inline-block` and `none` |
| width, height | the element's width and height, possible values look like `50px`, `100em`, `50%` |
| border | the element's border `1px solid black` |
| margin, padding | the element's margin (external) and padding (internal) |
| font-family, font-size | the font family and font sized used within the element |



## Position

The `position` property controls an elements position, whether it's relative to the parent, page, or viewport. You can read more about `position` on the MDN [here](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Positioning), [here](https://developer.mozilla.org/en-US/docs/Web/CSS/position), and [here](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Practical_positioning_examples). Also [here](https://cssreference.io/positioning/).

| Property | Example |
|--- |--- |
| `position` | `position:absolute` |
| `top` | `top:10px` |
| `bottom` | `bottom:10px` |
| `left` | `left:10px` |
| `right` | `right:10px` |
| `z-index`| `z-index:-1`, `z-index:10` |


### Position Values

| name | description |
|--- |--- |
| `static` | the default value |
| `relative` | positioned like `static`, but `top`, `bottom`, `left` and `right` can be used as offsets relative to its normal position (within its parent, among its siblings) |
| `absolute` | positioned relative to the top-left corner of the parent element, `top`, `bottom`, `left` and `right` can be used as offsets |
| `fixed` | positioned like `absolute`, but relative to the viewport |
| `sticky` | positioned like `static` until it reaches the top of the viewport, then it behaves like `fixed` |
| `inherit` | the same positioning as its parent |


### Z-Index

The property `z-index` determines how elements are displayed when they overlap. The value of `z-index` can either be an integer or `auto`, which takes the `z-index` the parent element. Elements with larger `z-index` values are 'closer' to the viewer, and are drawn 'on top', those with lower `z-index` values are 'further' from the viewer, and are drawn 'behind' them. You can read more about `z-index` on the [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/z-index).



