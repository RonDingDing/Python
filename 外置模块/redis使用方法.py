What is redis?

Redis is an open source (BSD licensed), in-memory data structure store, used as database, cache and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs and geospatial indexes with radius queries. Redis has built-in replication, Lua scripting, LRU eviction, transactions and different levels of on-disk persistence, and provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster.

Redis������http://redis.io/

����ժ�Թ�������
��װRedis

��װ

ģ��GitHub��ַ��https://github.com/WoLpH/redis-py

Shell

[root@anshengme ~]# yum -y install redis
1
[root@anshengme ~]# yum -y install redis
���ð󶨵�IP

Shell

[root@anshengme ~]# vim /etc/redis.conf 
bind 0.0.0.0
1
2
[root@anshengme ~]# vim /etc/redis.conf 
bind 0.0.0.0
���������ÿ���������

Shell

[root@anshengme ~]# systemctl start redis
[root@anshengme ~]# systemctl enable redis
Created symlink from /etc/systemd/system/multi-user.target.wants/redis.service to /usr/lib/systemd/system/redis.service.
1
2
3
[root@anshengme ~]# systemctl start redis
[root@anshengme ~]# systemctl enable redis
Created symlink from /etc/systemd/system/multi-user.target.wants/redis.service to /usr/lib/systemd/system/redis.service.
���

�鿴�˿�

Shell

[root@anshengme ~]# netstat -tlnp | grep "redis"
tcp        0      0 0.0.0.0:6379            0.0.0.0:*               LISTEN      1439/redis-server 0
1
2
[root@anshengme ~]# netstat -tlnp | grep "redis"
tcp        0      0 0.0.0.0:6379            0.0.0.0:*               LISTEN      1439/redis-server 0
����д�����

Shell

[root@anshengme ~]# /usr/bin/redis-cli 
127.0.0.1:6379> set url https://blog.ansheng.me
OK
127.0.0.1:6379> get url
"https://blog.ansheng.me"
127.0.0.1:6379> exit
1
2
3
4
5
6
[root@anshengme ~]# /usr/bin/redis-cli 
127.0.0.1:6379> set url https://blog.ansheng.me
OK
127.0.0.1:6379> get url
"https://blog.ansheng.me"
127.0.0.1:6379> exit
��װredis-py

��װredis-py

Shell

pip3 install redis
1
pip3 install redis
��Դ�밲װ

Shell

python setup.py install
1
python setup.py install
��鰲װ�Ƿ�ɹ�

Python

# ����ģ��û������װ�ɹ�
>>> import redis
1
2
# ����ģ��û������װ�ɹ�
>>> import redis
���ż�ʹ��

Python

# ����ģ��
>>> import redis
# ���ӵ�Redis������
>>> conn = redis.Redis(host='192.168.56.100', port=6379)
# д��һ������
>>> conn.set('name','ansheng')
True
# ��ȡһ������
>>> conn.get('name')
b'ansheng'
>>> conn.get('url')
b'https://blog.ansheng.me'
1
2
3
4
5
6
7
8
9
10
11
12
# ����ģ��
>>> import redis
# ���ӵ�Redis������
>>> conn = redis.Redis(host='192.168.56.100', port=6379)
# д��һ������
>>> conn.set('name','ansheng')
True
# ��ȡһ������
>>> conn.get('name')
b'ansheng'
>>> conn.get('url')
b'https://blog.ansheng.me'
ʹ�����ӳ����ӵ�Redis

Behind the scenes, redis-py uses a connection pool to manage connections to a Redis server. By default, each Redis instance you create will in turn create its own connection pool. You can override this behavior and use an existing connection pool by passing an already created connection pool instance to the connection_pool argument of the Redis class. You may choose to do this in order to implement client side sharding or have finer grain control of how connections are managed.
Python

>>> pool = redis.ConnectionPool(host='192.168.56.100', port=6379)
>>> conn = redis.Redis(connection_pool=pool)
>>> conn.set('hello','world')
True
>>> conn.get('hello')
b'world'
1
2
3
4
5
6
>>> pool = redis.ConnectionPool(host='192.168.56.100', port=6379)
>>> conn = redis.Redis(connection_pool=pool)
>>> conn.set('hello','world')
True
>>> conn.get('hello')
b'world'
ʹ���׽�������

Python

>>> r = redis.Redis(unix_socket_path='/tmp/redis.sock')
1
>>> r = redis.Redis(unix_socket_path='/tmp/redis.sock')
API

redis-py�ṩ��API��������redis

String API

set(name, value, ex=None, px=None, nx=False, xx=False)

����	����
ex	����ʱ�䣨�룩
px	����ʱ�䣨���룩
nx	�������ΪTrue����ֻ��name������ʱ����ǰset������ִ��
xx	�������ΪTrue����ֻ��name����ʱ����ǰset������ִ��
Python

>>> conn.set('k1', 'v1', ex=10, nx=True)
True
>>> conn.get('k1')
b'v1'
>>> conn.get('k1')
1
2
3
4
5
>>> conn.set('k1', 'v1', ex=10, nx=True)
True
>>> conn.get('k1')
b'v1'
>>> conn.get('k1')
setex(name, value, time)

���ù���ʱ��/��

Python

>>> conn.setex('k','v',1)
True
>>> conn.get('k')
1
2
3
>>> conn.setex('k','v',1)
True
>>> conn.get('k')
psetex(name, time_ms, value)

���ù���ʱ��/����

Python

>>> conn.psetex('k',10,'v')
True
>>> conn.get('k')
1
2
3
>>> conn.psetex('k',10,'v')
True
>>> conn.get('k')
setnx(name, value)

����ֵ��ֻ��key������ʱ��ִ�����ò���

Python

>>> conn.get('k1')
>>> conn.setnx('k1','v1')
True
>>> conn.get('k1')
b'v1'
>>> conn.setnx('k2','v2')
False
1
2
3
4
5
6
7
>>> conn.get('k1')
>>> conn.setnx('k1','v1')
True
>>> conn.get('k1')
b'v1'
>>> conn.setnx('k2','v2')
False
mset(*args, **kwargs)

ͬʱ���ö��key/value

Python

>>> conn.mset(k1='v1', k2='v2')
True
>>> conn.mset({'k1':'v1', 'k1':'v1'})
True
1
2
3
4
>>> conn.mset(k1='v1', k2='v2')
True
>>> conn.mset({'k1':'v1', 'k1':'v1'})
True
get(name)

��ȡ����ֵ

Python

>>> conn.get('k1')
b'v1'
1
2
>>> conn.get('k1')
b'v1'
mget(keys, *args)

��ȡ���ֵ

Python

>>> conn.mget('k1','k2')
[b'v1', b'v2']
# �����б�
>>> conn.mget(['name','url'])
[b'ansheng', b'https://blog.ansheng.me']
1
2
3
4
5
>>> conn.mget('k1','k2')
[b'v1', b'v2']
# �����б�
>>> conn.mget(['name','url'])
[b'ansheng', b'https://blog.ansheng.me']
getset(name, value)

������ֵ����ȡԭ����ֵ

Python

>>> conn.set('hello', 'world')
True
>>> result = conn.getset('hello', 'Linux')
>>> result
b'world'
>>> conn.get('hello')
b'Linux'
1
2
3
4
5
6
7
>>> conn.set('hello', 'world')
True
>>> result = conn.getset('hello', 'Linux')
>>> result
b'world'
>>> conn.get('hello')
b'Linux'
getrange(key, start, end)

ͨ�������ķ�ʽ����ȡvalue��ֵ

Python

>>> conn.set('key','value')
True
>>> conn.getrange('key', 1, 4)
b'alue'
1
2
3
4
>>> conn.set('key','value')
True
>>> conn.getrange('key', 1, 4)
b'alue'
setrange(name, offset, value)

���������޸�value

Python

>>> conn.set('n','123456789')
True
>>> conn.setrange('n', 0, 'a')
9
>>> conn.get('n')
b'a23456789'
1
2
3
4
5
6
>>> conn.set('n','123456789')
True
>>> conn.setrange('n', 0, 'a')
9
>>> conn.get('n')
b'a23456789'
setbit(name, offset, value)

getbit(name, offset)

��ȡvalue��Ӧĳһ������λ�ö�Ӧ��ֵ0/1

Python

>>> conn.getbit('k',1)
1
1
2
>>> conn.getbit('k',1)
1
bitcount(key, start=None, end=None)

��ȡkey��Ӧ�������б�ʾ1�ĸ���

bitop(operation, dest, *keys)

�����ֵ����ֵ���㣬�ó��Ľ�����浽һ����ֵ����

Python

>>> conn.mset(n1='abc',n2='cde',n3='adc')
True
>>> conn.bitop('AND','now_key','n1','n2','n3')
3
>>> conn.get('now_key')
b'a`a'
>>> conn.mget('n1','n2','n3')
[b'abc', b'cde', b'adc']
1
2
3
4
5
6
7
8
>>> conn.mset(n1='abc',n2='cde',n3='adc')
True
>>> conn.bitop('AND','now_key','n1','n2','n3')
3
>>> conn.get('now_key')
b'a`a'
>>> conn.mget('n1','n2','n3')
[b'abc', b'cde', b'adc']
operation֧��AND(��)��OR(��)��NOT(��)��XOR(���)
strlen(name)

��ȡvalue�ĳ���

Python

>>> conn.set('name','����')
True
>>> conn.strlen('name')
6
1
2
3
4
>>> conn.set('name','����')
True
>>> conn.strlen('name')
6
incr(name, amount=1)

��name��value�������������name�������򴴽�����������

Python

>>> conn.get('number')
>>> conn.incr('number')
1
>>> conn.get('number')
b'1'
>>> conn.incr('number')
2
>>> conn.incr('number', 10)
12
1
2
3
4
5
6
7
8
9
>>> conn.get('number')
>>> conn.incr('number')
1
>>> conn.get('number')
b'1'
>>> conn.incr('number')
2
>>> conn.incr('number', 10)
12
incrbyfloat(name, amount=1.0)

ͬ�ϣ�֧�ָ���������

Python

>>> conn.incrbyfloat('number', 1.5)
13.5
>>> conn.incrbyfloat('number', 1.1)
14.6
1
2
3
4
>>> conn.incrbyfloat('number', 1.5)
13.5
>>> conn.incrbyfloat('number', 1.1)
14.6
decr(name, amount=1)

�Լ���ͬ����һ������������Լ���value���������ͱ���

Python

>>> conn.set('n', 10)
True
>>> conn.decr('n')
9
>>> conn.decr('n', 9)
0
1
2
3
4
5
6
>>> conn.set('n', 10)
True
>>> conn.decr('n')
9
>>> conn.decr('n', 9)
0
append(key, value)

��value����׷������

Python

>>> conn.set('blog','https://blog.ansheng.me')
True
>>> conn.append('blog','/')
26
>>> conn.get('blog')
b'https://blog.ansheng.me/'
1
2
3
4
5
6
>>> conn.set('blog','https://blog.ansheng.me')
True
>>> conn.append('blog','/')
26
>>> conn.get('blog')
b'https://blog.ansheng.me/'
Hash API

hset(name, key, value)

����name�ļ�ֵ�ԣ������޸ģ�û���򴴽�

Python

>>> conn.hset('dic','k1','v1')
1
>>> conn.hget('dic','k1')
b'v1'
1
2
3
4
>>> conn.hset('dic','k1','v1')
1
>>> conn.hget('dic','k1')
b'v1'
hmset(name, mapping)

ͬʱ���ö��name��key/value

Python

>>> conn.hmset('dic', {'k1': 'v1', 'k2': 'v2'})
True
>>> conn.hget('dic','k2')
b'v2'
1
2
3
4
>>> conn.hmset('dic', {'k1': 'v1', 'k2': 'v2'})
True
>>> conn.hget('dic','k2')
b'v2'
hget(name, key)

��ȡname��key��ֵ

Python

>>> conn.hget('dic','k2')
b'v2'
1
2
>>> conn.hget('dic','k2')
b'v2'
hmget(name, keys, *args)

ͬʱ��ȡ���

Python

>>> conn.hmget('dic',['k1', 'k2'])
[b'v1', b'v2']
>>> conn.hmget('dic','k1', 'k2')
[b'v1', b'v2']
1
2
3
4
>>> conn.hmget('dic',['k1', 'k2'])
[b'v1', b'v2']
>>> conn.hmget('dic','k1', 'k2')
[b'v1', b'v2']
hgetall(name)

��ȡname��Ӧ������key/value

Python

>>> conn.hgetall('dic')
{b'k1': b'v1', b'k2': b'v2'}
1
2
>>> conn.hgetall('dic')
{b'k1': b'v1', b'k2': b'v2'}
hlen(name)

��ȡname��Ӧ��ֵ�Եĸ���

Python

>>> conn.hlen('dic')
2
1
2
>>> conn.hlen('dic')
2
hkeys(name)

��ȡname�����е�key

Python

>>> conn.hkeys('dic')
[b'k1', b'k2']
1
2
>>> conn.hkeys('dic')
[b'k1', b'k2']
hvals(name)

��ȡname�����е�value

Python

>>> conn.hvals('dic')
[b'v1', b'v2']
1
2
>>> conn.hvals('dic')
[b'v1', b'v2']
hexists(name, key)

��鵱ǰname���Ƿ��д����key

Python

>>> conn.hexists('dic','k1')
True
>>> conn.hexists('dic','kk')
False
1
2
3
4
>>> conn.hexists('dic','k1')
True
>>> conn.hexists('dic','kk')
False
hdel(self, name, *keys)

ɾ��name�ж�Ӧ��key

Python

>>> conn.hdel('dic','k1')
1
>>> conn.hget('dic','k1')
1
2
3
>>> conn.hdel('dic','k1')
1
>>> conn.hget('dic','k1')
hincrby(name, key, amount=1)

name��key��Ӧ��value��������������������򴴽�

Python

>>> conn.hincrby('dic','number')
1
>>> conn.hincrby('dic','number',10)
11
1
2
3
4
>>> conn.hincrby('dic','number')
1
>>> conn.hincrby('dic','number',10)
11
hincrbyfloat(name, key, amount=1.0)

value������֧�ָ�������ͬ��

Python

>>> conn.hincrbyfloat('dic','float')
1.0
>>> conn.hincrbyfloat('dic','float',0.3)
1.3
1
2
3
4
>>> conn.hincrbyfloat('dic','float')
1.0
>>> conn.hincrbyfloat('dic','float',0.3)
1.3
hscan(name, cursor=0, match=None, count=None)

����ʽ������ȡ��hscan����ʵ�ַ�Ƭ�Ļ�ȡ���ݣ�����һ���Խ�����ȫ����ȡ�꣬�Ӷ������ڴ汻�ű�

����	����
name	redis��name
cursor	�α꣨�����α����ȡ��ȡ���ݣ�
match	ƥ��ָ��key��Ĭ��None ��ʾ���е�key
count	ÿ�η�Ƭ���ٻ�ȡ������Ĭ��None��ʾ����Redis��Ĭ�Ϸ�Ƭ����
hscan_iter(name, match=None, count=None)

����yield��װhscan������������ʵ�ַ���ȥredis�л�ȡ����

����	����
match	ƥ��ָ��key��Ĭ��None ��ʾ���е�key
count	ÿ�η�Ƭ���ٻ�ȡ������Ĭ��None��ʾ����Redis��Ĭ�Ϸ�Ƭ����
�磺

Python

for item in r.hscan_iter('xx'):
    print item
1
2
for item in r.hscan_iter('xx'):
    print item
expire(name, time)

���ù���ʱ��

Python

>>> conn.hset('info','BlogUrl','https://blog.ansheng.me')
1
>>> conn.expire('info', 10)
True
>>> conn.hget('info','BlogUrl')
b'https://blog.ansheng.me'
>>> conn.hget('info','BlogUrl')
1
2
3
4
5
6
7
>>> conn.hset('info','BlogUrl','https://blog.ansheng.me')
1
>>> conn.expire('info', 10)
True
>>> conn.hget('info','BlogUrl')
b'https://blog.ansheng.me'
>>> conn.hget('info','BlogUrl')
ListAPI

lpush(name, *values)

����������ֵ

Python

>>> conn.lpush('li', 11,22,33)
3
>>> conn.lindex('li', 0)
b'33'
1
2
3
4
>>> conn.lpush('li', 11,22,33)
3
>>> conn.lindex('li', 0)
b'33'
rpush(name, *values)

�����ұ����ֵ

Python

>>> conn.rpush('lli', 11,22,33)
3
>>> conn.lindex('lli', 0)
b'11'
1
2
3
4
>>> conn.rpush('lli', 11,22,33)
3
>>> conn.lindex('lli', 0)
b'11'
lpushx(name, value)

ֻ��name�Ѿ�����ʱ��ֵ��ӵ��б�������

Python

>>> conn.lpushx('li', 'aa')
4
>>> conn.lindex('li', 0)
b'aa'
1
2
3
4
>>> conn.lpushx('li', 'aa')
4
>>> conn.lindex('li', 0)
b'aa'
rpushx(name, value)

ֻ��name�Ѿ�����ʱ��ֵ��ӵ��б�����ұ�

Python

>>> conn.rpushx('li', 'bb')
5
>>> conn.lindex('li', 0)
b'aa'
>>> conn.lindex('li', 4)
b'bb'
1
2
3
4
5
6
>>> conn.rpushx('li', 'bb')
5
>>> conn.lindex('li', 0)
b'aa'
>>> conn.lindex('li', 4)
b'bb'
llen(name)

��ȡnameԪ�صĸ���

Python

>>> conn.llen('li')
5
1
2
>>> conn.llen('li')
5
linsert(name, where, refvalue, value)

��name��ĳһ��ֵǰ����ߺ������һ����ֵ

Python

>>> conn.linsert('li','AFTER','11','cc')
6
>>> conn.lindex('li', 3)
b'11'
>>> conn.lindex('li', 4)
b'cc'
1
2
3
4
5
6
>>> conn.linsert('li','AFTER','11','cc')
6
>>> conn.lindex('li', 3)
b'11'
>>> conn.lindex('li', 4)
b'cc'
lset(name, index, value)

��name��index����λ�õ�ֵ�������¸�ֵ

Python

>>> conn.lindex('li', 4)
b'cc'
>>> conn.lset('li', 4, 'hello')
True
>>> conn.lindex('li', 4)
b'hello'
1
2
3
4
5
6
>>> conn.lindex('li', 4)
b'cc'
>>> conn.lset('li', 4, 'hello')
True
>>> conn.lindex('li', 4)
b'hello'
lrem(name, value, num=0)

ɾ��ָ��value�������ǰ���ֵ

num=2,��ǰ����ɾ��2����
num=-2,�Ӻ���ǰ��ɾ��2��
Python

>>> conn.llen('li')
6
>>> conn.lrem('li', 'hello')
1
>>> conn.llen('li')
5
>>> conn.lrem('li', '22', num=2)
2
>>> conn.llen('li')
3
1
2
3
4
5
6
7
8
9
10
>>> conn.llen('li')
6
>>> conn.lrem('li', 'hello')
1
>>> conn.llen('li')
5
>>> conn.lrem('li', '22', num=2)
2
>>> conn.llen('li')
3
lpop(name)

ɾ��name������һ��Ԫ��

Python

>>> conn.lindex('li', 0)
b'11'
>>> conn.lpop('li')
b'11'
1
2
3
4
>>> conn.lindex('li', 0)
b'11'
>>> conn.lpop('li')
b'11'
rpop(name)

ɾ��name���Ҳ��һ��Ԫ��

Python

>>> conn.rpop('li')
b'33'
1
2
>>> conn.rpop('li')
b'33'
lindex(name, index)

��ȡname�ж�Ӧ������ֵ

Python

>>> conn.lindex('li', 0)
b'aa'
1
2
>>> conn.lindex('li', 0)
b'aa'
lrange(name, start, end)

ʹ����Ƭ��ȡ����

Python

>>> conn.llen('li')
8
>>> conn.lrange('li',0,5)
[b'3', b'23', b'34', b'235', b'2', b'1']
1
2
3
4
>>> conn.llen('li')
8
>>> conn.lrange('li',0,5)
[b'3', b'23', b'34', b'235', b'2', b'1']
ltrim(name, start, end)

��name��Ӧ���б����Ƴ�û����start-end����֮���ֵ

Python

>>> conn.ltrim('li',0,5)
True
>>> conn.llen('li')
6
1
2
3
4
>>> conn.ltrim('li',0,5)
True
>>> conn.llen('li')
6
rpoplpush(src, dst)

��src�б���ȡ�����ұߵ�Ԫ�أ�ͬʱ���������dst�б�������

Python

>>> conn.lpush('li1', 1,2,3)
3
>>> conn.lpush('li2', 'a','b','c')
3
>>> conn.rpoplpush('li1','li2')
b'1'
1
2
3
4
5
6
>>> conn.lpush('li1', 1,2,3)
3
>>> conn.lpush('li2', 'a','b','c')
3
>>> conn.rpoplpush('li1','li2')
b'1'
blpop(keys, timeout=0)
brpop(keys, timeout=0)

brpoplpush(src, dst, timeout=0)

��src�б���Ҳ��Ƴ�һ��Ԫ�ز�������ӵ�dst�б�����

Python

>>> conn.lpush('ll', 'a','b','c')
3
>>> conn.lpush('aa', 'a','b','c')
3
>>> conn.brpoplpush('ll','aa')
b'a'
1
2
3
4
5
6
>>> conn.lpush('ll', 'a','b','c')
3
>>> conn.lpush('aa', 'a','b','c')
3
>>> conn.brpoplpush('ll','aa')
b'a'
timeout����src��Ӧ���б���û������ʱ�������ȴ��������ݵĳ�ʱʱ�䣨�룩��0 ��ʾ��Զ����
�Զ�����������

����redis�����û���ṩ���б�Ԫ�ص����������������Ҫѭ��name��Ӧ���б������Ԫ�أ���ô����Ҫ��

��ȡname��Ӧ�������б�
ѭ���б�
���ǣ�����б�ǳ�����ô���п����ڵ�һ��ʱ�ͽ���������ݳű��������б�Ҫ�Զ���һ�����������Ĺ��ܣ�

Python

def list_iter(name):
    """
    �Զ���redis�б���������
    :param name: redis�е�name����������name��Ӧ���б�
    :return: yield ���� �б�Ԫ��
    """
    list_count = r.llen(name)
    for index in xrange(list_count):
        yield r.lindex(name, index)
1
2
3
4
5
6
7
8
9
def list_iter(name):
    """
    �Զ���redis�б���������
    :param name: redis�е�name����������name��Ӧ���б�
    :return: yield ���� �б�Ԫ��
    """
    list_count = r.llen(name)
    for index in xrange(list_count):
        yield r.lindex(name, index)
ʹ��

Python

for item in list_iter('pp'):
    print item
1
2
for item in list_iter('pp'):
    print item
SET API

sadd(name, *values)

Ϊname���ֵ��������������

Python

>>> conn.sadd('s1', 1)
1
>>> conn.sadd('s1', 1)
0
1
2
3
4
>>> conn.sadd('s1', 1)
1
>>> conn.sadd('s1', 1)
0
scard(name)

����name��Ԫ������

Python

>>> conn.scard('s1')
1
1
2
>>> conn.scard('s1')
1
sdiff(keys, *args)

��keys�����в������������е�����

Python

>>> conn.sdiff('s1','s2')
{b'c', b'v', b'a'}
1
2
>>> conn.sdiff('s1','s2')
{b'c', b'v', b'a'}
sdiffstore(dest, keys, *args)

��keys�����в������������е����ݱ��浽dest������

Python

>>> conn.sdiffstore('news','s1','s2')
3
>>> conn.scard('news')
3
1
2
3
4
>>> conn.sdiffstore('news','s1','s2')
3
>>> conn.scard('news')
3
sinter(keys, *args)

��ȡkeys�����������������еĲ���

Python

>>> conn.sinter('s1','s2')
{b'2', b'3', b'1'}
1
2
>>> conn.sinter('s1','s2')
{b'2', b'3', b'1'}
sinterstore(dest, keys, *args)

��ȡkeys�����������������еĲ������ݲ����浽dest������

Python

>>> conn.sinterstore('news1','s1','s2')
3
1
2
>>> conn.sinterstore('news1','s1','s2')
3
sismember(name, value)

��ȡvalue�Ƿ���name�����еĳ�Ա

Python

>>> conn.sismember('news1','1')
True
>>> conn.sismember('news1','aa1')
False
1
2
3
4
>>> conn.sismember('news1','1')
True
>>> conn.sismember('news1','aa1')
False
smembers(name)

��ȡname���������еĳ�Ա

Python

>>> conn.smembers('news1')
{b'2', b'3', b'1'}
1
2
>>> conn.smembers('news1')
{b'2', b'3', b'1'}
smove(src, dst, value)

��src�е�value�ƶ���dst��

Python

>>> conn.smembers('s1')
{b'c', b'2', b'v', b'1', b'3', b'a'}
>>> conn.smembers('s2')
{b'2', b'3', b'1'}
>>> conn.smove('s1','s2','v')
True
>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.smembers('s2')
{b'2', b'v', b'3', b'1'}
1
2
3
4
5
6
7
8
9
10
>>> conn.smembers('s1')
{b'c', b'2', b'v', b'1', b'3', b'a'}
>>> conn.smembers('s2')
{b'2', b'3', b'1'}
>>> conn.smove('s1','s2','v')
True
>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.smembers('s2')
{b'2', b'v', b'3', b'1'}
spop(name)

ɾ��������name�е������Ա

Python

>>> conn.smembers('s2')
{b'2', b'v', b'3', b'1'}
>>> conn.spop('s2')
b'3'
>>> conn.smembers('s2')
{b'2', b'v', b'1'}
>>> conn.spop('s2')
b'2'
>>> conn.smembers('s2')
{b'v', b'1'}
>>> conn.spop('s2')
b'1'
>>> conn.smembers('s2')
{b'v'}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
>>> conn.smembers('s2')
{b'2', b'v', b'3', b'1'}
>>> conn.spop('s2')
b'3'
>>> conn.smembers('s2')
{b'2', b'v', b'1'}
>>> conn.spop('s2')
b'2'
>>> conn.smembers('s2')
{b'v', b'1'}
>>> conn.spop('s2')
b'1'
>>> conn.smembers('s2')
{b'v'}
srandmember(name, number=None)

�����ȡname�����е�number����Ա��Ĭ��number=1

Python

>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.srandmember('s1')
b'1'
>>> conn.srandmember('s1')
b'a'
>>> conn.srandmember('s1',number=2)
[b'3', b'a']
>>> conn.srandmember('s1',number=2)
[b'1', b'2']
1
2
3
4
5
6
7
8
9
10
>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.srandmember('s1')
b'1'
>>> conn.srandmember('s1')
b'a'
>>> conn.srandmember('s1',number=2)
[b'3', b'a']
>>> conn.srandmember('s1',number=2)
[b'1', b'2']
srem(name, *values)

ɾ��name�����е�values����

Python

>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.srem('s1','1','2')
2
>>> conn.smembers('s1')
{b'c', b'a', b'3'}
1
2
3
4
5
6
>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.srem('s1','1','2')
2
>>> conn.smembers('s1')
{b'c', b'a', b'3'}
sunion(keys, *args)

��ȡkeys�������������ϵĲ���

Python

>>> conn.sadd('a1',1,2,3)
3
>>> conn.sadd('a2',1,2,3,4,5,6,7)
7
>>> conn.sunion('a2','a1')
{b'2', b'7', b'1', b'3', b'6', b'5', b'4'}
1
2
3
4
5
6
>>> conn.sadd('a1',1,2,3)
3
>>> conn.sadd('a2',1,2,3,4,5,6,7)
7
>>> conn.sunion('a2','a1')
{b'2', b'7', b'1', b'3', b'6', b'5', b'4'}
sunionstore(dest, keys, *args)

��ȡkeys�������������ϵĲ��������浽dest��

Python

>>> conn.sunionstore('a3', 'a2','a1')
7
>>> conn.smembers('a3')
{b'2', b'7', b'1', b'3', b'6', b'5', b'4'}
1
2
3
4
>>> conn.sunionstore('a3', 'a2','a1')
7
>>> conn.smembers('a3')
{b'2', b'7', b'1', b'3', b'6', b'5', b'4'}
Ordered set API

zadd(name, *args, **kwargs)

Python

>>> conn.zadd('h1','n1',11,'n2',22)
2
>>> conn.zadd('h2',n1=11,n2=22)
2
1
2
3
4
>>> conn.zadd('h1','n1',11,'n2',22)
2
>>> conn.zadd('h2',n1=11,n2=22)
2
zcard(name)

�������򼯺�nameԪ�ص�����

Python

>>> conn.zcard('h1')
2
1
2
>>> conn.zcard('h1')
2
zcount(name, min, max)

������name��ֵ��min��max֮���ֵ����

Python

>>> conn.zcount('h1',10,30)
2
1
2
>>> conn.zcount('h1',10,30)
2
zincrby(name, value, amount=1)

name����value��ֵ����amount

Python

>>> conn.zincrby('h1','n1',10)
21.0
1
2
>>> conn.zincrby('h1','n1',10)
21.0
zinterstore(dest, keys, aggregate=None)
zlexcount(name, min, max)

zrange(name, start, end, desc=False, withscores=False, score_cast_func=float)

����	����
name	redis��name
start	���򼯺�������ʼλ�ã��Ƿ�����
end	���򼯺���������λ�ã��Ƿ�����
desc	�������Ĭ�ϰ��շ�����С��������
withscores	�Ƿ��ȡԪ�صķ�����Ĭ��ֻ��ȡԪ�ص�ֵ
score_cast_func	�Է�����������ת���ĺ���
Python

>>> conn.zrange('h1', 1, 2, desc=True, withscores=True, score_cast_func=float)
[(b'n1', 21.0)]
>>> conn.zrange('h1', 1, 2, desc=False, withscores=True, score_cast_func=float)
[(b'n2', 22.0)]
1
2
3
4
>>> conn.zrange('h1', 1, 2, desc=True, withscores=True, score_cast_func=float)
[(b'n1', 21.0)]
>>> conn.zrange('h1', 1, 2, desc=False, withscores=True, score_cast_func=float)
[(b'n2', 22.0)]
Python

# �Ӵ�С����
zrevrange(name, start, end, withscores=False, score_cast_func=float) 
# ���շ�����Χ��ȡname��Ӧ�����򼯺ϵ�Ԫ��
zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)
# �Ӵ�С����
zrevrangebyscore(name, max, min, start=None, num=None, withscores=False, score_cast_func=float)
1
2
3
4
5
6
# �Ӵ�С����
zrevrange(name, start, end, withscores=False, score_cast_func=float) 
# ���շ�����Χ��ȡname��Ӧ�����򼯺ϵ�Ԫ��
zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)
# �Ӵ�С����
zrevrangebyscore(name, max, min, start=None, num=None, withscores=False, score_cast_func=float)
zrangebylex(name, min, max, start=None, num=None)

�����򼯺ϵ����г�Ա��������ͬ�ķ�ֵʱ�����򼯺ϵ�Ԫ�ػ���ݳ�Ա�� ֵ ��lexicographical ordering�����������򣬶������������Է��ظ��������򼯺ϼ� key �У� Ԫ�ص�ֵ���� min �� max ֮��ĳ�Ա

�Լ����е�ÿ����Ա��������ֽڵĶԱȣ�byte-by-byte compare���� �����մӵ͵��ߵ�˳�� ���������ļ��ϳ�Ա�� ��������ַ�����һ������������ͬ�Ļ��� ��ô�������Ϊ�ϳ����ַ����Ƚ϶̵��ַ���Ҫ��

����	����
name	redis��name
min	������(ֵ) + ��ʾ�����ޣ� �C ��ʾ�����ޣ� ( ��ʾ�����䣻 [ ���ʾ������
min	�����䣨ֵ��
start	�Խ�����з�Ƭ��������λ��
num	�Խ�����з�Ƭ�������������num��Ԫ��
�磺

Python

ZADD myzset 0 aa 0 ba 0 ca 0 da 0 ea 0 fa 0 ga
# r.zrangebylex('myzset', "-", "[ca") ���Ϊ��['aa', 'ba', 'ca']
1
2
ZADD myzset 0 aa 0 ba 0 ca 0 da 0 ea 0 fa 0 ga
# r.zrangebylex('myzset', "-", "[ca") ���Ϊ��['aa', 'ba', 'ca']
���ࣺ

Python

# �Ӵ�С����
zrevrangebylex(name, max, min, start=None, num=None)
1
2
# �Ӵ�С����
zrevrangebylex(name, max, min, start=None, num=None)
zrevrangebylex(name, max, min, start=None, num=None)

zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)**

zrank(name, value)

���ػ���0��ֵ��ָʾ���������Ƶ�ֵ����

Python

>>> conn.zrank('h1','n1')
0
>>> conn.zrank('h1','n2')
1
1
2
3
4
>>> conn.zrank('h1','n1')
0
>>> conn.zrank('h1','n2')
1
zrevrank(name, value)���Ӵ�С����
zrem(name, *values)

ɾ��name�ж�Ӧ��values

Python

>>> conn.zrem('h1','n2')
1
>>> conn.zrem('h2',['n1','n2'])
2
1
2
3
4
>>> conn.zrem('h1','n2')
1
>>> conn.zrem('h2',['n1','n2'])
2
zremrangebyrank(name, min, max)

�������з�Χ����ɾ��

Python

>>> conn.zremrangebyrank('h1',1,2)
1
1
2
>>> conn.zremrangebyrank('h1',1,2)
1
zremrangebyscore(name, min, max)

���ݷ�����Χ����ɾ��

Python

>>> conn.zremrangebyscore('h1',10,20)
2
1
2
>>> conn.zremrangebyscore('h1',10,20)
2
zscore(name, value)

����ָ��value��ֵ�Ƕ���

Python

>>> conn.zscore('h1','n1')
11.0
1
2
>>> conn.zscore('h1','n1')
11.0
zunionstore(dest, keys, aggregate=None)

Global API

delete(*names)

��redis��ɾ��names

Python

>>> conn.delete('ooo')
1
1
2
>>> conn.delete('ooo')
1
exists(name)

���name�Ƿ����

Python

>>> conn.exists('iii')
False
>>> conn.exists('h1')
True
1
2
3
4
>>> conn.exists('iii')
False
>>> conn.exists('h1')
True
keys(pattern=��*��)

Python

# ƥ�����ݿ������� key 
>>> conn.keys(pattern='*')
[b'h2', b'kasd1', b'n2', b'url', b'name', b'n', b'li1', b'n1', b's1', b'now_key', b'l', b's2', b'number', b'numbers', b'a2', b'dic', b'a1', b'news', b'news1', b'aa', b'key', b'lli', b'll', b'k', b'li', b'k2', b'h1', b'li2', b'ccc', b'k1', b'blog', b'kaasdsd1', b'a3', b'l1', b'l2', b'n3', b'a']
1
2
3
# ƥ�����ݿ������� key 
>>> conn.keys(pattern='*')
[b'h2', b'kasd1', b'n2', b'url', b'name', b'n', b'li1', b'n1', b's1', b'now_key', b'l', b's2', b'number', b'numbers', b'a2', b'dic', b'a1', b'news', b'news1', b'aa', b'key', b'lli', b'll', b'k', b'li', b'k2', b'h1', b'li2', b'ccc', b'k1', b'blog', b'kaasdsd1', b'a3', b'l1', b'l2', b'n3', b'a']
Python

# ƥ��hello��hallo��hxllo��
conn.keys(pattern='h?llo')
# ƥ��hllo��heeeeello ��
conn.keys(pattern='h*llo')
# ƥ��hello��hallo������ƥ�� hillo
conn.keys(pattern='h[ae]llo')
1
2
3
4
5
6
# ƥ��hello��hallo��hxllo��
conn.keys(pattern='h?llo')
# ƥ��hllo��heeeeello ��
conn.keys(pattern='h*llo')
# ƥ��hello��hallo������ƥ�� hillo
conn.keys(pattern='h[ae]llo')
rename(src, dst)

��src��������dst

Python

>>> conn.set('k','v')
True
>>> conn.get('k')
b'v'
>>> conn.rename('k', 'kk')
True
>>> conn.get('k')
>>> conn.get('kk')
b'v'
1
2
3
4
5
6
7
8
9
>>> conn.set('k','v')
True
>>> conn.get('k')
b'v'
>>> conn.rename('k', 'kk')
True
>>> conn.get('k')
>>> conn.get('kk')
b'v'
move(name, db)

��redis��ĳ��ֵ�ƶ���ָ����db��

randomkey()

�����ȡһ��redis��name��������ɾ��

Python

>>> conn.randomkey()
b'll'
>>> conn.randomkey()
b'news1'
1
2
3
4
>>> conn.randomkey()
b'll'
>>> conn.randomkey()
b'news1'
type(name)

�鿴name������

Python

>>> conn.type('kk')
b'string'
1
2
>>> conn.type('kk')
b'string'
�ܵ�

redis-pyĬ����ִ��ÿ�����󶼻ᴴ�������ӳ��������ӣ��ͶϿ����黹���ӳأ�һ�����Ӳ����������Ҫ��һ��������ָ�������������ʹ��piplineʵ��һ������ָ������������Ĭ�������һ��pipline ��ԭ���Բ���(MySQL�е�����)��

Python

>>> import redis
>>> pool = redis.ConnectionPool(host='192.168.56.100', port=6379)
>>> r = redis.Redis(connection_pool=pool)
# ����һ��ͨ��֧������
>>> pipe = r.pipeline(transaction=True)
#
>>> r.set('hello', 'world')
True
>>> r.set('blog', 'ansheng.me')
True
# �����������������ֵ�Ĺ����г����ˣ���ô����ύ�Ͳ���ִ��
>>> pipe.execute()
[]
1
2
3
4
5
6
7
8
9
10
11
12
13
>>> import redis
>>> pool = redis.ConnectionPool(host='192.168.56.100', port=6379)
>>> r = redis.Redis(connection_pool=pool)
# ����һ��ͨ��֧������
>>> pipe = r.pipeline(transaction=True)
#
>>> r.set('hello', 'world')
True
>>> r.set('blog', 'ansheng.me')
True
# �����������������ֵ�Ĺ����г����ˣ���ô����ύ�Ͳ���ִ��
>>> pipe.execute()
[]
��������

Python

# monitor.py
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host='192.168.56.100')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'
    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True
    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub
# subscriber.py ������
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from monitor import RedisHelper
obj = RedisHelper()
redis_sub = obj.subscribe()
while True:
    msg = redis_sub.parse_response()
    print(msg)
# announcer.py ������
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from monitor import RedisHelper
obj = RedisHelper()
obj.public('hello')
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
# monitor.py
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host='192.168.56.100')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'
    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True
    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub
# subscriber.py ������
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from monitor import RedisHelper
obj = RedisHelper()
redis_sub = obj.subscribe()
while True:
    msg = redis_sub.parse_response()
    print(msg)
# announcer.py ������
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from monitor import RedisHelper
obj = RedisHelper()
obj.public('hello')
