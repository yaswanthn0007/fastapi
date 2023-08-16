

empid name did sal


did dnmae



select * from
(
select *, rownumber over(partition by did order by sal desc ) rn from
emp left join dept on emp.did=dept.did
)A where A.rn = 2













