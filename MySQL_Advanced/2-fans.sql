-- Rank country origins of bands by number of fans(non unique)

SELECT origin, SUM(fans) as nb_fans FROM metal_bands GROUP BY origin
ORDER BY nb_fans DESC;