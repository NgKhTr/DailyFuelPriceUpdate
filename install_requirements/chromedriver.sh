#!/bin/sh
chrome_version=$(google-chrome --version | cut -d ' ' -f 3)
echo $chrome_version
wget https://storage.googleapis.com/chrome-for-testing-public/${chrome_version}/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
cp chromedriver-linux64/chromedriver /usr/local/bin/
chromedriver -v