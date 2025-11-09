-- https://leetcode.com/problems/find-invalid-ip-addresses/

-- # Write your MySQL query statement below

select ip, count(ip) as invalid_count
from logs
where length(ip) - length(replace(ip, '.', '')) != 3
    or cast(substring_index(ip, '.', 1) as unsigned) > 255
    or left(substring_index(ip, '.', 1), 1) = "0"
    or cast(substring_index(substring_index(ip, '.', 2), '.', -1) as unsigned) > 255
    or left(substring_index(substring_index(ip, '.', 2), '.', -1), 1) = "0"
    or cast(substring_index(substring_index(ip, '.', 3), '.', -1) as unsigned) > 255
    or left(substring_index(substring_index(ip, '.', 3), '.', -1), 1) = "0"
    or cast(substring_index(substring_index(ip, '.', 4), '.', -1) as unsigned) > 255
    or left(substring_index(substring_index(ip, '.', 4), '.', -1), 1) = "0"
group by ip
order by invalid_count desc, ip desc;