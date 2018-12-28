# backbeat

A Python 3 checker to find 404s in your backlinks. Requires a CSV file with the following structure:

Column 1 - Source (list of source domains or URLs that link to you)
Column 2 - Destination (list of destination URLs on your site)

Backbeat will go through each URL in column 2 to see if it is a 404 and save the results into a CSV file.
