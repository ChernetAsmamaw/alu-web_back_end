-- List all the bands with Glam Rock as their main style, ranked by their longevity

SELECT band_name, COALESCE(split, 2000) - formed AS lifespan FROM metal_bands WHERE style LIKE '%Glam Rock%';