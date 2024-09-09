#!/bin/bash

# Git pull
git reset --hard
git pull origin master

# Update database


# Install node dependencies and build prod assets
npm install
npm audit fix
npm run build
