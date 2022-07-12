## Learn Git

CTRL + L --> clear the terminal without erase the curent command line

### Generating SSH Keys (Linux)
1. ssh-keygen -t ed25519 -C "samuel.gultom@student.president.ac.id"
2. Just enter for default settings
3. cat ~/.ssh/id_ed25519.pub
4. Copy the key and paste it while creating new SSH keys

### CONFIGURATION
1. git config --global user.name "Your Name"
2. git config --global user.email "Your Email"
3. git config --global color.ui auto --> colored output
4. git config --> Check the config command line


### Init
1. git init . --> Initialize the working directory
2. rm -rf .git --> Deleting the .git folder


### Add
1. touch file-name --> create a new file
2. git status --> Check the tracked file and staging area file(s)
3. git add file-name --> add specific file
3. git add *extension --> add specific file with same extension
4. git add . --> add all the files
5. git rm --cached file-name --> unstaging the file
6. git rm -r --cached --> unstaging all the files
7. if in you in specific directory and git add . , only the files(s) inside the directory will in the staging area.
8. git add -A --> add all the file(s) inside the specific directory


### Commit
1. git commit -m "your message" --> Make the file(s) in the commit stage/save area
2. git log --> Described all the changes
3. git show hasch-code(ex.35c07331bd53e9a1dbe704c9d0de3dfce221d515) --> Described specific project change(s) that already commit
4. cat file-name --> Showing all the code(read-only) scripts
5. git diff --> Showing changes
6. git log --> get the latest commit info
7. git show hash-code --> described the specific changes (same like git diff)
8. if you have some changes in specific file, you can type git diff to see what kind of changes that you had made (red = deletion, green = insertion)
9. git restore file-name --> to discard all the changes to the first fresh repo


### Amend Commits
1. git commit --amend -m "new message" --> Changing the commit message

### Push
1. git remote add origin ssh-url --> Remote the repo through ssh url
2. git branch --> Check the repo branch
3. git branch -M branch-name --> Initialize the repo branch (or change the local repo from master to the github repo branch (main))
4. git push -u origin branch-name --> Push the repo



