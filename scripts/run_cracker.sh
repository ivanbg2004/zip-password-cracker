#!/bin/bash

zip_file=""
max_length=""
retries=10

usage() {
    echo "Usage: $0 -z zip_file -m max_length [-r retries]"
    exit 1
}

while getopts ":z:m:r:" opt; do
  case ${opt} in
    z )
      zip_file=$OPTARG
      ;;
    m )
      max_length=$OPTARG
      ;;
    r )
      retries=$OPTARG
      ;;
    \? )
      usage
      ;;
    : )
      echo "Invalid option: $OPTARG requires an argument"
      usage
      ;;
  esac
done

if [[ -z "$zip_file" || -z "$max_length" ]]; then
    usage
    exit 1
fi

for i in $(seq 1 "$retries"); do
    python3 src/password_cracker.py "$zip_file" "$max_length"
    if [ "$?" -eq 0 ]; then
        echo "Password cracking completed successfully."
        break
    else
        echo "Password not found, retrying attempt: $i..."
    fi
    if [ "$i" -eq "$retries" ]; then
        echo "Exceeded maximum number of attempts. Exiting..."
        exit 1
    fi
done
