#!/bin/bash

#WARNING: will overwrite all your local repo shit. Replaces it with remote repo.

git fetch --all

git reset --hard origin/master
