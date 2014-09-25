import sublime, sublime_plugin, sys, json, inspect, os

# http://sublimetexttips.com/execute-a-command-every-time-sublime-launches/
def plugin_loaded():	
	sys.stdout.write('Loading AutoSpell\n')

	settings = sublime.load_settings("AutoSpell.sublime-settings")

	key_map = []

	replacements = settings.get('replacements', {})
	triggers = settings.get('triggers', [])

	for mispelled in replacements:
		replacement = replacements[mispelled]

		for key in triggers:
			char = key
			if char == 'enter':
				char = '\n'

			# lowercase version
			entry = {'command': 'insert', 'args': {}}
			entry['args']['characters'] = replacement + char
			entry['keys'] = list(mispelled)
			entry['keys'].append(key)

			key_map.append(entry)

			# TODO make it DRY
			# capitalize first letter version
			entry = {'command': 'insert', 'args': {}}
			entry['args']['characters'] = (replacement + char).capitalize()
			entry['keys'] = list(mispelled.capitalize())
			entry['keys'].append(key)

			key_map.append(entry)

	current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	key_map_data = open('%s/Default.sublime-keymap' % current_dir, 'r+')
	key_map_data.write(json.dumps(key_map, indent=2, sort_keys=True))
	key_map_data.close()
