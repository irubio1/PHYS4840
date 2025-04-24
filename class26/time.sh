#!/bin/bash

# Measure compilation time
echo "Compiling oddball.f90"
start_compile=$(date +%s.%N)
gfortran oddball.f90 -o oddball.exe
end_compile=$(date +%s.%N)
compile_time=$(echo "$end_compile - $start_compile" | bc)

echo "Running oddball.exe..."
# Measure execution time
start_exec=$(date +%s.%N)
./oddball.exe
end_exec=$(date +%s.%N)
exec_time=$(echo "$end_exec - $start_exec" | bc)

echo "Compilation time: $compile_time seconds for fortran"
echo "Execution time: $exec_time seconds for fortran"

python_script=true
if [ "$python_script" = true ]; then
    echo "Running rutherford...."
    
    # Measure execution time
    start_exec=$(date +%s.%N)
    python rutherford.py
    end_exec=$(date +%s.%N)

    exec_time=$(echo "$end_exec - $start_exec" | bc)
    echo "Execution time: $exec_time seconds for python"
fi
