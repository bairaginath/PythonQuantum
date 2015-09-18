__author__ = 'veradocs-web'

f=open('test.txt','w+')
f.write("National Institute of Technology,Calicut\nIndia")
f.close()


# It is good practice to use the with keyword when dealing with file objects. This has the advantage that the file is properly closed after its suite finishes,
# even if an exception is raised on the way. It is also much shorter than writing equivalent try-finally blocks:



with open('test.txt', 'r') as f:
     read_data = f.read()
     print read_data
