#!/usr/bin/env python3
"""
Annotations
"""

import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file, 'r') as file:
    lines = file.read().split("\n")

# remove #pragma once
del lines[0]

# remove class Actor1 : public Actor {
#        private:
for index, line in enumerate(lines):
    if line.startswith('class'):
        del lines[index]
        del lines[index]
        break

# remove std::cout...
cout_indices = []
for index, line in enumerate(lines):
    if line.lstrip().startswith('std::cout'):
        cout_indices.append(index)
for i in sorted(cout_indices, reverse=True):
    del lines[i]

# remove public:
#           constructor(...) {
#               ...
#           };  
index_0 = 0
for index, line in enumerate(lines):
    if line.startswith('public'):
        index_0 = index
    if line.lstrip().startswith('};') and index_0 != 0:
        for _ in range(index - index_0 + 1):
            del lines[index_0]
        break

# change void schedule(void) to int main(int argc, char* argv[])
for index, line in enumerate(lines):
    if line.lstrip().startswith('void schedule'):
        lines[index] = '\tint main(int argc, char* argv[]) {'
        break

# remove    void init(void) {
#               ...
#           }
#        };
index_0 = 0
for index, line in enumerate(lines):
    if line.lstrip().startswith('void init'):
        index_0 = index
    if line.lstrip().startswith('};') and index_0 != 0:
        for _ in range(index - index_0 + 1):
            del lines[index_0]
        break

with open(output_file, "w") as file:
    file.write("\n".join(lines))