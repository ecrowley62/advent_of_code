#/usr/bin/bash
##########################################################################
# Shell script for auto generating a given days files, becuase I am lazy #
##########################################################################

# Provide helpfull info about script
help() {
    echo "Create a given days directory and files"
    echo
    echo "-d The number for the day"
    echo
    echo "-n The name of the given days challange"
    echo
}

CHALLANGE_NAME="no_name_provided"

# Get input argument
while getopts "d:n:h" inputvalue; do
    case "${inputvalue}" in
        d)
            DAY_NUM=${OPTARG}
            ;;
        n)
            CHALLANGE_NAME=${OPTARG}
            ;;
        h)
            help
            exit 0
            ;;
        *)
            echo "Unrecognized arg provided"
            echo
            help
            exit 1
            ;;
    esac
done

# Error out if no args were provided to the script
if [ $# -eq 0 ]; then
    echo "No number of the day param or challange name was provided. This must be provided!"
    exit 1
fi

# Create the directory and boiler plate files
DIR_NAME="day${DAY_NUM}_${CHALLANGE_NAME}"
mkdir $DIR_NAME
touch ./$DIR_NAME/input.txt
touch ./$DIR_NAME/problem_statement.txt
touch ./$DIR_NAME/solution_one_value.txt
touch ./$DIR_NAME/solution_one.py
touch ./$DIR_NAME/solution_two_value.txt
touch ./$DIR_NAME/solution_two.py