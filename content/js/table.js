/*!
 * shariff - v1.23.0 - 26.01.2016
 * https://github.com/heiseonline/shariff
 * Copyright (c) 2016 Ines Pauer, Philipp Busse, Sebastian Hilbig, Erich Kramer, Deniz Sesli
 * Licensed under the MIT license
 */


/*!
  $(document).ready(function () {
    $("article table").addClass("table table-condensed table-bordered table-hover");
  });
 */

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
  tables[i].className = 'table table-bordered table-hover table-striped table-responsive';
}

