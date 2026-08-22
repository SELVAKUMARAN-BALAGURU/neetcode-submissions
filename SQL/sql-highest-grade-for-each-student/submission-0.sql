-- Write your query below
select student_id,exam_id,score from(
    select e.*,row_number() over(partition by student_id order by score desc,exam_id asc) as rnk from  exam_results e) x where x.rnk=1;

