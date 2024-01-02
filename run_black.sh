#!/bin/bash

# Example usages of the script:
# To run Black on files changed in this branch compared to the main branch, run:
# ./run_black.sh
# To run Black on files changed in this branch compared to some other branch, run:
# ./run_black.sh other-branch-name

# get the current git branch
CUR=`git rev-parse --abbrev-ref HEAD`
# The name of the branch that you want to compare against. This is typically the
# branch that you branched off from.
BRANCH=${1:-main}
# identify the files that differ from main branch
FILES=`git diff-tree -r --diff-filter=d --no-commit-id --name-only $BRANCH $CUR`

# apply black to python files
for f in ${FILES[@]}
do
   if [ ${f: -3} == ".py" ]
   then
       # The "--fast" flag is added to work around this Black Github issue:
       # https://github.com/psf/black/issues/1629
       black --fast $f
   fi
done