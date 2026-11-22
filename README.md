# Software testing fundamentals

Coursework for the course "Fundamentals of Software Testing". Two independent projects:

| Project | What it is |
|---------|------------|
| Dynamic library testing | Black-box testing of `quadratic.dll` |
| Web performance testing | Comparison of three websites with three tools |

## 1. Dynamic library testing

Black-box testing of `quadratic.dll`, a Windows library that solves quadratic
equations `a*x^2 + b*x + c = 0`. The library was tested only through its public
interface (`setA`, `setB`, `setC`, `getSolution`) using a Python script and
`ctypes`.

- Methods: equivalence partitioning, boundary value testing, repeat tests
- 11 test cases (TC01-TC11), 6 reported bugs (TC12-TC17)
- Environment: Windows 11, Python 3.13, `quadratic.dll` next to the script

## 2. Web performance testing

Three websites were measured with three tools:

- Websites: coursera.org, taltech.ee, european-union.europa.eu
- Tools: Pingdom (EU, North America, South America, Asia),
  WebPageTest (mobile 4G / desktop, several browsers and locations),
  Google PageSpeed Insights (mobile / desktop)
- Metrics: performance grade, load time, requests, FCP, TTFB, CLS, INP, LCP,
  Speed Index, TBT

The workbook `web-performance-testing.xlsx` has three sheets: `Pingdom`,
`WebPagetest - Google PageSpeed` and `Summary`.
