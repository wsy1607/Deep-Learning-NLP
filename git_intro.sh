#show file difference
git diff $file_name
#show commit history
git log
#commit without message
git commit
#show commit by hash
git show $first_few_characters_of_hash
#show most recent commit
git show HEAD~2
#show who made the change
git annotate $file_name
#show difference between commits
git diff HEAD HEAD~2
#see untracking files (edited file)
git clean -n
#delete untracking files (edited file)
git clean -f
#check local git config
git config --list --local
#change git config
git config --global $setting_name $setting_value
#discard file changes that have not yet been staged
git checkout -- $file_name
#discard file changes that have been staged
git reset HEAD $file_name
#restore a file to a older version
git checkout $first_few_characters_of_hash $file_name
#undo all the changes
git reset HEAD $repo
#show current branches
gir branch
#show difference between branches
git diff $branch_1..$branch_2
#switch to another branch
git checkout $branch_name
#create a branch
git checkout -b $branch_name
#merge two branches
git merge $source_branch $destination_branch
#create a new repository
git init $project_name
#show original repository
git remote -v
#add git remote repo
git remote add $remote_name $remote_url
#pull in changes from a remote repository
git pull $remote_name $branch_name
#push changes to a remote repository
git push $remote_name $branch_name
