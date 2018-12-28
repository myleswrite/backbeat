# backbeat

A Python 3 checker to find 404s in your backlinks. Requires a CSV file with the following structure:

Colum 1 - Blank
Column 2 - Headed Source (list of source domains or URLs that link to you)
Column 3 - Headed Destination (list of destination URLs on your site)

Backbeat will go through each URL in column 2 to see if it is a 404 and save the results into a CSV file.

If you want to know why column one is blank… It's bacause the csv module errors for some reason…
