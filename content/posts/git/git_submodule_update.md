Title: How to Update all Git Submodules
Date: 2019-12-19 14:36
Modified: 2019-12-19 14:36
Status: draft
Category: git
Tags: git, version control, pull request, pelican
Slug: git-submodule-update
Authors: Peter D. Kazarinoff

This post details how to update all of the submodules in a git repo.

To update all of the submodules in a git repo, open a termal and type the following commands:

```text
git submodule init
git submodule update --init --recursive
git pull origin master --recurse-submodules
```

Afterwards, update the main git repo

```text
git add .
git commit -m "my commit message"
git push origin master
```
