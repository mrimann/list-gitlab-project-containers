# See which of our Gitlab projects uses what container images

We're using Gitlab CI do build and deploy our projects. So far this was pretty aligned between project's major version matching an Ubuntu release. So for example, all Neos CMS v5.3.x are running on Ubuntu 20.04 LTS.

In our CI config, we therefore used container images that contained the matching toolset used for this project generation. At some point there was something to be changed in those toolset-containers that we considered **breaking** for existing projects and wanted to find out all projects that need a certain container image.

So the goal of this script is to enumerate all projects and generate a list like the one below, so we can prepare the needed changes for all affected projects, instead of finding out over the course of the next weeks or even months where ever we broke something...

```
(...)
OK, the following container images are used:
image: registry.example.org/infrastruktur/docker-surf-deploy:focal
	->  Project A
	->  Project B
	->  Project C
image: ubuntu:xenial
	->  Project B
	->  Project D
(...)
```

## Installation + Preparation
Install the `python-gitlab` package, e.g. via pip:
```
sudo pip install python-gitlab
```
Create a `gitlab.cfg` file in this repository containing the configuration, see `gitlab.cfg_example` for an example. You'll need

- the URL of your Gitlab instance, e.g. "https://gitlab.example.org"
- a personal access token for this gitlab installation

## Usage
Once configured, you can simply run the script and see it's output with:

```
python3 list_containers_used_in_projects.py
```

## License

Licensed under the permissive [MIT license](http://opensource.org/licenses/MIT) - have fun with it!

### Can I use it in commercial projects?

Yes, please! And if you save some of your precious time with it, I'd be very happy if you give something back - be it a warm "Thank you" by mail, spending me a drink at a conference, [send me a post card or some other surprise](http://www.rimann.org/support/) :-)