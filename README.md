AutoSpell
=============================

Sublime Text 3 packge to auto replace spelling mistakes.

By default the following characters will trigger a correction:

	-:;_,.  and the enter key

Settings can be added to in `SublimeText -> Preferences -> Package Settings -> AutoSpell -> Settings – User`

You can add to this list of triggers by modifying the `triggers` section.

By default the package corrects common words and their capitalized versions. For example `teh` and `Teh` will be replaced by `the` and `The`. You can add to this list of replacements by modifying the `replacements` section.

See the default config for examples.

If you have a list of words that would be good to add to the default list of replacements please submit a pull request.