SELECT
    p.book,
    SUM(p.position_size * pr.price) AS book_exposure
FROM positions p
JOIN commodity_prices pr
  ON p.commodity = pr.commodity
 AND p.date = pr.date
GROUP BY p.book
ORDER BY book_exposure DESC;
