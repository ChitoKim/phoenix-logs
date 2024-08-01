#!/bin/sh
help()
{
    echo "Automatic Paifu Crawling Shell Script"
}

year=2024
decompress=false

while getopts "cwdy:" opt;
do
    case $opt in
        c)
            current_year=true
            ;;
        w)
            week=true
            ;;   
        d)
            decompress=true
        y)
            year=$OPTARG
            ;;
        *)
            help
            exit 0
            ;;
    esac
done

if $year -eq 2024
then
    python3 main.py -a id -p ./db/$year.db
    python3 main.py -a content -p ./db/$year.db
else
    mkdir temp
    curl https://tenhou.net/sc/raw/scraw$year.zip -o ./temp/scraw$year.zip
    python3 main.py -y $year --from_archive -a id -p db/$year.db
    python3 main.py -a content -p ./db/$year.db
fi

if $decompress
then
    python3 getlog.py -p ./db/$year.db
fi