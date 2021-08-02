import sys


input = [
    1822,
    1917,
    1642,
    1617,
    1941,
    1740,
    1529,
    1896,
    1880,
    568,
    1897,
    1521,
    1832,
    1936,
    611,
    1475,
    1950,
    1895,
    1532,
    1721,
    1498,
    1905,
    1770,
    1845,
    2003,
    1854,
    1705,
    1916,
    1913,
    1956,
    1798,
    1823,
    1955,
    1713,
    1942,
    1710,
    1696,
    1590,
    1966,
    1476,
    1800,
    1672,
    1533,
    1524,
    1957,
    1923,
    1545,
    534,
    1707,
    1760,
    1104,
    1471,
    1947,
    1802,
    1525,
    1931,
    1653,
    1608,
    1937,
    1977,
    1598,
    1470,
    1794,
    1488,
    1786,
    1652,
    1482,
    1603,
    1667,
    1245,
    1478,
    667,
    1948,
    1885,
    547,
    1971,
    1795,
    1910,
    1571,
    1711,
    1727,
    1987,
    1597,
    1586,
    1661,
    1893,
    1873,
    1827,
    1561,
    2006,
    1782,
    1813,
    2000,
    1592,
    1714,
    1849,
    1501,
    1809,
    1751,
    1935,
    1692,
    1697,
    1878,
    1502,
    1738,
    1731,
    1682,
    1690,
    1499,
    1641,
    1925,
    1996,
    1972,
    1886,
    1836,
    1747,
    1841,
    1668,
    715,
    1698,
    1859,
    1637,
    1477,
    1785,
    1695,
    1702,
    1944,
    1631,
    1771,
    1623,
    1892,
    1466,
    1834,
    1899,
    201,
    1801,
    1978,
    1830,
    1591,
    1673,
    1949,
    1846,
    1677,
    1657,
    1576,
    1817,
    1851,
    1894,
    1754,
    1604,
    1568,
    1730,
    1985,
    1614,
    1980,
    1554,
    1997,
    1960,
    1983,
    1848,
    1883,
    1968,
    1729,
    1716,
    628,
    1472,
    1676,
    1943,
    1821,
    1681,
    1619,
    1644,
    842,
    1492,
    1633,
    1921,
    775,
    1861,
    1584,
    1974,
    585,
    1898,
    1560,
    1708,
    1927,
    1563,
    1872,
    1876,
    1865,
    1535,
    1994,
    1756,
    1662,
    1621,
    1993,
    1825,
    1679,
    1959,
    1691,
    1875,
]

# part 1
for num1 in input:
    num2 = 2020 - num1
    if num2 in input:
        print(num1 * num2)
        break

# part 2
for num1 in input:
    for num2 in input:
        num3 = 2020 - num1 - num2
        if num3 in input and len(set([num1, num2, num3])) == 3:
            print(num1 * num2 * num3)
            sys.exit()
