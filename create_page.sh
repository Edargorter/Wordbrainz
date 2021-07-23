#!/bin/bash

echo "" > words.html

cat <<EOF >> words.html
<html>
<head>
<title>Words Found</title>
<style>
  table,
  th,
  td {
	padding: 10px;
	border: 1px solid black;
	font-size: 20;
	border-collapse: collapse;
  }
</style>
</head>
<body>
<h1>Words Found</h1>
<table>
<tr>
<td>Word</td>
<td>Length</td>
</tr>
EOF

cat words_found.txt | sort | awk '{print "<tr>\n<td>"$1"</td>\n<td>"$2"</td></tr>\n"}' >> words.html

cat <<EOF >> words.html
</table>
</body>
</html>
EOF
