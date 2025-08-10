#!/bin/bash

# Usage: ./start_problem.sh <numero>
# Example: ./start_problem.sh 123

if [ -z "$1" ]; then
    echo "Uso: $0 <numero>"
    exit 1
fi

NUMERO="$1"
PROBLEM_DIR="problems/$NUMERO"

mkdir -p "$PROBLEM_DIR"
touch "$PROBLEM_DIR/main.py"
touch "$PROBLEM_DIR/tests_problem_${NUMERO}.py"

echo "Carpeta y archivos creados en $PROBLEM_DIR"

code "$PROBLEM_DIR/main.py" "$PROBLEM_DIR/tests_problem_${NUMERO}.py"