On admin view (NOT a streaming one)
===================================

ApacheBench
===========

master
------

::

    Server Software:        WSGIServer/0.1
    Server Hostname:        localhost
    Server Port:            8000

    Document Path:          /admin/polls/question/
    Document Length:        9493 bytes

    Concurrency Level:      30
    Time taken for tests:   98.884 seconds
    Complete requests:      1000
    Failed requests:        0
    Total transferred:      9940000 bytes
    HTML transferred:       9493000 bytes
    Requests per second:    10.11 [#/sec] (mean)
    Time per request:       2966.510 [ms] (mean)
    Time per request:       98.884 [ms] (mean, across all concurrent requests)
    Transfer rate:          98.17 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0   16 125.4      0    1000
    Processing:   803 2933 508.3   2897    4830
    Waiting:      787 2808 494.0   2763    4710
    Total:        803 2949 526.2   2907    5089

    Percentage of the requests served within a certain time (ms)
      50%   2907
      66%   3098
      75%   3251
      80%   3359
      90%   3623
      95%   3860
      98%   4174
      99%   4426
     100%   5089 (longest request)

ticket_13910
------------

::

    Server Software:        WSGIServer/0.1
    Server Hostname:        localhost
    Server Port:            8000

    Document Path:          /admin/polls/question/
    Document Length:        9493 bytes

    Concurrency Level:      30
    Time taken for tests:   102.117 seconds
    Complete requests:      1000
    Failed requests:        0
    Total transferred:      9940000 bytes
    HTML transferred:       9493000 bytes
    Requests per second:    9.79 [#/sec] (mean)
    Time per request:       3063.522 [ms] (mean)
    Time per request:       102.117 [ms] (mean, across all concurrent requests)
    Transfer rate:          95.06 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0   16 125.3      0     998
    Processing:   898 3031 478.4   3019    4815
    Waiting:      774 2903 467.0   2883    4693
    Total:        898 3047 494.5   3035    4815

    Percentage of the requests served within a certain time (ms)
      50%   3035
      66%   3205
      75%   3334
      80%   3419
      90%   3639
      95%   3868
      98%   4134
      99%   4408
     100%   4815 (longest request)


On streaming view
=================

ApacheBench
===========

Simple template with a 10000 for and concurrency
------------------------------------------------

master::

    Server Software:        WSGIServer/0.1
    Server Hostname:        localhost
    Server Port:            8000

    Document Path:          /polls/streaming/
    Document Length:        268906 bytes

    Concurrency Level:      30
    Time taken for tests:   505.948 seconds
    Complete requests:      1000
    Failed requests:        0
    Total transferred:      269068000 bytes
    HTML transferred:       268906000 bytes
    Requests per second:    1.98 [#/sec] (mean)
    Time per request:       15178.434 [ms] (mean)
    Time per request:       505.948 [ms] (mean, across all concurrent requests)
    Transfer rate:          519.35 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0   15 121.4      0    1000
    Processing:  7069 15088 2798.8  14889   21813
    Waiting:     5272 14213 2878.8  13988   20845
    Total:       7070 15104 2801.6  14926   21873

    Percentage of the requests served within a certain time (ms)
      50%  14926
      66%  16417
      75%  17208
      80%  17652
      90%  18883
      95%  19748
      98%  20536
      99%  20945
     100%  21873 (longest request)

ticket_13910 (stream=False)::

    Server Software:        WSGIServer/0.1
    Server Hostname:        localhost
    Server Port:            8000

    Document Path:          /polls/streaming/
    Document Length:        268906 bytes

    Concurrency Level:      30
    Time taken for tests:   946.826 seconds
    Complete requests:      1000
    Failed requests:        0
    Total transferred:      269068000 bytes
    HTML transferred:       268906000 bytes
    Requests per second:    1.06 [#/sec] (mean)
    Time per request:       28404.776 [ms] (mean)
    Time per request:       946.826 [ms] (mean, across all concurrent requests)
    Transfer rate:          277.52 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0   15 121.4      0     998
    Processing: 14057 28242 4994.4  27698   42388
    Waiting:    13101 27180 5150.0  26560   40964
    Total:      14057 28257 5022.7  27698   42867

    Percentage of the requests served within a certain time (ms)
      50%  27698
      66%  29893
      75%  31657
      80%  32905
      90%  35568
      95%  37122
      98%  38552
      99%  38987
     100%  42867 (longest request)

ticket_13910 (stream=True)::

    Server Software:        WSGIServer/0.1
    Server Hostname:        localhost
    Server Port:            8000

    Document Path:          /polls/streaming/
    Document Length:        268906 bytes

    Concurrency Level:      30
    Time taken for tests:   3900.056 seconds
    Complete requests:      1000
    Failed requests:        0
    Total transferred:      269068000 bytes
    HTML transferred:       268906000 bytes
    Requests per second:    0.26 [#/sec] (mean)
    Time per request:       117001.667 [ms] (mean)
    Time per request:       3900.056 [ms] (mean, across all concurrent requests)
    Transfer rate:          67.37 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0   16 125.3      0     998
    Processing: 39745 116288 8198.0 117759  122334
    Waiting:       22   92  37.7     85     390
    Total:      39745 116304 8201.1 117830  122334

    Percentage of the requests served within a certain time (ms)
      50%  117830
      66%  119128
      75%  119738
      80%  120063
      90%  120698
      95%  121162
      98%  121501
      99%  121661
     100%  122334 (longest request)

Simple template with a 10000 for and no concurrency
---------------------------------------------------

master::

    Server Software:        WSGIServer/0.1
    Server Hostname:        localhost
    Server Port:            8000

    Document Path:          /polls/streaming/
    Document Length:        268906 bytes

    Concurrency Level:      1
    Time taken for tests:   33.119 seconds
    Complete requests:      100
    Failed requests:        0
    Total transferred:      26906800 bytes
    HTML transferred:       26890600 bytes
    Requests per second:    3.02 [#/sec] (mean)
    Time per request:       331.191 [ms] (mean)
    Time per request:       331.191 [ms] (mean, across all concurrent requests)
    Transfer rate:          793.38 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    0   0.0      0       0
    Processing:   245  331  55.2    330     519
    Waiting:      244  330  55.0    329     517
    Total:        245  331  55.2    330     519

    Percentage of the requests served within a certain time (ms)
      50%    330
      66%    347
      75%    359
      80%    366
      90%    400
      95%    441
      98%    495
      99%    519
     100%    519 (longest request)

ticket_13910 (stream=False)::

    Server Software:        WSGIServer/0.1
    Server Hostname:        localhost
    Server Port:            8000

    Document Path:          /polls/streaming/
    Document Length:        268906 bytes

    Concurrency Level:      1
    Time taken for tests:   63.374 seconds
    Complete requests:      100
    Failed requests:        0
    Total transferred:      26906800 bytes
    HTML transferred:       26890600 bytes
    Requests per second:    1.58 [#/sec] (mean)
    Time per request:       633.742 [ms] (mean)
    Time per request:       633.742 [ms] (mean, across all concurrent requests)
    Transfer rate:          414.62 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    0   0.0      0       0
    Processing:   459  634  76.3    626     855
    Waiting:      458  632  76.1    625     854
    Total:        459  634  76.3    626     856

    Percentage of the requests served within a certain time (ms)
      50%    626
      66%    643
      75%    675
      80%    692
      90%    755
      95%    789
      98%    826
      99%    856
     100%    856 (longest request)

ticket_13910 (stream=True)::

    Server Software:        WSGIServer/0.1
    Server Hostname:        localhost
    Server Port:            8000

    Document Path:          /polls/streaming/
    Document Length:        268906 bytes

    Concurrency Level:      1
    Time taken for tests:   215.383 seconds
    Complete requests:      100
    Failed requests:        0
    Total transferred:      26906800 bytes
    HTML transferred:       26890600 bytes
    Requests per second:    0.46 [#/sec] (mean)
    Time per request:       2153.832 [ms] (mean)
    Time per request:       2153.832 [ms] (mean, across all concurrent requests)
    Transfer rate:          122.00 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    0   0.0      0       0
    Processing:  1722 2154 231.6   2247    2804
    Waiting:        2    3   1.6      2      14
    Total:       1722 2154 231.6   2247    2804

    Percentage of the requests served within a certain time (ms)
      50%   2247
      66%   2276
      75%   2298
      80%   2312
      90%   2360
      95%   2389
      98%   2466
      99%   2804
     100%   2804 (longest request)

