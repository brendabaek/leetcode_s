-- https://leetcode.com/problems/dna-pattern-recognition/

-- # Write your MySQL query statement below

select *,
    if(left(dna_sequence, 3) = 'ATG', 1, 0) as has_start,
    if(right(dna_sequence, 3) in ('TAA', 'TAG', 'TGA'), 1, 0) as has_stop,
    if(dna_sequence regexp 'ATAT', 1, 0) as has_atat,
    if(dna_sequence regexp 'GGG', 1, 0) as has_ggg
from Samples;