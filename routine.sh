#!/bin/sh
help()
{
    echo "Automatic Paifu Crawling Shell Script"
}

year=2024
decompress=false
current_year=2024
week=true

while getopts "csdy:" opt;
do
    case $opt in
        c)
            ;;
        s)
            week=false
            ;;   
        d)
            decompress=true
            ;;
        y)
            year=$OPTARG
            ;;
        *)
            help
            exit 0
            ;;
    esac
done

if [ "$year" -eq "$current_year" ]
then
    if [ "$week" == true ]
    then
        python3 main.py -a id -p ./db/$year.db
    else
        python3 main.py -a id -p ./db/$year.db -s
    fi
    python3 main.py -a content -p ./db/$year.db
else
    mkdir temp
    curl https://tenhou.net/sc/raw/scraw$year.zip -o ./temp/scraw$year.zip
    python3 main.py -y $year --from_archive -a id -p db/$year.db
    python3 main.py -a content -p ./db/$year.db
fi

if [ "$decompress" == true ]
then
    python3 getlog.py -p ./db/$year.db
fi