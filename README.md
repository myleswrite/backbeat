# backbeat

A Python 3 checker to find 404s in your backlinks. Requires a CSV file with the following structure:

+ Colum 1 - Blank
+ Column 2 - Headed Source (list of source domains or URLs that link to you)
+ Column 3 - Headed Destination (list of destination URLs on your site)

Backbeat will go through each URL in column 2 to see if it is a 404 and save the results into a CSV file. It uses the Requests module to get the URL info.

IF any pages have redirects these are followed and the history column of the cav file shows what type of redirection occured. There is also a colum showing what the final URL was.

If you want to know why column one is blank… It's bacause the csv module errors for some reason…
