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
