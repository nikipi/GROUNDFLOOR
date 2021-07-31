
age=input('How old are you:')
weight=input('How much do you weight:')
height=input('How tall are you:')

print(f"So you are {age} old,{height} cm tall and {weight}kg heavy")

age=['11','34']
weight=['12','12']

for i,j in age,weight:
    print('So you are ' + i + ' old,'+ j + 'cm heavy')
    
    
    
  def tag(name,*content,cls=None,**attrs):
    if cls is not None:
        attrs['class']=cls
    if attrs:
        attr_str=''.join(' %s="%s"'%(attr,value) for attr,value in sorted(attrs.items()))

    else:
        attr_str=''
    if content:
        return '\n'.join('<%s%s>%s</%s>'%(name,attr_str,c,name) for c in content)
    else:
        return '<%s %s />'%(name,attr_str)

print(tag('br'))
print(tag('p','hello'))
print(tag('p','hello','world'))
print(tag('p','hello',id=33))
print(tag('p','hello','world',cls='sidebar'))

my_tag={'name':"img",
        'src':'sunset.jpg','cls':'framed',}

print(tag(**my_tag))


emails = ("a@example.com", "b@example.com","c@example.com","d@example.com")
message = {
'emails': emails,
'subject': "You Have Mail!",
    'message': "Here's some mail for you!" }


template='''
From: <{}>
TO: <{}>
Subject: {}
Content: {}=

'''



for i in range(1,len(emails)):
 print(template.format(message['emails'][0],message['emails'][i],message['subject'],message['message']))
