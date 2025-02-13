"""
4a. Write a set of commands that would guarantee a clean push to your GitHub, starting from the
assumption that the code on your local machine is “ahead” of your main branch on GitHub.
Hint: Don’t forget to “pull” first
4b. Write a set of commands to remove git from your repository (un-git a repository)
"""


#Start with:

git status

""" Should return:
On branch main
Your branch is up to date with 'origin/main'

and is safe to continue"""

git pull origin main
""" Makes sure that my branch is up to date with my
 remote repository version on github.com """

git status 
git add <my_file.py>
git commit -m "useful commit message about the file I'm adding"
git push origin main



""" To REMOVE git from my respository (ungit)
* Be careful about these commands* """

rm -rf .git
rm -rf .gitignore

#then:
git status

"""This should return an error telling me there's no git repository present:
fatal: not a git repository (or any of the parent directories): .git

if this error does not show, something has gone horribly, terribly wrong 
(recursive versions of git)

"""

#Only if error doesn't return as it should:
find . -name ".git" -type d
find . -name ".gitignore" -type d

""" From here, ungit any respositories that turn up in your search """
