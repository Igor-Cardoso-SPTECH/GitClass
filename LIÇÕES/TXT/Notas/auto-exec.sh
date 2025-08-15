#!/bin/bash

data="$(date +"%d/%m/%Y %H:%M:%S")"

cd /home/kanjaxay/Documents/GitClass/

git add .
git commit -m "Atualização repositorio $data"
git push
