#!/bin/bash

# Delete Excess Files
#
# Purges subfolders of files if the folder exceed X amount of files.
#
# Arguments:
# - arg1: maximum amount of files
# - arg2: folder location
# - arg3: head/tail sorting
# - arg4: filetype (Optional)
#
# Example:
#  ./purge-excess.sh 250 /path/to/location head jpg
#
# Notes:
# - Tested on Bash 5.0.x. on Linux
# - Credits to vanillaknot for a helping hand.

# MIT License
#
# Copyright (c) 2021 Philip Andersen
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Required parameters
if [ -z "${1}" ] || [ -z "${2}" ] || [ -z "${3}" ]; then
    echo "Required parameters are missing";
    exit 0
else
    max="$1"
    folder="$2"
    filter="$3"
fi

# Optional parameter
if [[ -n ${4} ]]; then
    filetype="$4"
else
    filetype=false
fi


# Loop trough the subfolders
for filedirs in "$folder"/*; do

    filecount="$(ls -1tr "$filedirs" | wc -l)"
    offset=$(($filecount-$max))

    # Print current folder
    echo -e "\n- Folder: $filedirs ($filecount files)"

    # If the folder doesn't have any excess, skip it.
    if [ "$max" -gt "$filecount" ]; then continue; fi

    # Check if it's a directory
    if [ -d "$filedirs" ]; then

        # Try enter directory, else skipping
        cd "$filedirs" || continue

        # Remove whitespaces in filenames
        if [ "$filetype" = false ]; then
            find . -type f -name "* *.*" -exec bash -c 'mv "$0" "${0// /_}"' {} \;
        else
            find . -type f -name "* *.$filetype" -exec bash -c 'mv "$0" "${0// /_}"' {} \;
        fi

        # The purge
        if [ "$filetype" = false ]; then
            if [ "$filter" = "head" ]; then
                ls -1tr 2>/dev/null | sort | head -n "$offset" | xargs rm -v 2>/dev/null
            else
                ls -1tr 2>/dev/null | sort | tail -n "$offset" | xargs rm -v 2>/dev/null
            fi
        else
            if [ "$filter" = "head" ]; then
                ls -1tr *.$filetype 2>/dev/null | sort | head -n "$offset" | xargs rm -v 2>/dev/null
            else
                ls -1tr *.$filetype 2>/dev/null | sort | tail -n "$offset" | xargs rm -v 2>/dev/null
            fi
        fi

        # Go up before next iteration
        cd "../.."
    fi
done
exit 0