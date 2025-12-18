SELECT
    p.commodity,
    SUM(
        p.position_size * pr.price * (-0.05)
    ) AS scenario_pnl
FROM positions p
JOIN commodity_prices pr
  ON p.commodity = pr.commodity
 AND p.date = pr.date
GROUP BY p.commodity;
