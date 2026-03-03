# Write your MySQL query statement below
select ps.firstname,ps.lastname,ad.city,ad.state
 from person as ps left join address as ad on ps.personId = ad.personId;