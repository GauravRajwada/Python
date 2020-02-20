def dij(graph,start,stop):
    sortest_distance={}




infinity=9999999999
graph=[[0,50,45,10,infinity,infinity],
       [infinity,0,10,15,infinity,infinity],
       [infinity,infinity,0,infinity,30,infinity],
       [10,infinity,infinity,0,15,infinity],
       [infinity,20,35,infinity,0,infinity],
       [infinity,infinity,infinity,infinity,3,0]
]
source=1
destination=5
dij(graph,source,destination)
