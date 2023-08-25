find . -type f -not -name "*checkpoint*" -not -name "git" -regex ".*\.\(txt\|py\|log\|json\|yaml\)\.?" | xargs sed -i "s/$1/$2/g"
find . -type f -name "*$1*" -exec rename "s/$1\./$2\./" {} \;
find . -type f -name "*$1*" -exec rename "s/$1\-/$2\-/" {} \;