#! /bin/bash

source="lnxFtrPpsExData.txt"
result="lnxFtrPpsExResult.txt"

# create result file with headers
echo "Linux Scripts Module" > ${result} && echo "Filter & Pipes" >> ${result} && echo "Excercis 1 result:" >> ${result}

# get non-english speaking countries
grep "english" -v ${source} >> ${result}
echo >> ${file}

echo "Excercise 2 result:" >> ${result}

# get country of capital city "rome"
grep "rome" ${source} | cut -f 1 >> ${result}

# open result file
vim ${result}}
