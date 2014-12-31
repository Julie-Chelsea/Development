##wordsets: (Korean) Word Sets

####Purpose
This holds all of the possible word sets that the user can choose from to create their own specialized experience.

Note that while the title is wordsets, perhaps a better name would be lessons. Buuut I'm too lazy to change that now that I've used 'wordsets' so many times. Maybe later.

I don't know if this is possible, but perhaps we could modify the ID, position, and count columns for each of the users.

So perhaps the default order of the wordsets is [1] Food, [2] Education, and [3] Entertainment; if the user wants to learn those wordsets in the reverse category, then we would allow them to change the position that them (their learning path/experience), and then we would store override the data in the 'Position' column entries to reflect their chosen order.

If that's the case, then what we could do is have another table which tracks/saves the following:
* UserID
* ID (from wordset table)
* Position (from wordset table)

Should we let them change the number of words in each wordset ('Count')?  I think that would perhaps introduce too many options, and perhaps the user will spend more time on customization than they do on learning lol.

As for when we introduce new languages, perhaps we could have a column that indicates the language, or just have a different table for each language. We could always prefix the table with an abbreviation of the language name (eg. KOR-wordsets)

####Structure
Columns include:
* Name
* ID (doesn't have to be random, is unique)
* Position
* Count
* Category

#####Category
Let's use the following entries for categories:
* **[v]ocab**: Just individual words, such as ('Hello', 'Bye')
* **[p]hrases**: Self-explanatory, eg. Chelsea is awesome
* **[g]rammar**: Grammatical concepts (eg. conjugation)
* **[c]omplex**: Vocab and phrases
