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
	
   print "Content-type: text/html\n";
   print "\n";

   print "<html><head><title>${TITLE} </title></head>\n";
   print "<body text=\"${TEXT}\" bgcolor=\"${BG}\">\n";

   print "   <p>\n";
   print "   <h1>${MSG}</h1>\n";
   print "   </p>\n";
   print "   <p>${secondary_msg}</p>\n";
   print "</body>\n";
   print "</html>\n";
   exit 0;