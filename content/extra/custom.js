/*!
 * shariff - v1.23.0 - 26.01.2016
 * https://github.com/heiseonline/shariff
 * Copyright (c) 2016 Ines Pauer, Philipp Busse, Sebastian Hilbig, Erich Kramer, Deniz Sesli
 * Licensed under the MIT license
 */
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_HTML"></script>
<script async src="https://media.ethicalads.io/media/client/ethicalads.min.js"></script>

  $(document).ready(function () {
    $("article table").addClass("table table-condensed table-bordered table-hover");
  });


/*!
var tables, i;
tables = document.getElementsByTagName('table');
for (i=0;i<tables.length;i++) {
  tables[i].className = 'table table-striped';
}
 */

var tables, i;
tables = document.getElementsByTagName('table');
for (i=0;i<tables.length;i++) {
  tables[i].className = 'table table-bordered table-hover table-striped';
}

/*!
<script>
  $(document).ready(function () {
    $("table").attr("class","table table-condensed table-bordered");
  });
</script>
 */