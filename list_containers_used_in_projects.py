import gitlab
import re


# main entry point for script
def main():
	used_containers = {}

	# read config file
	gl = gitlab.Gitlab.from_config('my-gitlab', ['gitlab.cfg'])

	print('Hello, let\'s examine the projects at ', gl.url, ' today.')
	print('Going to fetch all repositories first...')

	# fetch all repositories from Gitlab
	projects = gl.projects.list(all=True)
	if len(projects) == 0:
		print('Could not find a single repo, giving up...')
		exit(1)
	else:
		print('OK, found {} repositories to check, please stand by'.format(len(projects)))

	# Check each repository for a .gitlab-ci.yml file
	for x in projects:
		# fetch the full project (otherwise files could not be fetched)
		project = gl.projects.get(x.id)

		try:
			# fetch the file including it's content
			f = project.files.get(file_path='.gitlab-ci.yml', ref='master')
		except:
			#print("OK: no Gitlab CI config file found.")
			continue

		# regex out all lines containing the string "image:"
		p = re.compile('image\:.*')
		images_used = p.findall(f.decode().decode('utf-8'))

		# for all images found, add them to the resulting list
		for image in images_used:
			if image not in used_containers:
				used_containers[image] = {}
			used_containers[image].update({project.name: 1})

	# Render the final output and show the list
	print()
	print('OK, the following container images are used:')
	for i in used_containers.keys():
		print(i)
		for project in used_containers[i]:
			print('	-> ', project)
	#	print('----------------------------------------')


if __name__ == "__main__":
    main()
