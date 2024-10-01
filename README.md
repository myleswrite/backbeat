# backbeat

A Python 3 checker to find 404s in your backlinks. Requires a CSV file with the following structure:

+ Colum 1 - Blank, or anything you like.
+ Column 2 - Headed Source (list of source domains or URLs that link to you).
+ Column 3 - Headed Destination (list of destination URLs on your site).

Backbeat will go through each URL in column 2 to see if it is a 404 and save the results into a CSV file. It uses the Requests module to get the URL info.

IF any pages have redirects these are followed and the history column of the cav file shows what type of redirection occured. There is also a colum showing what the final URL was.

If you want to know why column one is blank… It's because the csv module errors for some reason…

## Why would I use backbeat?

One of the SEO checks I do in my day job is to work through a list of sites linking to particular domain and check which of them end up in 404s. This is useful for a) Doing 301 redirects to a working page or b) Contacting the source domain and ask them to switch to a working URL. Backbeat automates working through the list and as a bonus makes it trivial to work through a list of A N Other's backlinks (for spotting opportunities to contact the source domain and ask them to switch from a 404 link on A N Other's site to a working link on mine.).

If you feel like buying me a beer for writing the script tip me here: <a href="https://www.paypal.me/mylesw42">https://www.paypal.me/mylesw42</a>
