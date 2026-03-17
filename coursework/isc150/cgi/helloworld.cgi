#! /usr/bin/perl

# file: helloworld.cgi
# This program demonstrates:
#     - printing the HTTP header BEFORE anything else
#     - sending "hard-coded" html to STDOUT.
#     - the use of the "special" first line beginning with a #!
#	  - using "variable substitution".

use 5.004;

	my $TITLE ="Hello World with Variables";
	my $BG = "#C6E2FF";
	my $TEXT = "#000000";
	my $MSG = "Hello World!";
	my $secondary_msg = '&mdash; I have variables!';
	my $german_msg = '&mdash; Wie Geht\'s?';
	my $aussie_msg = '&mdash; G\'Day!';
	my $italian_msg = '&mdash; Ciao!';
	my $hawaiian_msg = '&mdash; Aloha!';
	
   print <<"END_OF_STRING";
Content-type: text/html

<html><head><title>${TITLE}</title></head>
<body text="${TEXT}" bgcolor="${BG}">
   <p>
   <h1>${MSG}</h1>
   </p>
   <p>
From a list of characters
<ol type="i">
<li> German $german_msg
<li> Australian $aussie_msg
<li> Italian $italian_msg
<li> Hawaiian $hawaiian_msg
</ol>
   </p>
</body>
</html>

END_OF_STRING
   exit 0;

