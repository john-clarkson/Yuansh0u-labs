# Git-note
###author: yuanshou
### create a new repository on the command line
```sh
echo "# blank" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/john-clarkson/blank.git
git push -u origin master
```

### push an existing repository from the command line

```sh
git remote add origin https://github.com/john-clarkson/blank.git
git branch -M master
git push -u origin master
```
```sh
git remote add origin https://github.com/john-clarkson/yuansh0u-labs.git
git branch -M master
git push -u origin master
```

### my test cli
```sh
git add <folder name>
git commit -a --allow-empty-message -m ''
git rm =delete localfile and remote
git rm --cached =only remote not localfile
git push -f origin master =force sync without reject error
```

### example
```sh
$git config user.name 'yourname'
$git config user.email 'yourmail'
###.git folder is hidden.
$cat .gitconfig 
[user]
	email = 751070874@qq.com
	name = john-clarkson

$git add test-folder/
$git ls-files
$git commit -a --allow-empty-message -m ''
$git push -f origin master

Username for 'https://github.com': 751070874@qq.com
Password for 'https://751070874@qq.com@github.com': 
Enumerating objects: 840, done.
Counting objects: 100% (840/840), done.
Delta compression using up to 4 threads
Compressing objects: 100%
```
### git rm vs git rm --cached
```sh
$git rm -r testing-folder/
rm 'testing-folder/testing'
~
###so where is testing-folder??? gone...i'ts gone!!!
$ls
 ansible-playgroud   git-note.md                   lab-test-Yuansh0u         'Shrink vmdk.yaml'
 Desktop             go                            openbmp                    snap
 Documents           go1.14.6.linux-amd64.tar.gz   Pictures                   Yuansh0u-labs
 Downloads           gobuster-test.txt             python3-nornir-playgroud
 frr-debian          kuber-deployment              README.md
```

```sh

$git rm --cached README.md 
rm 'README.md'
~
###Still here!!!!
$ls
 ansible-playgroud   git-note.md                   lab-test-Yuansh0u         'Shrink vmdk.yaml'
 Desktop             go                            openbmp                    snap
 Documents           go1.14.6.linux-amd64.tar.gz   Pictures                   Yuansh0u-labs
 Downloads           gobuster-test.txt             python3-nornir-playgroud
 frr-debian          kuber-deployment              README.md
~
```
### vscode with git
```sh
#!bin/bash

git commit -a --allow-empty-message -m ''

git push -f origin master
```

   
