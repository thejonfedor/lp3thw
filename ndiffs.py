# source: https://stackoverflow.com/a/17904977
# attempting to show diffs between .m4s segment files

import difflib

cases=[('https://73vod-adaptive.akamaized.net/exp=1650593016~acl=%2F68ea7307-0e01-484e-8cb4-98ce4f0fa2a8%2F%2A~hmac=3a7be7973694c6735b332d146b606ff078fa7c21de0700f153f3a2c3a0e29098/68ea7307-0e01-484e-8cb4-98ce4f0fa2a8/sep/video/29ef8b9a/chop/segment-2.m4s', 'https://73vod-adaptive.akamaized.net/exp=1650593016~acl=%2F68ea7307-0e01-484e-8cb4-98ce4f0fa2a8%2F%2A~hmac=3a7be7973694c6735b332d146b606ff078fa7c21de0700f153f3a2c3a0e29098/68ea7307-0e01-484e-8cb4-98ce4f0fa2a8/sep/video/29ef8b9a/chop/segment-3.m4s'),
       ('afrykanerskojęzyczni', 'nieafrykanerskojęzyczni'),
       ('afrykanerskojęzycznym', 'afrykanerskojęzyczny'),
       ('nieafrykanerskojęzyczni', 'afrykanerskojęzyczni'),
       ('nieafrynerskojęzyczni', 'afrykanerskojzyczni'),
       ('abcdefg','xac')] 

for a,b in cases:     
    print('{} => {}'.format(a,b))  
    for i,s in enumerate(difflib.ndiff(a, b)):
        if s[0]==' ': continue
        elif s[0]=='-':
            print(u'Delete "{}" from position {}'.format(s[-1],i))
        elif s[0]=='+':
            print(u'Add "{}" to position {}'.format(s[-1],i))    
    print()      