Python files (generated from IPython notebooks) to extract pronoun sets from files retrieved by HTTP.

To run for yourself, do `python make_json.py`.

The output is formatted for https://github.com/dariusk/corpora/blob/master/data/humans/thirdPersonPronouns.json

To contribute, use `ipython notebook --script` (or equivalent non-deprecated command) to alter the `.ipynb` files. Manual changes to the `.py` files are overwritten.

Currently reading from :

* https://github.com/witch-house/pronoun.is/blob/develop/resources/pronouns.tab
* http://nonbinary.org/wiki/Pronouns (English section)
* http://askanonbinary.tumblr.com/pronouns
* http://pronoun-provider.tumblr.com/pronouns (the largest contributor)

TODO:

* process sets of 4 or fewer pronouns to figure out the full 5-pronoun set.
* correctly parse the various ways pronoun-provider specifies alternatives.

Dependencies:
* requests
* bs4
