# How to build the biography and award pages

Change the title of the page. Edit the ```<title>``` tag using the format "Tim Berners-Lee | Turing Awards"

Leave the navbar as is.

---
The structure of the page is up to you. Work inside the ```<section>``` tag.

### Columns

For positioning text aside the image we are using Bootstrap grid system.
Use the ```row``` and ```col-md-<x>``` tags.
It will look something like this:

```html

<div class="row">
    <div class="col-md-7 paragraph">
        <p>Your wonderful paragraph.</p>
    </div>
    <div class="col-md-5">
        <img class="brd-round" src="images/decades/2010/2016.jpg">
    </div>

</div>
```

The total number of columns is 12. You can adjust the extension of a column at your discretion. You can find
documentation about Bootstrap grid system [here](https://getbootstrap.com/docs/5.1/layout/grid/).

```paragraph``` class is used to justify text. Use it inside the parent div of a text element.

```brd-round``` class will round the borders. Use it in the ```<img>``` tags.

### Title

User the class ```title``` inside heading tags.

```html
<h1 class="title">Tim Berners-Lee</h1>
```

### Button

To add a button use an ```<a>``` tag. Simply add the ```button``` class.

```html
<a href="<your-link-here>" class="button">This is a button!</a>
```

### Centring

To center something just wrap the element in a ```<div>``` and add the following utilities
classes: ```d-flex justify-content-center align-items-center```

```html

<div class="d-flex justify-content-center align-items-center">
    ...
</div>
```

### Table

Use the table element normally, juyst add the ```tbl``` class. To make the first row a different color from the rest of
the table:
Use ```<thead>``` for the first row. Use ```<tbody>``` for the rest of te table.

```html

<table class="tbl">
    <thead>
        <tr>
            <th>This is</th>
            <th>your</th>
            <th>Title</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>table data</td>
            <td>some data</td>
            <td>other data</td>
        </tr>
        ...
        <tr>
            <td>hello fellow student</td>
            <td>there is so much data</td>
            <td>data is cool</td>
        </tr>
    </tbody>
</table>
```

### Link

To make a simple link just add the ```link``` class to an ```<a>``` tag.

```html
<a href="<your-link-here>" class="link">This is a link</a>
```

---
Don't worry about colors. We can change them later on.

## If you need help, have any suggestion or need any other element don't hesitate to mention the ```@css-leader```s on the [Discord server](https://discord.gg/mj5NDDUQf3) in the ```#css-discussion``` text channel.