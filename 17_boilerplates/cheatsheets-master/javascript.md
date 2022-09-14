# JavaScript

- `var current_url = window.location.pathname.split("/")`
- `parseInt(); parseFloat(); toString();`
- `for (property in object) { console.log(property); };`
- `for (var i = 0; i < array.length; i++) { console.log(array[i]); };`
- `var l = [];`: pop, push, shift, unshift, delete, splice, sort, reverse.

## Select2 library

- `$('#select').select2().select2('val', 'string');`
- `$('#select').select2('data').text;`
- `$('#select').select2({width: 'resolve'}); // or dropdownAutoWidth: True`

## JQuery

- `$('').show();`
- `$('').hide();`
- `$('').css('attr', 'value');`
- `$('').addClass();`
- `$('').removeClass();`
- `$('').append();`
- `$('').change(function(){};);`
- Text from input text field: `$().val()`
- Value of select option: `$('#selectid').val()`
- Text of select option: `$('#selectid option:selected').text()`

## General Solutions

### Refreshing the page

```javascript
function autoRefresh()
{
    window.location = window.location.href;
}
setInterval('autoRefresh()', 5000); // this will reload page after every 5 seconds
```

```javascript
 function autoRefresh1()
{
       window.location.reload();
}

setInterval('autoRefresh1()', 5000); // this will reload page after every 5 secounds; Method II
```

```javascript
 function autoRefresh1()
{
       window.location.reload();
}
 
 setInterval('autoRefresh1()', 5000); // this will reload page after every 5 secounds; Method II
```

#### Using metatags

```html
<head>
    <meta http-equiv="refresh" content="5" />
    <!-- This will refresh page in every 5 seconds, change content= x to refresh page after x seconds -->
</head>
```

```html
<head>
<meta http-equiv="refresh" content="5" />
    <!-- This will refresh page in every 5 seconds, change content= x to refresh page after x seconds -->
</head>
```

#### Refresh div or span on HTML page after specific time

`<div id="result"></div>`

Then jQuery code:

```javascript
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<script>
    function autoRefresh_div()
    {
        $("#result").load("load.html"); // a function which will load data from other file after x seconds
    }
    setInterval('autoRefresh_div()', 5000); // refresh div after 5 secs
</script>

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<script>
function autoRefresh_div()
{
     $("#result").load("load.html");// a function which will load data from other file after x seconds
}
 
setInterval('autoRefresh_div()', 5000); // refresh div after 5 secs
</script>
```

$.ajax() or $.post() and others can be used instead of load() function and put the response in a div or a span.
