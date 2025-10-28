-- https://leetcode.com/problems/find-covid-recovery-patients/

-- # Write your MySQL query statement below

select c1.patient_id, p.patient_name, p.age, min(datediff(c1.test_date, first_p)) as recovery_time
from covid_tests as c1
right join (
    select patient_id, min(test_date) as first_p
    from covid_tests
    where result = 'Positive'
    group by patient_id
    ) as c2 on c1.patient_id = c2.patient_id
left join patients as p on p.patient_id = c1.patient_id
where result = 'Negative' and first_p < c1.test_date
group by patient_id, patient_name, age
order by recovery_time, patient_name;