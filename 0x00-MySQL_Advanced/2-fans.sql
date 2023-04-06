-- Script ranking origin of bands based on country ordered by no of nonunique fans
SELECT origin, SUM(fans) as nb_fans FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
