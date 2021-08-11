linux source lists Treasure
---

# What is source list in linux?
Source list ("sources.list") is a file that contains software repositories (sources).
in some distributions like Arch or CentOS, there is no "source list". The name is "mirror list" !!!

## What is repository?
Linux repository is a storage location that contains source packages which organized in a special directory. Each repository is a set of software hosted on a remote server and intended to be used for installing and updating software packages. "package managers" can do this "installing and updating" part.

## Access to source list and write them

* Debian bases (debian, ubuntu, mint,...) :
	
	In this distributions, the package manager is **Apt**.
	[debian](https://wiki.debian.org/SourcesList) says:
		The main Apt sources configuration file is at `/etc/apt/sources.list`. You can edit this files (as root) using your favorite text editor. To add custom sources, creating separate files under `/etc/apt/sources.list.d/` is preferred. official repositories for example:
		```bash
		/etc/apt/sources.list.d/official-package-repositories.list
		```
		Ubuntu and mint and... are the same


* Arch and Manjaro:

	In this distributions, the package manager is **Pacman** and We have "mirror" instead of "source".
	You can access to this mirrors in:
	```bash
	/etc/pacman.d/mirrorlist
	```


* OpenSUSE:

	the package manager for OpenSUSE is **Zypper**.
	```bash
	/etc/zypp/repos.d/	
	```


* Gentoo:

	In this distribution, the package manager is **Portage**.
	find repository lists in:
	```bash
	/etc/portage/repos.conf	
	```


* CentOS:
	
	**Yum** is the package manager.
	Edit lists like `Centos-Base.repo` that contains main sources in:
	```bash
	/etc/yum.repos.d/
	```


* Fedora:
	
	I think Fedora is a improved CentOS. like CentOS ".rpm" is the format of packages but **Dnf** is the package manager.
	Fedora and CentOS were distributed from Red Hat. So the location is the same:
	```bash
	/etc/yum.repos.d
	```