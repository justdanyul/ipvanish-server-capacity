# ipvanish-server-capacity

ipvanish-server-capacity is a small little console application that queries the IPVanish server estate and reports on the current capacity across of the indivual servers. For example, running the command

```
ipvcap -c Denmark
```
will yield something similar to this
```
Server cph-c09.ipvanish.com in Copenhagen,Denmark is at 8%
Server cph-c12.ipvanish.com in Copenhagen,Denmark is at 8%
Server cph-c19.ipvanish.com in Copenhagen,Denmark is at 9%
Server cph-c15.ipvanish.com in Copenhagen,Denmark is at 10%
Server cph-c16.ipvanish.com in Copenhagen,Denmark is at 10%
Server cph-b01.ipvanish.com in Copenhagen,Denmark is at 11%
Server cph-c18.ipvanish.com in Copenhagen,Denmark is at 12%
Server cph-c07.ipvanish.com in Copenhagen,Denmark is at 13%
Server cph-c10.ipvanish.com in Copenhagen,Denmark is at 13%
Server cph-c17.ipvanish.com in Copenhagen,Denmark is at 13%
Server cph-c04.ipvanish.com in Copenhagen,Denmark is at 14%
Server cph-c20.ipvanish.com in Copenhagen,Denmark is at 14%
Server cph-c11.ipvanish.com in Copenhagen,Denmark is at 16%
Server cph-c13.ipvanish.com in Copenhagen,Denmark is at 17%
Server cph-c05.ipvanish.com in Copenhagen,Denmark is at 18%
Server cph-c08.ipvanish.com in Copenhagen,Denmark is at 20%
Server cph-c14.ipvanish.com in Copenhagen,Denmark is at 27%
Server cph-c03.ipvanish.com in Copenhagen,Denmark is at 30%
Server cph-c06.ipvanish.com in Copenhagen,Denmark is at 31%
```

### Installation
Just clone the repo
```
git clone https://github.com/justdanyul/ipvanish-server-capacity.git
```
run the setup.py as follows
```
sudo python3 setup.py setup
```
and you are done.

### Usage
Show help
```
ipvcap -h
```
Display capacity across all servers
```
ipvcap
```
Filter servers based on country
```
ipvcap -c COUNTRY
```
notice, if you are filtering based on country, remember quotes for country names containing spaces. For example
```
ipvcap -c "United Kingdom"
```
