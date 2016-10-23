Python files (generated from IPython notebooks) to extract pronoun sets from text files.

To run for yourself, do `python make_json.py`.

The output is formatted for https://github.com/dariusk/corpora/blob/master/data/humans/thirdPersonPronouns.json

Currently reading from (not necessarily the latest versions of):

https://github.com/witch-house/pronoun.is/blob/develop/resources/pronouns.tab

http://nonbinary.org/wiki/Pronouns (English section)

http://askanonbinary.tumblr.com/pronouns

http://destroythecistem.tumblr.com/pronouns

http://pronoun-provider.tumblr.com/pronouns

TODO:

process sets of 4 or fewer pronouns to figure out the full 5-pronoun set.

correctly parse the various ways pronoun-provider specifies alternatives.

dependencies:

requests

bs4
