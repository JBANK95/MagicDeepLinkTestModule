#!/bin/sh
pwd
cd ..
current_dir=`pwd`
echo "$current_dir"
podfile="$current_dir/Podfile"
echo "$podfile"
#/usr/bin/python3 MagicDeepLinkTestModule/MagicDeepLinkTestModule/.MagicDeeplinkConfig/.DeepLinkingCompliance.py
while read line; do
# reading each line
echo "$line"
done < $podfile
